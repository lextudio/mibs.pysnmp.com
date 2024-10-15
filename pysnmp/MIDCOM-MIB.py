# SNMP MIB module (MIDCOM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MIDCOM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:59 2024
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

(NatBindIdOrZero,) = mibBuilder.importSymbols(
    "NAT-MIB",
    "NatBindIdOrZero")

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
    "iso",
    "mib-2")

(DisplayString,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

midcomMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 171)
)
midcomMIB.setRevisions(
        ("2007-08-09 10:11",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class MidcomNatBindMode(Integer32, TextualConvention):
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
        *(("addressBind", 1),
          ("addressPortBind", 2),
          ("none", 3))
    )



class MidcomNatSessionIdOrZero(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"


# MIB Managed Objects in the order of their OIDs

_MidcomNotifications_ObjectIdentity = ObjectIdentity
midcomNotifications = _MidcomNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 171, 0)
)
_MidcomObjects_ObjectIdentity = ObjectIdentity
midcomObjects = _MidcomObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 171, 1)
)
_MidcomTransaction_ObjectIdentity = ObjectIdentity
midcomTransaction = _MidcomTransaction_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 171, 1, 1)
)
_MidcomRuleTable_Object = MibTable
midcomRuleTable = _MidcomRuleTable_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 1, 3)
)
if mibBuilder.loadTexts:
    midcomRuleTable.setStatus("current")
_MidcomRuleEntry_Object = MibTableRow
midcomRuleEntry = _MidcomRuleEntry_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 1, 3, 1)
)
midcomRuleEntry.setIndexNames(
    (0, "MIDCOM-MIB", "midcomRuleOwner"),
    (0, "MIDCOM-MIB", "midcomGroupIndex"),
    (0, "MIDCOM-MIB", "midcomRuleIndex"),
)
if mibBuilder.loadTexts:
    midcomRuleEntry.setStatus("current")


class _MidcomRuleOwner_Type(SnmpAdminString):
    """Custom type midcomRuleOwner based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MidcomRuleOwner_Type.__name__ = "SnmpAdminString"
_MidcomRuleOwner_Object = MibTableColumn
midcomRuleOwner = _MidcomRuleOwner_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 1, 3, 1, 1),
    _MidcomRuleOwner_Type()
)
midcomRuleOwner.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    midcomRuleOwner.setStatus("current")


class _MidcomRuleIndex_Type(Unsigned32):
    """Custom type midcomRuleIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_MidcomRuleIndex_Type.__name__ = "Unsigned32"
_MidcomRuleIndex_Object = MibTableColumn
midcomRuleIndex = _MidcomRuleIndex_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 1, 3, 1, 3),
    _MidcomRuleIndex_Type()
)
midcomRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    midcomRuleIndex.setStatus("current")


class _MidcomRuleAdminStatus_Type(Integer32):
    """Custom type midcomRuleAdminStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 2),
          ("notSet", 3),
          ("reserve", 1))
    )


_MidcomRuleAdminStatus_Type.__name__ = "Integer32"
_MidcomRuleAdminStatus_Object = MibTableColumn
midcomRuleAdminStatus = _MidcomRuleAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 1, 3, 1, 4),
    _MidcomRuleAdminStatus_Type()
)
midcomRuleAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midcomRuleAdminStatus.setStatus("current")


class _MidcomRuleOperStatus_Type(Integer32):
    """Custom type midcomRuleOperStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("checkingRequest", 3),
          ("enabled", 8),
          ("genericError", 12),
          ("incorrectRequest", 4),
          ("newEntry", 1),
          ("processingRequest", 5),
          ("requestRejected", 6),
          ("reserved", 7),
          ("setting", 2),
          ("terminated", 11),
          ("terminatedOnRequest", 10),
          ("timedOut", 9))
    )


_MidcomRuleOperStatus_Type.__name__ = "Integer32"
_MidcomRuleOperStatus_Object = MibTableColumn
midcomRuleOperStatus = _MidcomRuleOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 1, 3, 1, 5),
    _MidcomRuleOperStatus_Type()
)
midcomRuleOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midcomRuleOperStatus.setStatus("current")


class _MidcomRuleStorageType_Type(StorageType):
    """Custom type midcomRuleStorageType based on StorageType"""


_MidcomRuleStorageType_Object = MibTableColumn
midcomRuleStorageType = _MidcomRuleStorageType_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 1, 3, 1, 6),
    _MidcomRuleStorageType_Type()
)
midcomRuleStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midcomRuleStorageType.setStatus("current")


class _MidcomRuleStorageTime_Type(Unsigned32):
    """Custom type midcomRuleStorageTime based on Unsigned32"""
    defaultValue = 0


_MidcomRuleStorageTime_Object = MibTableColumn
midcomRuleStorageTime = _MidcomRuleStorageTime_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 1, 3, 1, 7),
    _MidcomRuleStorageTime_Type()
)
midcomRuleStorageTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midcomRuleStorageTime.setStatus("current")
if mibBuilder.loadTexts:
    midcomRuleStorageTime.setUnits("seconds")


class _MidcomRuleError_Type(SnmpAdminString):
    """Custom type midcomRuleError based on SnmpAdminString"""
    defaultHexValue = ""


_MidcomRuleError_Object = MibTableColumn
midcomRuleError = _MidcomRuleError_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 1, 3, 1, 8),
    _MidcomRuleError_Type()
)
midcomRuleError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midcomRuleError.setStatus("current")


class _MidcomRuleInterface_Type(InterfaceIndexOrZero):
    """Custom type midcomRuleInterface based on InterfaceIndexOrZero"""
    defaultValue = 0


_MidcomRuleInterface_Object = MibTableColumn
midcomRuleInterface = _MidcomRuleInterface_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 1, 3, 1, 9),
    _MidcomRuleInterface_Type()
)
midcomRuleInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midcomRuleInterface.setStatus("current")


class _MidcomRuleFlowDirection_Type(Integer32):
    """Custom type midcomRuleFlowDirection based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("biDirectional", 3),
          ("inbound", 1),
          ("outbound", 2))
    )


_MidcomRuleFlowDirection_Type.__name__ = "Integer32"
_MidcomRuleFlowDirection_Object = MibTableColumn
midcomRuleFlowDirection = _MidcomRuleFlowDirection_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 1, 3, 1, 10),
    _MidcomRuleFlowDirection_Type()
)
midcomRuleFlowDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midcomRuleFlowDirection.setStatus("current")


class _MidcomRuleMaxIdleTime_Type(Unsigned32):
    """Custom type midcomRuleMaxIdleTime based on Unsigned32"""
    defaultValue = 0


_MidcomRuleMaxIdleTime_Object = MibTableColumn
midcomRuleMaxIdleTime = _MidcomRuleMaxIdleTime_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 1, 3, 1, 11),
    _MidcomRuleMaxIdleTime_Type()
)
midcomRuleMaxIdleTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midcomRuleMaxIdleTime.setStatus("current")
if mibBuilder.loadTexts:
    midcomRuleMaxIdleTime.setUnits("seconds")


class _MidcomRuleTransportProtocol_Type(Unsigned32):
    """Custom type midcomRuleTransportProtocol based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MidcomRuleTransportProtocol_Type.__name__ = "Unsigned32"
_MidcomRuleTransportProtocol_Object = MibTableColumn
midcomRuleTransportProtocol = _MidcomRuleTransportProtocol_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 1, 3, 1, 12),
    _MidcomRuleTransportProtocol_Type()
)
midcomRuleTransportProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midcomRuleTransportProtocol.setStatus("current")


class _MidcomRulePortRange_Type(Integer32):
    """Custom type midcomRulePortRange based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pair", 2),
          ("single", 1))
    )


_MidcomRulePortRange_Type.__name__ = "Integer32"
_MidcomRulePortRange_Object = MibTableColumn
midcomRulePortRange = _MidcomRulePortRange_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 1, 3, 1, 13),
    _MidcomRulePortRange_Type()
)
midcomRulePortRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midcomRulePortRange.setStatus("current")


class _MidcomRuleInternalIpVersion_Type(InetAddressType):
    """Custom type midcomRuleInternalIpVersion based on InetAddressType"""


_MidcomRuleInternalIpVersion_Object = MibTableColumn
midcomRuleInternalIpVersion = _MidcomRuleInternalIpVersion_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 1, 3, 1, 14),
    _MidcomRuleInternalIpVersion_Type()
)
midcomRuleInternalIpVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midcomRuleInternalIpVersion.setStatus("current")


class _MidcomRuleExternalIpVersion_Type(InetAddressType):
    """Custom type midcomRuleExternalIpVersion based on InetAddressType"""


_MidcomRuleExternalIpVersion_Object = MibTableColumn
midcomRuleExternalIpVersion = _MidcomRuleExternalIpVersion_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 1, 3, 1, 15),
    _MidcomRuleExternalIpVersion_Type()
)
midcomRuleExternalIpVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midcomRuleExternalIpVersion.setStatus("current")
_MidcomRuleInternalIpAddr_Type = InetAddress
_MidcomRuleInternalIpAddr_Object = MibTableColumn
midcomRuleInternalIpAddr = _MidcomRuleInternalIpAddr_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 1, 3, 1, 16),
    _MidcomRuleInternalIpAddr_Type()
)
midcomRuleInternalIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midcomRuleInternalIpAddr.setStatus("current")


class _MidcomRuleInternalIpPrefixLength_Type(InetAddressPrefixLength):
    """Custom type midcomRuleInternalIpPrefixLength based on InetAddressPrefixLength"""
    defaultValue = 128


_MidcomRuleInternalIpPrefixLength_Object = MibTableColumn
midcomRuleInternalIpPrefixLength = _MidcomRuleInternalIpPrefixLength_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 1, 3, 1, 17),
    _MidcomRuleInternalIpPrefixLength_Type()
)
midcomRuleInternalIpPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midcomRuleInternalIpPrefixLength.setStatus("current")


class _MidcomRuleInternalPort_Type(InetPortNumber):
    """Custom type midcomRuleInternalPort based on InetPortNumber"""
    defaultValue = 0


_MidcomRuleInternalPort_Object = MibTableColumn
midcomRuleInternalPort = _MidcomRuleInternalPort_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 1, 3, 1, 18),
    _MidcomRuleInternalPort_Type()
)
midcomRuleInternalPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midcomRuleInternalPort.setStatus("current")
_MidcomRuleExternalIpAddr_Type = InetAddress
_MidcomRuleExternalIpAddr_Object = MibTableColumn
midcomRuleExternalIpAddr = _MidcomRuleExternalIpAddr_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 1, 3, 1, 19),
    _MidcomRuleExternalIpAddr_Type()
)
midcomRuleExternalIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midcomRuleExternalIpAddr.setStatus("current")


class _MidcomRuleExternalIpPrefixLength_Type(InetAddressPrefixLength):
    """Custom type midcomRuleExternalIpPrefixLength based on InetAddressPrefixLength"""
    defaultValue = 128


_MidcomRuleExternalIpPrefixLength_Object = MibTableColumn
midcomRuleExternalIpPrefixLength = _MidcomRuleExternalIpPrefixLength_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 1, 3, 1, 20),
    _MidcomRuleExternalIpPrefixLength_Type()
)
midcomRuleExternalIpPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midcomRuleExternalIpPrefixLength.setStatus("current")


class _MidcomRuleExternalPort_Type(InetPortNumber):
    """Custom type midcomRuleExternalPort based on InetPortNumber"""
    defaultValue = 0


_MidcomRuleExternalPort_Object = MibTableColumn
midcomRuleExternalPort = _MidcomRuleExternalPort_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 1, 3, 1, 21),
    _MidcomRuleExternalPort_Type()
)
midcomRuleExternalPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midcomRuleExternalPort.setStatus("current")
_MidcomRuleInsideIpAddr_Type = InetAddress
_MidcomRuleInsideIpAddr_Object = MibTableColumn
midcomRuleInsideIpAddr = _MidcomRuleInsideIpAddr_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 1, 3, 1, 22),
    _MidcomRuleInsideIpAddr_Type()
)
midcomRuleInsideIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midcomRuleInsideIpAddr.setStatus("current")
_MidcomRuleInsidePort_Type = InetPortNumber
_MidcomRuleInsidePort_Object = MibTableColumn
midcomRuleInsidePort = _MidcomRuleInsidePort_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 1, 3, 1, 23),
    _MidcomRuleInsidePort_Type()
)
midcomRuleInsidePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midcomRuleInsidePort.setStatus("current")
_MidcomRuleOutsideIpAddr_Type = InetAddress
_MidcomRuleOutsideIpAddr_Object = MibTableColumn
midcomRuleOutsideIpAddr = _MidcomRuleOutsideIpAddr_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 1, 3, 1, 24),
    _MidcomRuleOutsideIpAddr_Type()
)
midcomRuleOutsideIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midcomRuleOutsideIpAddr.setStatus("current")
_MidcomRuleOutsidePort_Type = InetPortNumber
_MidcomRuleOutsidePort_Object = MibTableColumn
midcomRuleOutsidePort = _MidcomRuleOutsidePort_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 1, 3, 1, 25),
    _MidcomRuleOutsidePort_Type()
)
midcomRuleOutsidePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midcomRuleOutsidePort.setStatus("current")


class _MidcomRuleLifetime_Type(Unsigned32):
    """Custom type midcomRuleLifetime based on Unsigned32"""
    defaultValue = 180


_MidcomRuleLifetime_Object = MibTableColumn
midcomRuleLifetime = _MidcomRuleLifetime_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 1, 3, 1, 26),
    _MidcomRuleLifetime_Type()
)
midcomRuleLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midcomRuleLifetime.setStatus("current")
if mibBuilder.loadTexts:
    midcomRuleLifetime.setUnits("seconds")
_MidcomRuleRowStatus_Type = RowStatus
_MidcomRuleRowStatus_Object = MibTableColumn
midcomRuleRowStatus = _MidcomRuleRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 1, 3, 1, 27),
    _MidcomRuleRowStatus_Type()
)
midcomRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midcomRuleRowStatus.setStatus("current")
_MidcomGroupTable_Object = MibTable
midcomGroupTable = _MidcomGroupTable_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 1, 4)
)
if mibBuilder.loadTexts:
    midcomGroupTable.setStatus("current")
_MidcomGroupEntry_Object = MibTableRow
midcomGroupEntry = _MidcomGroupEntry_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 1, 4, 1)
)
midcomGroupEntry.setIndexNames(
    (0, "MIDCOM-MIB", "midcomRuleOwner"),
    (0, "MIDCOM-MIB", "midcomGroupIndex"),
)
if mibBuilder.loadTexts:
    midcomGroupEntry.setStatus("current")


class _MidcomGroupIndex_Type(Unsigned32):
    """Custom type midcomGroupIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_MidcomGroupIndex_Type.__name__ = "Unsigned32"
_MidcomGroupIndex_Object = MibTableColumn
midcomGroupIndex = _MidcomGroupIndex_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 1, 4, 1, 2),
    _MidcomGroupIndex_Type()
)
midcomGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    midcomGroupIndex.setStatus("current")
_MidcomGroupLifetime_Type = Unsigned32
_MidcomGroupLifetime_Object = MibTableColumn
midcomGroupLifetime = _MidcomGroupLifetime_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 1, 4, 1, 3),
    _MidcomGroupLifetime_Type()
)
midcomGroupLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midcomGroupLifetime.setStatus("current")
if mibBuilder.loadTexts:
    midcomGroupLifetime.setUnits("seconds")
_MidcomConfig_ObjectIdentity = ObjectIdentity
midcomConfig = _MidcomConfig_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 171, 1, 2)
)
_MidcomConfigMaxLifetime_Type = Unsigned32
_MidcomConfigMaxLifetime_Object = MibScalar
midcomConfigMaxLifetime = _MidcomConfigMaxLifetime_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 2, 1),
    _MidcomConfigMaxLifetime_Type()
)
midcomConfigMaxLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midcomConfigMaxLifetime.setStatus("current")
if mibBuilder.loadTexts:
    midcomConfigMaxLifetime.setUnits("seconds")
_MidcomConfigPersistentRules_Type = TruthValue
_MidcomConfigPersistentRules_Object = MibScalar
midcomConfigPersistentRules = _MidcomConfigPersistentRules_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 2, 2),
    _MidcomConfigPersistentRules_Type()
)
midcomConfigPersistentRules.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midcomConfigPersistentRules.setStatus("current")
_MidcomConfigIfTable_Object = MibTable
midcomConfigIfTable = _MidcomConfigIfTable_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 2, 3)
)
if mibBuilder.loadTexts:
    midcomConfigIfTable.setStatus("current")
_MidcomConfigIfEntry_Object = MibTableRow
midcomConfigIfEntry = _MidcomConfigIfEntry_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 2, 3, 1)
)
midcomConfigIfEntry.setIndexNames(
    (0, "MIDCOM-MIB", "midcomConfigIfIndex"),
)
if mibBuilder.loadTexts:
    midcomConfigIfEntry.setStatus("current")
_MidcomConfigIfIndex_Type = InterfaceIndexOrZero
_MidcomConfigIfIndex_Object = MibTableColumn
midcomConfigIfIndex = _MidcomConfigIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 2, 3, 1, 1),
    _MidcomConfigIfIndex_Type()
)
midcomConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    midcomConfigIfIndex.setStatus("current")


class _MidcomConfigIfBits_Type(Bits):
    """Custom type midcomConfigIfBits based on Bits"""
    namedValues = NamedValues(
        *(("addressWildcards", 2),
          ("firewall", 4),
          ("inside", 9),
          ("ipv4", 0),
          ("ipv6", 1),
          ("nat", 5),
          ("portTranslation", 6),
          ("portWildcards", 3),
          ("protocolTranslation", 7),
          ("twiceNat", 8))
    )

_MidcomConfigIfBits_Type.__name__ = "Bits"
_MidcomConfigIfBits_Object = MibTableColumn
midcomConfigIfBits = _MidcomConfigIfBits_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 2, 3, 1, 2),
    _MidcomConfigIfBits_Type()
)
midcomConfigIfBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midcomConfigIfBits.setStatus("current")


class _MidcomConfigIfEnabled_Type(TruthValue):
    """Custom type midcomConfigIfEnabled based on TruthValue"""


_MidcomConfigIfEnabled_Object = MibTableColumn
midcomConfigIfEnabled = _MidcomConfigIfEnabled_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 2, 3, 1, 3),
    _MidcomConfigIfEnabled_Type()
)
midcomConfigIfEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midcomConfigIfEnabled.setStatus("current")
_MidcomConfigFirewallTable_Object = MibTable
midcomConfigFirewallTable = _MidcomConfigFirewallTable_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 2, 4)
)
if mibBuilder.loadTexts:
    midcomConfigFirewallTable.setStatus("current")
_MidcomConfigFirewallEntry_Object = MibTableRow
midcomConfigFirewallEntry = _MidcomConfigFirewallEntry_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 2, 4, 1)
)
midcomConfigFirewallEntry.setIndexNames(
    (0, "MIDCOM-MIB", "midcomConfigFirewallIndex"),
)
if mibBuilder.loadTexts:
    midcomConfigFirewallEntry.setStatus("current")
_MidcomConfigFirewallIndex_Type = InterfaceIndexOrZero
_MidcomConfigFirewallIndex_Object = MibTableColumn
midcomConfigFirewallIndex = _MidcomConfigFirewallIndex_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 2, 4, 1, 1),
    _MidcomConfigFirewallIndex_Type()
)
midcomConfigFirewallIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    midcomConfigFirewallIndex.setStatus("current")
_MidcomConfigFirewallGroupId_Type = SnmpAdminString
_MidcomConfigFirewallGroupId_Object = MibTableColumn
midcomConfigFirewallGroupId = _MidcomConfigFirewallGroupId_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 2, 4, 1, 2),
    _MidcomConfigFirewallGroupId_Type()
)
midcomConfigFirewallGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midcomConfigFirewallGroupId.setStatus("current")
_MidcomConfigFirewallPriority_Type = Unsigned32
_MidcomConfigFirewallPriority_Object = MibTableColumn
midcomConfigFirewallPriority = _MidcomConfigFirewallPriority_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 2, 4, 1, 3),
    _MidcomConfigFirewallPriority_Type()
)
midcomConfigFirewallPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midcomConfigFirewallPriority.setStatus("current")
_MidcomMonitoring_ObjectIdentity = ObjectIdentity
midcomMonitoring = _MidcomMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 171, 1, 3)
)
_MidcomResourceTable_Object = MibTable
midcomResourceTable = _MidcomResourceTable_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 3, 1)
)
if mibBuilder.loadTexts:
    midcomResourceTable.setStatus("current")
_MidcomResourceEntry_Object = MibTableRow
midcomResourceEntry = _MidcomResourceEntry_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    midcomResourceEntry.setStatus("current")
_MidcomRscNatInternalAddrBindMode_Type = MidcomNatBindMode
_MidcomRscNatInternalAddrBindMode_Object = MibTableColumn
midcomRscNatInternalAddrBindMode = _MidcomRscNatInternalAddrBindMode_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 3, 1, 1, 4),
    _MidcomRscNatInternalAddrBindMode_Type()
)
midcomRscNatInternalAddrBindMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midcomRscNatInternalAddrBindMode.setStatus("current")
_MidcomRscNatInternalAddrBindId_Type = NatBindIdOrZero
_MidcomRscNatInternalAddrBindId_Object = MibTableColumn
midcomRscNatInternalAddrBindId = _MidcomRscNatInternalAddrBindId_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 3, 1, 1, 5),
    _MidcomRscNatInternalAddrBindId_Type()
)
midcomRscNatInternalAddrBindId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midcomRscNatInternalAddrBindId.setStatus("current")
_MidcomRscNatInsideAddrBindMode_Type = MidcomNatBindMode
_MidcomRscNatInsideAddrBindMode_Object = MibTableColumn
midcomRscNatInsideAddrBindMode = _MidcomRscNatInsideAddrBindMode_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 3, 1, 1, 6),
    _MidcomRscNatInsideAddrBindMode_Type()
)
midcomRscNatInsideAddrBindMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midcomRscNatInsideAddrBindMode.setStatus("current")
_MidcomRscNatInsideAddrBindId_Type = NatBindIdOrZero
_MidcomRscNatInsideAddrBindId_Object = MibTableColumn
midcomRscNatInsideAddrBindId = _MidcomRscNatInsideAddrBindId_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 3, 1, 1, 7),
    _MidcomRscNatInsideAddrBindId_Type()
)
midcomRscNatInsideAddrBindId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midcomRscNatInsideAddrBindId.setStatus("current")
_MidcomRscNatSessionId1_Type = MidcomNatSessionIdOrZero
_MidcomRscNatSessionId1_Object = MibTableColumn
midcomRscNatSessionId1 = _MidcomRscNatSessionId1_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 3, 1, 1, 8),
    _MidcomRscNatSessionId1_Type()
)
midcomRscNatSessionId1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midcomRscNatSessionId1.setStatus("current")
_MidcomRscNatSessionId2_Type = MidcomNatSessionIdOrZero
_MidcomRscNatSessionId2_Object = MibTableColumn
midcomRscNatSessionId2 = _MidcomRscNatSessionId2_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 3, 1, 1, 9),
    _MidcomRscNatSessionId2_Type()
)
midcomRscNatSessionId2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midcomRscNatSessionId2.setStatus("current")
_MidcomRscFirewallRuleId_Type = Unsigned32
_MidcomRscFirewallRuleId_Object = MibTableColumn
midcomRscFirewallRuleId = _MidcomRscFirewallRuleId_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 3, 1, 1, 10),
    _MidcomRscFirewallRuleId_Type()
)
midcomRscFirewallRuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midcomRscFirewallRuleId.setStatus("current")
_MidcomStatistics_ObjectIdentity = ObjectIdentity
midcomStatistics = _MidcomStatistics_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 171, 1, 3, 2)
)
_MidcomCurrentOwners_Type = Gauge32
_MidcomCurrentOwners_Object = MibScalar
midcomCurrentOwners = _MidcomCurrentOwners_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 3, 2, 1),
    _MidcomCurrentOwners_Type()
)
midcomCurrentOwners.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midcomCurrentOwners.setStatus("current")
_MidcomTotalRejectedRuleEntries_Type = Counter32
_MidcomTotalRejectedRuleEntries_Object = MibScalar
midcomTotalRejectedRuleEntries = _MidcomTotalRejectedRuleEntries_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 3, 2, 2),
    _MidcomTotalRejectedRuleEntries_Type()
)
midcomTotalRejectedRuleEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midcomTotalRejectedRuleEntries.setStatus("current")
_MidcomCurrentRulesIncomplete_Type = Gauge32
_MidcomCurrentRulesIncomplete_Object = MibScalar
midcomCurrentRulesIncomplete = _MidcomCurrentRulesIncomplete_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 3, 2, 3),
    _MidcomCurrentRulesIncomplete_Type()
)
midcomCurrentRulesIncomplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midcomCurrentRulesIncomplete.setStatus("current")
_MidcomTotalIncorrectReserveRules_Type = Counter32
_MidcomTotalIncorrectReserveRules_Object = MibScalar
midcomTotalIncorrectReserveRules = _MidcomTotalIncorrectReserveRules_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 3, 2, 4),
    _MidcomTotalIncorrectReserveRules_Type()
)
midcomTotalIncorrectReserveRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midcomTotalIncorrectReserveRules.setStatus("current")
_MidcomTotalRejectedReserveRules_Type = Counter32
_MidcomTotalRejectedReserveRules_Object = MibScalar
midcomTotalRejectedReserveRules = _MidcomTotalRejectedReserveRules_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 3, 2, 5),
    _MidcomTotalRejectedReserveRules_Type()
)
midcomTotalRejectedReserveRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midcomTotalRejectedReserveRules.setStatus("current")
_MidcomCurrentActiveReserveRules_Type = Gauge32
_MidcomCurrentActiveReserveRules_Object = MibScalar
midcomCurrentActiveReserveRules = _MidcomCurrentActiveReserveRules_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 3, 2, 6),
    _MidcomCurrentActiveReserveRules_Type()
)
midcomCurrentActiveReserveRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midcomCurrentActiveReserveRules.setStatus("current")
_MidcomTotalExpiredReserveRules_Type = Counter32
_MidcomTotalExpiredReserveRules_Object = MibScalar
midcomTotalExpiredReserveRules = _MidcomTotalExpiredReserveRules_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 3, 2, 7),
    _MidcomTotalExpiredReserveRules_Type()
)
midcomTotalExpiredReserveRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midcomTotalExpiredReserveRules.setStatus("current")
_MidcomTotalTerminatedOnRqReserveRules_Type = Counter32
_MidcomTotalTerminatedOnRqReserveRules_Object = MibScalar
midcomTotalTerminatedOnRqReserveRules = _MidcomTotalTerminatedOnRqReserveRules_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 3, 2, 8),
    _MidcomTotalTerminatedOnRqReserveRules_Type()
)
midcomTotalTerminatedOnRqReserveRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midcomTotalTerminatedOnRqReserveRules.setStatus("current")
_MidcomTotalTerminatedReserveRules_Type = Counter32
_MidcomTotalTerminatedReserveRules_Object = MibScalar
midcomTotalTerminatedReserveRules = _MidcomTotalTerminatedReserveRules_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 3, 2, 9),
    _MidcomTotalTerminatedReserveRules_Type()
)
midcomTotalTerminatedReserveRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midcomTotalTerminatedReserveRules.setStatus("current")
_MidcomTotalIncorrectEnableRules_Type = Counter32
_MidcomTotalIncorrectEnableRules_Object = MibScalar
midcomTotalIncorrectEnableRules = _MidcomTotalIncorrectEnableRules_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 3, 2, 10),
    _MidcomTotalIncorrectEnableRules_Type()
)
midcomTotalIncorrectEnableRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midcomTotalIncorrectEnableRules.setStatus("current")
_MidcomTotalRejectedEnableRules_Type = Counter32
_MidcomTotalRejectedEnableRules_Object = MibScalar
midcomTotalRejectedEnableRules = _MidcomTotalRejectedEnableRules_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 3, 2, 11),
    _MidcomTotalRejectedEnableRules_Type()
)
midcomTotalRejectedEnableRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midcomTotalRejectedEnableRules.setStatus("current")
_MidcomCurrentActiveEnableRules_Type = Gauge32
_MidcomCurrentActiveEnableRules_Object = MibScalar
midcomCurrentActiveEnableRules = _MidcomCurrentActiveEnableRules_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 3, 2, 12),
    _MidcomCurrentActiveEnableRules_Type()
)
midcomCurrentActiveEnableRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midcomCurrentActiveEnableRules.setStatus("current")
_MidcomTotalExpiredEnableRules_Type = Counter32
_MidcomTotalExpiredEnableRules_Object = MibScalar
midcomTotalExpiredEnableRules = _MidcomTotalExpiredEnableRules_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 3, 2, 13),
    _MidcomTotalExpiredEnableRules_Type()
)
midcomTotalExpiredEnableRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midcomTotalExpiredEnableRules.setStatus("current")
_MidcomTotalTerminatedOnRqEnableRules_Type = Counter32
_MidcomTotalTerminatedOnRqEnableRules_Object = MibScalar
midcomTotalTerminatedOnRqEnableRules = _MidcomTotalTerminatedOnRqEnableRules_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 3, 2, 14),
    _MidcomTotalTerminatedOnRqEnableRules_Type()
)
midcomTotalTerminatedOnRqEnableRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midcomTotalTerminatedOnRqEnableRules.setStatus("current")
_MidcomTotalTerminatedEnableRules_Type = Counter32
_MidcomTotalTerminatedEnableRules_Object = MibScalar
midcomTotalTerminatedEnableRules = _MidcomTotalTerminatedEnableRules_Object(
    (1, 3, 6, 1, 2, 1, 171, 1, 3, 2, 15),
    _MidcomTotalTerminatedEnableRules_Type()
)
midcomTotalTerminatedEnableRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midcomTotalTerminatedEnableRules.setStatus("current")
_MidcomConformance_ObjectIdentity = ObjectIdentity
midcomConformance = _MidcomConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 171, 2)
)
_MidcomCompliances_ObjectIdentity = ObjectIdentity
midcomCompliances = _MidcomCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 171, 2, 1)
)
_MidcomGroups_ObjectIdentity = ObjectIdentity
midcomGroups = _MidcomGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 171, 2, 2)
)
midcomRuleEntry.registerAugmentions(
    ("MIDCOM-MIB",
     "midcomResourceEntry")
)
midcomResourceEntry.setIndexNames(*midcomRuleEntry.getIndexNames())

# Managed Objects groups

midcomRuleGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 171, 2, 2, 1)
)
midcomRuleGroup.setObjects(
      *(("MIDCOM-MIB", "midcomRuleAdminStatus"),
        ("MIDCOM-MIB", "midcomRuleOperStatus"),
        ("MIDCOM-MIB", "midcomRuleStorageType"),
        ("MIDCOM-MIB", "midcomRuleStorageTime"),
        ("MIDCOM-MIB", "midcomRuleError"),
        ("MIDCOM-MIB", "midcomRuleInterface"),
        ("MIDCOM-MIB", "midcomRuleFlowDirection"),
        ("MIDCOM-MIB", "midcomRuleMaxIdleTime"),
        ("MIDCOM-MIB", "midcomRuleTransportProtocol"),
        ("MIDCOM-MIB", "midcomRulePortRange"),
        ("MIDCOM-MIB", "midcomRuleInternalIpVersion"),
        ("MIDCOM-MIB", "midcomRuleExternalIpVersion"),
        ("MIDCOM-MIB", "midcomRuleInternalIpAddr"),
        ("MIDCOM-MIB", "midcomRuleInternalIpPrefixLength"),
        ("MIDCOM-MIB", "midcomRuleInternalPort"),
        ("MIDCOM-MIB", "midcomRuleExternalIpAddr"),
        ("MIDCOM-MIB", "midcomRuleExternalIpPrefixLength"),
        ("MIDCOM-MIB", "midcomRuleExternalPort"),
        ("MIDCOM-MIB", "midcomRuleInsideIpAddr"),
        ("MIDCOM-MIB", "midcomRuleInsidePort"),
        ("MIDCOM-MIB", "midcomRuleOutsideIpAddr"),
        ("MIDCOM-MIB", "midcomRuleOutsidePort"),
        ("MIDCOM-MIB", "midcomRuleLifetime"),
        ("MIDCOM-MIB", "midcomRuleRowStatus"),
        ("MIDCOM-MIB", "midcomGroupLifetime"))
)
if mibBuilder.loadTexts:
    midcomRuleGroup.setStatus("current")

midcomCapabilitiesGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 171, 2, 2, 2)
)
midcomCapabilitiesGroup.setObjects(
      *(("MIDCOM-MIB", "midcomConfigMaxLifetime"),
        ("MIDCOM-MIB", "midcomConfigPersistentRules"),
        ("MIDCOM-MIB", "midcomConfigIfBits"),
        ("MIDCOM-MIB", "midcomConfigIfEnabled"))
)
if mibBuilder.loadTexts:
    midcomCapabilitiesGroup.setStatus("current")

midcomConfigFirewallGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 171, 2, 2, 3)
)
midcomConfigFirewallGroup.setObjects(
      *(("MIDCOM-MIB", "midcomConfigFirewallGroupId"),
        ("MIDCOM-MIB", "midcomConfigFirewallPriority"))
)
if mibBuilder.loadTexts:
    midcomConfigFirewallGroup.setStatus("current")

midcomResourceGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 171, 2, 2, 4)
)
midcomResourceGroup.setObjects(
      *(("MIDCOM-MIB", "midcomRscNatInternalAddrBindMode"),
        ("MIDCOM-MIB", "midcomRscNatInternalAddrBindId"),
        ("MIDCOM-MIB", "midcomRscNatInsideAddrBindMode"),
        ("MIDCOM-MIB", "midcomRscNatInsideAddrBindId"),
        ("MIDCOM-MIB", "midcomRscNatSessionId1"),
        ("MIDCOM-MIB", "midcomRscNatSessionId2"),
        ("MIDCOM-MIB", "midcomRscFirewallRuleId"))
)
if mibBuilder.loadTexts:
    midcomResourceGroup.setStatus("current")

midcomStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 171, 2, 2, 5)
)
midcomStatisticsGroup.setObjects(
      *(("MIDCOM-MIB", "midcomCurrentOwners"),
        ("MIDCOM-MIB", "midcomTotalRejectedRuleEntries"),
        ("MIDCOM-MIB", "midcomCurrentRulesIncomplete"),
        ("MIDCOM-MIB", "midcomTotalIncorrectReserveRules"),
        ("MIDCOM-MIB", "midcomTotalRejectedReserveRules"),
        ("MIDCOM-MIB", "midcomCurrentActiveReserveRules"),
        ("MIDCOM-MIB", "midcomTotalExpiredReserveRules"),
        ("MIDCOM-MIB", "midcomTotalTerminatedOnRqReserveRules"),
        ("MIDCOM-MIB", "midcomTotalTerminatedReserveRules"),
        ("MIDCOM-MIB", "midcomTotalIncorrectEnableRules"),
        ("MIDCOM-MIB", "midcomTotalRejectedEnableRules"),
        ("MIDCOM-MIB", "midcomCurrentActiveEnableRules"),
        ("MIDCOM-MIB", "midcomTotalExpiredEnableRules"),
        ("MIDCOM-MIB", "midcomTotalTerminatedOnRqEnableRules"),
        ("MIDCOM-MIB", "midcomTotalTerminatedEnableRules"))
)
if mibBuilder.loadTexts:
    midcomStatisticsGroup.setStatus("current")


# Notification objects

midcomUnsolicitedRuleEvent = NotificationType(
    (1, 3, 6, 1, 2, 1, 171, 0, 1)
)
midcomUnsolicitedRuleEvent.setObjects(
      *(("MIDCOM-MIB", "midcomRuleOperStatus"),
        ("MIDCOM-MIB", "midcomRuleLifetime"))
)
if mibBuilder.loadTexts:
    midcomUnsolicitedRuleEvent.setStatus(
        "current"
    )

midcomSolicitedRuleEvent = NotificationType(
    (1, 3, 6, 1, 2, 1, 171, 0, 2)
)
midcomSolicitedRuleEvent.setObjects(
      *(("MIDCOM-MIB", "midcomRuleOperStatus"),
        ("MIDCOM-MIB", "midcomRuleLifetime"))
)
if mibBuilder.loadTexts:
    midcomSolicitedRuleEvent.setStatus(
        "current"
    )

midcomSolicitedGroupEvent = NotificationType(
    (1, 3, 6, 1, 2, 1, 171, 0, 3)
)
midcomSolicitedGroupEvent.setObjects(
    ("MIDCOM-MIB", "midcomGroupLifetime")
)
if mibBuilder.loadTexts:
    midcomSolicitedGroupEvent.setStatus(
        "current"
    )


# Notifications groups

midcomNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 171, 2, 2, 6)
)
midcomNotificationsGroup.setObjects(
      *(("MIDCOM-MIB", "midcomUnsolicitedRuleEvent"),
        ("MIDCOM-MIB", "midcomSolicitedRuleEvent"),
        ("MIDCOM-MIB", "midcomSolicitedGroupEvent"))
)
if mibBuilder.loadTexts:
    midcomNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

midcomCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 171, 2, 1, 1)
)
if mibBuilder.loadTexts:
    midcomCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MIDCOM-MIB",
    **{"MidcomNatBindMode": MidcomNatBindMode,
       "MidcomNatSessionIdOrZero": MidcomNatSessionIdOrZero,
       "midcomMIB": midcomMIB,
       "midcomNotifications": midcomNotifications,
       "midcomUnsolicitedRuleEvent": midcomUnsolicitedRuleEvent,
       "midcomSolicitedRuleEvent": midcomSolicitedRuleEvent,
       "midcomSolicitedGroupEvent": midcomSolicitedGroupEvent,
       "midcomObjects": midcomObjects,
       "midcomTransaction": midcomTransaction,
       "midcomRuleTable": midcomRuleTable,
       "midcomRuleEntry": midcomRuleEntry,
       "midcomRuleOwner": midcomRuleOwner,
       "midcomRuleIndex": midcomRuleIndex,
       "midcomRuleAdminStatus": midcomRuleAdminStatus,
       "midcomRuleOperStatus": midcomRuleOperStatus,
       "midcomRuleStorageType": midcomRuleStorageType,
       "midcomRuleStorageTime": midcomRuleStorageTime,
       "midcomRuleError": midcomRuleError,
       "midcomRuleInterface": midcomRuleInterface,
       "midcomRuleFlowDirection": midcomRuleFlowDirection,
       "midcomRuleMaxIdleTime": midcomRuleMaxIdleTime,
       "midcomRuleTransportProtocol": midcomRuleTransportProtocol,
       "midcomRulePortRange": midcomRulePortRange,
       "midcomRuleInternalIpVersion": midcomRuleInternalIpVersion,
       "midcomRuleExternalIpVersion": midcomRuleExternalIpVersion,
       "midcomRuleInternalIpAddr": midcomRuleInternalIpAddr,
       "midcomRuleInternalIpPrefixLength": midcomRuleInternalIpPrefixLength,
       "midcomRuleInternalPort": midcomRuleInternalPort,
       "midcomRuleExternalIpAddr": midcomRuleExternalIpAddr,
       "midcomRuleExternalIpPrefixLength": midcomRuleExternalIpPrefixLength,
       "midcomRuleExternalPort": midcomRuleExternalPort,
       "midcomRuleInsideIpAddr": midcomRuleInsideIpAddr,
       "midcomRuleInsidePort": midcomRuleInsidePort,
       "midcomRuleOutsideIpAddr": midcomRuleOutsideIpAddr,
       "midcomRuleOutsidePort": midcomRuleOutsidePort,
       "midcomRuleLifetime": midcomRuleLifetime,
       "midcomRuleRowStatus": midcomRuleRowStatus,
       "midcomGroupTable": midcomGroupTable,
       "midcomGroupEntry": midcomGroupEntry,
       "midcomGroupIndex": midcomGroupIndex,
       "midcomGroupLifetime": midcomGroupLifetime,
       "midcomConfig": midcomConfig,
       "midcomConfigMaxLifetime": midcomConfigMaxLifetime,
       "midcomConfigPersistentRules": midcomConfigPersistentRules,
       "midcomConfigIfTable": midcomConfigIfTable,
       "midcomConfigIfEntry": midcomConfigIfEntry,
       "midcomConfigIfIndex": midcomConfigIfIndex,
       "midcomConfigIfBits": midcomConfigIfBits,
       "midcomConfigIfEnabled": midcomConfigIfEnabled,
       "midcomConfigFirewallTable": midcomConfigFirewallTable,
       "midcomConfigFirewallEntry": midcomConfigFirewallEntry,
       "midcomConfigFirewallIndex": midcomConfigFirewallIndex,
       "midcomConfigFirewallGroupId": midcomConfigFirewallGroupId,
       "midcomConfigFirewallPriority": midcomConfigFirewallPriority,
       "midcomMonitoring": midcomMonitoring,
       "midcomResourceTable": midcomResourceTable,
       "midcomResourceEntry": midcomResourceEntry,
       "midcomRscNatInternalAddrBindMode": midcomRscNatInternalAddrBindMode,
       "midcomRscNatInternalAddrBindId": midcomRscNatInternalAddrBindId,
       "midcomRscNatInsideAddrBindMode": midcomRscNatInsideAddrBindMode,
       "midcomRscNatInsideAddrBindId": midcomRscNatInsideAddrBindId,
       "midcomRscNatSessionId1": midcomRscNatSessionId1,
       "midcomRscNatSessionId2": midcomRscNatSessionId2,
       "midcomRscFirewallRuleId": midcomRscFirewallRuleId,
       "midcomStatistics": midcomStatistics,
       "midcomCurrentOwners": midcomCurrentOwners,
       "midcomTotalRejectedRuleEntries": midcomTotalRejectedRuleEntries,
       "midcomCurrentRulesIncomplete": midcomCurrentRulesIncomplete,
       "midcomTotalIncorrectReserveRules": midcomTotalIncorrectReserveRules,
       "midcomTotalRejectedReserveRules": midcomTotalRejectedReserveRules,
       "midcomCurrentActiveReserveRules": midcomCurrentActiveReserveRules,
       "midcomTotalExpiredReserveRules": midcomTotalExpiredReserveRules,
       "midcomTotalTerminatedOnRqReserveRules": midcomTotalTerminatedOnRqReserveRules,
       "midcomTotalTerminatedReserveRules": midcomTotalTerminatedReserveRules,
       "midcomTotalIncorrectEnableRules": midcomTotalIncorrectEnableRules,
       "midcomTotalRejectedEnableRules": midcomTotalRejectedEnableRules,
       "midcomCurrentActiveEnableRules": midcomCurrentActiveEnableRules,
       "midcomTotalExpiredEnableRules": midcomTotalExpiredEnableRules,
       "midcomTotalTerminatedOnRqEnableRules": midcomTotalTerminatedOnRqEnableRules,
       "midcomTotalTerminatedEnableRules": midcomTotalTerminatedEnableRules,
       "midcomConformance": midcomConformance,
       "midcomCompliances": midcomCompliances,
       "midcomCompliance": midcomCompliance,
       "midcomGroups": midcomGroups,
       "midcomRuleGroup": midcomRuleGroup,
       "midcomCapabilitiesGroup": midcomCapabilitiesGroup,
       "midcomConfigFirewallGroup": midcomConfigFirewallGroup,
       "midcomResourceGroup": midcomResourceGroup,
       "midcomStatisticsGroup": midcomStatisticsGroup,
       "midcomNotificationsGroup": midcomNotificationsGroup}
)
