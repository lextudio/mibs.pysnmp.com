# SNMP MIB module (COMPELLENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/COMPELLENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:50 2024
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
 iso) = mibBuilder.importSymbols(
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
    "iso")

(DateAndTime,
 DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

compellentModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 16139, 1)
)
compellentModule.setRevisions(
        ("2013-05-20 00:00",
         "2013-02-08 00:00",
         "2011-07-12 00:00",
         "2009-05-18 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ScHardwareType(Integer32, TextualConvention):
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
        *(("audiblealarm", 6),
          ("fan", 1),
          ("iomodule", 5),
          ("powersupply", 2),
          ("tempsensor", 3),
          ("voltagesensor", 4))
    )



class ScStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 3),
          ("down", 2),
          ("up", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CompellentEnterprise_ObjectIdentity = ObjectIdentity
compellentEnterprise = _CompellentEnterprise_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16139)
)
if mibBuilder.loadTexts:
    compellentEnterprise.setStatus("current")
_CompellentObjects_ObjectIdentity = ObjectIdentity
compellentObjects = _CompellentObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16139, 2)
)
if mibBuilder.loadTexts:
    compellentObjects.setStatus("current")
_ProductIDDisplayName_Type = SnmpAdminString
_ProductIDDisplayName_Object = MibScalar
productIDDisplayName = _ProductIDDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 1),
    _ProductIDDisplayName_Type()
)
productIDDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productIDDisplayName.setStatus("current")
_ProductIDDescription_Type = SnmpAdminString
_ProductIDDescription_Object = MibScalar
productIDDescription = _ProductIDDescription_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 2),
    _ProductIDDescription_Type()
)
productIDDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productIDDescription.setStatus("current")
_ProductIDVendor_Type = SnmpAdminString
_ProductIDVendor_Object = MibScalar
productIDVendor = _ProductIDVendor_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 3),
    _ProductIDVendor_Type()
)
productIDVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productIDVendor.setStatus("current")
_ProductIDVersion_Type = SnmpAdminString
_ProductIDVersion_Object = MibScalar
productIDVersion = _ProductIDVersion_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 4),
    _ProductIDVersion_Type()
)
productIDVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productIDVersion.setStatus("current")
_ProductIDSerialNumber_Type = SnmpAdminString
_ProductIDSerialNumber_Object = MibScalar
productIDSerialNumber = _ProductIDSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 5),
    _ProductIDSerialNumber_Type()
)
productIDSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productIDSerialNumber.setStatus("current")


class _ProductIDGlobalStatus_Type(Integer32):
    """Custom type productIDGlobalStatus based on Integer32"""
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
        *(("critical", 5),
          ("noncritical", 4),
          ("nonrecoverable", 6),
          ("ok", 3),
          ("other", 1),
          ("unknown", 2))
    )


_ProductIDGlobalStatus_Type.__name__ = "Integer32"
_ProductIDGlobalStatus_Object = MibScalar
productIDGlobalStatus = _ProductIDGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 6),
    _ProductIDGlobalStatus_Type()
)
productIDGlobalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productIDGlobalStatus.setStatus("current")
_ProductIDBuildNumber_Type = SnmpAdminString
_ProductIDBuildNumber_Object = MibScalar
productIDBuildNumber = _ProductIDBuildNumber_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 7),
    _ProductIDBuildNumber_Type()
)
productIDBuildNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productIDBuildNumber.setStatus("current")
_ProductIDURL_Type = SnmpAdminString
_ProductIDURL_Object = MibScalar
productIDURL = _ProductIDURL_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 8),
    _ProductIDURL_Type()
)
productIDURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productIDURL.setStatus("current")
_ScAlertDef_Type = SnmpAdminString
_ScAlertDef_Object = MibScalar
scAlertDef = _ScAlertDef_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 9),
    _ScAlertDef_Type()
)
scAlertDef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scAlertDef.setStatus("current")
_ScIndex_Type = Unsigned32
_ScIndex_Object = MibScalar
scIndex = _ScIndex_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 10),
    _ScIndex_Type()
)
scIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scIndex.setStatus("current")
_ScTestString_Type = SnmpAdminString
_ScTestString_Object = MibScalar
scTestString = _ScTestString_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 11),
    _ScTestString_Type()
)
scTestString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scTestString.setStatus("current")
_ScMiscAlertString_Type = SnmpAdminString
_ScMiscAlertString_Object = MibScalar
scMiscAlertString = _ScMiscAlertString_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 12),
    _ScMiscAlertString_Type()
)
scMiscAlertString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scMiscAlertString.setStatus("current")
_ScCtlrTable_Object = MibTable
scCtlrTable = _ScCtlrTable_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 13)
)
if mibBuilder.loadTexts:
    scCtlrTable.setStatus("current")
_ScCtlrEntry_Object = MibTableRow
scCtlrEntry = _ScCtlrEntry_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 13, 1)
)
scCtlrEntry.setIndexNames(
    (0, "COMPELLENT-MIB", "scCtlrIndex"),
)
if mibBuilder.loadTexts:
    scCtlrEntry.setStatus("current")


class _ScCtlrIndex_Type(Unsigned32):
    """Custom type scCtlrIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ScCtlrIndex_Type.__name__ = "Unsigned32"
_ScCtlrIndex_Object = MibTableColumn
scCtlrIndex = _ScCtlrIndex_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 13, 1, 1),
    _ScCtlrIndex_Type()
)
scCtlrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scCtlrIndex.setStatus("current")


class _ScCtlrNbr_Type(Unsigned32):
    """Custom type scCtlrNbr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ScCtlrNbr_Type.__name__ = "Unsigned32"
_ScCtlrNbr_Object = MibTableColumn
scCtlrNbr = _ScCtlrNbr_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 13, 1, 2),
    _ScCtlrNbr_Type()
)
scCtlrNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCtlrNbr.setStatus("current")
_ScCtlrStatus_Type = ScStatus
_ScCtlrStatus_Object = MibTableColumn
scCtlrStatus = _ScCtlrStatus_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 13, 1, 3),
    _ScCtlrStatus_Type()
)
scCtlrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCtlrStatus.setStatus("current")
_ScCtlrName_Type = SnmpAdminString
_ScCtlrName_Object = MibTableColumn
scCtlrName = _ScCtlrName_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 13, 1, 4),
    _ScCtlrName_Type()
)
scCtlrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCtlrName.setStatus("current")
_ScCtlrIpAddr_Type = SnmpAdminString
_ScCtlrIpAddr_Object = MibTableColumn
scCtlrIpAddr = _ScCtlrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 13, 1, 5),
    _ScCtlrIpAddr_Type()
)
scCtlrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCtlrIpAddr.setStatus("current")
_ScCtlrForceTrap_Type = SnmpAdminString
_ScCtlrForceTrap_Object = MibTableColumn
scCtlrForceTrap = _ScCtlrForceTrap_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 13, 1, 6),
    _ScCtlrForceTrap_Type()
)
scCtlrForceTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scCtlrForceTrap.setStatus("current")
_ScCtlrModel_Type = SnmpAdminString
_ScCtlrModel_Object = MibTableColumn
scCtlrModel = _ScCtlrModel_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 13, 1, 7),
    _ScCtlrModel_Type()
)
scCtlrModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scCtlrModel.setStatus("current")
_ScCtlrServiceTag_Type = SnmpAdminString
_ScCtlrServiceTag_Object = MibTableColumn
scCtlrServiceTag = _ScCtlrServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 13, 1, 8),
    _ScCtlrServiceTag_Type()
)
scCtlrServiceTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scCtlrServiceTag.setStatus("current")
_ScCtlrAssetTag_Type = SnmpAdminString
_ScCtlrAssetTag_Object = MibTableColumn
scCtlrAssetTag = _ScCtlrAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 13, 1, 9),
    _ScCtlrAssetTag_Type()
)
scCtlrAssetTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scCtlrAssetTag.setStatus("current")
_ScDiskTable_Object = MibTable
scDiskTable = _ScDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 14)
)
if mibBuilder.loadTexts:
    scDiskTable.setStatus("current")
_ScDiskEntry_Object = MibTableRow
scDiskEntry = _ScDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 14, 1)
)
scDiskEntry.setIndexNames(
    (0, "COMPELLENT-MIB", "scDiskIndex"),
)
if mibBuilder.loadTexts:
    scDiskEntry.setStatus("current")


class _ScDiskIndex_Type(Unsigned32):
    """Custom type scDiskIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_ScDiskIndex_Type.__name__ = "Unsigned32"
_ScDiskIndex_Object = MibTableColumn
scDiskIndex = _ScDiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 14, 1, 1),
    _ScDiskIndex_Type()
)
scDiskIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scDiskIndex.setStatus("current")


class _ScDiskNbr_Type(Unsigned32):
    """Custom type scDiskNbr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_ScDiskNbr_Type.__name__ = "Unsigned32"
_ScDiskNbr_Object = MibTableColumn
scDiskNbr = _ScDiskNbr_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 14, 1, 2),
    _ScDiskNbr_Type()
)
scDiskNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scDiskNbr.setStatus("current")
_ScDiskStatus_Type = ScStatus
_ScDiskStatus_Object = MibTableColumn
scDiskStatus = _ScDiskStatus_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 14, 1, 3),
    _ScDiskStatus_Type()
)
scDiskStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scDiskStatus.setStatus("current")
_ScDiskNamePosition_Type = SnmpAdminString
_ScDiskNamePosition_Object = MibTableColumn
scDiskNamePosition = _ScDiskNamePosition_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 14, 1, 4),
    _ScDiskNamePosition_Type()
)
scDiskNamePosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scDiskNamePosition.setStatus("current")
_ScDiskHealthy_Type = TruthValue
_ScDiskHealthy_Object = MibTableColumn
scDiskHealthy = _ScDiskHealthy_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 14, 1, 5),
    _ScDiskHealthy_Type()
)
scDiskHealthy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scDiskHealthy.setStatus("current")
_ScDiskStatusMsg_Type = SnmpAdminString
_ScDiskStatusMsg_Object = MibTableColumn
scDiskStatusMsg = _ScDiskStatusMsg_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 14, 1, 6),
    _ScDiskStatusMsg_Type()
)
scDiskStatusMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scDiskStatusMsg.setStatus("current")
_ScDiskApiIndex_Type = Unsigned32
_ScDiskApiIndex_Object = MibTableColumn
scDiskApiIndex = _ScDiskApiIndex_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 14, 1, 7),
    _ScDiskApiIndex_Type()
)
scDiskApiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scDiskApiIndex.setStatus("current")
_ScDiskForceTrap_Type = SnmpAdminString
_ScDiskForceTrap_Object = MibTableColumn
scDiskForceTrap = _ScDiskForceTrap_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 14, 1, 8),
    _ScDiskForceTrap_Type()
)
scDiskForceTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scDiskForceTrap.setStatus("current")
_ScDiskSize_Type = Unsigned32
_ScDiskSize_Object = MibTableColumn
scDiskSize = _ScDiskSize_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 14, 1, 9),
    _ScDiskSize_Type()
)
scDiskSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scDiskSize.setStatus("current")


class _ScDiskIoPortType_Type(Integer32):
    """Custom type scDiskIoPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("fibrechannel", 1),
          ("fibrechanneloverethernet", 3),
          ("iscsi", 2),
          ("sas", 4),
          ("unknown", 5))
    )


_ScDiskIoPortType_Type.__name__ = "Integer32"
_ScDiskIoPortType_Object = MibTableColumn
scDiskIoPortType = _ScDiskIoPortType_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 14, 1, 10),
    _ScDiskIoPortType_Type()
)
scDiskIoPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scDiskIoPortType.setStatus("current")
_ScDiskEnclosure_Type = Unsigned32
_ScDiskEnclosure_Object = MibTableColumn
scDiskEnclosure = _ScDiskEnclosure_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 14, 1, 11),
    _ScDiskEnclosure_Type()
)
scDiskEnclosure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scDiskEnclosure.setStatus("current")
_ScEnclTable_Object = MibTable
scEnclTable = _ScEnclTable_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 15)
)
if mibBuilder.loadTexts:
    scEnclTable.setStatus("current")
_ScEnclEntry_Object = MibTableRow
scEnclEntry = _ScEnclEntry_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 15, 1)
)
scEnclEntry.setIndexNames(
    (0, "COMPELLENT-MIB", "scEnclIndex"),
)
if mibBuilder.loadTexts:
    scEnclEntry.setStatus("current")


class _ScEnclIndex_Type(Unsigned32):
    """Custom type scEnclIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ScEnclIndex_Type.__name__ = "Unsigned32"
_ScEnclIndex_Object = MibTableColumn
scEnclIndex = _ScEnclIndex_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 15, 1, 1),
    _ScEnclIndex_Type()
)
scEnclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scEnclIndex.setStatus("current")


class _ScEnclNbr_Type(Unsigned32):
    """Custom type scEnclNbr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ScEnclNbr_Type.__name__ = "Unsigned32"
_ScEnclNbr_Object = MibTableColumn
scEnclNbr = _ScEnclNbr_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 15, 1, 2),
    _ScEnclNbr_Type()
)
scEnclNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEnclNbr.setStatus("current")
_ScEnclStatus_Type = ScStatus
_ScEnclStatus_Object = MibTableColumn
scEnclStatus = _ScEnclStatus_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 15, 1, 3),
    _ScEnclStatus_Type()
)
scEnclStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEnclStatus.setStatus("current")
_ScEnclName_Type = SnmpAdminString
_ScEnclName_Object = MibTableColumn
scEnclName = _ScEnclName_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 15, 1, 4),
    _ScEnclName_Type()
)
scEnclName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEnclName.setStatus("current")
_ScEnclStatusDescr_Type = SnmpAdminString
_ScEnclStatusDescr_Object = MibTableColumn
scEnclStatusDescr = _ScEnclStatusDescr_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 15, 1, 5),
    _ScEnclStatusDescr_Type()
)
scEnclStatusDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEnclStatusDescr.setStatus("current")
_ScEnclType_Type = SnmpAdminString
_ScEnclType_Object = MibTableColumn
scEnclType = _ScEnclType_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 15, 1, 6),
    _ScEnclType_Type()
)
scEnclType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEnclType.setStatus("current")
_ScEnclModel_Type = SnmpAdminString
_ScEnclModel_Object = MibTableColumn
scEnclModel = _ScEnclModel_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 15, 1, 7),
    _ScEnclModel_Type()
)
scEnclModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEnclModel.setStatus("current")
_ScEnclForceTrap_Type = SnmpAdminString
_ScEnclForceTrap_Object = MibTableColumn
scEnclForceTrap = _ScEnclForceTrap_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 15, 1, 8),
    _ScEnclForceTrap_Type()
)
scEnclForceTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scEnclForceTrap.setStatus("current")
_ScEnclServiceTag_Type = SnmpAdminString
_ScEnclServiceTag_Object = MibTableColumn
scEnclServiceTag = _ScEnclServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 15, 1, 9),
    _ScEnclServiceTag_Type()
)
scEnclServiceTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scEnclServiceTag.setStatus("current")
_ScEnclAssetTag_Type = SnmpAdminString
_ScEnclAssetTag_Object = MibTableColumn
scEnclAssetTag = _ScEnclAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 15, 1, 10),
    _ScEnclAssetTag_Type()
)
scEnclAssetTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scEnclAssetTag.setStatus("current")
_ScCtlrFanTable_Object = MibTable
scCtlrFanTable = _ScCtlrFanTable_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 16)
)
if mibBuilder.loadTexts:
    scCtlrFanTable.setStatus("current")
_ScCtlrFanEntry_Object = MibTableRow
scCtlrFanEntry = _ScCtlrFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 16, 1)
)
scCtlrFanEntry.setIndexNames(
    (0, "COMPELLENT-MIB", "scCtlrIndex"),
    (0, "COMPELLENT-MIB", "scCtlrFanIndex"),
)
if mibBuilder.loadTexts:
    scCtlrFanEntry.setStatus("current")


class _ScCtlrFanIndex_Type(Unsigned32):
    """Custom type scCtlrFanIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ScCtlrFanIndex_Type.__name__ = "Unsigned32"
_ScCtlrFanIndex_Object = MibTableColumn
scCtlrFanIndex = _ScCtlrFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 16, 1, 1),
    _ScCtlrFanIndex_Type()
)
scCtlrFanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scCtlrFanIndex.setStatus("current")


class _ScCtlrFanNbr_Type(Unsigned32):
    """Custom type scCtlrFanNbr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ScCtlrFanNbr_Type.__name__ = "Unsigned32"
_ScCtlrFanNbr_Object = MibTableColumn
scCtlrFanNbr = _ScCtlrFanNbr_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 16, 1, 2),
    _ScCtlrFanNbr_Type()
)
scCtlrFanNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCtlrFanNbr.setStatus("current")
_ScCtlrFanStatus_Type = ScStatus
_ScCtlrFanStatus_Object = MibTableColumn
scCtlrFanStatus = _ScCtlrFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 16, 1, 3),
    _ScCtlrFanStatus_Type()
)
scCtlrFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCtlrFanStatus.setStatus("current")
_ScCtlrFanName_Type = SnmpAdminString
_ScCtlrFanName_Object = MibTableColumn
scCtlrFanName = _ScCtlrFanName_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 16, 1, 4),
    _ScCtlrFanName_Type()
)
scCtlrFanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCtlrFanName.setStatus("current")
_ScCtlrFanCurrentRpm_Type = Unsigned32
_ScCtlrFanCurrentRpm_Object = MibTableColumn
scCtlrFanCurrentRpm = _ScCtlrFanCurrentRpm_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 16, 1, 5),
    _ScCtlrFanCurrentRpm_Type()
)
scCtlrFanCurrentRpm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCtlrFanCurrentRpm.setStatus("current")
_ScCtlrFanNormMaxRpm_Type = Unsigned32
_ScCtlrFanNormMaxRpm_Object = MibTableColumn
scCtlrFanNormMaxRpm = _ScCtlrFanNormMaxRpm_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 16, 1, 6),
    _ScCtlrFanNormMaxRpm_Type()
)
scCtlrFanNormMaxRpm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCtlrFanNormMaxRpm.setStatus("current")
_ScCtlrFanNormMinRpm_Type = Unsigned32
_ScCtlrFanNormMinRpm_Object = MibTableColumn
scCtlrFanNormMinRpm = _ScCtlrFanNormMinRpm_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 16, 1, 7),
    _ScCtlrFanNormMinRpm_Type()
)
scCtlrFanNormMinRpm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCtlrFanNormMinRpm.setStatus("current")
_ScCtlrFanWarnLwrRpm_Type = Unsigned32
_ScCtlrFanWarnLwrRpm_Object = MibTableColumn
scCtlrFanWarnLwrRpm = _ScCtlrFanWarnLwrRpm_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 16, 1, 8),
    _ScCtlrFanWarnLwrRpm_Type()
)
scCtlrFanWarnLwrRpm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCtlrFanWarnLwrRpm.setStatus("current")
_ScCtlrFanWarnUprRpm_Type = Unsigned32
_ScCtlrFanWarnUprRpm_Object = MibTableColumn
scCtlrFanWarnUprRpm = _ScCtlrFanWarnUprRpm_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 16, 1, 9),
    _ScCtlrFanWarnUprRpm_Type()
)
scCtlrFanWarnUprRpm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCtlrFanWarnUprRpm.setStatus("current")
_ScCtlrFanCritLwrRpm_Type = Unsigned32
_ScCtlrFanCritLwrRpm_Object = MibTableColumn
scCtlrFanCritLwrRpm = _ScCtlrFanCritLwrRpm_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 16, 1, 10),
    _ScCtlrFanCritLwrRpm_Type()
)
scCtlrFanCritLwrRpm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCtlrFanCritLwrRpm.setStatus("current")
_ScCtlrFanCritUprRpm_Type = Unsigned32
_ScCtlrFanCritUprRpm_Object = MibTableColumn
scCtlrFanCritUprRpm = _ScCtlrFanCritUprRpm_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 16, 1, 11),
    _ScCtlrFanCritUprRpm_Type()
)
scCtlrFanCritUprRpm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCtlrFanCritUprRpm.setStatus("current")
_ScCtlrFanForceTrap_Type = SnmpAdminString
_ScCtlrFanForceTrap_Object = MibTableColumn
scCtlrFanForceTrap = _ScCtlrFanForceTrap_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 16, 1, 12),
    _ScCtlrFanForceTrap_Type()
)
scCtlrFanForceTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scCtlrFanForceTrap.setStatus("current")
_ScCtlrFanApiIndex_Type = Unsigned32
_ScCtlrFanApiIndex_Object = MibTableColumn
scCtlrFanApiIndex = _ScCtlrFanApiIndex_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 16, 1, 13),
    _ScCtlrFanApiIndex_Type()
)
scCtlrFanApiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCtlrFanApiIndex.setStatus("current")
_ScCtlrPowerTable_Object = MibTable
scCtlrPowerTable = _ScCtlrPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 17)
)
if mibBuilder.loadTexts:
    scCtlrPowerTable.setStatus("current")
_ScCtlrPowerEntry_Object = MibTableRow
scCtlrPowerEntry = _ScCtlrPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 17, 1)
)
scCtlrPowerEntry.setIndexNames(
    (0, "COMPELLENT-MIB", "scCtlrIndex"),
    (0, "COMPELLENT-MIB", "scCtlrPowerIndex"),
)
if mibBuilder.loadTexts:
    scCtlrPowerEntry.setStatus("current")


class _ScCtlrPowerIndex_Type(Unsigned32):
    """Custom type scCtlrPowerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ScCtlrPowerIndex_Type.__name__ = "Unsigned32"
_ScCtlrPowerIndex_Object = MibTableColumn
scCtlrPowerIndex = _ScCtlrPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 17, 1, 1),
    _ScCtlrPowerIndex_Type()
)
scCtlrPowerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scCtlrPowerIndex.setStatus("current")


class _ScCtlrPowerNbr_Type(Unsigned32):
    """Custom type scCtlrPowerNbr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ScCtlrPowerNbr_Type.__name__ = "Unsigned32"
_ScCtlrPowerNbr_Object = MibTableColumn
scCtlrPowerNbr = _ScCtlrPowerNbr_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 17, 1, 2),
    _ScCtlrPowerNbr_Type()
)
scCtlrPowerNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCtlrPowerNbr.setStatus("current")
_ScCtlrPowerStatus_Type = ScStatus
_ScCtlrPowerStatus_Object = MibTableColumn
scCtlrPowerStatus = _ScCtlrPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 17, 1, 3),
    _ScCtlrPowerStatus_Type()
)
scCtlrPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCtlrPowerStatus.setStatus("current")
_ScCtlrPowerName_Type = SnmpAdminString
_ScCtlrPowerName_Object = MibTableColumn
scCtlrPowerName = _ScCtlrPowerName_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 17, 1, 4),
    _ScCtlrPowerName_Type()
)
scCtlrPowerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCtlrPowerName.setStatus("current")
_ScCtlrPowerForceTrap_Type = SnmpAdminString
_ScCtlrPowerForceTrap_Object = MibTableColumn
scCtlrPowerForceTrap = _ScCtlrPowerForceTrap_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 17, 1, 5),
    _ScCtlrPowerForceTrap_Type()
)
scCtlrPowerForceTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scCtlrPowerForceTrap.setStatus("current")
_ScCtlrVoltageTable_Object = MibTable
scCtlrVoltageTable = _ScCtlrVoltageTable_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 18)
)
if mibBuilder.loadTexts:
    scCtlrVoltageTable.setStatus("current")
_ScCtlrVoltageEntry_Object = MibTableRow
scCtlrVoltageEntry = _ScCtlrVoltageEntry_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 18, 1)
)
scCtlrVoltageEntry.setIndexNames(
    (0, "COMPELLENT-MIB", "scCtlrIndex"),
    (0, "COMPELLENT-MIB", "scCtlrVoltageIndex"),
)
if mibBuilder.loadTexts:
    scCtlrVoltageEntry.setStatus("current")


class _ScCtlrVoltageIndex_Type(Unsigned32):
    """Custom type scCtlrVoltageIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ScCtlrVoltageIndex_Type.__name__ = "Unsigned32"
_ScCtlrVoltageIndex_Object = MibTableColumn
scCtlrVoltageIndex = _ScCtlrVoltageIndex_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 18, 1, 1),
    _ScCtlrVoltageIndex_Type()
)
scCtlrVoltageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scCtlrVoltageIndex.setStatus("current")


class _ScCtlrVoltageNbr_Type(Unsigned32):
    """Custom type scCtlrVoltageNbr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ScCtlrVoltageNbr_Type.__name__ = "Unsigned32"
_ScCtlrVoltageNbr_Object = MibTableColumn
scCtlrVoltageNbr = _ScCtlrVoltageNbr_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 18, 1, 2),
    _ScCtlrVoltageNbr_Type()
)
scCtlrVoltageNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCtlrVoltageNbr.setStatus("current")
_ScCtlrVoltageStatus_Type = ScStatus
_ScCtlrVoltageStatus_Object = MibTableColumn
scCtlrVoltageStatus = _ScCtlrVoltageStatus_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 18, 1, 3),
    _ScCtlrVoltageStatus_Type()
)
scCtlrVoltageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCtlrVoltageStatus.setStatus("current")
_ScCtlrVoltageName_Type = SnmpAdminString
_ScCtlrVoltageName_Object = MibTableColumn
scCtlrVoltageName = _ScCtlrVoltageName_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 18, 1, 4),
    _ScCtlrVoltageName_Type()
)
scCtlrVoltageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCtlrVoltageName.setStatus("current")
_ScCtlrVoltageCurrentV_Type = Unsigned32
_ScCtlrVoltageCurrentV_Object = MibTableColumn
scCtlrVoltageCurrentV = _ScCtlrVoltageCurrentV_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 18, 1, 5),
    _ScCtlrVoltageCurrentV_Type()
)
scCtlrVoltageCurrentV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCtlrVoltageCurrentV.setStatus("current")
_ScCtlrVoltageNormMaxV_Type = Unsigned32
_ScCtlrVoltageNormMaxV_Object = MibTableColumn
scCtlrVoltageNormMaxV = _ScCtlrVoltageNormMaxV_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 18, 1, 6),
    _ScCtlrVoltageNormMaxV_Type()
)
scCtlrVoltageNormMaxV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCtlrVoltageNormMaxV.setStatus("current")
_ScCtlrVoltageNormMinV_Type = Unsigned32
_ScCtlrVoltageNormMinV_Object = MibTableColumn
scCtlrVoltageNormMinV = _ScCtlrVoltageNormMinV_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 18, 1, 7),
    _ScCtlrVoltageNormMinV_Type()
)
scCtlrVoltageNormMinV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCtlrVoltageNormMinV.setStatus("current")
_ScCtlrVoltageWarnLwrV_Type = Unsigned32
_ScCtlrVoltageWarnLwrV_Object = MibTableColumn
scCtlrVoltageWarnLwrV = _ScCtlrVoltageWarnLwrV_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 18, 1, 8),
    _ScCtlrVoltageWarnLwrV_Type()
)
scCtlrVoltageWarnLwrV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCtlrVoltageWarnLwrV.setStatus("current")
_ScCtlrVoltageWarnUprV_Type = Unsigned32
_ScCtlrVoltageWarnUprV_Object = MibTableColumn
scCtlrVoltageWarnUprV = _ScCtlrVoltageWarnUprV_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 18, 1, 9),
    _ScCtlrVoltageWarnUprV_Type()
)
scCtlrVoltageWarnUprV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCtlrVoltageWarnUprV.setStatus("current")
_ScCtlrVoltageCritLwrV_Type = Unsigned32
_ScCtlrVoltageCritLwrV_Object = MibTableColumn
scCtlrVoltageCritLwrV = _ScCtlrVoltageCritLwrV_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 18, 1, 10),
    _ScCtlrVoltageCritLwrV_Type()
)
scCtlrVoltageCritLwrV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCtlrVoltageCritLwrV.setStatus("current")
_ScCtlrVoltageCritUprV_Type = Unsigned32
_ScCtlrVoltageCritUprV_Object = MibTableColumn
scCtlrVoltageCritUprV = _ScCtlrVoltageCritUprV_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 18, 1, 11),
    _ScCtlrVoltageCritUprV_Type()
)
scCtlrVoltageCritUprV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCtlrVoltageCritUprV.setStatus("current")
_ScCtlrVoltageForceTrap_Type = SnmpAdminString
_ScCtlrVoltageForceTrap_Object = MibTableColumn
scCtlrVoltageForceTrap = _ScCtlrVoltageForceTrap_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 18, 1, 12),
    _ScCtlrVoltageForceTrap_Type()
)
scCtlrVoltageForceTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scCtlrVoltageForceTrap.setStatus("current")
_ScCtlrTempTable_Object = MibTable
scCtlrTempTable = _ScCtlrTempTable_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 19)
)
if mibBuilder.loadTexts:
    scCtlrTempTable.setStatus("current")
_ScCtlrTempEntry_Object = MibTableRow
scCtlrTempEntry = _ScCtlrTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 19, 1)
)
scCtlrTempEntry.setIndexNames(
    (0, "COMPELLENT-MIB", "scCtlrIndex"),
    (0, "COMPELLENT-MIB", "scCtlrTempIndex"),
)
if mibBuilder.loadTexts:
    scCtlrTempEntry.setStatus("current")


class _ScCtlrTempIndex_Type(Unsigned32):
    """Custom type scCtlrTempIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ScCtlrTempIndex_Type.__name__ = "Unsigned32"
_ScCtlrTempIndex_Object = MibTableColumn
scCtlrTempIndex = _ScCtlrTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 19, 1, 1),
    _ScCtlrTempIndex_Type()
)
scCtlrTempIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scCtlrTempIndex.setStatus("current")


class _ScCtlrTempNbr_Type(Unsigned32):
    """Custom type scCtlrTempNbr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ScCtlrTempNbr_Type.__name__ = "Unsigned32"
_ScCtlrTempNbr_Object = MibTableColumn
scCtlrTempNbr = _ScCtlrTempNbr_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 19, 1, 2),
    _ScCtlrTempNbr_Type()
)
scCtlrTempNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCtlrTempNbr.setStatus("current")
_ScCtlrTempStatus_Type = ScStatus
_ScCtlrTempStatus_Object = MibTableColumn
scCtlrTempStatus = _ScCtlrTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 19, 1, 3),
    _ScCtlrTempStatus_Type()
)
scCtlrTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCtlrTempStatus.setStatus("current")
_ScCtlrTempName_Type = SnmpAdminString
_ScCtlrTempName_Object = MibTableColumn
scCtlrTempName = _ScCtlrTempName_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 19, 1, 4),
    _ScCtlrTempName_Type()
)
scCtlrTempName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCtlrTempName.setStatus("current")
_ScCtlrTempCurrentC_Type = Unsigned32
_ScCtlrTempCurrentC_Object = MibTableColumn
scCtlrTempCurrentC = _ScCtlrTempCurrentC_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 19, 1, 5),
    _ScCtlrTempCurrentC_Type()
)
scCtlrTempCurrentC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCtlrTempCurrentC.setStatus("current")
_ScCtlrTempNormMaxC_Type = Unsigned32
_ScCtlrTempNormMaxC_Object = MibTableColumn
scCtlrTempNormMaxC = _ScCtlrTempNormMaxC_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 19, 1, 6),
    _ScCtlrTempNormMaxC_Type()
)
scCtlrTempNormMaxC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCtlrTempNormMaxC.setStatus("current")
_ScCtlrTempNormMinC_Type = Unsigned32
_ScCtlrTempNormMinC_Object = MibTableColumn
scCtlrTempNormMinC = _ScCtlrTempNormMinC_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 19, 1, 7),
    _ScCtlrTempNormMinC_Type()
)
scCtlrTempNormMinC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCtlrTempNormMinC.setStatus("current")
_ScCtlrTempWarnLwrC_Type = Unsigned32
_ScCtlrTempWarnLwrC_Object = MibTableColumn
scCtlrTempWarnLwrC = _ScCtlrTempWarnLwrC_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 19, 1, 8),
    _ScCtlrTempWarnLwrC_Type()
)
scCtlrTempWarnLwrC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCtlrTempWarnLwrC.setStatus("current")
_ScCtlrTempWarnUprC_Type = Unsigned32
_ScCtlrTempWarnUprC_Object = MibTableColumn
scCtlrTempWarnUprC = _ScCtlrTempWarnUprC_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 19, 1, 9),
    _ScCtlrTempWarnUprC_Type()
)
scCtlrTempWarnUprC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCtlrTempWarnUprC.setStatus("current")
_ScCtlrTempCritLwrC_Type = Unsigned32
_ScCtlrTempCritLwrC_Object = MibTableColumn
scCtlrTempCritLwrC = _ScCtlrTempCritLwrC_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 19, 1, 10),
    _ScCtlrTempCritLwrC_Type()
)
scCtlrTempCritLwrC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCtlrTempCritLwrC.setStatus("current")
_ScCtlrTempCritUprC_Type = Unsigned32
_ScCtlrTempCritUprC_Object = MibTableColumn
scCtlrTempCritUprC = _ScCtlrTempCritUprC_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 19, 1, 11),
    _ScCtlrTempCritUprC_Type()
)
scCtlrTempCritUprC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCtlrTempCritUprC.setStatus("current")
_ScCtlrTempForceTrap_Type = SnmpAdminString
_ScCtlrTempForceTrap_Object = MibTableColumn
scCtlrTempForceTrap = _ScCtlrTempForceTrap_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 19, 1, 12),
    _ScCtlrTempForceTrap_Type()
)
scCtlrTempForceTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scCtlrTempForceTrap.setStatus("current")
_ScEnclFanTable_Object = MibTable
scEnclFanTable = _ScEnclFanTable_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 20)
)
if mibBuilder.loadTexts:
    scEnclFanTable.setStatus("current")
_ScEnclFanEntry_Object = MibTableRow
scEnclFanEntry = _ScEnclFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 20, 1)
)
scEnclFanEntry.setIndexNames(
    (0, "COMPELLENT-MIB", "scEnclIndex"),
    (0, "COMPELLENT-MIB", "scEnclFanIndex"),
)
if mibBuilder.loadTexts:
    scEnclFanEntry.setStatus("current")


class _ScEnclFanIndex_Type(Unsigned32):
    """Custom type scEnclFanIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ScEnclFanIndex_Type.__name__ = "Unsigned32"
_ScEnclFanIndex_Object = MibTableColumn
scEnclFanIndex = _ScEnclFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 20, 1, 1),
    _ScEnclFanIndex_Type()
)
scEnclFanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scEnclFanIndex.setStatus("current")


class _ScEnclFanNbr_Type(Unsigned32):
    """Custom type scEnclFanNbr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ScEnclFanNbr_Type.__name__ = "Unsigned32"
_ScEnclFanNbr_Object = MibTableColumn
scEnclFanNbr = _ScEnclFanNbr_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 20, 1, 2),
    _ScEnclFanNbr_Type()
)
scEnclFanNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEnclFanNbr.setStatus("current")
_ScEnclFanStatus_Type = ScStatus
_ScEnclFanStatus_Object = MibTableColumn
scEnclFanStatus = _ScEnclFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 20, 1, 3),
    _ScEnclFanStatus_Type()
)
scEnclFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEnclFanStatus.setStatus("current")
_ScEnclFanLocation_Type = SnmpAdminString
_ScEnclFanLocation_Object = MibTableColumn
scEnclFanLocation = _ScEnclFanLocation_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 20, 1, 4),
    _ScEnclFanLocation_Type()
)
scEnclFanLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEnclFanLocation.setStatus("current")
_ScEnclFanCurrentS_Type = SnmpAdminString
_ScEnclFanCurrentS_Object = MibTableColumn
scEnclFanCurrentS = _ScEnclFanCurrentS_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 20, 1, 5),
    _ScEnclFanCurrentS_Type()
)
scEnclFanCurrentS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEnclFanCurrentS.setStatus("current")
_ScEnclFanForceTrap_Type = SnmpAdminString
_ScEnclFanForceTrap_Object = MibTableColumn
scEnclFanForceTrap = _ScEnclFanForceTrap_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 20, 1, 6),
    _ScEnclFanForceTrap_Type()
)
scEnclFanForceTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scEnclFanForceTrap.setStatus("current")
_ScEnclPowerTable_Object = MibTable
scEnclPowerTable = _ScEnclPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 21)
)
if mibBuilder.loadTexts:
    scEnclPowerTable.setStatus("current")
_ScEnclPowerEntry_Object = MibTableRow
scEnclPowerEntry = _ScEnclPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 21, 1)
)
scEnclPowerEntry.setIndexNames(
    (0, "COMPELLENT-MIB", "scEnclIndex"),
    (0, "COMPELLENT-MIB", "scEnclPowerIndex"),
)
if mibBuilder.loadTexts:
    scEnclPowerEntry.setStatus("current")


class _ScEnclPowerIndex_Type(Unsigned32):
    """Custom type scEnclPowerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ScEnclPowerIndex_Type.__name__ = "Unsigned32"
_ScEnclPowerIndex_Object = MibTableColumn
scEnclPowerIndex = _ScEnclPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 21, 1, 1),
    _ScEnclPowerIndex_Type()
)
scEnclPowerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scEnclPowerIndex.setStatus("current")


class _ScEnclPowerNbr_Type(Unsigned32):
    """Custom type scEnclPowerNbr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ScEnclPowerNbr_Type.__name__ = "Unsigned32"
_ScEnclPowerNbr_Object = MibTableColumn
scEnclPowerNbr = _ScEnclPowerNbr_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 21, 1, 2),
    _ScEnclPowerNbr_Type()
)
scEnclPowerNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEnclPowerNbr.setStatus("current")
_ScEnclPowerStatus_Type = ScStatus
_ScEnclPowerStatus_Object = MibTableColumn
scEnclPowerStatus = _ScEnclPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 21, 1, 3),
    _ScEnclPowerStatus_Type()
)
scEnclPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEnclPowerStatus.setStatus("current")
_ScEnclPowerPosition_Type = SnmpAdminString
_ScEnclPowerPosition_Object = MibTableColumn
scEnclPowerPosition = _ScEnclPowerPosition_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 21, 1, 4),
    _ScEnclPowerPosition_Type()
)
scEnclPowerPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEnclPowerPosition.setStatus("current")
_ScEnclPowerForceTrap_Type = SnmpAdminString
_ScEnclPowerForceTrap_Object = MibTableColumn
scEnclPowerForceTrap = _ScEnclPowerForceTrap_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 21, 1, 5),
    _ScEnclPowerForceTrap_Type()
)
scEnclPowerForceTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scEnclPowerForceTrap.setStatus("current")
_ScEnclIoModTable_Object = MibTable
scEnclIoModTable = _ScEnclIoModTable_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 22)
)
if mibBuilder.loadTexts:
    scEnclIoModTable.setStatus("current")
_ScEnclIoModEntry_Object = MibTableRow
scEnclIoModEntry = _ScEnclIoModEntry_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 22, 1)
)
scEnclIoModEntry.setIndexNames(
    (0, "COMPELLENT-MIB", "scEnclIndex"),
    (0, "COMPELLENT-MIB", "scEnclIoModIndex"),
)
if mibBuilder.loadTexts:
    scEnclIoModEntry.setStatus("current")


class _ScEnclIoModIndex_Type(Unsigned32):
    """Custom type scEnclIoModIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ScEnclIoModIndex_Type.__name__ = "Unsigned32"
_ScEnclIoModIndex_Object = MibTableColumn
scEnclIoModIndex = _ScEnclIoModIndex_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 22, 1, 1),
    _ScEnclIoModIndex_Type()
)
scEnclIoModIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scEnclIoModIndex.setStatus("current")


class _ScEnclIoModNbr_Type(Unsigned32):
    """Custom type scEnclIoModNbr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ScEnclIoModNbr_Type.__name__ = "Unsigned32"
_ScEnclIoModNbr_Object = MibTableColumn
scEnclIoModNbr = _ScEnclIoModNbr_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 22, 1, 2),
    _ScEnclIoModNbr_Type()
)
scEnclIoModNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEnclIoModNbr.setStatus("current")
_ScEnclIoModStatus_Type = ScStatus
_ScEnclIoModStatus_Object = MibTableColumn
scEnclIoModStatus = _ScEnclIoModStatus_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 22, 1, 3),
    _ScEnclIoModStatus_Type()
)
scEnclIoModStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEnclIoModStatus.setStatus("current")
_ScEnclIoModPosition_Type = SnmpAdminString
_ScEnclIoModPosition_Object = MibTableColumn
scEnclIoModPosition = _ScEnclIoModPosition_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 22, 1, 4),
    _ScEnclIoModPosition_Type()
)
scEnclIoModPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEnclIoModPosition.setStatus("current")
_ScEnclIoModForceTrap_Type = SnmpAdminString
_ScEnclIoModForceTrap_Object = MibTableColumn
scEnclIoModForceTrap = _ScEnclIoModForceTrap_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 22, 1, 5),
    _ScEnclIoModForceTrap_Type()
)
scEnclIoModForceTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scEnclIoModForceTrap.setStatus("current")
_ScEnclTempTable_Object = MibTable
scEnclTempTable = _ScEnclTempTable_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 23)
)
if mibBuilder.loadTexts:
    scEnclTempTable.setStatus("current")
_ScEnclTempEntry_Object = MibTableRow
scEnclTempEntry = _ScEnclTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 23, 1)
)
scEnclTempEntry.setIndexNames(
    (0, "COMPELLENT-MIB", "scEnclIndex"),
    (0, "COMPELLENT-MIB", "scEnclTempIndex"),
)
if mibBuilder.loadTexts:
    scEnclTempEntry.setStatus("current")


class _ScEnclTempIndex_Type(Unsigned32):
    """Custom type scEnclTempIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ScEnclTempIndex_Type.__name__ = "Unsigned32"
_ScEnclTempIndex_Object = MibTableColumn
scEnclTempIndex = _ScEnclTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 23, 1, 1),
    _ScEnclTempIndex_Type()
)
scEnclTempIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scEnclTempIndex.setStatus("current")


class _ScEnclTempNbr_Type(Unsigned32):
    """Custom type scEnclTempNbr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ScEnclTempNbr_Type.__name__ = "Unsigned32"
_ScEnclTempNbr_Object = MibTableColumn
scEnclTempNbr = _ScEnclTempNbr_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 23, 1, 2),
    _ScEnclTempNbr_Type()
)
scEnclTempNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEnclTempNbr.setStatus("current")
_ScEnclTempStatus_Type = ScStatus
_ScEnclTempStatus_Object = MibTableColumn
scEnclTempStatus = _ScEnclTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 23, 1, 3),
    _ScEnclTempStatus_Type()
)
scEnclTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEnclTempStatus.setStatus("current")
_ScEnclTempLocation_Type = SnmpAdminString
_ScEnclTempLocation_Object = MibTableColumn
scEnclTempLocation = _ScEnclTempLocation_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 23, 1, 4),
    _ScEnclTempLocation_Type()
)
scEnclTempLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEnclTempLocation.setStatus("current")
_ScEnclTempCurrentC_Type = Unsigned32
_ScEnclTempCurrentC_Object = MibTableColumn
scEnclTempCurrentC = _ScEnclTempCurrentC_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 23, 1, 5),
    _ScEnclTempCurrentC_Type()
)
scEnclTempCurrentC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEnclTempCurrentC.setStatus("current")
_ScEnclTempForceTrap_Type = SnmpAdminString
_ScEnclTempForceTrap_Object = MibTableColumn
scEnclTempForceTrap = _ScEnclTempForceTrap_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 23, 1, 6),
    _ScEnclTempForceTrap_Type()
)
scEnclTempForceTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scEnclTempForceTrap.setStatus("current")
_ScEnclAlarmTable_Object = MibTable
scEnclAlarmTable = _ScEnclAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 24)
)
if mibBuilder.loadTexts:
    scEnclAlarmTable.setStatus("current")
_ScEnclAlarmEntry_Object = MibTableRow
scEnclAlarmEntry = _ScEnclAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 24, 1)
)
scEnclAlarmEntry.setIndexNames(
    (0, "COMPELLENT-MIB", "scEnclIndex"),
    (0, "COMPELLENT-MIB", "scEnclAlarmIndex"),
)
if mibBuilder.loadTexts:
    scEnclAlarmEntry.setStatus("current")


class _ScEnclAlarmIndex_Type(Unsigned32):
    """Custom type scEnclAlarmIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ScEnclAlarmIndex_Type.__name__ = "Unsigned32"
_ScEnclAlarmIndex_Object = MibTableColumn
scEnclAlarmIndex = _ScEnclAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 24, 1, 1),
    _ScEnclAlarmIndex_Type()
)
scEnclAlarmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scEnclAlarmIndex.setStatus("current")


class _ScEnclAlarmNbr_Type(Unsigned32):
    """Custom type scEnclAlarmNbr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ScEnclAlarmNbr_Type.__name__ = "Unsigned32"
_ScEnclAlarmNbr_Object = MibTableColumn
scEnclAlarmNbr = _ScEnclAlarmNbr_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 24, 1, 2),
    _ScEnclAlarmNbr_Type()
)
scEnclAlarmNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEnclAlarmNbr.setStatus("current")
_ScEnclAlarmStatus_Type = ScStatus
_ScEnclAlarmStatus_Object = MibTableColumn
scEnclAlarmStatus = _ScEnclAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 24, 1, 3),
    _ScEnclAlarmStatus_Type()
)
scEnclAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEnclAlarmStatus.setStatus("current")
_ScEnclAlarmName_Type = SnmpAdminString
_ScEnclAlarmName_Object = MibTableColumn
scEnclAlarmName = _ScEnclAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 24, 1, 4),
    _ScEnclAlarmName_Type()
)
scEnclAlarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scEnclAlarmName.setStatus("current")
_ScEnclAlarmForceTrap_Type = SnmpAdminString
_ScEnclAlarmForceTrap_Object = MibTableColumn
scEnclAlarmForceTrap = _ScEnclAlarmForceTrap_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 24, 1, 5),
    _ScEnclAlarmForceTrap_Type()
)
scEnclAlarmForceTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scEnclAlarmForceTrap.setStatus("current")
_ScDiskFolderTable_Object = MibTable
scDiskFolderTable = _ScDiskFolderTable_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 25)
)
if mibBuilder.loadTexts:
    scDiskFolderTable.setStatus("current")
_ScDiskFolderEntry_Object = MibTableRow
scDiskFolderEntry = _ScDiskFolderEntry_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 25, 1)
)
scDiskFolderEntry.setIndexNames(
    (0, "COMPELLENT-MIB", "scDiskFolderIndex"),
)
if mibBuilder.loadTexts:
    scDiskFolderEntry.setStatus("current")


class _ScDiskFolderIndex_Type(Unsigned32):
    """Custom type scDiskFolderIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_ScDiskFolderIndex_Type.__name__ = "Unsigned32"
_ScDiskFolderIndex_Object = MibTableColumn
scDiskFolderIndex = _ScDiskFolderIndex_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 25, 1, 1),
    _ScDiskFolderIndex_Type()
)
scDiskFolderIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scDiskFolderIndex.setStatus("current")


class _ScDiskFolderNbr_Type(Unsigned32):
    """Custom type scDiskFolderNbr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_ScDiskFolderNbr_Type.__name__ = "Unsigned32"
_ScDiskFolderNbr_Object = MibTableColumn
scDiskFolderNbr = _ScDiskFolderNbr_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 25, 1, 2),
    _ScDiskFolderNbr_Type()
)
scDiskFolderNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scDiskFolderNbr.setStatus("current")
_ScDiskFolderStatus_Type = ScStatus
_ScDiskFolderStatus_Object = MibTableColumn
scDiskFolderStatus = _ScDiskFolderStatus_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 25, 1, 3),
    _ScDiskFolderStatus_Type()
)
scDiskFolderStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scDiskFolderStatus.setStatus("current")
_ScDiskFolderName_Type = SnmpAdminString
_ScDiskFolderName_Object = MibTableColumn
scDiskFolderName = _ScDiskFolderName_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 25, 1, 4),
    _ScDiskFolderName_Type()
)
scDiskFolderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scDiskFolderName.setStatus("current")
_ScDiskFolderCapcty_Type = Unsigned32
_ScDiskFolderCapcty_Object = MibTableColumn
scDiskFolderCapcty = _ScDiskFolderCapcty_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 25, 1, 5),
    _ScDiskFolderCapcty_Type()
)
scDiskFolderCapcty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scDiskFolderCapcty.setStatus("current")
_ScDiskFolderAlrtThr_Type = Unsigned32
_ScDiskFolderAlrtThr_Object = MibTableColumn
scDiskFolderAlrtThr = _ScDiskFolderAlrtThr_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 25, 1, 6),
    _ScDiskFolderAlrtThr_Type()
)
scDiskFolderAlrtThr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scDiskFolderAlrtThr.setStatus("current")
_ScDiskFolderApiIndex_Type = Unsigned32
_ScDiskFolderApiIndex_Object = MibTableColumn
scDiskFolderApiIndex = _ScDiskFolderApiIndex_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 25, 1, 7),
    _ScDiskFolderApiIndex_Type()
)
scDiskFolderApiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scDiskFolderApiIndex.setStatus("current")
_ScDiskFolderForceTrap_Type = SnmpAdminString
_ScDiskFolderForceTrap_Object = MibTableColumn
scDiskFolderForceTrap = _ScDiskFolderForceTrap_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 25, 1, 8),
    _ScDiskFolderForceTrap_Type()
)
scDiskFolderForceTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scDiskFolderForceTrap.setStatus("current")
_ScVolumeTable_Object = MibTable
scVolumeTable = _ScVolumeTable_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 26)
)
if mibBuilder.loadTexts:
    scVolumeTable.setStatus("current")
_ScVolumeEntry_Object = MibTableRow
scVolumeEntry = _ScVolumeEntry_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 26, 1)
)
scVolumeEntry.setIndexNames(
    (0, "COMPELLENT-MIB", "scVolumeIndex"),
)
if mibBuilder.loadTexts:
    scVolumeEntry.setStatus("current")


class _ScVolumeIndex_Type(Unsigned32):
    """Custom type scVolumeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4000),
    )


_ScVolumeIndex_Type.__name__ = "Unsigned32"
_ScVolumeIndex_Object = MibTableColumn
scVolumeIndex = _ScVolumeIndex_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 26, 1, 1),
    _ScVolumeIndex_Type()
)
scVolumeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scVolumeIndex.setStatus("current")


class _ScVolumeNbr_Type(Unsigned32):
    """Custom type scVolumeNbr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4000),
    )


_ScVolumeNbr_Type.__name__ = "Unsigned32"
_ScVolumeNbr_Object = MibTableColumn
scVolumeNbr = _ScVolumeNbr_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 26, 1, 2),
    _ScVolumeNbr_Type()
)
scVolumeNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scVolumeNbr.setStatus("current")
_ScVolumeStatus_Type = ScStatus
_ScVolumeStatus_Object = MibTableColumn
scVolumeStatus = _ScVolumeStatus_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 26, 1, 3),
    _ScVolumeStatus_Type()
)
scVolumeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scVolumeStatus.setStatus("current")
_ScVolumeName_Type = SnmpAdminString
_ScVolumeName_Object = MibTableColumn
scVolumeName = _ScVolumeName_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 26, 1, 4),
    _ScVolumeName_Type()
)
scVolumeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scVolumeName.setStatus("current")
_ScVolumeApiIndex_Type = Unsigned32
_ScVolumeApiIndex_Object = MibTableColumn
scVolumeApiIndex = _ScVolumeApiIndex_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 26, 1, 5),
    _ScVolumeApiIndex_Type()
)
scVolumeApiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scVolumeApiIndex.setStatus("current")
_ScVolumeForceTrap_Type = SnmpAdminString
_ScVolumeForceTrap_Object = MibTableColumn
scVolumeForceTrap = _ScVolumeForceTrap_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 26, 1, 6),
    _ScVolumeForceTrap_Type()
)
scVolumeForceTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scVolumeForceTrap.setStatus("current")
_ScServerTable_Object = MibTable
scServerTable = _ScServerTable_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 27)
)
if mibBuilder.loadTexts:
    scServerTable.setStatus("current")
_ScServerEntry_Object = MibTableRow
scServerEntry = _ScServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 27, 1)
)
scServerEntry.setIndexNames(
    (0, "COMPELLENT-MIB", "scServerIndex"),
)
if mibBuilder.loadTexts:
    scServerEntry.setStatus("current")


class _ScServerIndex_Type(Unsigned32):
    """Custom type scServerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_ScServerIndex_Type.__name__ = "Unsigned32"
_ScServerIndex_Object = MibTableColumn
scServerIndex = _ScServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 27, 1, 1),
    _ScServerIndex_Type()
)
scServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scServerIndex.setStatus("current")


class _ScServerNbr_Type(Unsigned32):
    """Custom type scServerNbr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_ScServerNbr_Type.__name__ = "Unsigned32"
_ScServerNbr_Object = MibTableColumn
scServerNbr = _ScServerNbr_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 27, 1, 2),
    _ScServerNbr_Type()
)
scServerNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scServerNbr.setStatus("current")
_ScServerStatus_Type = ScStatus
_ScServerStatus_Object = MibTableColumn
scServerStatus = _ScServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 27, 1, 3),
    _ScServerStatus_Type()
)
scServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scServerStatus.setStatus("current")
_ScServerName_Type = SnmpAdminString
_ScServerName_Object = MibTableColumn
scServerName = _ScServerName_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 27, 1, 4),
    _ScServerName_Type()
)
scServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scServerName.setStatus("current")


class _ScServerCnctvy_Type(Integer32):
    """Custom type scServerCnctvy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("partial", 3),
          ("up", 1))
    )


_ScServerCnctvy_Type.__name__ = "Integer32"
_ScServerCnctvy_Object = MibTableColumn
scServerCnctvy = _ScServerCnctvy_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 27, 1, 5),
    _ScServerCnctvy_Type()
)
scServerCnctvy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scServerCnctvy.setStatus("current")
_ScServerPathCount_Type = Unsigned32
_ScServerPathCount_Object = MibTableColumn
scServerPathCount = _ScServerPathCount_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 27, 1, 6),
    _ScServerPathCount_Type()
)
scServerPathCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scServerPathCount.setStatus("current")
_ScServerApiIndex_Type = Unsigned32
_ScServerApiIndex_Object = MibTableColumn
scServerApiIndex = _ScServerApiIndex_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 27, 1, 7),
    _ScServerApiIndex_Type()
)
scServerApiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scServerApiIndex.setStatus("current")
_ScServerForceTrap_Type = SnmpAdminString
_ScServerForceTrap_Object = MibTableColumn
scServerForceTrap = _ScServerForceTrap_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 27, 1, 8),
    _ScServerForceTrap_Type()
)
scServerForceTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scServerForceTrap.setStatus("current")
_ScCacheTable_Object = MibTable
scCacheTable = _ScCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 28)
)
if mibBuilder.loadTexts:
    scCacheTable.setStatus("current")
_ScCacheEntry_Object = MibTableRow
scCacheEntry = _ScCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 28, 1)
)
scCacheEntry.setIndexNames(
    (0, "COMPELLENT-MIB", "scCacheIndex"),
)
if mibBuilder.loadTexts:
    scCacheEntry.setStatus("current")


class _ScCacheIndex_Type(Unsigned32):
    """Custom type scCacheIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ScCacheIndex_Type.__name__ = "Unsigned32"
_ScCacheIndex_Object = MibTableColumn
scCacheIndex = _ScCacheIndex_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 28, 1, 1),
    _ScCacheIndex_Type()
)
scCacheIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scCacheIndex.setStatus("current")


class _ScCacheNbr_Type(Unsigned32):
    """Custom type scCacheNbr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ScCacheNbr_Type.__name__ = "Unsigned32"
_ScCacheNbr_Object = MibTableColumn
scCacheNbr = _ScCacheNbr_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 28, 1, 2),
    _ScCacheNbr_Type()
)
scCacheNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCacheNbr.setStatus("current")
_ScCacheStatus_Type = ScStatus
_ScCacheStatus_Object = MibTableColumn
scCacheStatus = _ScCacheStatus_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 28, 1, 3),
    _ScCacheStatus_Type()
)
scCacheStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCacheStatus.setStatus("current")
_ScCacheName_Type = SnmpAdminString
_ScCacheName_Object = MibTableColumn
scCacheName = _ScCacheName_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 28, 1, 4),
    _ScCacheName_Type()
)
scCacheName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCacheName.setStatus("current")


class _ScCacheBatStat_Type(Integer32):
    """Custom type scCacheBatStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("expirationPending", 2),
          ("expired", 3),
          ("noBattery", 0),
          ("normal", 1))
    )


_ScCacheBatStat_Type.__name__ = "Integer32"
_ScCacheBatStat_Object = MibTableColumn
scCacheBatStat = _ScCacheBatStat_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 28, 1, 5),
    _ScCacheBatStat_Type()
)
scCacheBatStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCacheBatStat.setStatus("current")
_ScCacheBatExpr_Type = DateAndTime
_ScCacheBatExpr_Object = MibTableColumn
scCacheBatExpr = _ScCacheBatExpr_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 28, 1, 6),
    _ScCacheBatExpr_Type()
)
scCacheBatExpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCacheBatExpr.setStatus("current")
_ScCacheForceTrap_Type = SnmpAdminString
_ScCacheForceTrap_Object = MibTableColumn
scCacheForceTrap = _ScCacheForceTrap_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 28, 1, 7),
    _ScCacheForceTrap_Type()
)
scCacheForceTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scCacheForceTrap.setStatus("current")
_ScScTable_Object = MibTable
scScTable = _ScScTable_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 29)
)
if mibBuilder.loadTexts:
    scScTable.setStatus("current")
_ScScEntry_Object = MibTableRow
scScEntry = _ScScEntry_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 29, 1)
)
scScEntry.setIndexNames(
    (0, "COMPELLENT-MIB", "scScIndex"),
)
if mibBuilder.loadTexts:
    scScEntry.setStatus("current")


class _ScScIndex_Type(Unsigned32):
    """Custom type scScIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ScScIndex_Type.__name__ = "Unsigned32"
_ScScIndex_Object = MibTableColumn
scScIndex = _ScScIndex_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 29, 1, 1),
    _ScScIndex_Type()
)
scScIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scScIndex.setStatus("current")


class _ScScNbr_Type(Unsigned32):
    """Custom type scScNbr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ScScNbr_Type.__name__ = "Unsigned32"
_ScScNbr_Object = MibTableColumn
scScNbr = _ScScNbr_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 29, 1, 2),
    _ScScNbr_Type()
)
scScNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scScNbr.setStatus("current")
_ScScStatus_Type = ScStatus
_ScScStatus_Object = MibTableColumn
scScStatus = _ScScStatus_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 29, 1, 3),
    _ScScStatus_Type()
)
scScStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scScStatus.setStatus("current")
_ScScName_Type = SnmpAdminString
_ScScName_Object = MibTableColumn
scScName = _ScScName_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 29, 1, 4),
    _ScScName_Type()
)
scScName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scScName.setStatus("current")
_ScScContact_Type = SnmpAdminString
_ScScContact_Object = MibTableColumn
scScContact = _ScScContact_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 29, 1, 5),
    _ScScContact_Type()
)
scScContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scScContact.setStatus("current")
_ScScLocation_Type = SnmpAdminString
_ScScLocation_Object = MibTableColumn
scScLocation = _ScScLocation_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 29, 1, 6),
    _ScScLocation_Type()
)
scScLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scScLocation.setStatus("current")
_ScScPortsBal_Type = TruthValue
_ScScPortsBal_Object = MibTableColumn
scScPortsBal = _ScScPortsBal_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 29, 1, 7),
    _ScScPortsBal_Type()
)
scScPortsBal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scScPortsBal.setStatus("current")
_ScScMgmtIP_Type = SnmpAdminString
_ScScMgmtIP_Object = MibTableColumn
scScMgmtIP = _ScScMgmtIP_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 29, 1, 8),
    _ScScMgmtIP_Type()
)
scScMgmtIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scScMgmtIP.setStatus("current")
_ScScSerial_Type = Unsigned32
_ScScSerial_Object = MibTableColumn
scScSerial = _ScScSerial_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 29, 1, 9),
    _ScScSerial_Type()
)
scScSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scScSerial.setStatus("current")
_ScScForceTrap_Type = SnmpAdminString
_ScScForceTrap_Object = MibTableColumn
scScForceTrap = _ScScForceTrap_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 29, 1, 10),
    _ScScForceTrap_Type()
)
scScForceTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scScForceTrap.setStatus("current")
_ScUPSTable_Object = MibTable
scUPSTable = _ScUPSTable_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 30)
)
if mibBuilder.loadTexts:
    scUPSTable.setStatus("current")
_ScUPSEntry_Object = MibTableRow
scUPSEntry = _ScUPSEntry_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 30, 1)
)
scUPSEntry.setIndexNames(
    (0, "COMPELLENT-MIB", "scUPSIndex"),
)
if mibBuilder.loadTexts:
    scUPSEntry.setStatus("current")


class _ScUPSIndex_Type(Unsigned32):
    """Custom type scUPSIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ScUPSIndex_Type.__name__ = "Unsigned32"
_ScUPSIndex_Object = MibTableColumn
scUPSIndex = _ScUPSIndex_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 30, 1, 1),
    _ScUPSIndex_Type()
)
scUPSIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scUPSIndex.setStatus("current")


class _ScUPSNbr_Type(Unsigned32):
    """Custom type scUPSNbr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ScUPSNbr_Type.__name__ = "Unsigned32"
_ScUPSNbr_Object = MibTableColumn
scUPSNbr = _ScUPSNbr_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 30, 1, 2),
    _ScUPSNbr_Type()
)
scUPSNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scUPSNbr.setStatus("current")
_ScUPSStatus_Type = ScStatus
_ScUPSStatus_Object = MibTableColumn
scUPSStatus = _ScUPSStatus_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 30, 1, 3),
    _ScUPSStatus_Type()
)
scUPSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scUPSStatus.setStatus("current")
_ScUPSName_Type = SnmpAdminString
_ScUPSName_Object = MibTableColumn
scUPSName = _ScUPSName_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 30, 1, 4),
    _ScUPSName_Type()
)
scUPSName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scUPSName.setStatus("current")
_ScUPSBatLife_Type = SnmpAdminString
_ScUPSBatLife_Object = MibTableColumn
scUPSBatLife = _ScUPSBatLife_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 30, 1, 5),
    _ScUPSBatLife_Type()
)
scUPSBatLife.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scUPSBatLife.setStatus("current")
_ScUPSStatusDescr_Type = SnmpAdminString
_ScUPSStatusDescr_Object = MibTableColumn
scUPSStatusDescr = _ScUPSStatusDescr_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 30, 1, 6),
    _ScUPSStatusDescr_Type()
)
scUPSStatusDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scUPSStatusDescr.setStatus("current")
_ScUPSApiIndex_Type = Unsigned32
_ScUPSApiIndex_Object = MibTableColumn
scUPSApiIndex = _ScUPSApiIndex_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 30, 1, 7),
    _ScUPSApiIndex_Type()
)
scUPSApiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scUPSApiIndex.setStatus("current")
_ScUPSForceTrap_Type = SnmpAdminString
_ScUPSForceTrap_Object = MibTableColumn
scUPSForceTrap = _ScUPSForceTrap_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 30, 1, 8),
    _ScUPSForceTrap_Type()
)
scUPSForceTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scUPSForceTrap.setStatus("current")
_ScObjCntTable_Object = MibTable
scObjCntTable = _ScObjCntTable_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 31)
)
if mibBuilder.loadTexts:
    scObjCntTable.setStatus("current")
_ScObjCntEntry_Object = MibTableRow
scObjCntEntry = _ScObjCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 31, 1)
)
scObjCntEntry.setIndexNames(
    (0, "COMPELLENT-MIB", "scObjCntIndex"),
)
if mibBuilder.loadTexts:
    scObjCntEntry.setStatus("current")


class _ScObjCntIndex_Type(Unsigned32):
    """Custom type scObjCntIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ScObjCntIndex_Type.__name__ = "Unsigned32"
_ScObjCntIndex_Object = MibTableColumn
scObjCntIndex = _ScObjCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 31, 1, 1),
    _ScObjCntIndex_Type()
)
scObjCntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scObjCntIndex.setStatus("current")


class _ScObjCntNbr_Type(Unsigned32):
    """Custom type scObjCntNbr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ScObjCntNbr_Type.__name__ = "Unsigned32"
_ScObjCntNbr_Object = MibTableColumn
scObjCntNbr = _ScObjCntNbr_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 31, 1, 2),
    _ScObjCntNbr_Type()
)
scObjCntNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scObjCntNbr.setStatus("current")
_ScObjCntDevsInUse_Type = Unsigned32
_ScObjCntDevsInUse_Object = MibTableColumn
scObjCntDevsInUse = _ScObjCntDevsInUse_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 31, 1, 3),
    _ScObjCntDevsInUse_Type()
)
scObjCntDevsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scObjCntDevsInUse.setStatus("current")
_ScObjCntReplays_Type = Unsigned32
_ScObjCntReplays_Object = MibTableColumn
scObjCntReplays = _ScObjCntReplays_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 31, 1, 4),
    _ScObjCntReplays_Type()
)
scObjCntReplays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scObjCntReplays.setStatus("current")
_ScObjCntDisks_Type = Unsigned32
_ScObjCntDisks_Object = MibTableColumn
scObjCntDisks = _ScObjCntDisks_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 31, 1, 5),
    _ScObjCntDisks_Type()
)
scObjCntDisks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scObjCntDisks.setStatus("current")
_ScObjCntServers_Type = Unsigned32
_ScObjCntServers_Object = MibTableColumn
scObjCntServers = _ScObjCntServers_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 31, 1, 6),
    _ScObjCntServers_Type()
)
scObjCntServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scObjCntServers.setStatus("current")
_ScObjCntVolumes_Type = Unsigned32
_ScObjCntVolumes_Object = MibTableColumn
scObjCntVolumes = _ScObjCntVolumes_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 31, 1, 7),
    _ScObjCntVolumes_Type()
)
scObjCntVolumes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scObjCntVolumes.setStatus("current")
_ScDiskFolderSUTable_Object = MibTable
scDiskFolderSUTable = _ScDiskFolderSUTable_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 32)
)
if mibBuilder.loadTexts:
    scDiskFolderSUTable.setStatus("current")
_ScDiskFolderSUEntry_Object = MibTableRow
scDiskFolderSUEntry = _ScDiskFolderSUEntry_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 32, 1)
)
scDiskFolderSUEntry.setIndexNames(
    (0, "COMPELLENT-MIB", "scDiskFolderSUIndex"),
)
if mibBuilder.loadTexts:
    scDiskFolderSUEntry.setStatus("current")


class _ScDiskFolderSUIndex_Type(Unsigned32):
    """Custom type scDiskFolderSUIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_ScDiskFolderSUIndex_Type.__name__ = "Unsigned32"
_ScDiskFolderSUIndex_Object = MibTableColumn
scDiskFolderSUIndex = _ScDiskFolderSUIndex_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 32, 1, 1),
    _ScDiskFolderSUIndex_Type()
)
scDiskFolderSUIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scDiskFolderSUIndex.setStatus("current")


class _ScDiskFolderSUNbr_Type(Unsigned32):
    """Custom type scDiskFolderSUNbr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_ScDiskFolderSUNbr_Type.__name__ = "Unsigned32"
_ScDiskFolderSUNbr_Object = MibTableColumn
scDiskFolderSUNbr = _ScDiskFolderSUNbr_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 32, 1, 2),
    _ScDiskFolderSUNbr_Type()
)
scDiskFolderSUNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scDiskFolderSUNbr.setStatus("current")
_ScDiskFolderSUTotalSpace_Type = Unsigned32
_ScDiskFolderSUTotalSpace_Object = MibTableColumn
scDiskFolderSUTotalSpace = _ScDiskFolderSUTotalSpace_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 32, 1, 3),
    _ScDiskFolderSUTotalSpace_Type()
)
scDiskFolderSUTotalSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scDiskFolderSUTotalSpace.setStatus("current")
_ScDiskFolderSUUsedSpace_Type = Unsigned32
_ScDiskFolderSUUsedSpace_Object = MibTableColumn
scDiskFolderSUUsedSpace = _ScDiskFolderSUUsedSpace_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 32, 1, 4),
    _ScDiskFolderSUUsedSpace_Type()
)
scDiskFolderSUUsedSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scDiskFolderSUUsedSpace.setStatus("current")


class _ScSIDeviceType_Type(Integer32):
    """Custom type scSIDeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disk", 1),
          ("unknown", 2))
    )


_ScSIDeviceType_Type.__name__ = "Integer32"
_ScSIDeviceType_Object = MibScalar
scSIDeviceType = _ScSIDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 33),
    _ScSIDeviceType_Type()
)
scSIDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scSIDeviceType.setStatus("current")
_ScSIDeviceStatus_Type = ScStatus
_ScSIDeviceStatus_Object = MibScalar
scSIDeviceStatus = _ScSIDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 34),
    _ScSIDeviceStatus_Type()
)
scSIDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scSIDeviceStatus.setStatus("current")
_ScHWCompStatus_Type = ScStatus
_ScHWCompStatus_Object = MibScalar
scHWCompStatus = _ScHWCompStatus_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 35),
    _ScHWCompStatus_Type()
)
scHWCompStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scHWCompStatus.setStatus("current")
_ScHWCompName_Type = SnmpAdminString
_ScHWCompName_Object = MibScalar
scHWCompName = _ScHWCompName_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 36),
    _ScHWCompName_Type()
)
scHWCompName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scHWCompName.setStatus("current")
_ScHWCompPosition_Type = SnmpAdminString
_ScHWCompPosition_Object = MibScalar
scHWCompPosition = _ScHWCompPosition_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 37),
    _ScHWCompPosition_Type()
)
scHWCompPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scHWCompPosition.setStatus("current")
_ScHWCompType_Type = ScHardwareType
_ScHWCompType_Object = MibScalar
scHWCompType = _ScHWCompType_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 38),
    _ScHWCompType_Type()
)
scHWCompType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scHWCompType.setStatus("current")
_ScHWCompState_Type = SnmpAdminString
_ScHWCompState_Object = MibScalar
scHWCompState = _ScHWCompState_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 39),
    _ScHWCompState_Type()
)
scHWCompState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scHWCompState.setStatus("current")
_ScTrapAction_Type = SnmpAdminString
_ScTrapAction_Object = MibScalar
scTrapAction = _ScTrapAction_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 40),
    _ScTrapAction_Type()
)
scTrapAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scTrapAction.setStatus("current")
_ScAlertMsg_Type = SnmpAdminString
_ScAlertMsg_Object = MibScalar
scAlertMsg = _ScAlertMsg_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 41),
    _ScAlertMsg_Type()
)
scAlertMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scAlertMsg.setStatus("current")
_ScForceTrap_Type = SnmpAdminString
_ScForceTrap_Object = MibScalar
scForceTrap = _ScForceTrap_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 42),
    _ScForceTrap_Type()
)
scForceTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scForceTrap.setStatus("current")
_ScTrapNormalized_Type = TruthValue
_ScTrapNormalized_Object = MibScalar
scTrapNormalized = _ScTrapNormalized_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 43),
    _ScTrapNormalized_Type()
)
scTrapNormalized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scTrapNormalized.setStatus("current")
_ScLastWorstAlert_Type = Unsigned32
_ScLastWorstAlert_Object = MibScalar
scLastWorstAlert = _ScLastWorstAlert_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 44),
    _ScLastWorstAlert_Type()
)
scLastWorstAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scLastWorstAlert.setStatus("current")
_ScDiskConfigTable_Object = MibTable
scDiskConfigTable = _ScDiskConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 45)
)
if mibBuilder.loadTexts:
    scDiskConfigTable.setStatus("current")
_ScDiskConfigEntry_Object = MibTableRow
scDiskConfigEntry = _ScDiskConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 45, 1)
)
scDiskConfigEntry.setIndexNames(
    (0, "COMPELLENT-MIB", "scDiskConfigIndex"),
)
if mibBuilder.loadTexts:
    scDiskConfigEntry.setStatus("current")


class _ScDiskConfigIndex_Type(Unsigned32):
    """Custom type scDiskConfigIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_ScDiskConfigIndex_Type.__name__ = "Unsigned32"
_ScDiskConfigIndex_Object = MibTableColumn
scDiskConfigIndex = _ScDiskConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 45, 1, 1),
    _ScDiskConfigIndex_Type()
)
scDiskConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scDiskConfigIndex.setStatus("current")


class _ScDiskConfigNbr_Type(Unsigned32):
    """Custom type scDiskConfigNbr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_ScDiskConfigNbr_Type.__name__ = "Unsigned32"
_ScDiskConfigNbr_Object = MibTableColumn
scDiskConfigNbr = _ScDiskConfigNbr_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 45, 1, 2),
    _ScDiskConfigNbr_Type()
)
scDiskConfigNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scDiskConfigNbr.setStatus("current")
_ScDiskConfigSerial_Type = SnmpAdminString
_ScDiskConfigSerial_Object = MibTableColumn
scDiskConfigSerial = _ScDiskConfigSerial_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 45, 1, 3),
    _ScDiskConfigSerial_Type()
)
scDiskConfigSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scDiskConfigSerial.setStatus("current")
_ScDiskConfigVendor_Type = SnmpAdminString
_ScDiskConfigVendor_Object = MibTableColumn
scDiskConfigVendor = _ScDiskConfigVendor_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 45, 1, 4),
    _ScDiskConfigVendor_Type()
)
scDiskConfigVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scDiskConfigVendor.setStatus("current")
_ScDiskConfigProduct_Type = SnmpAdminString
_ScDiskConfigProduct_Object = MibTableColumn
scDiskConfigProduct = _ScDiskConfigProduct_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 45, 1, 5),
    _ScDiskConfigProduct_Type()
)
scDiskConfigProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scDiskConfigProduct.setStatus("current")
_ScDiskConfigModel_Type = SnmpAdminString
_ScDiskConfigModel_Object = MibTableColumn
scDiskConfigModel = _ScDiskConfigModel_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 45, 1, 6),
    _ScDiskConfigModel_Type()
)
scDiskConfigModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scDiskConfigModel.setStatus("current")
_ScDiskConfigRev_Type = SnmpAdminString
_ScDiskConfigRev_Object = MibTableColumn
scDiskConfigRev = _ScDiskConfigRev_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 45, 1, 7),
    _ScDiskConfigRev_Type()
)
scDiskConfigRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scDiskConfigRev.setStatus("current")
_ScDiskConfigApiIndex_Type = Unsigned32
_ScDiskConfigApiIndex_Object = MibTableColumn
scDiskConfigApiIndex = _ScDiskConfigApiIndex_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 45, 1, 8),
    _ScDiskConfigApiIndex_Type()
)
scDiskConfigApiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scDiskConfigApiIndex.setStatus("current")
_ScAlertTable_Object = MibTable
scAlertTable = _ScAlertTable_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 46)
)
if mibBuilder.loadTexts:
    scAlertTable.setStatus("current")
_ScAlertEntry_Object = MibTableRow
scAlertEntry = _ScAlertEntry_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 46, 1)
)
scAlertEntry.setIndexNames(
    (0, "COMPELLENT-MIB", "scCtlrIndex"),
    (0, "COMPELLENT-MIB", "scAlertIndex"),
)
if mibBuilder.loadTexts:
    scAlertEntry.setStatus("current")


class _ScAlertIndex_Type(Unsigned32):
    """Custom type scAlertIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_ScAlertIndex_Type.__name__ = "Unsigned32"
_ScAlertIndex_Object = MibTableColumn
scAlertIndex = _ScAlertIndex_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 46, 1, 1),
    _ScAlertIndex_Type()
)
scAlertIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scAlertIndex.setStatus("current")


class _ScAlertNbr_Type(Unsigned32):
    """Custom type scAlertNbr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_ScAlertNbr_Type.__name__ = "Unsigned32"
_ScAlertNbr_Object = MibTableColumn
scAlertNbr = _ScAlertNbr_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 46, 1, 2),
    _ScAlertNbr_Type()
)
scAlertNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scAlertNbr.setStatus("current")


class _ScAlertStatus_Type(Integer32):
    """Custom type scAlertStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("complete", 0),
          ("critical", 1),
          ("degraded", 2),
          ("deleting", 3),
          ("down", 4),
          ("emergency", 5),
          ("inform", 6),
          ("okay", 7),
          ("unavailable", 8),
          ("unknown", 9))
    )


_ScAlertStatus_Type.__name__ = "Integer32"
_ScAlertStatus_Object = MibTableColumn
scAlertStatus = _ScAlertStatus_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 46, 1, 3),
    _ScAlertStatus_Type()
)
scAlertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scAlertStatus.setStatus("current")
_ScAlertApiIndex_Type = Unsigned32
_ScAlertApiIndex_Object = MibTableColumn
scAlertApiIndex = _ScAlertApiIndex_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 46, 1, 4),
    _ScAlertApiIndex_Type()
)
scAlertApiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scAlertApiIndex.setStatus("current")
_ScAlertDefinition_Type = SnmpAdminString
_ScAlertDefinition_Object = MibTableColumn
scAlertDefinition = _ScAlertDefinition_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 46, 1, 5),
    _ScAlertDefinition_Type()
)
scAlertDefinition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scAlertDefinition.setStatus("current")


class _ScAlertCategory_Type(Integer32):
    """Custom type scAlertCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("connectivity", 0),
          ("disk", 1),
          ("hardware", 2),
          ("storage", 3),
          ("system", 4),
          ("unknown", 5))
    )


_ScAlertCategory_Type.__name__ = "Integer32"
_ScAlertCategory_Object = MibTableColumn
scAlertCategory = _ScAlertCategory_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 46, 1, 6),
    _ScAlertCategory_Type()
)
scAlertCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scAlertCategory.setStatus("current")
_ScAlertCreateTime_Type = SnmpAdminString
_ScAlertCreateTime_Object = MibTableColumn
scAlertCreateTime = _ScAlertCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 46, 1, 7),
    _ScAlertCreateTime_Type()
)
scAlertCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scAlertCreateTime.setStatus("current")
_ScAlertMessage_Type = SnmpAdminString
_ScAlertMessage_Object = MibTableColumn
scAlertMessage = _ScAlertMessage_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 46, 1, 8),
    _ScAlertMessage_Type()
)
scAlertMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scAlertMessage.setStatus("current")


class _ScAlertType_Type(Integer32):
    """Custom type scAlertType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alert", 0),
          ("indiction", 1),
          ("unknown", 3))
    )


_ScAlertType_Type.__name__ = "Integer32"
_ScAlertType_Object = MibTableColumn
scAlertType = _ScAlertType_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 46, 1, 9),
    _ScAlertType_Type()
)
scAlertType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scAlertType.setStatus("current")
_ScAlertAcknowledged_Type = TruthValue
_ScAlertAcknowledged_Object = MibTableColumn
scAlertAcknowledged = _ScAlertAcknowledged_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 46, 1, 10),
    _ScAlertAcknowledged_Type()
)
scAlertAcknowledged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scAlertAcknowledged.setStatus("current")
_ScAlertActive_Type = TruthValue
_ScAlertActive_Object = MibTableColumn
scAlertActive = _ScAlertActive_Object(
    (1, 3, 6, 1, 4, 1, 16139, 2, 46, 1, 11),
    _ScAlertActive_Type()
)
scAlertActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scAlertActive.setStatus("current")
_CompellentConformance_ObjectIdentity = ObjectIdentity
compellentConformance = _CompellentConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16139, 3)
)
if mibBuilder.loadTexts:
    compellentConformance.setStatus("current")
_CompellentCompliances_ObjectIdentity = ObjectIdentity
compellentCompliances = _CompellentCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16139, 3, 1)
)
if mibBuilder.loadTexts:
    compellentCompliances.setStatus("current")
_CompellentGroups_ObjectIdentity = ObjectIdentity
compellentGroups = _CompellentGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16139, 3, 2)
)
if mibBuilder.loadTexts:
    compellentGroups.setStatus("current")
_CompellentTrapsNotif_ObjectIdentity = ObjectIdentity
compellentTrapsNotif = _CompellentTrapsNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16139, 251)
)
if mibBuilder.loadTexts:
    compellentTrapsNotif.setStatus("current")
_TrapSevPrefix_ObjectIdentity = ObjectIdentity
trapSevPrefix = _TrapSevPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16139, 251, 0)
)
if mibBuilder.loadTexts:
    trapSevPrefix.setStatus("current")

# Managed Objects groups

compellentObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16139, 3, 2, 3)
)
compellentObjectsGroup.setObjects(
      *(("COMPELLENT-MIB", "scAlertDef"),
        ("COMPELLENT-MIB", "scIndex"),
        ("COMPELLENT-MIB", "scTestString"),
        ("COMPELLENT-MIB", "scMiscAlertString"),
        ("COMPELLENT-MIB", "scDiskNbr"),
        ("COMPELLENT-MIB", "scDiskStatus"),
        ("COMPELLENT-MIB", "scDiskNamePosition"),
        ("COMPELLENT-MIB", "scDiskHealthy"),
        ("COMPELLENT-MIB", "scDiskStatusMsg"),
        ("COMPELLENT-MIB", "scDiskApiIndex"),
        ("COMPELLENT-MIB", "scDiskForceTrap"),
        ("COMPELLENT-MIB", "scDiskSize"),
        ("COMPELLENT-MIB", "scDiskIoPortType"),
        ("COMPELLENT-MIB", "scDiskEnclosure"),
        ("COMPELLENT-MIB", "scCtlrNbr"),
        ("COMPELLENT-MIB", "scCtlrStatus"),
        ("COMPELLENT-MIB", "scCtlrName"),
        ("COMPELLENT-MIB", "scCtlrIpAddr"),
        ("COMPELLENT-MIB", "scCtlrForceTrap"),
        ("COMPELLENT-MIB", "scCtlrModel"),
        ("COMPELLENT-MIB", "scCtlrServiceTag"),
        ("COMPELLENT-MIB", "scCtlrAssetTag"),
        ("COMPELLENT-MIB", "scCtlrFanNbr"),
        ("COMPELLENT-MIB", "scCtlrFanStatus"),
        ("COMPELLENT-MIB", "scCtlrFanName"),
        ("COMPELLENT-MIB", "scCtlrFanCurrentRpm"),
        ("COMPELLENT-MIB", "scCtlrFanNormMaxRpm"),
        ("COMPELLENT-MIB", "scCtlrFanNormMinRpm"),
        ("COMPELLENT-MIB", "scCtlrFanWarnLwrRpm"),
        ("COMPELLENT-MIB", "scCtlrFanWarnUprRpm"),
        ("COMPELLENT-MIB", "scCtlrFanCritLwrRpm"),
        ("COMPELLENT-MIB", "scCtlrFanCritUprRpm"),
        ("COMPELLENT-MIB", "scCtlrFanForceTrap"),
        ("COMPELLENT-MIB", "scCtlrFanApiIndex"),
        ("COMPELLENT-MIB", "scCtlrPowerNbr"),
        ("COMPELLENT-MIB", "scCtlrPowerStatus"),
        ("COMPELLENT-MIB", "scCtlrPowerName"),
        ("COMPELLENT-MIB", "scCtlrPowerForceTrap"),
        ("COMPELLENT-MIB", "scCtlrVoltageNbr"),
        ("COMPELLENT-MIB", "scCtlrVoltageStatus"),
        ("COMPELLENT-MIB", "scCtlrVoltageName"),
        ("COMPELLENT-MIB", "scCtlrVoltageCurrentV"),
        ("COMPELLENT-MIB", "scCtlrVoltageNormMaxV"),
        ("COMPELLENT-MIB", "scCtlrVoltageNormMinV"),
        ("COMPELLENT-MIB", "scCtlrVoltageWarnLwrV"),
        ("COMPELLENT-MIB", "scCtlrVoltageWarnUprV"),
        ("COMPELLENT-MIB", "scCtlrVoltageCritLwrV"),
        ("COMPELLENT-MIB", "scCtlrVoltageCritUprV"),
        ("COMPELLENT-MIB", "scCtlrVoltageForceTrap"),
        ("COMPELLENT-MIB", "scCtlrTempNbr"),
        ("COMPELLENT-MIB", "scCtlrTempStatus"),
        ("COMPELLENT-MIB", "scCtlrTempName"),
        ("COMPELLENT-MIB", "scCtlrTempCurrentC"),
        ("COMPELLENT-MIB", "scCtlrTempNormMaxC"),
        ("COMPELLENT-MIB", "scCtlrTempNormMinC"),
        ("COMPELLENT-MIB", "scCtlrTempWarnLwrC"),
        ("COMPELLENT-MIB", "scCtlrTempWarnUprC"),
        ("COMPELLENT-MIB", "scCtlrTempCritLwrC"),
        ("COMPELLENT-MIB", "scCtlrTempCritUprC"),
        ("COMPELLENT-MIB", "scCtlrTempForceTrap"),
        ("COMPELLENT-MIB", "scEnclNbr"),
        ("COMPELLENT-MIB", "scEnclStatus"),
        ("COMPELLENT-MIB", "scEnclName"),
        ("COMPELLENT-MIB", "scEnclStatusDescr"),
        ("COMPELLENT-MIB", "scEnclType"),
        ("COMPELLENT-MIB", "scEnclModel"),
        ("COMPELLENT-MIB", "scEnclForceTrap"),
        ("COMPELLENT-MIB", "scEnclServiceTag"),
        ("COMPELLENT-MIB", "scEnclAssetTag"),
        ("COMPELLENT-MIB", "scEnclFanNbr"),
        ("COMPELLENT-MIB", "scEnclFanStatus"),
        ("COMPELLENT-MIB", "scEnclFanLocation"),
        ("COMPELLENT-MIB", "scEnclFanCurrentS"),
        ("COMPELLENT-MIB", "scEnclFanForceTrap"),
        ("COMPELLENT-MIB", "scEnclPowerNbr"),
        ("COMPELLENT-MIB", "scEnclPowerStatus"),
        ("COMPELLENT-MIB", "scEnclPowerPosition"),
        ("COMPELLENT-MIB", "scEnclPowerForceTrap"),
        ("COMPELLENT-MIB", "scEnclIoModNbr"),
        ("COMPELLENT-MIB", "scEnclIoModStatus"),
        ("COMPELLENT-MIB", "scEnclIoModPosition"),
        ("COMPELLENT-MIB", "scEnclIoModForceTrap"),
        ("COMPELLENT-MIB", "scEnclTempNbr"),
        ("COMPELLENT-MIB", "scEnclTempStatus"),
        ("COMPELLENT-MIB", "scEnclTempLocation"),
        ("COMPELLENT-MIB", "scEnclTempCurrentC"),
        ("COMPELLENT-MIB", "scEnclTempForceTrap"),
        ("COMPELLENT-MIB", "scEnclAlarmNbr"),
        ("COMPELLENT-MIB", "scEnclAlarmStatus"),
        ("COMPELLENT-MIB", "scEnclAlarmName"),
        ("COMPELLENT-MIB", "scEnclAlarmForceTrap"),
        ("COMPELLENT-MIB", "scDiskFolderNbr"),
        ("COMPELLENT-MIB", "scDiskFolderStatus"),
        ("COMPELLENT-MIB", "scDiskFolderName"),
        ("COMPELLENT-MIB", "scDiskFolderCapcty"),
        ("COMPELLENT-MIB", "scDiskFolderAlrtThr"),
        ("COMPELLENT-MIB", "scDiskFolderApiIndex"),
        ("COMPELLENT-MIB", "scDiskFolderForceTrap"),
        ("COMPELLENT-MIB", "scVolumeNbr"),
        ("COMPELLENT-MIB", "scVolumeStatus"),
        ("COMPELLENT-MIB", "scVolumeName"),
        ("COMPELLENT-MIB", "scVolumeApiIndex"),
        ("COMPELLENT-MIB", "scVolumeForceTrap"),
        ("COMPELLENT-MIB", "scServerNbr"),
        ("COMPELLENT-MIB", "scServerStatus"),
        ("COMPELLENT-MIB", "scServerName"),
        ("COMPELLENT-MIB", "scServerCnctvy"),
        ("COMPELLENT-MIB", "scServerPathCount"),
        ("COMPELLENT-MIB", "scServerApiIndex"),
        ("COMPELLENT-MIB", "scServerForceTrap"),
        ("COMPELLENT-MIB", "scCacheNbr"),
        ("COMPELLENT-MIB", "scCacheStatus"),
        ("COMPELLENT-MIB", "scCacheName"),
        ("COMPELLENT-MIB", "scCacheBatStat"),
        ("COMPELLENT-MIB", "scCacheBatExpr"),
        ("COMPELLENT-MIB", "scCacheForceTrap"),
        ("COMPELLENT-MIB", "scScNbr"),
        ("COMPELLENT-MIB", "scScStatus"),
        ("COMPELLENT-MIB", "scScName"),
        ("COMPELLENT-MIB", "scScContact"),
        ("COMPELLENT-MIB", "scScLocation"),
        ("COMPELLENT-MIB", "scScPortsBal"),
        ("COMPELLENT-MIB", "scScMgmtIP"),
        ("COMPELLENT-MIB", "scScSerial"),
        ("COMPELLENT-MIB", "scScForceTrap"),
        ("COMPELLENT-MIB", "scUPSNbr"),
        ("COMPELLENT-MIB", "scUPSStatus"),
        ("COMPELLENT-MIB", "scUPSName"),
        ("COMPELLENT-MIB", "scUPSBatLife"),
        ("COMPELLENT-MIB", "scUPSStatusDescr"),
        ("COMPELLENT-MIB", "scUPSApiIndex"),
        ("COMPELLENT-MIB", "scUPSForceTrap"),
        ("COMPELLENT-MIB", "scTrapNormalized"),
        ("COMPELLENT-MIB", "scLastWorstAlert"),
        ("COMPELLENT-MIB", "scObjCntNbr"),
        ("COMPELLENT-MIB", "scObjCntDevsInUse"),
        ("COMPELLENT-MIB", "scObjCntReplays"),
        ("COMPELLENT-MIB", "scObjCntDisks"),
        ("COMPELLENT-MIB", "scObjCntServers"),
        ("COMPELLENT-MIB", "scObjCntVolumes"),
        ("COMPELLENT-MIB", "scDiskFolderSUNbr"),
        ("COMPELLENT-MIB", "scDiskFolderSUTotalSpace"),
        ("COMPELLENT-MIB", "scDiskFolderSUUsedSpace"),
        ("COMPELLENT-MIB", "scSIDeviceType"),
        ("COMPELLENT-MIB", "scSIDeviceStatus"),
        ("COMPELLENT-MIB", "scHWCompStatus"),
        ("COMPELLENT-MIB", "scHWCompType"),
        ("COMPELLENT-MIB", "scHWCompName"),
        ("COMPELLENT-MIB", "scHWCompPosition"),
        ("COMPELLENT-MIB", "scHWCompState"),
        ("COMPELLENT-MIB", "scTrapAction"),
        ("COMPELLENT-MIB", "scAlertMsg"),
        ("COMPELLENT-MIB", "scForceTrap"),
        ("COMPELLENT-MIB", "scDiskConfigNbr"),
        ("COMPELLENT-MIB", "scDiskConfigSerial"),
        ("COMPELLENT-MIB", "scDiskConfigVendor"),
        ("COMPELLENT-MIB", "scDiskConfigProduct"),
        ("COMPELLENT-MIB", "scDiskConfigModel"),
        ("COMPELLENT-MIB", "scDiskConfigRev"),
        ("COMPELLENT-MIB", "scDiskConfigApiIndex"),
        ("COMPELLENT-MIB", "scAlertNbr"),
        ("COMPELLENT-MIB", "scAlertStatus"),
        ("COMPELLENT-MIB", "scAlertApiIndex"),
        ("COMPELLENT-MIB", "scAlertDefinition"),
        ("COMPELLENT-MIB", "scAlertCategory"),
        ("COMPELLENT-MIB", "scAlertCreateTime"),
        ("COMPELLENT-MIB", "scAlertMessage"),
        ("COMPELLENT-MIB", "scAlertType"),
        ("COMPELLENT-MIB", "scAlertAcknowledged"),
        ("COMPELLENT-MIB", "scAlertActive"))
)
if mibBuilder.loadTexts:
    compellentObjectsGroup.setStatus("current")

productID = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16139, 3, 2, 4)
)
productID.setObjects(
      *(("COMPELLENT-MIB", "productIDDisplayName"),
        ("COMPELLENT-MIB", "productIDDescription"),
        ("COMPELLENT-MIB", "productIDVendor"),
        ("COMPELLENT-MIB", "productIDVersion"),
        ("COMPELLENT-MIB", "productIDSerialNumber"),
        ("COMPELLENT-MIB", "productIDGlobalStatus"),
        ("COMPELLENT-MIB", "productIDBuildNumber"),
        ("COMPELLENT-MIB", "productIDURL"))
)
if mibBuilder.loadTexts:
    productID.setStatus("current")


# Notification objects

trapStatusOkay = NotificationType(
    (1, 3, 6, 1, 4, 1, 16139, 251, 0, 1)
)
trapStatusOkay.setObjects(
    ("SNMPv2-MIB", "sysName")
)
if mibBuilder.loadTexts:
    trapStatusOkay.setStatus(
        "deprecated"
    )

trapStatusDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 16139, 251, 0, 2)
)
trapStatusDegraded.setObjects(
    ("SNMPv2-MIB", "sysName")
)
if mibBuilder.loadTexts:
    trapStatusDegraded.setStatus(
        "deprecated"
    )

trapStatusDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 16139, 251, 0, 3)
)
trapStatusDown.setObjects(
    ("SNMPv2-MIB", "sysName")
)
if mibBuilder.loadTexts:
    trapStatusDown.setStatus(
        "deprecated"
    )

trapStatusInform = NotificationType(
    (1, 3, 6, 1, 4, 1, 16139, 251, 0, 4)
)
trapStatusInform.setObjects(
    ("SNMPv2-MIB", "sysName")
)
if mibBuilder.loadTexts:
    trapStatusInform.setStatus(
        "deprecated"
    )

trapStatusCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 16139, 251, 0, 5)
)
trapStatusCritical.setObjects(
    ("SNMPv2-MIB", "sysName")
)
if mibBuilder.loadTexts:
    trapStatusCritical.setStatus(
        "deprecated"
    )

trapStatusComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 16139, 251, 0, 6)
)
trapStatusComplete.setObjects(
    ("SNMPv2-MIB", "sysName")
)
if mibBuilder.loadTexts:
    trapStatusComplete.setStatus(
        "deprecated"
    )

trapStatusEmergency = NotificationType(
    (1, 3, 6, 1, 4, 1, 16139, 251, 0, 7)
)
trapStatusEmergency.setObjects(
    ("SNMPv2-MIB", "sysName")
)
if mibBuilder.loadTexts:
    trapStatusEmergency.setStatus(
        "deprecated"
    )

trapStatusUnavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 16139, 251, 0, 8)
)
trapStatusUnavailable.setObjects(
    ("SNMPv2-MIB", "sysName")
)
if mibBuilder.loadTexts:
    trapStatusUnavailable.setStatus(
        "deprecated"
    )

trapStatusTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 16139, 251, 0, 100)
)
trapStatusTest.setObjects(
    ("SNMPv2-MIB", "sysName")
)
if mibBuilder.loadTexts:
    trapStatusTest.setStatus(
        "deprecated"
    )

trapStatusTestSpecific = NotificationType(
    (1, 3, 6, 1, 4, 1, 16139, 251, 0, 101)
)
trapStatusTestSpecific.setObjects(
    ("SNMPv2-MIB", "sysName")
)
if mibBuilder.loadTexts:
    trapStatusTestSpecific.setStatus(
        "deprecated"
    )

scTestTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 16139, 251, 0, 200)
)
scTestTrap.setObjects(
      *(("COMPELLENT-MIB", "scIndex"),
        ("COMPELLENT-MIB", "scAlertDef"),
        ("COMPELLENT-MIB", "scTestString"))
)
if mibBuilder.loadTexts:
    scTestTrap.setStatus(
        "current"
    )

scMiscAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 16139, 251, 0, 201)
)
scMiscAlert.setObjects(
      *(("COMPELLENT-MIB", "scIndex"),
        ("COMPELLENT-MIB", "scMiscAlertString"),
        ("COMPELLENT-MIB", "scTrapNormalized"))
)
if mibBuilder.loadTexts:
    scMiscAlert.setStatus(
        "current"
    )

scDiskStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 16139, 251, 0, 202)
)
scDiskStatusChange.setObjects(
      *(("COMPELLENT-MIB", "scIndex"),
        ("COMPELLENT-MIB", "scAlertDef"),
        ("COMPELLENT-MIB", "scDiskNbr"),
        ("COMPELLENT-MIB", "scDiskStatus"),
        ("COMPELLENT-MIB", "scDiskNamePosition"),
        ("COMPELLENT-MIB", "scDiskHealthy"),
        ("COMPELLENT-MIB", "scDiskStatusMsg"),
        ("COMPELLENT-MIB", "scEnclName"),
        ("COMPELLENT-MIB", "scAlertMsg"),
        ("COMPELLENT-MIB", "scTrapAction"),
        ("COMPELLENT-MIB", "scDiskConfigNbr"),
        ("COMPELLENT-MIB", "scTrapNormalized"))
)
if mibBuilder.loadTexts:
    scDiskStatusChange.setStatus(
        "current"
    )

scCtlrStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 16139, 251, 0, 203)
)
scCtlrStatusChange.setObjects(
      *(("COMPELLENT-MIB", "scIndex"),
        ("COMPELLENT-MIB", "scAlertDef"),
        ("COMPELLENT-MIB", "scCtlrNbr"),
        ("COMPELLENT-MIB", "scCtlrStatus"),
        ("COMPELLENT-MIB", "scCtlrName"),
        ("COMPELLENT-MIB", "scAlertMsg"),
        ("COMPELLENT-MIB", "scTrapAction"),
        ("COMPELLENT-MIB", "scTrapNormalized"))
)
if mibBuilder.loadTexts:
    scCtlrStatusChange.setStatus(
        "current"
    )

scCtlrCompStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 16139, 251, 0, 204)
)
scCtlrCompStatusChange.setObjects(
      *(("COMPELLENT-MIB", "scIndex"),
        ("COMPELLENT-MIB", "scAlertDef"),
        ("COMPELLENT-MIB", "scCtlrNbr"),
        ("COMPELLENT-MIB", "scCtlrName"),
        ("COMPELLENT-MIB", "scHWCompType"),
        ("COMPELLENT-MIB", "scHWCompName"),
        ("COMPELLENT-MIB", "scHWCompStatus"),
        ("COMPELLENT-MIB", "scHWCompPosition"),
        ("COMPELLENT-MIB", "scHWCompState"),
        ("COMPELLENT-MIB", "scAlertMsg"),
        ("COMPELLENT-MIB", "scTrapAction"),
        ("COMPELLENT-MIB", "scTrapNormalized"))
)
if mibBuilder.loadTexts:
    scCtlrCompStatusChange.setStatus(
        "current"
    )

scEnclStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 16139, 251, 0, 205)
)
scEnclStatusChange.setObjects(
      *(("COMPELLENT-MIB", "scIndex"),
        ("COMPELLENT-MIB", "scAlertDef"),
        ("COMPELLENT-MIB", "scEnclNbr"),
        ("COMPELLENT-MIB", "scEnclName"),
        ("COMPELLENT-MIB", "scEnclStatus"),
        ("COMPELLENT-MIB", "scEnclStatusDescr"),
        ("COMPELLENT-MIB", "scEnclType"),
        ("COMPELLENT-MIB", "scEnclModel"),
        ("COMPELLENT-MIB", "scAlertMsg"),
        ("COMPELLENT-MIB", "scTrapAction"),
        ("COMPELLENT-MIB", "scTrapNormalized"))
)
if mibBuilder.loadTexts:
    scEnclStatusChange.setStatus(
        "current"
    )

scEnclCompStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 16139, 251, 0, 206)
)
scEnclCompStatusChange.setObjects(
      *(("COMPELLENT-MIB", "scIndex"),
        ("COMPELLENT-MIB", "scAlertDef"),
        ("COMPELLENT-MIB", "scEnclNbr"),
        ("COMPELLENT-MIB", "scEnclName"),
        ("COMPELLENT-MIB", "scHWCompType"),
        ("COMPELLENT-MIB", "scHWCompName"),
        ("COMPELLENT-MIB", "scHWCompStatus"),
        ("COMPELLENT-MIB", "scHWCompPosition"),
        ("COMPELLENT-MIB", "scHWCompState"),
        ("COMPELLENT-MIB", "scAlertMsg"),
        ("COMPELLENT-MIB", "scTrapAction"),
        ("COMPELLENT-MIB", "scTrapNormalized"))
)
if mibBuilder.loadTexts:
    scEnclCompStatusChange.setStatus(
        "current"
    )

scDiskFolderStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 16139, 251, 0, 207)
)
scDiskFolderStatusChange.setObjects(
      *(("COMPELLENT-MIB", "scIndex"),
        ("COMPELLENT-MIB", "scAlertDef"),
        ("COMPELLENT-MIB", "scDiskFolderNbr"),
        ("COMPELLENT-MIB", "scDiskFolderStatus"),
        ("COMPELLENT-MIB", "scDiskFolderName"),
        ("COMPELLENT-MIB", "scDiskFolderCapcty"),
        ("COMPELLENT-MIB", "scDiskFolderAlrtThr"),
        ("COMPELLENT-MIB", "scAlertMsg"),
        ("COMPELLENT-MIB", "scTrapAction"),
        ("COMPELLENT-MIB", "scTrapNormalized"))
)
if mibBuilder.loadTexts:
    scDiskFolderStatusChange.setStatus(
        "current"
    )

scVolumeStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 16139, 251, 0, 208)
)
scVolumeStatusChange.setObjects(
      *(("COMPELLENT-MIB", "scIndex"),
        ("COMPELLENT-MIB", "scAlertDef"),
        ("COMPELLENT-MIB", "scVolumeNbr"),
        ("COMPELLENT-MIB", "scVolumeStatus"),
        ("COMPELLENT-MIB", "scVolumeName"),
        ("COMPELLENT-MIB", "scAlertMsg"),
        ("COMPELLENT-MIB", "scTrapAction"),
        ("COMPELLENT-MIB", "scTrapNormalized"))
)
if mibBuilder.loadTexts:
    scVolumeStatusChange.setStatus(
        "current"
    )

scServerStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 16139, 251, 0, 209)
)
scServerStatusChange.setObjects(
      *(("COMPELLENT-MIB", "scIndex"),
        ("COMPELLENT-MIB", "scAlertDef"),
        ("COMPELLENT-MIB", "scServerNbr"),
        ("COMPELLENT-MIB", "scServerStatus"),
        ("COMPELLENT-MIB", "scServerName"),
        ("COMPELLENT-MIB", "scServerCnctvy"),
        ("COMPELLENT-MIB", "scServerPathCount"),
        ("COMPELLENT-MIB", "scAlertMsg"),
        ("COMPELLENT-MIB", "scTrapAction"),
        ("COMPELLENT-MIB", "scTrapNormalized"))
)
if mibBuilder.loadTexts:
    scServerStatusChange.setStatus(
        "current"
    )

scCacheStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 16139, 251, 0, 210)
)
scCacheStatusChange.setObjects(
      *(("COMPELLENT-MIB", "scIndex"),
        ("COMPELLENT-MIB", "scAlertDef"),
        ("COMPELLENT-MIB", "scCacheNbr"),
        ("COMPELLENT-MIB", "scCacheStatus"),
        ("COMPELLENT-MIB", "scCacheName"),
        ("COMPELLENT-MIB", "scCacheBatStat"),
        ("COMPELLENT-MIB", "scCacheBatExpr"),
        ("COMPELLENT-MIB", "scAlertMsg"),
        ("COMPELLENT-MIB", "scTrapAction"),
        ("COMPELLENT-MIB", "scTrapNormalized"))
)
if mibBuilder.loadTexts:
    scCacheStatusChange.setStatus(
        "current"
    )

scLocalPortCondStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 16139, 251, 0, 211)
)
scLocalPortCondStatusChange.setObjects(
      *(("COMPELLENT-MIB", "scIndex"),
        ("COMPELLENT-MIB", "scAlertDef"),
        ("COMPELLENT-MIB", "scScPortsBal"),
        ("COMPELLENT-MIB", "scAlertMsg"),
        ("COMPELLENT-MIB", "scTrapAction"),
        ("COMPELLENT-MIB", "scTrapNormalized"))
)
if mibBuilder.loadTexts:
    scLocalPortCondStatusChange.setStatus(
        "current"
    )

scMonitoredUPSStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 16139, 251, 0, 212)
)
scMonitoredUPSStatusChange.setObjects(
      *(("COMPELLENT-MIB", "scIndex"),
        ("COMPELLENT-MIB", "scAlertDef"),
        ("COMPELLENT-MIB", "scUPSNbr"),
        ("COMPELLENT-MIB", "scUPSStatus"),
        ("COMPELLENT-MIB", "scUPSName"),
        ("COMPELLENT-MIB", "scUPSBatLife"),
        ("COMPELLENT-MIB", "scUPSStatusDescr"),
        ("COMPELLENT-MIB", "scAlertMsg"),
        ("COMPELLENT-MIB", "scTrapAction"),
        ("COMPELLENT-MIB", "scTrapNormalized"))
)
if mibBuilder.loadTexts:
    scMonitoredUPSStatusChange.setStatus(
        "current"
    )

scSIDeviceStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 16139, 251, 0, 213)
)
scSIDeviceStatusChange.setObjects(
      *(("COMPELLENT-MIB", "scIndex"),
        ("COMPELLENT-MIB", "scAlertDef"),
        ("COMPELLENT-MIB", "scSIDeviceType"),
        ("COMPELLENT-MIB", "scSIDeviceStatus"),
        ("COMPELLENT-MIB", "scDiskNbr"),
        ("COMPELLENT-MIB", "scDiskNamePosition"),
        ("COMPELLENT-MIB", "scEnclNbr"),
        ("COMPELLENT-MIB", "scEnclName"),
        ("COMPELLENT-MIB", "scAlertMsg"),
        ("COMPELLENT-MIB", "scTrapAction"),
        ("COMPELLENT-MIB", "scTrapNormalized"))
)
if mibBuilder.loadTexts:
    scSIDeviceStatusChange.setStatus(
        "current"
    )


# Notifications groups

compellentNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 16139, 3, 2, 1)
)
compellentNotificationsGroup.setObjects(
      *(("COMPELLENT-MIB", "trapStatusOkay"),
        ("COMPELLENT-MIB", "trapStatusDegraded"),
        ("COMPELLENT-MIB", "trapStatusDown"),
        ("COMPELLENT-MIB", "trapStatusInform"),
        ("COMPELLENT-MIB", "trapStatusCritical"),
        ("COMPELLENT-MIB", "trapStatusComplete"),
        ("COMPELLENT-MIB", "trapStatusEmergency"),
        ("COMPELLENT-MIB", "trapStatusUnavailable"),
        ("COMPELLENT-MIB", "trapStatusTest"),
        ("COMPELLENT-MIB", "trapStatusTestSpecific"))
)
if mibBuilder.loadTexts:
    compellentNotificationsGroup.setStatus(
        "deprecated"
    )

compellentNotificationsGroup2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 16139, 3, 2, 2)
)
compellentNotificationsGroup2.setObjects(
      *(("COMPELLENT-MIB", "scTestTrap"),
        ("COMPELLENT-MIB", "scMiscAlert"),
        ("COMPELLENT-MIB", "scDiskStatusChange"),
        ("COMPELLENT-MIB", "scCtlrStatusChange"),
        ("COMPELLENT-MIB", "scCtlrCompStatusChange"),
        ("COMPELLENT-MIB", "scEnclStatusChange"),
        ("COMPELLENT-MIB", "scEnclCompStatusChange"),
        ("COMPELLENT-MIB", "scDiskFolderStatusChange"),
        ("COMPELLENT-MIB", "scVolumeStatusChange"),
        ("COMPELLENT-MIB", "scServerStatusChange"),
        ("COMPELLENT-MIB", "scCacheStatusChange"),
        ("COMPELLENT-MIB", "scLocalPortCondStatusChange"),
        ("COMPELLENT-MIB", "scMonitoredUPSStatusChange"),
        ("COMPELLENT-MIB", "scSIDeviceStatusChange"))
)
if mibBuilder.loadTexts:
    compellentNotificationsGroup2.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

compellentCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 16139, 3, 1, 1)
)
if mibBuilder.loadTexts:
    compellentCompliance1.setStatus(
        "deprecated"
    )

compellentCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 16139, 3, 1, 2)
)
if mibBuilder.loadTexts:
    compellentCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COMPELLENT-MIB",
    **{"ScHardwareType": ScHardwareType,
       "ScStatus": ScStatus,
       "compellentEnterprise": compellentEnterprise,
       "compellentModule": compellentModule,
       "compellentObjects": compellentObjects,
       "productIDDisplayName": productIDDisplayName,
       "productIDDescription": productIDDescription,
       "productIDVendor": productIDVendor,
       "productIDVersion": productIDVersion,
       "productIDSerialNumber": productIDSerialNumber,
       "productIDGlobalStatus": productIDGlobalStatus,
       "productIDBuildNumber": productIDBuildNumber,
       "productIDURL": productIDURL,
       "scAlertDef": scAlertDef,
       "scIndex": scIndex,
       "scTestString": scTestString,
       "scMiscAlertString": scMiscAlertString,
       "scCtlrTable": scCtlrTable,
       "scCtlrEntry": scCtlrEntry,
       "scCtlrIndex": scCtlrIndex,
       "scCtlrNbr": scCtlrNbr,
       "scCtlrStatus": scCtlrStatus,
       "scCtlrName": scCtlrName,
       "scCtlrIpAddr": scCtlrIpAddr,
       "scCtlrForceTrap": scCtlrForceTrap,
       "scCtlrModel": scCtlrModel,
       "scCtlrServiceTag": scCtlrServiceTag,
       "scCtlrAssetTag": scCtlrAssetTag,
       "scDiskTable": scDiskTable,
       "scDiskEntry": scDiskEntry,
       "scDiskIndex": scDiskIndex,
       "scDiskNbr": scDiskNbr,
       "scDiskStatus": scDiskStatus,
       "scDiskNamePosition": scDiskNamePosition,
       "scDiskHealthy": scDiskHealthy,
       "scDiskStatusMsg": scDiskStatusMsg,
       "scDiskApiIndex": scDiskApiIndex,
       "scDiskForceTrap": scDiskForceTrap,
       "scDiskSize": scDiskSize,
       "scDiskIoPortType": scDiskIoPortType,
       "scDiskEnclosure": scDiskEnclosure,
       "scEnclTable": scEnclTable,
       "scEnclEntry": scEnclEntry,
       "scEnclIndex": scEnclIndex,
       "scEnclNbr": scEnclNbr,
       "scEnclStatus": scEnclStatus,
       "scEnclName": scEnclName,
       "scEnclStatusDescr": scEnclStatusDescr,
       "scEnclType": scEnclType,
       "scEnclModel": scEnclModel,
       "scEnclForceTrap": scEnclForceTrap,
       "scEnclServiceTag": scEnclServiceTag,
       "scEnclAssetTag": scEnclAssetTag,
       "scCtlrFanTable": scCtlrFanTable,
       "scCtlrFanEntry": scCtlrFanEntry,
       "scCtlrFanIndex": scCtlrFanIndex,
       "scCtlrFanNbr": scCtlrFanNbr,
       "scCtlrFanStatus": scCtlrFanStatus,
       "scCtlrFanName": scCtlrFanName,
       "scCtlrFanCurrentRpm": scCtlrFanCurrentRpm,
       "scCtlrFanNormMaxRpm": scCtlrFanNormMaxRpm,
       "scCtlrFanNormMinRpm": scCtlrFanNormMinRpm,
       "scCtlrFanWarnLwrRpm": scCtlrFanWarnLwrRpm,
       "scCtlrFanWarnUprRpm": scCtlrFanWarnUprRpm,
       "scCtlrFanCritLwrRpm": scCtlrFanCritLwrRpm,
       "scCtlrFanCritUprRpm": scCtlrFanCritUprRpm,
       "scCtlrFanForceTrap": scCtlrFanForceTrap,
       "scCtlrFanApiIndex": scCtlrFanApiIndex,
       "scCtlrPowerTable": scCtlrPowerTable,
       "scCtlrPowerEntry": scCtlrPowerEntry,
       "scCtlrPowerIndex": scCtlrPowerIndex,
       "scCtlrPowerNbr": scCtlrPowerNbr,
       "scCtlrPowerStatus": scCtlrPowerStatus,
       "scCtlrPowerName": scCtlrPowerName,
       "scCtlrPowerForceTrap": scCtlrPowerForceTrap,
       "scCtlrVoltageTable": scCtlrVoltageTable,
       "scCtlrVoltageEntry": scCtlrVoltageEntry,
       "scCtlrVoltageIndex": scCtlrVoltageIndex,
       "scCtlrVoltageNbr": scCtlrVoltageNbr,
       "scCtlrVoltageStatus": scCtlrVoltageStatus,
       "scCtlrVoltageName": scCtlrVoltageName,
       "scCtlrVoltageCurrentV": scCtlrVoltageCurrentV,
       "scCtlrVoltageNormMaxV": scCtlrVoltageNormMaxV,
       "scCtlrVoltageNormMinV": scCtlrVoltageNormMinV,
       "scCtlrVoltageWarnLwrV": scCtlrVoltageWarnLwrV,
       "scCtlrVoltageWarnUprV": scCtlrVoltageWarnUprV,
       "scCtlrVoltageCritLwrV": scCtlrVoltageCritLwrV,
       "scCtlrVoltageCritUprV": scCtlrVoltageCritUprV,
       "scCtlrVoltageForceTrap": scCtlrVoltageForceTrap,
       "scCtlrTempTable": scCtlrTempTable,
       "scCtlrTempEntry": scCtlrTempEntry,
       "scCtlrTempIndex": scCtlrTempIndex,
       "scCtlrTempNbr": scCtlrTempNbr,
       "scCtlrTempStatus": scCtlrTempStatus,
       "scCtlrTempName": scCtlrTempName,
       "scCtlrTempCurrentC": scCtlrTempCurrentC,
       "scCtlrTempNormMaxC": scCtlrTempNormMaxC,
       "scCtlrTempNormMinC": scCtlrTempNormMinC,
       "scCtlrTempWarnLwrC": scCtlrTempWarnLwrC,
       "scCtlrTempWarnUprC": scCtlrTempWarnUprC,
       "scCtlrTempCritLwrC": scCtlrTempCritLwrC,
       "scCtlrTempCritUprC": scCtlrTempCritUprC,
       "scCtlrTempForceTrap": scCtlrTempForceTrap,
       "scEnclFanTable": scEnclFanTable,
       "scEnclFanEntry": scEnclFanEntry,
       "scEnclFanIndex": scEnclFanIndex,
       "scEnclFanNbr": scEnclFanNbr,
       "scEnclFanStatus": scEnclFanStatus,
       "scEnclFanLocation": scEnclFanLocation,
       "scEnclFanCurrentS": scEnclFanCurrentS,
       "scEnclFanForceTrap": scEnclFanForceTrap,
       "scEnclPowerTable": scEnclPowerTable,
       "scEnclPowerEntry": scEnclPowerEntry,
       "scEnclPowerIndex": scEnclPowerIndex,
       "scEnclPowerNbr": scEnclPowerNbr,
       "scEnclPowerStatus": scEnclPowerStatus,
       "scEnclPowerPosition": scEnclPowerPosition,
       "scEnclPowerForceTrap": scEnclPowerForceTrap,
       "scEnclIoModTable": scEnclIoModTable,
       "scEnclIoModEntry": scEnclIoModEntry,
       "scEnclIoModIndex": scEnclIoModIndex,
       "scEnclIoModNbr": scEnclIoModNbr,
       "scEnclIoModStatus": scEnclIoModStatus,
       "scEnclIoModPosition": scEnclIoModPosition,
       "scEnclIoModForceTrap": scEnclIoModForceTrap,
       "scEnclTempTable": scEnclTempTable,
       "scEnclTempEntry": scEnclTempEntry,
       "scEnclTempIndex": scEnclTempIndex,
       "scEnclTempNbr": scEnclTempNbr,
       "scEnclTempStatus": scEnclTempStatus,
       "scEnclTempLocation": scEnclTempLocation,
       "scEnclTempCurrentC": scEnclTempCurrentC,
       "scEnclTempForceTrap": scEnclTempForceTrap,
       "scEnclAlarmTable": scEnclAlarmTable,
       "scEnclAlarmEntry": scEnclAlarmEntry,
       "scEnclAlarmIndex": scEnclAlarmIndex,
       "scEnclAlarmNbr": scEnclAlarmNbr,
       "scEnclAlarmStatus": scEnclAlarmStatus,
       "scEnclAlarmName": scEnclAlarmName,
       "scEnclAlarmForceTrap": scEnclAlarmForceTrap,
       "scDiskFolderTable": scDiskFolderTable,
       "scDiskFolderEntry": scDiskFolderEntry,
       "scDiskFolderIndex": scDiskFolderIndex,
       "scDiskFolderNbr": scDiskFolderNbr,
       "scDiskFolderStatus": scDiskFolderStatus,
       "scDiskFolderName": scDiskFolderName,
       "scDiskFolderCapcty": scDiskFolderCapcty,
       "scDiskFolderAlrtThr": scDiskFolderAlrtThr,
       "scDiskFolderApiIndex": scDiskFolderApiIndex,
       "scDiskFolderForceTrap": scDiskFolderForceTrap,
       "scVolumeTable": scVolumeTable,
       "scVolumeEntry": scVolumeEntry,
       "scVolumeIndex": scVolumeIndex,
       "scVolumeNbr": scVolumeNbr,
       "scVolumeStatus": scVolumeStatus,
       "scVolumeName": scVolumeName,
       "scVolumeApiIndex": scVolumeApiIndex,
       "scVolumeForceTrap": scVolumeForceTrap,
       "scServerTable": scServerTable,
       "scServerEntry": scServerEntry,
       "scServerIndex": scServerIndex,
       "scServerNbr": scServerNbr,
       "scServerStatus": scServerStatus,
       "scServerName": scServerName,
       "scServerCnctvy": scServerCnctvy,
       "scServerPathCount": scServerPathCount,
       "scServerApiIndex": scServerApiIndex,
       "scServerForceTrap": scServerForceTrap,
       "scCacheTable": scCacheTable,
       "scCacheEntry": scCacheEntry,
       "scCacheIndex": scCacheIndex,
       "scCacheNbr": scCacheNbr,
       "scCacheStatus": scCacheStatus,
       "scCacheName": scCacheName,
       "scCacheBatStat": scCacheBatStat,
       "scCacheBatExpr": scCacheBatExpr,
       "scCacheForceTrap": scCacheForceTrap,
       "scScTable": scScTable,
       "scScEntry": scScEntry,
       "scScIndex": scScIndex,
       "scScNbr": scScNbr,
       "scScStatus": scScStatus,
       "scScName": scScName,
       "scScContact": scScContact,
       "scScLocation": scScLocation,
       "scScPortsBal": scScPortsBal,
       "scScMgmtIP": scScMgmtIP,
       "scScSerial": scScSerial,
       "scScForceTrap": scScForceTrap,
       "scUPSTable": scUPSTable,
       "scUPSEntry": scUPSEntry,
       "scUPSIndex": scUPSIndex,
       "scUPSNbr": scUPSNbr,
       "scUPSStatus": scUPSStatus,
       "scUPSName": scUPSName,
       "scUPSBatLife": scUPSBatLife,
       "scUPSStatusDescr": scUPSStatusDescr,
       "scUPSApiIndex": scUPSApiIndex,
       "scUPSForceTrap": scUPSForceTrap,
       "scObjCntTable": scObjCntTable,
       "scObjCntEntry": scObjCntEntry,
       "scObjCntIndex": scObjCntIndex,
       "scObjCntNbr": scObjCntNbr,
       "scObjCntDevsInUse": scObjCntDevsInUse,
       "scObjCntReplays": scObjCntReplays,
       "scObjCntDisks": scObjCntDisks,
       "scObjCntServers": scObjCntServers,
       "scObjCntVolumes": scObjCntVolumes,
       "scDiskFolderSUTable": scDiskFolderSUTable,
       "scDiskFolderSUEntry": scDiskFolderSUEntry,
       "scDiskFolderSUIndex": scDiskFolderSUIndex,
       "scDiskFolderSUNbr": scDiskFolderSUNbr,
       "scDiskFolderSUTotalSpace": scDiskFolderSUTotalSpace,
       "scDiskFolderSUUsedSpace": scDiskFolderSUUsedSpace,
       "scSIDeviceType": scSIDeviceType,
       "scSIDeviceStatus": scSIDeviceStatus,
       "scHWCompStatus": scHWCompStatus,
       "scHWCompName": scHWCompName,
       "scHWCompPosition": scHWCompPosition,
       "scHWCompType": scHWCompType,
       "scHWCompState": scHWCompState,
       "scTrapAction": scTrapAction,
       "scAlertMsg": scAlertMsg,
       "scForceTrap": scForceTrap,
       "scTrapNormalized": scTrapNormalized,
       "scLastWorstAlert": scLastWorstAlert,
       "scDiskConfigTable": scDiskConfigTable,
       "scDiskConfigEntry": scDiskConfigEntry,
       "scDiskConfigIndex": scDiskConfigIndex,
       "scDiskConfigNbr": scDiskConfigNbr,
       "scDiskConfigSerial": scDiskConfigSerial,
       "scDiskConfigVendor": scDiskConfigVendor,
       "scDiskConfigProduct": scDiskConfigProduct,
       "scDiskConfigModel": scDiskConfigModel,
       "scDiskConfigRev": scDiskConfigRev,
       "scDiskConfigApiIndex": scDiskConfigApiIndex,
       "scAlertTable": scAlertTable,
       "scAlertEntry": scAlertEntry,
       "scAlertIndex": scAlertIndex,
       "scAlertNbr": scAlertNbr,
       "scAlertStatus": scAlertStatus,
       "scAlertApiIndex": scAlertApiIndex,
       "scAlertDefinition": scAlertDefinition,
       "scAlertCategory": scAlertCategory,
       "scAlertCreateTime": scAlertCreateTime,
       "scAlertMessage": scAlertMessage,
       "scAlertType": scAlertType,
       "scAlertAcknowledged": scAlertAcknowledged,
       "scAlertActive": scAlertActive,
       "compellentConformance": compellentConformance,
       "compellentCompliances": compellentCompliances,
       "compellentCompliance1": compellentCompliance1,
       "compellentCompliance2": compellentCompliance2,
       "compellentGroups": compellentGroups,
       "compellentNotificationsGroup": compellentNotificationsGroup,
       "compellentNotificationsGroup2": compellentNotificationsGroup2,
       "compellentObjectsGroup": compellentObjectsGroup,
       "productID": productID,
       "compellentTrapsNotif": compellentTrapsNotif,
       "trapSevPrefix": trapSevPrefix,
       "trapStatusOkay": trapStatusOkay,
       "trapStatusDegraded": trapStatusDegraded,
       "trapStatusDown": trapStatusDown,
       "trapStatusInform": trapStatusInform,
       "trapStatusCritical": trapStatusCritical,
       "trapStatusComplete": trapStatusComplete,
       "trapStatusEmergency": trapStatusEmergency,
       "trapStatusUnavailable": trapStatusUnavailable,
       "trapStatusTest": trapStatusTest,
       "trapStatusTestSpecific": trapStatusTestSpecific,
       "scTestTrap": scTestTrap,
       "scMiscAlert": scMiscAlert,
       "scDiskStatusChange": scDiskStatusChange,
       "scCtlrStatusChange": scCtlrStatusChange,
       "scCtlrCompStatusChange": scCtlrCompStatusChange,
       "scEnclStatusChange": scEnclStatusChange,
       "scEnclCompStatusChange": scEnclCompStatusChange,
       "scDiskFolderStatusChange": scDiskFolderStatusChange,
       "scVolumeStatusChange": scVolumeStatusChange,
       "scServerStatusChange": scServerStatusChange,
       "scCacheStatusChange": scCacheStatusChange,
       "scLocalPortCondStatusChange": scLocalPortCondStatusChange,
       "scMonitoredUPSStatusChange": scMonitoredUPSStatusChange,
       "scSIDeviceStatusChange": scSIDeviceStatusChange}
)
