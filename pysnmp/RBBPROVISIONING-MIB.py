# SNMP MIB module (RBBPROVISIONING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBBPROVISIONING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:44:49 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(AtmAddr,
 AtmConnCastType,
 AtmConnKind,
 AtmServiceCategory,
 AtmTrafficDescrParamIndex,
 AtmVcIdentifier,
 AtmVpIdentifier) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmAddr",
    "AtmConnCastType",
    "AtmConnKind",
    "AtmServiceCategory",
    "AtmTrafficDescrParamIndex",
    "AtmVcIdentifier",
    "AtmVpIdentifier")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso,
 mib_2) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rbbProvMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4839, 32)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RBBServiceID(ObjectIdentifier, TextualConvention):
    status = "current"


class RBBServiceName(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class RBBServiceProvider(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class RBBServiceStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("adminDown", 4),
          ("down", 3),
          ("other", 1),
          ("up", 2))
    )



class RBBURLType(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )



class RBBCPEAuthType(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class RBBMailAddr(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class RBBCPESerialNumber(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class RBBVendorModel(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class RowStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )



# MIB Managed Objects in the order of their OIDs

_RbbProvMIBObjects_ObjectIdentity = ObjectIdentity
rbbProvMIBObjects = _RbbProvMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1)
)
_RbbServicesGroup_ObjectIdentity = ObjectIdentity
rbbServicesGroup = _RbbServicesGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 1)
)
_SrvServicesTable_Object = MibTable
srvServicesTable = _SrvServicesTable_Object(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 1, 1)
)
if mibBuilder.loadTexts:
    srvServicesTable.setStatus("current")
_SrvServiceEntry_Object = MibTableRow
srvServiceEntry = _SrvServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 1, 1, 1)
)
srvServiceEntry.setIndexNames(
    (0, "RBBPROVISIONING-MIB", "srvServiceIdentifier"),
)
if mibBuilder.loadTexts:
    srvServiceEntry.setStatus("current")
_SrvServiceIdentifier_Type = RBBServiceID
_SrvServiceIdentifier_Object = MibTableColumn
srvServiceIdentifier = _SrvServiceIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 1, 1, 1, 1),
    _SrvServiceIdentifier_Type()
)
srvServiceIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srvServiceIdentifier.setStatus("current")
_SrvServiceName_Type = RBBServiceName
_SrvServiceName_Object = MibTableColumn
srvServiceName = _SrvServiceName_Object(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 1, 1, 1, 2),
    _SrvServiceName_Type()
)
srvServiceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srvServiceName.setStatus("current")
_SrvServiceProvider_Type = RBBServiceProvider
_SrvServiceProvider_Object = MibTableColumn
srvServiceProvider = _SrvServiceProvider_Object(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 1, 1, 1, 3),
    _SrvServiceProvider_Type()
)
srvServiceProvider.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srvServiceProvider.setStatus("current")
_SrvServiceStatus_Type = RBBServiceStatus
_SrvServiceStatus_Object = MibTableColumn
srvServiceStatus = _SrvServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 1, 1, 1, 4),
    _SrvServiceStatus_Type()
)
srvServiceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srvServiceStatus.setStatus("current")
_SrvServiceConnType_Type = AtmConnKind
_SrvServiceConnType_Object = MibTableColumn
srvServiceConnType = _SrvServiceConnType_Object(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 1, 1, 1, 5),
    _SrvServiceConnType_Type()
)
srvServiceConnType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srvServiceConnType.setStatus("current")
_SrvServiceQOSType_Type = Integer32
_SrvServiceQOSType_Object = MibTableColumn
srvServiceQOSType = _SrvServiceQOSType_Object(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 1, 1, 1, 6),
    _SrvServiceQOSType_Type()
)
srvServiceQOSType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srvServiceQOSType.setStatus("current")
_SrvServiceSpeedReq_Type = Integer32
_SrvServiceSpeedReq_Object = MibTableColumn
srvServiceSpeedReq = _SrvServiceSpeedReq_Object(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 1, 1, 1, 7),
    _SrvServiceSpeedReq_Type()
)
srvServiceSpeedReq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srvServiceSpeedReq.setStatus("current")


class _SrvServiceLatencyReq_Type(Integer32):
    """Custom type srvServiceLatencyReq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 3),
          ("med", 2))
    )


_SrvServiceLatencyReq_Type.__name__ = "Integer32"
_SrvServiceLatencyReq_Object = MibTableColumn
srvServiceLatencyReq = _SrvServiceLatencyReq_Object(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 1, 1, 1, 8),
    _SrvServiceLatencyReq_Type()
)
srvServiceLatencyReq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srvServiceLatencyReq.setStatus("current")
_SrvServiceURL_Type = RBBURLType
_SrvServiceURL_Object = MibTableColumn
srvServiceURL = _SrvServiceURL_Object(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 1, 1, 1, 9),
    _SrvServiceURL_Type()
)
srvServiceURL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srvServiceURL.setStatus("current")


class _SrvServiceDescr_Type(DisplayString):
    """Custom type srvServiceDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SrvServiceDescr_Type.__name__ = "DisplayString"
_SrvServiceDescr_Object = MibTableColumn
srvServiceDescr = _SrvServiceDescr_Object(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 1, 1, 1, 10),
    _SrvServiceDescr_Type()
)
srvServiceDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srvServiceDescr.setStatus("current")
_SrvAdminContact_Type = RBBMailAddr
_SrvAdminContact_Object = MibTableColumn
srvAdminContact = _SrvAdminContact_Object(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 1, 1, 1, 11),
    _SrvAdminContact_Type()
)
srvAdminContact.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srvAdminContact.setStatus("current")
_SrvRowInfo_Type = RowStatus
_SrvRowInfo_Object = MibTableColumn
srvRowInfo = _SrvRowInfo_Object(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 1, 1, 1, 12),
    _SrvRowInfo_Type()
)
srvRowInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srvRowInfo.setStatus("current")
_RbbSubGroup_ObjectIdentity = ObjectIdentity
rbbSubGroup = _RbbSubGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 2)
)
_RbbSubTable_Object = MibTable
rbbSubTable = _RbbSubTable_Object(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 2, 1)
)
if mibBuilder.loadTexts:
    rbbSubTable.setStatus("current")
_RbbSubEntry_Object = MibTableRow
rbbSubEntry = _RbbSubEntry_Object(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 2, 1, 1)
)
rbbSubEntry.setIndexNames(
    (0, "RBBPROVISIONING-MIB", "rbbSubVendor"),
    (0, "RBBPROVISIONING-MIB", "rbbSubModel"),
    (0, "RBBPROVISIONING-MIB", "rbbSubSerialNumber"),
    (0, "RBBPROVISIONING-MIB", "rbbSubServiceIdentifier"),
)
if mibBuilder.loadTexts:
    rbbSubEntry.setStatus("current")
_RbbSubVendor_Type = ObjectIdentifier
_RbbSubVendor_Object = MibTableColumn
rbbSubVendor = _RbbSubVendor_Object(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 2, 1, 1, 1),
    _RbbSubVendor_Type()
)
rbbSubVendor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbbSubVendor.setStatus("current")
_RbbSubModel_Type = RBBVendorModel
_RbbSubModel_Object = MibTableColumn
rbbSubModel = _RbbSubModel_Object(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 2, 1, 1, 3),
    _RbbSubModel_Type()
)
rbbSubModel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbbSubModel.setStatus("current")
_RbbSubSerialNumber_Type = DisplayString
_RbbSubSerialNumber_Object = MibTableColumn
rbbSubSerialNumber = _RbbSubSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 2, 1, 1, 4),
    _RbbSubSerialNumber_Type()
)
rbbSubSerialNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbbSubSerialNumber.setStatus("current")
_RbbSubServiceIdentifier_Type = RBBServiceID
_RbbSubServiceIdentifier_Object = MibTableColumn
rbbSubServiceIdentifier = _RbbSubServiceIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 2, 1, 1, 5),
    _RbbSubServiceIdentifier_Type()
)
rbbSubServiceIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbbSubServiceIdentifier.setStatus("current")
_RbbSubVPI_Type = AtmVpIdentifier
_RbbSubVPI_Object = MibTableColumn
rbbSubVPI = _RbbSubVPI_Object(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 2, 1, 1, 6),
    _RbbSubVPI_Type()
)
rbbSubVPI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbbSubVPI.setStatus("current")
_RbbSubVCI_Type = AtmVcIdentifier
_RbbSubVCI_Object = MibTableColumn
rbbSubVCI = _RbbSubVCI_Object(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 2, 1, 1, 7),
    _RbbSubVCI_Type()
)
rbbSubVCI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbbSubVCI.setStatus("current")
_RbbSubAddr_Type = AtmAddr
_RbbSubAddr_Object = MibTableColumn
rbbSubAddr = _RbbSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 2, 1, 1, 8),
    _RbbSubAddr_Type()
)
rbbSubAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbbSubAddr.setStatus("current")
_RbbSubStatus_Type = RBBServiceStatus
_RbbSubStatus_Object = MibTableColumn
rbbSubStatus = _RbbSubStatus_Object(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 2, 1, 1, 9),
    _RbbSubStatus_Type()
)
rbbSubStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbbSubStatus.setStatus("current")
_RbbSubRowInfo_Type = RowStatus
_RbbSubRowInfo_Object = MibTableColumn
rbbSubRowInfo = _RbbSubRowInfo_Object(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 2, 1, 1, 10),
    _RbbSubRowInfo_Type()
)
rbbSubRowInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbbSubRowInfo.setStatus("current")
_RbbCPEGroup_ObjectIdentity = ObjectIdentity
rbbCPEGroup = _RbbCPEGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 3)
)
_RbbCPETable_Object = MibTable
rbbCPETable = _RbbCPETable_Object(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 3, 1)
)
if mibBuilder.loadTexts:
    rbbCPETable.setStatus("current")
_RbbCPEEntry_Object = MibTableRow
rbbCPEEntry = _RbbCPEEntry_Object(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 3, 1, 1)
)
rbbCPEEntry.setIndexNames(
    (0, "RBBPROVISIONING-MIB", "rbbVendorOID"),
    (0, "RBBPROVISIONING-MIB", "rbbVendorModel"),
    (0, "RBBPROVISIONING-MIB", "rbbCPESerialNumber"),
)
if mibBuilder.loadTexts:
    rbbCPEEntry.setStatus("current")
_RbbCPEAuthValue_Type = RBBCPEAuthType
_RbbCPEAuthValue_Object = MibTableColumn
rbbCPEAuthValue = _RbbCPEAuthValue_Object(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 3, 1, 1, 1),
    _RbbCPEAuthValue_Type()
)
rbbCPEAuthValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbbCPEAuthValue.setStatus("current")
_RbbCPEVendorOID_Type = ObjectIdentifier
_RbbCPEVendorOID_Object = MibTableColumn
rbbCPEVendorOID = _RbbCPEVendorOID_Object(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 3, 1, 1, 2),
    _RbbCPEVendorOID_Type()
)
rbbCPEVendorOID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbbCPEVendorOID.setStatus("current")
_RbbCPEVendorModel_Type = RBBVendorModel
_RbbCPEVendorModel_Object = MibTableColumn
rbbCPEVendorModel = _RbbCPEVendorModel_Object(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 3, 1, 1, 3),
    _RbbCPEVendorModel_Type()
)
rbbCPEVendorModel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbbCPEVendorModel.setStatus("current")
_RbbCPEStatus_Type = Integer32
_RbbCPEStatus_Object = MibTableColumn
rbbCPEStatus = _RbbCPEStatus_Object(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 3, 1, 1, 4),
    _RbbCPEStatus_Type()
)
rbbCPEStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbbCPEStatus.setStatus("current")
_RbbCPESubCount_Type = Integer32
_RbbCPESubCount_Object = MibTableColumn
rbbCPESubCount = _RbbCPESubCount_Object(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 3, 1, 1, 5),
    _RbbCPESubCount_Type()
)
rbbCPESubCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbbCPESubCount.setStatus("current")
_RbbCPESubAggrSpeed_Type = Integer32
_RbbCPESubAggrSpeed_Object = MibTableColumn
rbbCPESubAggrSpeed = _RbbCPESubAggrSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 3, 1, 1, 6),
    _RbbCPESubAggrSpeed_Type()
)
rbbCPESubAggrSpeed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbbCPESubAggrSpeed.setStatus("current")
_RbbCPECustContact_Type = RBBMailAddr
_RbbCPECustContact_Object = MibTableColumn
rbbCPECustContact = _RbbCPECustContact_Object(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 3, 1, 1, 7),
    _RbbCPECustContact_Type()
)
rbbCPECustContact.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbbCPECustContact.setStatus("current")
_RbbCPESerialNumber_Type = RBBCPESerialNumber
_RbbCPESerialNumber_Object = MibTableColumn
rbbCPESerialNumber = _RbbCPESerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 3, 1, 1, 8),
    _RbbCPESerialNumber_Type()
)
rbbCPESerialNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbbCPESerialNumber.setStatus("current")
_RbbCPETrapEnable_Type = Integer32
_RbbCPETrapEnable_Object = MibTableColumn
rbbCPETrapEnable = _RbbCPETrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 3, 1, 1, 9),
    _RbbCPETrapEnable_Type()
)
rbbCPETrapEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbbCPETrapEnable.setStatus("current")
_RbbCPECurrentImage_Type = RBBURLType
_RbbCPECurrentImage_Object = MibTableColumn
rbbCPECurrentImage = _RbbCPECurrentImage_Object(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 3, 1, 1, 10),
    _RbbCPECurrentImage_Type()
)
rbbCPECurrentImage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbbCPECurrentImage.setStatus("current")
_RbbCPEIpAddress_Type = IpAddress
_RbbCPEIpAddress_Object = MibTableColumn
rbbCPEIpAddress = _RbbCPEIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 3, 1, 1, 11),
    _RbbCPEIpAddress_Type()
)
rbbCPEIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbbCPEIpAddress.setStatus("current")
_RbbCPERowInfo_Type = RowStatus
_RbbCPERowInfo_Object = MibTableColumn
rbbCPERowInfo = _RbbCPERowInfo_Object(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 3, 1, 1, 12),
    _RbbCPERowInfo_Type()
)
rbbCPERowInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbbCPERowInfo.setStatus("current")
_RbbVendorGroup_ObjectIdentity = ObjectIdentity
rbbVendorGroup = _RbbVendorGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 4)
)
_RbbVendorTable_Object = MibTable
rbbVendorTable = _RbbVendorTable_Object(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 4, 1)
)
if mibBuilder.loadTexts:
    rbbVendorTable.setStatus("current")
_RbbVendorEntry_Object = MibTableRow
rbbVendorEntry = _RbbVendorEntry_Object(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 4, 1, 1)
)
rbbVendorEntry.setIndexNames(
    (0, "RBBPROVISIONING-MIB", "rbbVendorOID"),
    (0, "RBBPROVISIONING-MIB", "rbbVendorModel"),
)
if mibBuilder.loadTexts:
    rbbVendorEntry.setStatus("current")
_RbbVendorOID_Type = ObjectIdentifier
_RbbVendorOID_Object = MibTableColumn
rbbVendorOID = _RbbVendorOID_Object(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 4, 1, 1, 1),
    _RbbVendorOID_Type()
)
rbbVendorOID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbbVendorOID.setStatus("current")
_RbbVendorModel_Type = RBBVendorModel
_RbbVendorModel_Object = MibTableColumn
rbbVendorModel = _RbbVendorModel_Object(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 4, 1, 1, 2),
    _RbbVendorModel_Type()
)
rbbVendorModel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbbVendorModel.setStatus("current")
_RbbVendorImageURL_Type = RBBURLType
_RbbVendorImageURL_Object = MibTableColumn
rbbVendorImageURL = _RbbVendorImageURL_Object(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 4, 1, 1, 3),
    _RbbVendorImageURL_Type()
)
rbbVendorImageURL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbbVendorImageURL.setStatus("current")
_RbbVendorRowInfo_Type = RowStatus
_RbbVendorRowInfo_Object = MibTableColumn
rbbVendorRowInfo = _RbbVendorRowInfo_Object(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 4, 1, 1, 4),
    _RbbVendorRowInfo_Type()
)
rbbVendorRowInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbbVendorRowInfo.setStatus("current")
_RbbSrvGrpSerialNumber_Type = Counter32
_RbbSrvGrpSerialNumber_Object = MibScalar
rbbSrvGrpSerialNumber = _RbbSrvGrpSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 5),
    _RbbSrvGrpSerialNumber_Type()
)
rbbSrvGrpSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbbSrvGrpSerialNumber.setStatus("current")
_RbbSubGrpSerialNumber_Type = Counter32
_RbbSubGrpSerialNumber_Object = MibScalar
rbbSubGrpSerialNumber = _RbbSubGrpSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 6),
    _RbbSubGrpSerialNumber_Type()
)
rbbSubGrpSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbbSubGrpSerialNumber.setStatus("current")
_RbbCPEGrpSerialNumber_Type = Counter32
_RbbCPEGrpSerialNumber_Object = MibScalar
rbbCPEGrpSerialNumber = _RbbCPEGrpSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 7),
    _RbbCPEGrpSerialNumber_Type()
)
rbbCPEGrpSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbbCPEGrpSerialNumber.setStatus("current")
_RbbVendorGrpSerialNumber_Type = Counter32
_RbbVendorGrpSerialNumber_Object = MibScalar
rbbVendorGrpSerialNumber = _RbbVendorGrpSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 8),
    _RbbVendorGrpSerialNumber_Type()
)
rbbVendorGrpSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbbVendorGrpSerialNumber.setStatus("current")
_RbbNotifyGroup_ObjectIdentity = ObjectIdentity
rbbNotifyGroup = _RbbNotifyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 12)
)

# Managed Objects groups


# Notification objects

rbbSubNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 12, 1)
)
rbbSubNotify.setObjects(
      *(("RBBPROVISIONING-MIB", "rbbSubVendor"),
        ("RBBPROVISIONING-MIB", "rbbSubModel"),
        ("RBBPROVISIONING-MIB", "rbbSubSerialNumber"),
        ("RBBPROVISIONING-MIB", "rbbSubServiceIdentifier"))
)
if mibBuilder.loadTexts:
    rbbSubNotify.setStatus(
        "current"
    )

rbbPowerUpNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4839, 32, 1, 12, 2)
)
rbbPowerUpNotify.setObjects(
      *(("RBBPROVISIONING-MIB", "rbbCPEVendorOID"),
        ("RBBPROVISIONING-MIB", "rbbCPEVendorModel"),
        ("RBBPROVISIONING-MIB", "rbbCPESerialNumber"))
)
if mibBuilder.loadTexts:
    rbbPowerUpNotify.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBBPROVISIONING-MIB",
    **{"RBBServiceID": RBBServiceID,
       "RBBServiceName": RBBServiceName,
       "RBBServiceProvider": RBBServiceProvider,
       "RBBServiceStatus": RBBServiceStatus,
       "RBBURLType": RBBURLType,
       "RBBCPEAuthType": RBBCPEAuthType,
       "RBBMailAddr": RBBMailAddr,
       "RBBCPESerialNumber": RBBCPESerialNumber,
       "RBBVendorModel": RBBVendorModel,
       "RowStatus": RowStatus,
       "rbbProvMIB": rbbProvMIB,
       "rbbProvMIBObjects": rbbProvMIBObjects,
       "rbbServicesGroup": rbbServicesGroup,
       "srvServicesTable": srvServicesTable,
       "srvServiceEntry": srvServiceEntry,
       "srvServiceIdentifier": srvServiceIdentifier,
       "srvServiceName": srvServiceName,
       "srvServiceProvider": srvServiceProvider,
       "srvServiceStatus": srvServiceStatus,
       "srvServiceConnType": srvServiceConnType,
       "srvServiceQOSType": srvServiceQOSType,
       "srvServiceSpeedReq": srvServiceSpeedReq,
       "srvServiceLatencyReq": srvServiceLatencyReq,
       "srvServiceURL": srvServiceURL,
       "srvServiceDescr": srvServiceDescr,
       "srvAdminContact": srvAdminContact,
       "srvRowInfo": srvRowInfo,
       "rbbSubGroup": rbbSubGroup,
       "rbbSubTable": rbbSubTable,
       "rbbSubEntry": rbbSubEntry,
       "rbbSubVendor": rbbSubVendor,
       "rbbSubModel": rbbSubModel,
       "rbbSubSerialNumber": rbbSubSerialNumber,
       "rbbSubServiceIdentifier": rbbSubServiceIdentifier,
       "rbbSubVPI": rbbSubVPI,
       "rbbSubVCI": rbbSubVCI,
       "rbbSubAddr": rbbSubAddr,
       "rbbSubStatus": rbbSubStatus,
       "rbbSubRowInfo": rbbSubRowInfo,
       "rbbCPEGroup": rbbCPEGroup,
       "rbbCPETable": rbbCPETable,
       "rbbCPEEntry": rbbCPEEntry,
       "rbbCPEAuthValue": rbbCPEAuthValue,
       "rbbCPEVendorOID": rbbCPEVendorOID,
       "rbbCPEVendorModel": rbbCPEVendorModel,
       "rbbCPEStatus": rbbCPEStatus,
       "rbbCPESubCount": rbbCPESubCount,
       "rbbCPESubAggrSpeed": rbbCPESubAggrSpeed,
       "rbbCPECustContact": rbbCPECustContact,
       "rbbCPESerialNumber": rbbCPESerialNumber,
       "rbbCPETrapEnable": rbbCPETrapEnable,
       "rbbCPECurrentImage": rbbCPECurrentImage,
       "rbbCPEIpAddress": rbbCPEIpAddress,
       "rbbCPERowInfo": rbbCPERowInfo,
       "rbbVendorGroup": rbbVendorGroup,
       "rbbVendorTable": rbbVendorTable,
       "rbbVendorEntry": rbbVendorEntry,
       "rbbVendorOID": rbbVendorOID,
       "rbbVendorModel": rbbVendorModel,
       "rbbVendorImageURL": rbbVendorImageURL,
       "rbbVendorRowInfo": rbbVendorRowInfo,
       "rbbSrvGrpSerialNumber": rbbSrvGrpSerialNumber,
       "rbbSubGrpSerialNumber": rbbSubGrpSerialNumber,
       "rbbCPEGrpSerialNumber": rbbCPEGrpSerialNumber,
       "rbbVendorGrpSerialNumber": rbbVendorGrpSerialNumber,
       "rbbNotifyGroup": rbbNotifyGroup,
       "rbbSubNotify": rbbSubNotify,
       "rbbPowerUpNotify": rbbPowerUpNotify}
)
