# SNMP MIB module (ALCATEL-IND1-APP-FINGERPRINT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-APP-FINGERPRINT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:41 2024
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

(softentIND1AppFingerPrintMIB,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1AppFingerPrintMIB")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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
    "iso")

(DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1AppFPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1)
)
alcatelIND1AppFPMIB.setRevisions(
        ("2013-01-09 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1AppFPMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1AppFPMIBObjects = _AlcatelIND1AppFPMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1AppFPMIBObjects.setStatus("current")
_AlaAppFPMIBNotifications_ObjectIdentity = ObjectIdentity
alaAppFPMIBNotifications = _AlaAppFPMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1, 1, 0)
)
_AlaAppFPGlobalMIBConfigObjects_ObjectIdentity = ObjectIdentity
alaAppFPGlobalMIBConfigObjects = _AlaAppFPGlobalMIBConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1, 1, 1)
)


class _AlaAppFPGlobalAdminState_Type(Integer32):
    """Custom type alaAppFPGlobalAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AlaAppFPGlobalAdminState_Type.__name__ = "Integer32"
_AlaAppFPGlobalAdminState_Object = MibScalar
alaAppFPGlobalAdminState = _AlaAppFPGlobalAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1, 1, 1, 1),
    _AlaAppFPGlobalAdminState_Type()
)
alaAppFPGlobalAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAppFPGlobalAdminState.setStatus("current")


class _AlaAppFPGlobalSignatureFile_Type(SnmpAdminString):
    """Custom type alaAppFPGlobalSignatureFile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_AlaAppFPGlobalSignatureFile_Type.__name__ = "SnmpAdminString"
_AlaAppFPGlobalSignatureFile_Object = MibScalar
alaAppFPGlobalSignatureFile = _AlaAppFPGlobalSignatureFile_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1, 1, 1, 2),
    _AlaAppFPGlobalSignatureFile_Type()
)
alaAppFPGlobalSignatureFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAppFPGlobalSignatureFile.setStatus("current")


class _AlaAppFPGlobalReloadSignatureFile_Type(Integer32):
    """Custom type alaAppFPGlobalReloadSignatureFile based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("reload", 1))
    )


_AlaAppFPGlobalReloadSignatureFile_Type.__name__ = "Integer32"
_AlaAppFPGlobalReloadSignatureFile_Object = MibScalar
alaAppFPGlobalReloadSignatureFile = _AlaAppFPGlobalReloadSignatureFile_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1, 1, 1, 3),
    _AlaAppFPGlobalReloadSignatureFile_Type()
)
alaAppFPGlobalReloadSignatureFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAppFPGlobalReloadSignatureFile.setStatus("current")


class _AlaAppFPGlobalTrapConfig_Type(Integer32):
    """Custom type alaAppFPGlobalTrapConfig based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AlaAppFPGlobalTrapConfig_Type.__name__ = "Integer32"
_AlaAppFPGlobalTrapConfig_Object = MibScalar
alaAppFPGlobalTrapConfig = _AlaAppFPGlobalTrapConfig_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1, 1, 1, 4),
    _AlaAppFPGlobalTrapConfig_Type()
)
alaAppFPGlobalTrapConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAppFPGlobalTrapConfig.setStatus("current")
_AlaAppFPMIBObjects_ObjectIdentity = ObjectIdentity
alaAppFPMIBObjects = _AlaAppFPMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1, 1, 2)
)
_AlaAppFPPortTable_Object = MibTable
alaAppFPPortTable = _AlaAppFPPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alaAppFPPortTable.setStatus("current")
_AlaAppFPPortEntry_Object = MibTableRow
alaAppFPPortEntry = _AlaAppFPPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1, 1, 2, 1, 1)
)
alaAppFPPortEntry.setIndexNames(
    (0, "ALCATEL-IND1-APP-FINGERPRINT-MIB", "alaAppFPPort"),
    (0, "ALCATEL-IND1-APP-FINGERPRINT-MIB", "alaAppFPGroupNameOrPolicyList"),
)
if mibBuilder.loadTexts:
    alaAppFPPortEntry.setStatus("current")
_AlaAppFPPort_Type = InterfaceIndex
_AlaAppFPPort_Object = MibTableColumn
alaAppFPPort = _AlaAppFPPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1, 1, 2, 1, 1, 1),
    _AlaAppFPPort_Type()
)
alaAppFPPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaAppFPPort.setStatus("current")


class _AlaAppFPGroupNameOrPolicyList_Type(SnmpAdminString):
    """Custom type alaAppFPGroupNameOrPolicyList based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlaAppFPGroupNameOrPolicyList_Type.__name__ = "SnmpAdminString"
_AlaAppFPGroupNameOrPolicyList_Object = MibTableColumn
alaAppFPGroupNameOrPolicyList = _AlaAppFPGroupNameOrPolicyList_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1, 1, 2, 1, 1, 2),
    _AlaAppFPGroupNameOrPolicyList_Type()
)
alaAppFPGroupNameOrPolicyList.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaAppFPGroupNameOrPolicyList.setStatus("current")


class _AlaAppFPPortOperationMode_Type(Integer32):
    """Custom type alaAppFPPortOperationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("monitoring", 1),
          ("qos", 2),
          ("unp", 3))
    )


_AlaAppFPPortOperationMode_Type.__name__ = "Integer32"
_AlaAppFPPortOperationMode_Object = MibTableColumn
alaAppFPPortOperationMode = _AlaAppFPPortOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1, 1, 2, 1, 1, 3),
    _AlaAppFPPortOperationMode_Type()
)
alaAppFPPortOperationMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAppFPPortOperationMode.setStatus("current")


class _AlaAppFPPortStatus_Type(Integer32):
    """Custom type alaAppFPPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_AlaAppFPPortStatus_Type.__name__ = "Integer32"
_AlaAppFPPortStatus_Object = MibTableColumn
alaAppFPPortStatus = _AlaAppFPPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1, 1, 2, 1, 1, 4),
    _AlaAppFPPortStatus_Type()
)
alaAppFPPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppFPPortStatus.setStatus("current")
_AlaAppFPPortRowStatus_Type = RowStatus
_AlaAppFPPortRowStatus_Object = MibTableColumn
alaAppFPPortRowStatus = _AlaAppFPPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1, 1, 2, 1, 1, 5),
    _AlaAppFPPortRowStatus_Type()
)
alaAppFPPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAppFPPortRowStatus.setStatus("current")
_AlaAppFPAppNameTable_Object = MibTable
alaAppFPAppNameTable = _AlaAppFPAppNameTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alaAppFPAppNameTable.setStatus("current")
_AlaAppFPAppNameEntry_Object = MibTableRow
alaAppFPAppNameEntry = _AlaAppFPAppNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1, 1, 2, 2, 1)
)
alaAppFPAppNameEntry.setIndexNames(
    (0, "ALCATEL-IND1-APP-FINGERPRINT-MIB", "alaAppFPAppName"),
)
if mibBuilder.loadTexts:
    alaAppFPAppNameEntry.setStatus("current")


class _AlaAppFPAppName_Type(SnmpAdminString):
    """Custom type alaAppFPAppName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_AlaAppFPAppName_Type.__name__ = "SnmpAdminString"
_AlaAppFPAppName_Object = MibTableColumn
alaAppFPAppName = _AlaAppFPAppName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1, 1, 2, 2, 1, 1),
    _AlaAppFPAppName_Type()
)
alaAppFPAppName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaAppFPAppName.setStatus("current")


class _AlaAppFPAppDescription_Type(SnmpAdminString):
    """Custom type alaAppFPAppDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AlaAppFPAppDescription_Type.__name__ = "SnmpAdminString"
_AlaAppFPAppDescription_Object = MibTableColumn
alaAppFPAppDescription = _AlaAppFPAppDescription_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1, 1, 2, 2, 1, 2),
    _AlaAppFPAppDescription_Type()
)
alaAppFPAppDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppFPAppDescription.setStatus("current")


class _AlaAppFPAppSignature_Type(SnmpAdminString):
    """Custom type alaAppFPAppSignature based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_AlaAppFPAppSignature_Type.__name__ = "SnmpAdminString"
_AlaAppFPAppSignature_Object = MibTableColumn
alaAppFPAppSignature = _AlaAppFPAppSignature_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1, 1, 2, 2, 1, 3),
    _AlaAppFPAppSignature_Type()
)
alaAppFPAppSignature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppFPAppSignature.setStatus("current")
_AlaAppFPDatabaseTable_Object = MibTable
alaAppFPDatabaseTable = _AlaAppFPDatabaseTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    alaAppFPDatabaseTable.setStatus("current")
_AlaAppFPDatabaseEntry_Object = MibTableRow
alaAppFPDatabaseEntry = _AlaAppFPDatabaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1, 1, 2, 3, 1)
)
alaAppFPDatabaseEntry.setIndexNames(
    (0, "ALCATEL-IND1-APP-FINGERPRINT-MIB", "alaAppFPDbPort"),
    (0, "ALCATEL-IND1-APP-FINGERPRINT-MIB", "alaAppFPDbAppGroupName"),
    (0, "ALCATEL-IND1-APP-FINGERPRINT-MIB", "alaAppFPDbAppName"),
    (0, "ALCATEL-IND1-APP-FINGERPRINT-MIB", "alaAppFPDbSrcMacAddr"),
    (0, "ALCATEL-IND1-APP-FINGERPRINT-MIB", "alaAppFPDbVlanId"),
    (0, "ALCATEL-IND1-APP-FINGERPRINT-MIB", "alaAppFPDbSrcIpAddrType"),
    (0, "ALCATEL-IND1-APP-FINGERPRINT-MIB", "alaAppFPDbSrcIpAddr"),
    (0, "ALCATEL-IND1-APP-FINGERPRINT-MIB", "alaAppFPDbSrcPort"),
)
if mibBuilder.loadTexts:
    alaAppFPDatabaseEntry.setStatus("current")
_AlaAppFPDbPort_Type = InterfaceIndex
_AlaAppFPDbPort_Object = MibTableColumn
alaAppFPDbPort = _AlaAppFPDbPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1, 1, 2, 3, 1, 1),
    _AlaAppFPDbPort_Type()
)
alaAppFPDbPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaAppFPDbPort.setStatus("current")


class _AlaAppFPDbAppGroupName_Type(SnmpAdminString):
    """Custom type alaAppFPDbAppGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_AlaAppFPDbAppGroupName_Type.__name__ = "SnmpAdminString"
_AlaAppFPDbAppGroupName_Object = MibTableColumn
alaAppFPDbAppGroupName = _AlaAppFPDbAppGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1, 1, 2, 3, 1, 2),
    _AlaAppFPDbAppGroupName_Type()
)
alaAppFPDbAppGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaAppFPDbAppGroupName.setStatus("current")


class _AlaAppFPDbAppName_Type(SnmpAdminString):
    """Custom type alaAppFPDbAppName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_AlaAppFPDbAppName_Type.__name__ = "SnmpAdminString"
_AlaAppFPDbAppName_Object = MibTableColumn
alaAppFPDbAppName = _AlaAppFPDbAppName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1, 1, 2, 3, 1, 3),
    _AlaAppFPDbAppName_Type()
)
alaAppFPDbAppName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaAppFPDbAppName.setStatus("current")
_AlaAppFPDbSrcMacAddr_Type = MacAddress
_AlaAppFPDbSrcMacAddr_Object = MibTableColumn
alaAppFPDbSrcMacAddr = _AlaAppFPDbSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1, 1, 2, 3, 1, 4),
    _AlaAppFPDbSrcMacAddr_Type()
)
alaAppFPDbSrcMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaAppFPDbSrcMacAddr.setStatus("current")
_AlaAppFPDbVlanId_Type = Unsigned32
_AlaAppFPDbVlanId_Object = MibTableColumn
alaAppFPDbVlanId = _AlaAppFPDbVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1, 1, 2, 3, 1, 5),
    _AlaAppFPDbVlanId_Type()
)
alaAppFPDbVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaAppFPDbVlanId.setStatus("current")
_AlaAppFPDbSrcIpAddrType_Type = InetAddressType
_AlaAppFPDbSrcIpAddrType_Object = MibTableColumn
alaAppFPDbSrcIpAddrType = _AlaAppFPDbSrcIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1, 1, 2, 3, 1, 6),
    _AlaAppFPDbSrcIpAddrType_Type()
)
alaAppFPDbSrcIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaAppFPDbSrcIpAddrType.setStatus("current")


class _AlaAppFPDbSrcIpAddr_Type(InetAddress):
    """Custom type alaAppFPDbSrcIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_AlaAppFPDbSrcIpAddr_Type.__name__ = "InetAddress"
_AlaAppFPDbSrcIpAddr_Object = MibTableColumn
alaAppFPDbSrcIpAddr = _AlaAppFPDbSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1, 1, 2, 3, 1, 7),
    _AlaAppFPDbSrcIpAddr_Type()
)
alaAppFPDbSrcIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaAppFPDbSrcIpAddr.setStatus("current")
_AlaAppFPDbSrcPort_Type = InetPortNumber
_AlaAppFPDbSrcPort_Object = MibTableColumn
alaAppFPDbSrcPort = _AlaAppFPDbSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1, 1, 2, 3, 1, 8),
    _AlaAppFPDbSrcPort_Type()
)
alaAppFPDbSrcPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaAppFPDbSrcPort.setStatus("current")
_AlaAppFPDbDstIpAddrType_Type = InetAddressType
_AlaAppFPDbDstIpAddrType_Object = MibTableColumn
alaAppFPDbDstIpAddrType = _AlaAppFPDbDstIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1, 1, 2, 3, 1, 9),
    _AlaAppFPDbDstIpAddrType_Type()
)
alaAppFPDbDstIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppFPDbDstIpAddrType.setStatus("current")


class _AlaAppFPDbDstIpAddr_Type(InetAddress):
    """Custom type alaAppFPDbDstIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_AlaAppFPDbDstIpAddr_Type.__name__ = "InetAddress"
_AlaAppFPDbDstIpAddr_Object = MibTableColumn
alaAppFPDbDstIpAddr = _AlaAppFPDbDstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1, 1, 2, 3, 1, 10),
    _AlaAppFPDbDstIpAddr_Type()
)
alaAppFPDbDstIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppFPDbDstIpAddr.setStatus("current")
_AlaAppFPDbDstPort_Type = InetPortNumber
_AlaAppFPDbDstPort_Object = MibTableColumn
alaAppFPDbDstPort = _AlaAppFPDbDstPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1, 1, 2, 3, 1, 11),
    _AlaAppFPDbDstPort_Type()
)
alaAppFPDbDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppFPDbDstPort.setStatus("current")
_AlaAppFPDbDstMacAddr_Type = MacAddress
_AlaAppFPDbDstMacAddr_Object = MibTableColumn
alaAppFPDbDstMacAddr = _AlaAppFPDbDstMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1, 1, 2, 3, 1, 12),
    _AlaAppFPDbDstMacAddr_Type()
)
alaAppFPDbDstMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppFPDbDstMacAddr.setStatus("current")
_AlaAppFPAppGrpNameTable_Object = MibTable
alaAppFPAppGrpNameTable = _AlaAppFPAppGrpNameTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    alaAppFPAppGrpNameTable.setStatus("current")
_AppFPAppGrpNameEntry_Object = MibTableRow
appFPAppGrpNameEntry = _AppFPAppGrpNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1, 1, 2, 4, 1)
)
appFPAppGrpNameEntry.setIndexNames(
    (0, "ALCATEL-IND1-APP-FINGERPRINT-MIB", "alaAppFPAppGroupName"),
    (0, "ALCATEL-IND1-APP-FINGERPRINT-MIB", "alaAppFPGrpAppName"),
)
if mibBuilder.loadTexts:
    appFPAppGrpNameEntry.setStatus("current")


class _AlaAppFPAppGroupName_Type(SnmpAdminString):
    """Custom type alaAppFPAppGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_AlaAppFPAppGroupName_Type.__name__ = "SnmpAdminString"
_AlaAppFPAppGroupName_Object = MibTableColumn
alaAppFPAppGroupName = _AlaAppFPAppGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1, 1, 2, 4, 1, 1),
    _AlaAppFPAppGroupName_Type()
)
alaAppFPAppGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaAppFPAppGroupName.setStatus("current")


class _AlaAppFPGrpAppName_Type(SnmpAdminString):
    """Custom type alaAppFPGrpAppName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_AlaAppFPGrpAppName_Type.__name__ = "SnmpAdminString"
_AlaAppFPGrpAppName_Object = MibTableColumn
alaAppFPGrpAppName = _AlaAppFPGrpAppName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1, 1, 2, 4, 1, 2),
    _AlaAppFPGrpAppName_Type()
)
alaAppFPGrpAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppFPGrpAppName.setStatus("current")
_AlaAppFPStatsTable_Object = MibTable
alaAppFPStatsTable = _AlaAppFPStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    alaAppFPStatsTable.setStatus("current")
_AlaAppFPStatsEntry_Object = MibTableRow
alaAppFPStatsEntry = _AlaAppFPStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1, 1, 2, 5, 1)
)
alaAppFPStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-APP-FINGERPRINT-MIB", "alaAppFPStatsPort"),
    (0, "ALCATEL-IND1-APP-FINGERPRINT-MIB", "alaAppFPStatsGroupName"),
    (0, "ALCATEL-IND1-APP-FINGERPRINT-MIB", "alaAppFPStatsAppName"),
)
if mibBuilder.loadTexts:
    alaAppFPStatsEntry.setStatus("current")
_AlaAppFPStatsPort_Type = InterfaceIndex
_AlaAppFPStatsPort_Object = MibTableColumn
alaAppFPStatsPort = _AlaAppFPStatsPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1, 1, 2, 5, 1, 1),
    _AlaAppFPStatsPort_Type()
)
alaAppFPStatsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaAppFPStatsPort.setStatus("current")


class _AlaAppFPStatsGroupName_Type(SnmpAdminString):
    """Custom type alaAppFPStatsGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_AlaAppFPStatsGroupName_Type.__name__ = "SnmpAdminString"
_AlaAppFPStatsGroupName_Object = MibTableColumn
alaAppFPStatsGroupName = _AlaAppFPStatsGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1, 1, 2, 5, 1, 2),
    _AlaAppFPStatsGroupName_Type()
)
alaAppFPStatsGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaAppFPStatsGroupName.setStatus("current")


class _AlaAppFPStatsAppName_Type(SnmpAdminString):
    """Custom type alaAppFPStatsAppName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_AlaAppFPStatsAppName_Type.__name__ = "SnmpAdminString"
_AlaAppFPStatsAppName_Object = MibTableColumn
alaAppFPStatsAppName = _AlaAppFPStatsAppName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1, 1, 2, 5, 1, 3),
    _AlaAppFPStatsAppName_Type()
)
alaAppFPStatsAppName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaAppFPStatsAppName.setStatus("current")
_AlaAppFPTotalMatchedLast1Hour_Type = Counter32
_AlaAppFPTotalMatchedLast1Hour_Object = MibTableColumn
alaAppFPTotalMatchedLast1Hour = _AlaAppFPTotalMatchedLast1Hour_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1, 1, 2, 5, 1, 4),
    _AlaAppFPTotalMatchedLast1Hour_Type()
)
alaAppFPTotalMatchedLast1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppFPTotalMatchedLast1Hour.setStatus("current")
_AlaAppFPTotalMatchedLast1Day_Type = Counter32
_AlaAppFPTotalMatchedLast1Day_Object = MibTableColumn
alaAppFPTotalMatchedLast1Day = _AlaAppFPTotalMatchedLast1Day_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1, 1, 2, 5, 1, 5),
    _AlaAppFPTotalMatchedLast1Day_Type()
)
alaAppFPTotalMatchedLast1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAppFPTotalMatchedLast1Day.setStatus("current")
_AlcatelIND1AppFPMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1AppFPMIBConformance = _AlcatelIND1AppFPMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1AppFPMIBConformance.setStatus("current")
_AlcatelIND1AppFPMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1AppFPMIBGroups = _AlcatelIND1AppFPMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1AppFPMIBGroups.setStatus("current")
_AlcatelIND1AppFPMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1AppFPMIBCompliances = _AlcatelIND1AppFPMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1AppFPMIBCompliances.setStatus("current")

# Managed Objects groups

alaAppFPModuleConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1, 2, 1, 1)
)
alaAppFPModuleConfigGroup.setObjects(
      *(("ALCATEL-IND1-APP-FINGERPRINT-MIB", "alaAppFPGlobalAdminState"),
        ("ALCATEL-IND1-APP-FINGERPRINT-MIB", "alaAppFPGlobalReloadSignatureFile"),
        ("ALCATEL-IND1-APP-FINGERPRINT-MIB", "alaAppFPGlobalSignatureFile"),
        ("ALCATEL-IND1-APP-FINGERPRINT-MIB", "alaAppFPGlobalTrapConfig"))
)
if mibBuilder.loadTexts:
    alaAppFPModuleConfigGroup.setStatus("current")

alaAppFPModulePortModeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1, 2, 1, 2)
)
alaAppFPModulePortModeGroup.setObjects(
      *(("ALCATEL-IND1-APP-FINGERPRINT-MIB", "alaAppFPAppDescription"),
        ("ALCATEL-IND1-APP-FINGERPRINT-MIB", "alaAppFPAppSignature"),
        ("ALCATEL-IND1-APP-FINGERPRINT-MIB", "alaAppFPPortOperationMode"),
        ("ALCATEL-IND1-APP-FINGERPRINT-MIB", "alaAppFPPortStatus"),
        ("ALCATEL-IND1-APP-FINGERPRINT-MIB", "alaAppFPPortRowStatus"))
)
if mibBuilder.loadTexts:
    alaAppFPModulePortModeGroup.setStatus("current")

alaAppFPModulePortDBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1, 2, 1, 3)
)
alaAppFPModulePortDBGroup.setObjects(
      *(("ALCATEL-IND1-APP-FINGERPRINT-MIB", "alaAppFPDbDstIpAddrType"),
        ("ALCATEL-IND1-APP-FINGERPRINT-MIB", "alaAppFPDbDstIpAddr"),
        ("ALCATEL-IND1-APP-FINGERPRINT-MIB", "alaAppFPDbDstPort"),
        ("ALCATEL-IND1-APP-FINGERPRINT-MIB", "alaAppFPDbDstMacAddr"),
        ("ALCATEL-IND1-APP-FINGERPRINT-MIB", "alaAppFPGrpAppName"))
)
if mibBuilder.loadTexts:
    alaAppFPModulePortDBGroup.setStatus("current")

alaAppFPModulePortStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1, 2, 1, 4)
)
alaAppFPModulePortStatsGroup.setObjects(
      *(("ALCATEL-IND1-APP-FINGERPRINT-MIB", "alaAppFPTotalMatchedLast1Hour"),
        ("ALCATEL-IND1-APP-FINGERPRINT-MIB", "alaAppFPTotalMatchedLast1Day"))
)
if mibBuilder.loadTexts:
    alaAppFPModulePortStatsGroup.setStatus("current")


# Notification objects

appFPSignatureMatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1, 1, 0, 1)
)
appFPSignatureMatchTrap.setObjects(
      *(("ALCATEL-IND1-APP-FINGERPRINT-MIB", "alaAppFPPort"),
        ("ALCATEL-IND1-APP-FINGERPRINT-MIB", "alaAppFPDbAppGroupName"),
        ("ALCATEL-IND1-APP-FINGERPRINT-MIB", "alaAppFPDbAppName"),
        ("ALCATEL-IND1-APP-FINGERPRINT-MIB", "alaAppFPDbSrcMacAddr"),
        ("ALCATEL-IND1-APP-FINGERPRINT-MIB", "alaAppFPDbVlanId"),
        ("ALCATEL-IND1-APP-FINGERPRINT-MIB", "alaAppFPDbSrcIpAddrType"),
        ("ALCATEL-IND1-APP-FINGERPRINT-MIB", "alaAppFPDbSrcIpAddr"),
        ("ALCATEL-IND1-APP-FINGERPRINT-MIB", "alaAppFPDbSrcPort"))
)
if mibBuilder.loadTexts:
    appFPSignatureMatchTrap.setStatus(
        "current"
    )


# Notifications groups

alaAppFPNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1, 2, 1, 5)
)
alaAppFPNotificationsGroup.setObjects(
    ("ALCATEL-IND1-APP-FINGERPRINT-MIB", "appFPSignatureMatchTrap")
)
if mibBuilder.loadTexts:
    alaAppFPNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alaAppFPMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alaAppFPMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-APP-FINGERPRINT-MIB",
    **{"alcatelIND1AppFPMIB": alcatelIND1AppFPMIB,
       "alcatelIND1AppFPMIBObjects": alcatelIND1AppFPMIBObjects,
       "alaAppFPMIBNotifications": alaAppFPMIBNotifications,
       "appFPSignatureMatchTrap": appFPSignatureMatchTrap,
       "alaAppFPGlobalMIBConfigObjects": alaAppFPGlobalMIBConfigObjects,
       "alaAppFPGlobalAdminState": alaAppFPGlobalAdminState,
       "alaAppFPGlobalSignatureFile": alaAppFPGlobalSignatureFile,
       "alaAppFPGlobalReloadSignatureFile": alaAppFPGlobalReloadSignatureFile,
       "alaAppFPGlobalTrapConfig": alaAppFPGlobalTrapConfig,
       "alaAppFPMIBObjects": alaAppFPMIBObjects,
       "alaAppFPPortTable": alaAppFPPortTable,
       "alaAppFPPortEntry": alaAppFPPortEntry,
       "alaAppFPPort": alaAppFPPort,
       "alaAppFPGroupNameOrPolicyList": alaAppFPGroupNameOrPolicyList,
       "alaAppFPPortOperationMode": alaAppFPPortOperationMode,
       "alaAppFPPortStatus": alaAppFPPortStatus,
       "alaAppFPPortRowStatus": alaAppFPPortRowStatus,
       "alaAppFPAppNameTable": alaAppFPAppNameTable,
       "alaAppFPAppNameEntry": alaAppFPAppNameEntry,
       "alaAppFPAppName": alaAppFPAppName,
       "alaAppFPAppDescription": alaAppFPAppDescription,
       "alaAppFPAppSignature": alaAppFPAppSignature,
       "alaAppFPDatabaseTable": alaAppFPDatabaseTable,
       "alaAppFPDatabaseEntry": alaAppFPDatabaseEntry,
       "alaAppFPDbPort": alaAppFPDbPort,
       "alaAppFPDbAppGroupName": alaAppFPDbAppGroupName,
       "alaAppFPDbAppName": alaAppFPDbAppName,
       "alaAppFPDbSrcMacAddr": alaAppFPDbSrcMacAddr,
       "alaAppFPDbVlanId": alaAppFPDbVlanId,
       "alaAppFPDbSrcIpAddrType": alaAppFPDbSrcIpAddrType,
       "alaAppFPDbSrcIpAddr": alaAppFPDbSrcIpAddr,
       "alaAppFPDbSrcPort": alaAppFPDbSrcPort,
       "alaAppFPDbDstIpAddrType": alaAppFPDbDstIpAddrType,
       "alaAppFPDbDstIpAddr": alaAppFPDbDstIpAddr,
       "alaAppFPDbDstPort": alaAppFPDbDstPort,
       "alaAppFPDbDstMacAddr": alaAppFPDbDstMacAddr,
       "alaAppFPAppGrpNameTable": alaAppFPAppGrpNameTable,
       "appFPAppGrpNameEntry": appFPAppGrpNameEntry,
       "alaAppFPAppGroupName": alaAppFPAppGroupName,
       "alaAppFPGrpAppName": alaAppFPGrpAppName,
       "alaAppFPStatsTable": alaAppFPStatsTable,
       "alaAppFPStatsEntry": alaAppFPStatsEntry,
       "alaAppFPStatsPort": alaAppFPStatsPort,
       "alaAppFPStatsGroupName": alaAppFPStatsGroupName,
       "alaAppFPStatsAppName": alaAppFPStatsAppName,
       "alaAppFPTotalMatchedLast1Hour": alaAppFPTotalMatchedLast1Hour,
       "alaAppFPTotalMatchedLast1Day": alaAppFPTotalMatchedLast1Day,
       "alcatelIND1AppFPMIBConformance": alcatelIND1AppFPMIBConformance,
       "alcatelIND1AppFPMIBGroups": alcatelIND1AppFPMIBGroups,
       "alaAppFPModuleConfigGroup": alaAppFPModuleConfigGroup,
       "alaAppFPModulePortModeGroup": alaAppFPModulePortModeGroup,
       "alaAppFPModulePortDBGroup": alaAppFPModulePortDBGroup,
       "alaAppFPModulePortStatsGroup": alaAppFPModulePortStatsGroup,
       "alaAppFPNotificationsGroup": alaAppFPNotificationsGroup,
       "alcatelIND1AppFPMIBCompliances": alcatelIND1AppFPMIBCompliances,
       "alaAppFPMIBCompliance": alaAppFPMIBCompliance}
)
