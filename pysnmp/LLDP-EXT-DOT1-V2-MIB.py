# SNMP MIB module (LLDP-EXT-DOT1-V2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LLDP-EXT-DOT1-V2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:49 2024
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

(IEEE8021PriorityValue,) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "IEEE8021PriorityValue")

(ifGeneralInformationGroup,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifGeneralInformationGroup")

(lldpV2Extensions,
 lldpV2LocPortIfIndex,
 lldpV2PortConfigEntry,
 lldpV2RemIndex,
 lldpV2RemLocalDestMACAddress,
 lldpV2RemLocalIfIndex,
 lldpV2RemTimeMark) = mibBuilder.importSymbols(
    "LLDP-V2-MIB",
    "lldpV2Extensions",
    "lldpV2LocPortIfIndex",
    "lldpV2PortConfigEntry",
    "lldpV2RemIndex",
    "lldpV2RemLocalDestMACAddress",
    "lldpV2RemLocalIfIndex",
    "lldpV2RemTimeMark")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

lldpV2Xdot1MIB = ModuleIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962)
)
lldpV2Xdot1MIB.setRevisions(
        ("2018-06-21 00:00",
         "2015-02-16 00:00",
         "2015-02-16 00:00",
         "2014-12-15 00:00",
         "2011-03-25 00:00",
         "2011-03-23 00:00",
         "2009-06-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class LldpV2XLinkAggStatusMap(Bits, TextualConvention):
    status = "current"


class LldpV2CnBitVector(Bits, TextualConvention):
    status = "current"


class LldpXdot1dcbxTrafficClassValue(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class LldpXdot1dcbxTrafficClassBandwidthValue(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class LldpXdot1dcbxAppSelector(Integer32, TextualConvention):
    status = "current"
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
        *(("asDSCPValue", 5),
          ("asEthertype", 1),
          ("asTCPPortNumber", 2),
          ("asTCPUDPPortNumber", 4),
          ("asUDPPortNumber", 3))
    )



class LldpXdot1dcbxAppProtocol(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class LldpXdot1dcbxSupportedCapacity(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )



class LldpXdot1dcbxTrafficSelectionAlgorithm(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("tsaCreditBasedShaper", 1),
          ("tsaEnhancedTransmission", 2),
          ("tsaStrictPriority", 0),
          ("tsaVendorSpecific", 255))
    )



# MIB Managed Objects in the order of their OIDs

_LldpV2Xdot1Objects_ObjectIdentity = ObjectIdentity
lldpV2Xdot1Objects = _LldpV2Xdot1Objects_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1)
)
_LldpV2Xdot1Config_ObjectIdentity = ObjectIdentity
lldpV2Xdot1Config = _LldpV2Xdot1Config_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 1)
)
_LldpV2Xdot1ConfigPortVlanTable_Object = MibTable
lldpV2Xdot1ConfigPortVlanTable = _LldpV2Xdot1ConfigPortVlanTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 1, 1)
)
if mibBuilder.loadTexts:
    lldpV2Xdot1ConfigPortVlanTable.setStatus("current")
_LldpV2Xdot1ConfigPortVlanEntry_Object = MibTableRow
lldpV2Xdot1ConfigPortVlanEntry = _LldpV2Xdot1ConfigPortVlanEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    lldpV2Xdot1ConfigPortVlanEntry.setStatus("current")


class _LldpV2Xdot1ConfigPortVlanTxEnable_Type(TruthValue):
    """Custom type lldpV2Xdot1ConfigPortVlanTxEnable based on TruthValue"""


_LldpV2Xdot1ConfigPortVlanTxEnable_Object = MibTableColumn
lldpV2Xdot1ConfigPortVlanTxEnable = _LldpV2Xdot1ConfigPortVlanTxEnable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 1, 1, 1, 1),
    _LldpV2Xdot1ConfigPortVlanTxEnable_Type()
)
lldpV2Xdot1ConfigPortVlanTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpV2Xdot1ConfigPortVlanTxEnable.setStatus("current")
_LldpV2Xdot1ConfigVlanNameTable_Object = MibTable
lldpV2Xdot1ConfigVlanNameTable = _LldpV2Xdot1ConfigVlanNameTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 1, 2)
)
if mibBuilder.loadTexts:
    lldpV2Xdot1ConfigVlanNameTable.setStatus("current")
_LldpV2Xdot1ConfigVlanNameEntry_Object = MibTableRow
lldpV2Xdot1ConfigVlanNameEntry = _LldpV2Xdot1ConfigVlanNameEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    lldpV2Xdot1ConfigVlanNameEntry.setStatus("current")


class _LldpV2Xdot1ConfigVlanNameTxEnable_Type(TruthValue):
    """Custom type lldpV2Xdot1ConfigVlanNameTxEnable based on TruthValue"""


_LldpV2Xdot1ConfigVlanNameTxEnable_Object = MibTableColumn
lldpV2Xdot1ConfigVlanNameTxEnable = _LldpV2Xdot1ConfigVlanNameTxEnable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 1, 2, 1, 1),
    _LldpV2Xdot1ConfigVlanNameTxEnable_Type()
)
lldpV2Xdot1ConfigVlanNameTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpV2Xdot1ConfigVlanNameTxEnable.setStatus("current")
_LldpV2Xdot1ConfigProtoVlanTable_Object = MibTable
lldpV2Xdot1ConfigProtoVlanTable = _LldpV2Xdot1ConfigProtoVlanTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 1, 3)
)
if mibBuilder.loadTexts:
    lldpV2Xdot1ConfigProtoVlanTable.setStatus("current")
_LldpV2Xdot1ConfigProtoVlanEntry_Object = MibTableRow
lldpV2Xdot1ConfigProtoVlanEntry = _LldpV2Xdot1ConfigProtoVlanEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    lldpV2Xdot1ConfigProtoVlanEntry.setStatus("current")


class _LldpV2Xdot1ConfigProtoVlanTxEnable_Type(TruthValue):
    """Custom type lldpV2Xdot1ConfigProtoVlanTxEnable based on TruthValue"""


_LldpV2Xdot1ConfigProtoVlanTxEnable_Object = MibTableColumn
lldpV2Xdot1ConfigProtoVlanTxEnable = _LldpV2Xdot1ConfigProtoVlanTxEnable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 1, 3, 1, 1),
    _LldpV2Xdot1ConfigProtoVlanTxEnable_Type()
)
lldpV2Xdot1ConfigProtoVlanTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpV2Xdot1ConfigProtoVlanTxEnable.setStatus("current")
_LldpV2Xdot1ConfigProtocolTable_Object = MibTable
lldpV2Xdot1ConfigProtocolTable = _LldpV2Xdot1ConfigProtocolTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 1, 4)
)
if mibBuilder.loadTexts:
    lldpV2Xdot1ConfigProtocolTable.setStatus("current")
_LldpV2Xdot1ConfigProtocolEntry_Object = MibTableRow
lldpV2Xdot1ConfigProtocolEntry = _LldpV2Xdot1ConfigProtocolEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    lldpV2Xdot1ConfigProtocolEntry.setStatus("current")


class _LldpV2Xdot1ConfigProtocolTxEnable_Type(TruthValue):
    """Custom type lldpV2Xdot1ConfigProtocolTxEnable based on TruthValue"""


_LldpV2Xdot1ConfigProtocolTxEnable_Object = MibTableColumn
lldpV2Xdot1ConfigProtocolTxEnable = _LldpV2Xdot1ConfigProtocolTxEnable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 1, 4, 1, 1),
    _LldpV2Xdot1ConfigProtocolTxEnable_Type()
)
lldpV2Xdot1ConfigProtocolTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpV2Xdot1ConfigProtocolTxEnable.setStatus("current")
_LldpV2Xdot1ConfigVidUsageDigestTable_Object = MibTable
lldpV2Xdot1ConfigVidUsageDigestTable = _LldpV2Xdot1ConfigVidUsageDigestTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 1, 5)
)
if mibBuilder.loadTexts:
    lldpV2Xdot1ConfigVidUsageDigestTable.setStatus("current")
_LldpV2Xdot1ConfigVidUsageDigestEntry_Object = MibTableRow
lldpV2Xdot1ConfigVidUsageDigestEntry = _LldpV2Xdot1ConfigVidUsageDigestEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    lldpV2Xdot1ConfigVidUsageDigestEntry.setStatus("current")


class _LldpV2Xdot1ConfigVidUsageDigestTxEnable_Type(TruthValue):
    """Custom type lldpV2Xdot1ConfigVidUsageDigestTxEnable based on TruthValue"""


_LldpV2Xdot1ConfigVidUsageDigestTxEnable_Object = MibTableColumn
lldpV2Xdot1ConfigVidUsageDigestTxEnable = _LldpV2Xdot1ConfigVidUsageDigestTxEnable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 1, 5, 1, 1),
    _LldpV2Xdot1ConfigVidUsageDigestTxEnable_Type()
)
lldpV2Xdot1ConfigVidUsageDigestTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpV2Xdot1ConfigVidUsageDigestTxEnable.setStatus("current")
_LldpV2Xdot1ConfigManVidTable_Object = MibTable
lldpV2Xdot1ConfigManVidTable = _LldpV2Xdot1ConfigManVidTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 1, 6)
)
if mibBuilder.loadTexts:
    lldpV2Xdot1ConfigManVidTable.setStatus("current")
_LldpV2Xdot1ConfigManVidEntry_Object = MibTableRow
lldpV2Xdot1ConfigManVidEntry = _LldpV2Xdot1ConfigManVidEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    lldpV2Xdot1ConfigManVidEntry.setStatus("current")


class _LldpV2Xdot1ConfigManVidTxEnable_Type(TruthValue):
    """Custom type lldpV2Xdot1ConfigManVidTxEnable based on TruthValue"""


_LldpV2Xdot1ConfigManVidTxEnable_Object = MibTableColumn
lldpV2Xdot1ConfigManVidTxEnable = _LldpV2Xdot1ConfigManVidTxEnable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 1, 6, 1, 1),
    _LldpV2Xdot1ConfigManVidTxEnable_Type()
)
lldpV2Xdot1ConfigManVidTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpV2Xdot1ConfigManVidTxEnable.setStatus("current")
_LldpV2Xdot1LocalData_ObjectIdentity = ObjectIdentity
lldpV2Xdot1LocalData = _LldpV2Xdot1LocalData_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 2)
)
_LldpV2Xdot1LocTable_Object = MibTable
lldpV2Xdot1LocTable = _LldpV2Xdot1LocTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 2, 1)
)
if mibBuilder.loadTexts:
    lldpV2Xdot1LocTable.setStatus("current")
_LldpV2Xdot1LocEntry_Object = MibTableRow
lldpV2Xdot1LocEntry = _LldpV2Xdot1LocEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 2, 1, 1)
)
lldpV2Xdot1LocEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
)
if mibBuilder.loadTexts:
    lldpV2Xdot1LocEntry.setStatus("current")


class _LldpV2Xdot1LocPortVlanId_Type(Unsigned32):
    """Custom type lldpV2Xdot1LocPortVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )


_LldpV2Xdot1LocPortVlanId_Type.__name__ = "Unsigned32"
_LldpV2Xdot1LocPortVlanId_Object = MibTableColumn
lldpV2Xdot1LocPortVlanId = _LldpV2Xdot1LocPortVlanId_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 2, 1, 1, 1),
    _LldpV2Xdot1LocPortVlanId_Type()
)
lldpV2Xdot1LocPortVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot1LocPortVlanId.setStatus("current")
_LldpV2Xdot1LocProtoVlanTable_Object = MibTable
lldpV2Xdot1LocProtoVlanTable = _LldpV2Xdot1LocProtoVlanTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 2, 2)
)
if mibBuilder.loadTexts:
    lldpV2Xdot1LocProtoVlanTable.setStatus("current")
_LldpV2Xdot1LocProtoVlanEntry_Object = MibTableRow
lldpV2Xdot1LocProtoVlanEntry = _LldpV2Xdot1LocProtoVlanEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 2, 2, 1)
)
lldpV2Xdot1LocProtoVlanEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
    (0, "LLDP-EXT-DOT1-V2-MIB", "lldpV2Xdot1LocProtoVlanId"),
)
if mibBuilder.loadTexts:
    lldpV2Xdot1LocProtoVlanEntry.setStatus("current")


class _LldpV2Xdot1LocProtoVlanId_Type(Unsigned32):
    """Custom type lldpV2Xdot1LocProtoVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )


_LldpV2Xdot1LocProtoVlanId_Type.__name__ = "Unsigned32"
_LldpV2Xdot1LocProtoVlanId_Object = MibTableColumn
lldpV2Xdot1LocProtoVlanId = _LldpV2Xdot1LocProtoVlanId_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 2, 2, 1, 1),
    _LldpV2Xdot1LocProtoVlanId_Type()
)
lldpV2Xdot1LocProtoVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpV2Xdot1LocProtoVlanId.setStatus("current")
_LldpV2Xdot1LocProtoVlanSupported_Type = TruthValue
_LldpV2Xdot1LocProtoVlanSupported_Object = MibTableColumn
lldpV2Xdot1LocProtoVlanSupported = _LldpV2Xdot1LocProtoVlanSupported_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 2, 2, 1, 2),
    _LldpV2Xdot1LocProtoVlanSupported_Type()
)
lldpV2Xdot1LocProtoVlanSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot1LocProtoVlanSupported.setStatus("current")
_LldpV2Xdot1LocProtoVlanEnabled_Type = TruthValue
_LldpV2Xdot1LocProtoVlanEnabled_Object = MibTableColumn
lldpV2Xdot1LocProtoVlanEnabled = _LldpV2Xdot1LocProtoVlanEnabled_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 2, 2, 1, 3),
    _LldpV2Xdot1LocProtoVlanEnabled_Type()
)
lldpV2Xdot1LocProtoVlanEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot1LocProtoVlanEnabled.setStatus("current")
_LldpV2Xdot1LocVlanNameTable_Object = MibTable
lldpV2Xdot1LocVlanNameTable = _LldpV2Xdot1LocVlanNameTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 2, 3)
)
if mibBuilder.loadTexts:
    lldpV2Xdot1LocVlanNameTable.setStatus("current")
_LldpV2Xdot1LocVlanNameEntry_Object = MibTableRow
lldpV2Xdot1LocVlanNameEntry = _LldpV2Xdot1LocVlanNameEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 2, 3, 1)
)
lldpV2Xdot1LocVlanNameEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
    (0, "LLDP-EXT-DOT1-V2-MIB", "lldpV2Xdot1LocVlanId"),
)
if mibBuilder.loadTexts:
    lldpV2Xdot1LocVlanNameEntry.setStatus("current")
_LldpV2Xdot1LocVlanId_Type = VlanId
_LldpV2Xdot1LocVlanId_Object = MibTableColumn
lldpV2Xdot1LocVlanId = _LldpV2Xdot1LocVlanId_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 2, 3, 1, 1),
    _LldpV2Xdot1LocVlanId_Type()
)
lldpV2Xdot1LocVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpV2Xdot1LocVlanId.setStatus("current")


class _LldpV2Xdot1LocVlanName_Type(SnmpAdminString):
    """Custom type lldpV2Xdot1LocVlanName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_LldpV2Xdot1LocVlanName_Type.__name__ = "SnmpAdminString"
_LldpV2Xdot1LocVlanName_Object = MibTableColumn
lldpV2Xdot1LocVlanName = _LldpV2Xdot1LocVlanName_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 2, 3, 1, 2),
    _LldpV2Xdot1LocVlanName_Type()
)
lldpV2Xdot1LocVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot1LocVlanName.setStatus("current")
_LldpV2Xdot1LocProtocolTable_Object = MibTable
lldpV2Xdot1LocProtocolTable = _LldpV2Xdot1LocProtocolTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 2, 4)
)
if mibBuilder.loadTexts:
    lldpV2Xdot1LocProtocolTable.setStatus("current")
_LldpV2Xdot1LocProtocolEntry_Object = MibTableRow
lldpV2Xdot1LocProtocolEntry = _LldpV2Xdot1LocProtocolEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 2, 4, 1)
)
lldpV2Xdot1LocProtocolEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
    (0, "LLDP-EXT-DOT1-V2-MIB", "lldpV2Xdot1LocProtocolIndex"),
)
if mibBuilder.loadTexts:
    lldpV2Xdot1LocProtocolEntry.setStatus("current")


class _LldpV2Xdot1LocProtocolIndex_Type(Unsigned32):
    """Custom type lldpV2Xdot1LocProtocolIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LldpV2Xdot1LocProtocolIndex_Type.__name__ = "Unsigned32"
_LldpV2Xdot1LocProtocolIndex_Object = MibTableColumn
lldpV2Xdot1LocProtocolIndex = _LldpV2Xdot1LocProtocolIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 2, 4, 1, 1),
    _LldpV2Xdot1LocProtocolIndex_Type()
)
lldpV2Xdot1LocProtocolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpV2Xdot1LocProtocolIndex.setStatus("current")


class _LldpV2Xdot1LocProtocolId_Type(OctetString):
    """Custom type lldpV2Xdot1LocProtocolId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_LldpV2Xdot1LocProtocolId_Type.__name__ = "OctetString"
_LldpV2Xdot1LocProtocolId_Object = MibTableColumn
lldpV2Xdot1LocProtocolId = _LldpV2Xdot1LocProtocolId_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 2, 4, 1, 2),
    _LldpV2Xdot1LocProtocolId_Type()
)
lldpV2Xdot1LocProtocolId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot1LocProtocolId.setStatus("current")
_LldpV2Xdot1LocVidUsageDigestTable_Object = MibTable
lldpV2Xdot1LocVidUsageDigestTable = _LldpV2Xdot1LocVidUsageDigestTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 2, 5)
)
if mibBuilder.loadTexts:
    lldpV2Xdot1LocVidUsageDigestTable.setStatus("current")
_LldpV2Xdot1LocVidUsageDigestEntry_Object = MibTableRow
lldpV2Xdot1LocVidUsageDigestEntry = _LldpV2Xdot1LocVidUsageDigestEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 2, 5, 1)
)
lldpV2Xdot1LocVidUsageDigestEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
)
if mibBuilder.loadTexts:
    lldpV2Xdot1LocVidUsageDigestEntry.setStatus("current")
_LldpV2Xdot1LocVidUsageDigest_Type = Unsigned32
_LldpV2Xdot1LocVidUsageDigest_Object = MibTableColumn
lldpV2Xdot1LocVidUsageDigest = _LldpV2Xdot1LocVidUsageDigest_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 2, 5, 1, 1),
    _LldpV2Xdot1LocVidUsageDigest_Type()
)
lldpV2Xdot1LocVidUsageDigest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot1LocVidUsageDigest.setStatus("current")
_LldpV2Xdot1LocManVidTable_Object = MibTable
lldpV2Xdot1LocManVidTable = _LldpV2Xdot1LocManVidTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 2, 6)
)
if mibBuilder.loadTexts:
    lldpV2Xdot1LocManVidTable.setStatus("current")
_LldpV2Xdot1LocManVidEntry_Object = MibTableRow
lldpV2Xdot1LocManVidEntry = _LldpV2Xdot1LocManVidEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 2, 6, 1)
)
lldpV2Xdot1LocManVidEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
)
if mibBuilder.loadTexts:
    lldpV2Xdot1LocManVidEntry.setStatus("current")


class _LldpV2Xdot1LocManVid_Type(Unsigned32):
    """Custom type lldpV2Xdot1LocManVid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )


_LldpV2Xdot1LocManVid_Type.__name__ = "Unsigned32"
_LldpV2Xdot1LocManVid_Object = MibTableColumn
lldpV2Xdot1LocManVid = _LldpV2Xdot1LocManVid_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 2, 6, 1, 1),
    _LldpV2Xdot1LocManVid_Type()
)
lldpV2Xdot1LocManVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot1LocManVid.setStatus("current")
_LldpV2Xdot1LocLinkAggTable_Object = MibTable
lldpV2Xdot1LocLinkAggTable = _LldpV2Xdot1LocLinkAggTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 2, 7)
)
if mibBuilder.loadTexts:
    lldpV2Xdot1LocLinkAggTable.setStatus("current")
_LldpV2Xdot1LocLinkAggEntry_Object = MibTableRow
lldpV2Xdot1LocLinkAggEntry = _LldpV2Xdot1LocLinkAggEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 2, 7, 1)
)
lldpV2Xdot1LocLinkAggEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
)
if mibBuilder.loadTexts:
    lldpV2Xdot1LocLinkAggEntry.setStatus("current")
_LldpV2Xdot1LocLinkAggStatus_Type = LldpV2XLinkAggStatusMap
_LldpV2Xdot1LocLinkAggStatus_Object = MibTableColumn
lldpV2Xdot1LocLinkAggStatus = _LldpV2Xdot1LocLinkAggStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 2, 7, 1, 1),
    _LldpV2Xdot1LocLinkAggStatus_Type()
)
lldpV2Xdot1LocLinkAggStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot1LocLinkAggStatus.setStatus("current")


class _LldpV2Xdot1LocLinkAggPortId_Type(Unsigned32):
    """Custom type lldpV2Xdot1LocLinkAggPortId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_LldpV2Xdot1LocLinkAggPortId_Type.__name__ = "Unsigned32"
_LldpV2Xdot1LocLinkAggPortId_Object = MibTableColumn
lldpV2Xdot1LocLinkAggPortId = _LldpV2Xdot1LocLinkAggPortId_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 2, 7, 1, 2),
    _LldpV2Xdot1LocLinkAggPortId_Type()
)
lldpV2Xdot1LocLinkAggPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot1LocLinkAggPortId.setStatus("current")
_LldpV2Xdot1RemoteData_ObjectIdentity = ObjectIdentity
lldpV2Xdot1RemoteData = _LldpV2Xdot1RemoteData_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 3)
)
_LldpV2Xdot1RemTable_Object = MibTable
lldpV2Xdot1RemTable = _LldpV2Xdot1RemTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 3, 1)
)
if mibBuilder.loadTexts:
    lldpV2Xdot1RemTable.setStatus("current")
_LldpV2Xdot1RemEntry_Object = MibTableRow
lldpV2Xdot1RemEntry = _LldpV2Xdot1RemEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 3, 1, 1)
)
lldpV2Xdot1RemEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2RemTimeMark"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"),
    (0, "LLDP-V2-MIB", "lldpV2RemIndex"),
)
if mibBuilder.loadTexts:
    lldpV2Xdot1RemEntry.setStatus("current")


class _LldpV2Xdot1RemPortVlanId_Type(Unsigned32):
    """Custom type lldpV2Xdot1RemPortVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )


_LldpV2Xdot1RemPortVlanId_Type.__name__ = "Unsigned32"
_LldpV2Xdot1RemPortVlanId_Object = MibTableColumn
lldpV2Xdot1RemPortVlanId = _LldpV2Xdot1RemPortVlanId_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 3, 1, 1, 1),
    _LldpV2Xdot1RemPortVlanId_Type()
)
lldpV2Xdot1RemPortVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot1RemPortVlanId.setStatus("current")
_LldpV2Xdot1RemProtoVlanTable_Object = MibTable
lldpV2Xdot1RemProtoVlanTable = _LldpV2Xdot1RemProtoVlanTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 3, 2)
)
if mibBuilder.loadTexts:
    lldpV2Xdot1RemProtoVlanTable.setStatus("current")
_LldpV2Xdot1RemProtoVlanEntry_Object = MibTableRow
lldpV2Xdot1RemProtoVlanEntry = _LldpV2Xdot1RemProtoVlanEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 3, 2, 1)
)
lldpV2Xdot1RemProtoVlanEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2RemTimeMark"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"),
    (0, "LLDP-V2-MIB", "lldpV2RemIndex"),
    (0, "LLDP-EXT-DOT1-V2-MIB", "lldpV2Xdot1RemProtoVlanId"),
)
if mibBuilder.loadTexts:
    lldpV2Xdot1RemProtoVlanEntry.setStatus("current")


class _LldpV2Xdot1RemProtoVlanId_Type(Unsigned32):
    """Custom type lldpV2Xdot1RemProtoVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )


_LldpV2Xdot1RemProtoVlanId_Type.__name__ = "Unsigned32"
_LldpV2Xdot1RemProtoVlanId_Object = MibTableColumn
lldpV2Xdot1RemProtoVlanId = _LldpV2Xdot1RemProtoVlanId_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 3, 2, 1, 1),
    _LldpV2Xdot1RemProtoVlanId_Type()
)
lldpV2Xdot1RemProtoVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpV2Xdot1RemProtoVlanId.setStatus("current")
_LldpV2Xdot1RemProtoVlanSupported_Type = TruthValue
_LldpV2Xdot1RemProtoVlanSupported_Object = MibTableColumn
lldpV2Xdot1RemProtoVlanSupported = _LldpV2Xdot1RemProtoVlanSupported_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 3, 2, 1, 2),
    _LldpV2Xdot1RemProtoVlanSupported_Type()
)
lldpV2Xdot1RemProtoVlanSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot1RemProtoVlanSupported.setStatus("current")
_LldpV2Xdot1RemProtoVlanEnabled_Type = TruthValue
_LldpV2Xdot1RemProtoVlanEnabled_Object = MibTableColumn
lldpV2Xdot1RemProtoVlanEnabled = _LldpV2Xdot1RemProtoVlanEnabled_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 3, 2, 1, 3),
    _LldpV2Xdot1RemProtoVlanEnabled_Type()
)
lldpV2Xdot1RemProtoVlanEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot1RemProtoVlanEnabled.setStatus("current")
_LldpV2Xdot1RemVlanNameTable_Object = MibTable
lldpV2Xdot1RemVlanNameTable = _LldpV2Xdot1RemVlanNameTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 3, 3)
)
if mibBuilder.loadTexts:
    lldpV2Xdot1RemVlanNameTable.setStatus("current")
_LldpV2Xdot1RemVlanNameEntry_Object = MibTableRow
lldpV2Xdot1RemVlanNameEntry = _LldpV2Xdot1RemVlanNameEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 3, 3, 1)
)
lldpV2Xdot1RemVlanNameEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2RemTimeMark"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"),
    (0, "LLDP-V2-MIB", "lldpV2RemIndex"),
    (0, "LLDP-EXT-DOT1-V2-MIB", "lldpV2Xdot1RemVlanId"),
)
if mibBuilder.loadTexts:
    lldpV2Xdot1RemVlanNameEntry.setStatus("current")
_LldpV2Xdot1RemVlanId_Type = VlanId
_LldpV2Xdot1RemVlanId_Object = MibTableColumn
lldpV2Xdot1RemVlanId = _LldpV2Xdot1RemVlanId_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 3, 3, 1, 1),
    _LldpV2Xdot1RemVlanId_Type()
)
lldpV2Xdot1RemVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpV2Xdot1RemVlanId.setStatus("current")


class _LldpV2Xdot1RemVlanName_Type(SnmpAdminString):
    """Custom type lldpV2Xdot1RemVlanName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_LldpV2Xdot1RemVlanName_Type.__name__ = "SnmpAdminString"
_LldpV2Xdot1RemVlanName_Object = MibTableColumn
lldpV2Xdot1RemVlanName = _LldpV2Xdot1RemVlanName_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 3, 3, 1, 2),
    _LldpV2Xdot1RemVlanName_Type()
)
lldpV2Xdot1RemVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot1RemVlanName.setStatus("current")
_LldpV2Xdot1RemProtocolTable_Object = MibTable
lldpV2Xdot1RemProtocolTable = _LldpV2Xdot1RemProtocolTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 3, 4)
)
if mibBuilder.loadTexts:
    lldpV2Xdot1RemProtocolTable.setStatus("current")
_LldpV2Xdot1RemProtocolEntry_Object = MibTableRow
lldpV2Xdot1RemProtocolEntry = _LldpV2Xdot1RemProtocolEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 3, 4, 1)
)
lldpV2Xdot1RemProtocolEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2RemTimeMark"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"),
    (0, "LLDP-V2-MIB", "lldpV2RemIndex"),
    (0, "LLDP-EXT-DOT1-V2-MIB", "lldpV2Xdot1RemProtocolIndex"),
)
if mibBuilder.loadTexts:
    lldpV2Xdot1RemProtocolEntry.setStatus("current")


class _LldpV2Xdot1RemProtocolIndex_Type(Unsigned32):
    """Custom type lldpV2Xdot1RemProtocolIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LldpV2Xdot1RemProtocolIndex_Type.__name__ = "Unsigned32"
_LldpV2Xdot1RemProtocolIndex_Object = MibTableColumn
lldpV2Xdot1RemProtocolIndex = _LldpV2Xdot1RemProtocolIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 3, 4, 1, 1),
    _LldpV2Xdot1RemProtocolIndex_Type()
)
lldpV2Xdot1RemProtocolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpV2Xdot1RemProtocolIndex.setStatus("current")


class _LldpV2Xdot1RemProtocolId_Type(OctetString):
    """Custom type lldpV2Xdot1RemProtocolId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_LldpV2Xdot1RemProtocolId_Type.__name__ = "OctetString"
_LldpV2Xdot1RemProtocolId_Object = MibTableColumn
lldpV2Xdot1RemProtocolId = _LldpV2Xdot1RemProtocolId_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 3, 4, 1, 2),
    _LldpV2Xdot1RemProtocolId_Type()
)
lldpV2Xdot1RemProtocolId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot1RemProtocolId.setStatus("current")
_LldpV2Xdot1RemVidUsageDigestTable_Object = MibTable
lldpV2Xdot1RemVidUsageDigestTable = _LldpV2Xdot1RemVidUsageDigestTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 3, 5)
)
if mibBuilder.loadTexts:
    lldpV2Xdot1RemVidUsageDigestTable.setStatus("deprecated")
_LldpV2Xdot1RemVidUsageDigestEntry_Object = MibTableRow
lldpV2Xdot1RemVidUsageDigestEntry = _LldpV2Xdot1RemVidUsageDigestEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 3, 5, 1)
)
lldpV2Xdot1RemVidUsageDigestEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2RemTimeMark"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"),
)
if mibBuilder.loadTexts:
    lldpV2Xdot1RemVidUsageDigestEntry.setStatus("deprecated")
_LldpV2Xdot1RemVidUsageDigest_Type = Unsigned32
_LldpV2Xdot1RemVidUsageDigest_Object = MibTableColumn
lldpV2Xdot1RemVidUsageDigest = _LldpV2Xdot1RemVidUsageDigest_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 3, 5, 1, 1),
    _LldpV2Xdot1RemVidUsageDigest_Type()
)
lldpV2Xdot1RemVidUsageDigest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot1RemVidUsageDigest.setStatus("deprecated")
_LldpV2Xdot1RemManVidTable_Object = MibTable
lldpV2Xdot1RemManVidTable = _LldpV2Xdot1RemManVidTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 3, 6)
)
if mibBuilder.loadTexts:
    lldpV2Xdot1RemManVidTable.setStatus("deprecated")
_LldpV2Xdot1RemManVidEntry_Object = MibTableRow
lldpV2Xdot1RemManVidEntry = _LldpV2Xdot1RemManVidEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 3, 6, 1)
)
lldpV2Xdot1RemManVidEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2RemTimeMark"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"),
)
if mibBuilder.loadTexts:
    lldpV2Xdot1RemManVidEntry.setStatus("deprecated")


class _LldpV2Xdot1RemManVid_Type(Unsigned32):
    """Custom type lldpV2Xdot1RemManVid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )


_LldpV2Xdot1RemManVid_Type.__name__ = "Unsigned32"
_LldpV2Xdot1RemManVid_Object = MibTableColumn
lldpV2Xdot1RemManVid = _LldpV2Xdot1RemManVid_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 3, 6, 1, 1),
    _LldpV2Xdot1RemManVid_Type()
)
lldpV2Xdot1RemManVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot1RemManVid.setStatus("deprecated")
_LldpV2Xdot1RemLinkAggTable_Object = MibTable
lldpV2Xdot1RemLinkAggTable = _LldpV2Xdot1RemLinkAggTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 3, 7)
)
if mibBuilder.loadTexts:
    lldpV2Xdot1RemLinkAggTable.setStatus("current")
_LldpV2Xdot1RemLinkAggEntry_Object = MibTableRow
lldpV2Xdot1RemLinkAggEntry = _LldpV2Xdot1RemLinkAggEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 3, 7, 1)
)
lldpV2Xdot1RemLinkAggEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2RemTimeMark"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"),
    (0, "LLDP-V2-MIB", "lldpV2RemIndex"),
)
if mibBuilder.loadTexts:
    lldpV2Xdot1RemLinkAggEntry.setStatus("current")
_LldpV2Xdot1RemLinkAggStatus_Type = LldpV2XLinkAggStatusMap
_LldpV2Xdot1RemLinkAggStatus_Object = MibTableColumn
lldpV2Xdot1RemLinkAggStatus = _LldpV2Xdot1RemLinkAggStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 3, 7, 1, 1),
    _LldpV2Xdot1RemLinkAggStatus_Type()
)
lldpV2Xdot1RemLinkAggStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot1RemLinkAggStatus.setStatus("current")


class _LldpV2Xdot1RemLinkAggPortId_Type(Unsigned32):
    """Custom type lldpV2Xdot1RemLinkAggPortId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_LldpV2Xdot1RemLinkAggPortId_Type.__name__ = "Unsigned32"
_LldpV2Xdot1RemLinkAggPortId_Object = MibTableColumn
lldpV2Xdot1RemLinkAggPortId = _LldpV2Xdot1RemLinkAggPortId_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 3, 7, 1, 2),
    _LldpV2Xdot1RemLinkAggPortId_Type()
)
lldpV2Xdot1RemLinkAggPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot1RemLinkAggPortId.setStatus("current")
_LldpV2Xdot1RemVidUsageDigestV2Table_Object = MibTable
lldpV2Xdot1RemVidUsageDigestV2Table = _LldpV2Xdot1RemVidUsageDigestV2Table_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 3, 8)
)
if mibBuilder.loadTexts:
    lldpV2Xdot1RemVidUsageDigestV2Table.setStatus("current")
_LldpV2Xdot1RemVidUsageDigestV2Entry_Object = MibTableRow
lldpV2Xdot1RemVidUsageDigestV2Entry = _LldpV2Xdot1RemVidUsageDigestV2Entry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 3, 8, 1)
)
lldpV2Xdot1RemVidUsageDigestV2Entry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2RemTimeMark"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"),
    (0, "LLDP-V2-MIB", "lldpV2RemIndex"),
)
if mibBuilder.loadTexts:
    lldpV2Xdot1RemVidUsageDigestV2Entry.setStatus("current")
_LldpV2Xdot1RemVidUsageDigestV2_Type = Unsigned32
_LldpV2Xdot1RemVidUsageDigestV2_Object = MibTableColumn
lldpV2Xdot1RemVidUsageDigestV2 = _LldpV2Xdot1RemVidUsageDigestV2_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 3, 8, 1, 1),
    _LldpV2Xdot1RemVidUsageDigestV2_Type()
)
lldpV2Xdot1RemVidUsageDigestV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot1RemVidUsageDigestV2.setStatus("current")
_LldpV2Xdot1RemManVidV2Table_Object = MibTable
lldpV2Xdot1RemManVidV2Table = _LldpV2Xdot1RemManVidV2Table_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 3, 9)
)
if mibBuilder.loadTexts:
    lldpV2Xdot1RemManVidV2Table.setStatus("current")
_LldpV2Xdot1RemManVidV2Entry_Object = MibTableRow
lldpV2Xdot1RemManVidV2Entry = _LldpV2Xdot1RemManVidV2Entry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 3, 9, 1)
)
lldpV2Xdot1RemManVidV2Entry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2RemTimeMark"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"),
    (0, "LLDP-V2-MIB", "lldpV2RemIndex"),
)
if mibBuilder.loadTexts:
    lldpV2Xdot1RemManVidV2Entry.setStatus("current")


class _LldpV2Xdot1RemManVidV2_Type(Unsigned32):
    """Custom type lldpV2Xdot1RemManVidV2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )


_LldpV2Xdot1RemManVidV2_Type.__name__ = "Unsigned32"
_LldpV2Xdot1RemManVidV2_Object = MibTableColumn
lldpV2Xdot1RemManVidV2 = _LldpV2Xdot1RemManVidV2_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 1, 3, 9, 1, 1),
    _LldpV2Xdot1RemManVidV2_Type()
)
lldpV2Xdot1RemManVidV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot1RemManVidV2.setStatus("current")
_LldpV2Xdot1Conformance_ObjectIdentity = ObjectIdentity
lldpV2Xdot1Conformance = _LldpV2Xdot1Conformance_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 2)
)
_LldpV2Xdot1Compliances_ObjectIdentity = ObjectIdentity
lldpV2Xdot1Compliances = _LldpV2Xdot1Compliances_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 2, 1)
)
_LldpV2Xdot1Groups_ObjectIdentity = ObjectIdentity
lldpV2Xdot1Groups = _LldpV2Xdot1Groups_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 2, 2)
)
_LldpXdot1CnMIB_ObjectIdentity = ObjectIdentity
lldpXdot1CnMIB = _LldpXdot1CnMIB_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 3)
)
_LldpXdot1CnObjects_ObjectIdentity = ObjectIdentity
lldpXdot1CnObjects = _LldpXdot1CnObjects_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 3, 1)
)
_LldpXdot1CnConfig_ObjectIdentity = ObjectIdentity
lldpXdot1CnConfig = _LldpXdot1CnConfig_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 3, 1, 1)
)
_LldpXdot1CnConfigCnTable_Object = MibTable
lldpXdot1CnConfigCnTable = _LldpXdot1CnConfigCnTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1CnConfigCnTable.setStatus("current")
_LldpXdot1CnConfigCnEntry_Object = MibTableRow
lldpXdot1CnConfigCnEntry = _LldpXdot1CnConfigCnEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 3, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1CnConfigCnEntry.setStatus("current")


class _LldpXdot1CnConfigCnTxEnable_Type(TruthValue):
    """Custom type lldpXdot1CnConfigCnTxEnable based on TruthValue"""


_LldpXdot1CnConfigCnTxEnable_Object = MibTableColumn
lldpXdot1CnConfigCnTxEnable = _LldpXdot1CnConfigCnTxEnable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 3, 1, 1, 1, 1, 1),
    _LldpXdot1CnConfigCnTxEnable_Type()
)
lldpXdot1CnConfigCnTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot1CnConfigCnTxEnable.setStatus("current")
_LldpXdot1CnLocalData_ObjectIdentity = ObjectIdentity
lldpXdot1CnLocalData = _LldpXdot1CnLocalData_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 3, 1, 2)
)
_LldpV2Xdot1LocCnTable_Object = MibTable
lldpV2Xdot1LocCnTable = _LldpV2Xdot1LocCnTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    lldpV2Xdot1LocCnTable.setStatus("current")
_LldpV2Xdot1LocCnEntry_Object = MibTableRow
lldpV2Xdot1LocCnEntry = _LldpV2Xdot1LocCnEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 3, 1, 2, 1, 1)
)
lldpV2Xdot1LocCnEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
)
if mibBuilder.loadTexts:
    lldpV2Xdot1LocCnEntry.setStatus("current")
_LldpV2Xdot1LocCNPVIndicators_Type = LldpV2CnBitVector
_LldpV2Xdot1LocCNPVIndicators_Object = MibTableColumn
lldpV2Xdot1LocCNPVIndicators = _LldpV2Xdot1LocCNPVIndicators_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 3, 1, 2, 1, 1, 1),
    _LldpV2Xdot1LocCNPVIndicators_Type()
)
lldpV2Xdot1LocCNPVIndicators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot1LocCNPVIndicators.setStatus("current")
_LldpV2Xdot1LocReadyIndicators_Type = LldpV2CnBitVector
_LldpV2Xdot1LocReadyIndicators_Object = MibTableColumn
lldpV2Xdot1LocReadyIndicators = _LldpV2Xdot1LocReadyIndicators_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 3, 1, 2, 1, 1, 2),
    _LldpV2Xdot1LocReadyIndicators_Type()
)
lldpV2Xdot1LocReadyIndicators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot1LocReadyIndicators.setStatus("current")
_LldpXdot1CnRemoteData_ObjectIdentity = ObjectIdentity
lldpXdot1CnRemoteData = _LldpXdot1CnRemoteData_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 3, 1, 3)
)
_LldpV2Xdot1RemCnTable_Object = MibTable
lldpV2Xdot1RemCnTable = _LldpV2Xdot1RemCnTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    lldpV2Xdot1RemCnTable.setStatus("current")
_LldpV2Xdot1RemCnEntry_Object = MibTableRow
lldpV2Xdot1RemCnEntry = _LldpV2Xdot1RemCnEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 3, 1, 3, 1, 1)
)
lldpV2Xdot1RemCnEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2RemTimeMark"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"),
    (0, "LLDP-V2-MIB", "lldpV2RemIndex"),
)
if mibBuilder.loadTexts:
    lldpV2Xdot1RemCnEntry.setStatus("current")
_LldpV2Xdot1RemCNPVIndicators_Type = LldpV2CnBitVector
_LldpV2Xdot1RemCNPVIndicators_Object = MibTableColumn
lldpV2Xdot1RemCNPVIndicators = _LldpV2Xdot1RemCNPVIndicators_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 3, 1, 3, 1, 1, 1),
    _LldpV2Xdot1RemCNPVIndicators_Type()
)
lldpV2Xdot1RemCNPVIndicators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot1RemCNPVIndicators.setStatus("current")
_LldpV2Xdot1RemReadyIndicators_Type = LldpV2CnBitVector
_LldpV2Xdot1RemReadyIndicators_Object = MibTableColumn
lldpV2Xdot1RemReadyIndicators = _LldpV2Xdot1RemReadyIndicators_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 3, 1, 3, 1, 1, 2),
    _LldpV2Xdot1RemReadyIndicators_Type()
)
lldpV2Xdot1RemReadyIndicators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot1RemReadyIndicators.setStatus("current")
_LldpXdot1CnConformance_ObjectIdentity = ObjectIdentity
lldpXdot1CnConformance = _LldpXdot1CnConformance_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 4)
)
_LldpXdot1CnCompliances_ObjectIdentity = ObjectIdentity
lldpXdot1CnCompliances = _LldpXdot1CnCompliances_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 4, 1)
)
_LldpXdot1CnGroups_ObjectIdentity = ObjectIdentity
lldpXdot1CnGroups = _LldpXdot1CnGroups_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 4, 2)
)
_LldpXdot1dcbxMIB_ObjectIdentity = ObjectIdentity
lldpXdot1dcbxMIB = _LldpXdot1dcbxMIB_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5)
)
_LldpXdot1dcbxObjects_ObjectIdentity = ObjectIdentity
lldpXdot1dcbxObjects = _LldpXdot1dcbxObjects_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1)
)
_LldpXdot1dcbxConfig_ObjectIdentity = ObjectIdentity
lldpXdot1dcbxConfig = _LldpXdot1dcbxConfig_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 1)
)
_LldpXdot1dcbxConfigETSConfigurationTable_Object = MibTable
lldpXdot1dcbxConfigETSConfigurationTable = _LldpXdot1dcbxConfigETSConfigurationTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 1, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxConfigETSConfigurationTable.setStatus("current")
_LldpXdot1dcbxConfigETSConfigurationEntry_Object = MibTableRow
lldpXdot1dcbxConfigETSConfigurationEntry = _LldpXdot1dcbxConfigETSConfigurationEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxConfigETSConfigurationEntry.setStatus("current")


class _LldpXdot1dcbxConfigETSConfigurationTxEnable_Type(TruthValue):
    """Custom type lldpXdot1dcbxConfigETSConfigurationTxEnable based on TruthValue"""


_LldpXdot1dcbxConfigETSConfigurationTxEnable_Object = MibTableColumn
lldpXdot1dcbxConfigETSConfigurationTxEnable = _LldpXdot1dcbxConfigETSConfigurationTxEnable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 1, 1, 1, 1),
    _LldpXdot1dcbxConfigETSConfigurationTxEnable_Type()
)
lldpXdot1dcbxConfigETSConfigurationTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot1dcbxConfigETSConfigurationTxEnable.setStatus("current")
_LldpXdot1dcbxConfigETSRecommendationTable_Object = MibTable
lldpXdot1dcbxConfigETSRecommendationTable = _LldpXdot1dcbxConfigETSRecommendationTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 1, 2)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxConfigETSRecommendationTable.setStatus("current")
_LldpXdot1dcbxConfigETSRecommendationEntry_Object = MibTableRow
lldpXdot1dcbxConfigETSRecommendationEntry = _LldpXdot1dcbxConfigETSRecommendationEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxConfigETSRecommendationEntry.setStatus("current")


class _LldpXdot1dcbxConfigETSRecommendationTxEnable_Type(TruthValue):
    """Custom type lldpXdot1dcbxConfigETSRecommendationTxEnable based on TruthValue"""


_LldpXdot1dcbxConfigETSRecommendationTxEnable_Object = MibTableColumn
lldpXdot1dcbxConfigETSRecommendationTxEnable = _LldpXdot1dcbxConfigETSRecommendationTxEnable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 1, 2, 1, 1),
    _LldpXdot1dcbxConfigETSRecommendationTxEnable_Type()
)
lldpXdot1dcbxConfigETSRecommendationTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot1dcbxConfigETSRecommendationTxEnable.setStatus("current")
_LldpXdot1dcbxConfigPFCTable_Object = MibTable
lldpXdot1dcbxConfigPFCTable = _LldpXdot1dcbxConfigPFCTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 1, 3)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxConfigPFCTable.setStatus("current")
_LldpXdot1dcbxConfigPFCEntry_Object = MibTableRow
lldpXdot1dcbxConfigPFCEntry = _LldpXdot1dcbxConfigPFCEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxConfigPFCEntry.setStatus("current")


class _LldpXdot1dcbxConfigPFCTxEnable_Type(TruthValue):
    """Custom type lldpXdot1dcbxConfigPFCTxEnable based on TruthValue"""


_LldpXdot1dcbxConfigPFCTxEnable_Object = MibTableColumn
lldpXdot1dcbxConfigPFCTxEnable = _LldpXdot1dcbxConfigPFCTxEnable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 1, 3, 1, 1),
    _LldpXdot1dcbxConfigPFCTxEnable_Type()
)
lldpXdot1dcbxConfigPFCTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot1dcbxConfigPFCTxEnable.setStatus("current")
_LldpXdot1dcbxConfigApplicationPriorityTable_Object = MibTable
lldpXdot1dcbxConfigApplicationPriorityTable = _LldpXdot1dcbxConfigApplicationPriorityTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 1, 4)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxConfigApplicationPriorityTable.setStatus("current")
_LldpXdot1dcbxConfigApplicationPriorityEntry_Object = MibTableRow
lldpXdot1dcbxConfigApplicationPriorityEntry = _LldpXdot1dcbxConfigApplicationPriorityEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxConfigApplicationPriorityEntry.setStatus("current")


class _LldpXdot1dcbxConfigApplicationPriorityTxEnable_Type(TruthValue):
    """Custom type lldpXdot1dcbxConfigApplicationPriorityTxEnable based on TruthValue"""


_LldpXdot1dcbxConfigApplicationPriorityTxEnable_Object = MibTableColumn
lldpXdot1dcbxConfigApplicationPriorityTxEnable = _LldpXdot1dcbxConfigApplicationPriorityTxEnable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 1, 4, 1, 1),
    _LldpXdot1dcbxConfigApplicationPriorityTxEnable_Type()
)
lldpXdot1dcbxConfigApplicationPriorityTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot1dcbxConfigApplicationPriorityTxEnable.setStatus("current")
_LldpXdot1dcbxConfigApplicationVlanTable_Object = MibTable
lldpXdot1dcbxConfigApplicationVlanTable = _LldpXdot1dcbxConfigApplicationVlanTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 1, 5)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxConfigApplicationVlanTable.setStatus("current")
_LldpXdot1dcbxConfigApplicationVlanEntry_Object = MibTableRow
lldpXdot1dcbxConfigApplicationVlanEntry = _LldpXdot1dcbxConfigApplicationVlanEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxConfigApplicationVlanEntry.setStatus("current")


class _LldpXdot1dcbxConfigApplicationVlanTxEnable_Type(TruthValue):
    """Custom type lldpXdot1dcbxConfigApplicationVlanTxEnable based on TruthValue"""


_LldpXdot1dcbxConfigApplicationVlanTxEnable_Object = MibTableColumn
lldpXdot1dcbxConfigApplicationVlanTxEnable = _LldpXdot1dcbxConfigApplicationVlanTxEnable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 1, 5, 1, 1),
    _LldpXdot1dcbxConfigApplicationVlanTxEnable_Type()
)
lldpXdot1dcbxConfigApplicationVlanTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot1dcbxConfigApplicationVlanTxEnable.setStatus("current")
_LldpXdot1dcbxLocalData_ObjectIdentity = ObjectIdentity
lldpXdot1dcbxLocalData = _LldpXdot1dcbxLocalData_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2)
)
_LldpXdot1dcbxLocETSConfiguration_ObjectIdentity = ObjectIdentity
lldpXdot1dcbxLocETSConfiguration = _LldpXdot1dcbxLocETSConfiguration_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 1)
)
_LldpXdot1dcbxLocETSBasicConfigurationTable_Object = MibTable
lldpXdot1dcbxLocETSBasicConfigurationTable = _LldpXdot1dcbxLocETSBasicConfigurationTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocETSBasicConfigurationTable.setStatus("current")
_LldpXdot1dcbxLocETSBasicConfigurationEntry_Object = MibTableRow
lldpXdot1dcbxLocETSBasicConfigurationEntry = _LldpXdot1dcbxLocETSBasicConfigurationEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 1, 1, 1)
)
lldpXdot1dcbxLocETSBasicConfigurationEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocETSBasicConfigurationEntry.setStatus("current")
_LldpXdot1dcbxLocETSConCreditBasedShaperSupport_Type = TruthValue
_LldpXdot1dcbxLocETSConCreditBasedShaperSupport_Object = MibTableColumn
lldpXdot1dcbxLocETSConCreditBasedShaperSupport = _LldpXdot1dcbxLocETSConCreditBasedShaperSupport_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 1, 1, 1, 1),
    _LldpXdot1dcbxLocETSConCreditBasedShaperSupport_Type()
)
lldpXdot1dcbxLocETSConCreditBasedShaperSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocETSConCreditBasedShaperSupport.setStatus("current")
_LldpXdot1dcbxLocETSConTrafficClassesSupported_Type = LldpXdot1dcbxSupportedCapacity
_LldpXdot1dcbxLocETSConTrafficClassesSupported_Object = MibTableColumn
lldpXdot1dcbxLocETSConTrafficClassesSupported = _LldpXdot1dcbxLocETSConTrafficClassesSupported_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 1, 1, 1, 2),
    _LldpXdot1dcbxLocETSConTrafficClassesSupported_Type()
)
lldpXdot1dcbxLocETSConTrafficClassesSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocETSConTrafficClassesSupported.setStatus("current")
_LldpXdot1dcbxLocETSConWilling_Type = TruthValue
_LldpXdot1dcbxLocETSConWilling_Object = MibTableColumn
lldpXdot1dcbxLocETSConWilling = _LldpXdot1dcbxLocETSConWilling_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 1, 1, 1, 3),
    _LldpXdot1dcbxLocETSConWilling_Type()
)
lldpXdot1dcbxLocETSConWilling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocETSConWilling.setStatus("current")
_LldpXdot1dcbxLocETSConPriorityAssignmentTable_Object = MibTable
lldpXdot1dcbxLocETSConPriorityAssignmentTable = _LldpXdot1dcbxLocETSConPriorityAssignmentTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocETSConPriorityAssignmentTable.setStatus("current")
_LldpXdot1dcbxLocETSConPriorityAssignmentEntry_Object = MibTableRow
lldpXdot1dcbxLocETSConPriorityAssignmentEntry = _LldpXdot1dcbxLocETSConPriorityAssignmentEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 1, 2, 1)
)
lldpXdot1dcbxLocETSConPriorityAssignmentEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
    (0, "LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxLocETSConPriority"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocETSConPriorityAssignmentEntry.setStatus("current")
_LldpXdot1dcbxLocETSConPriority_Type = IEEE8021PriorityValue
_LldpXdot1dcbxLocETSConPriority_Object = MibTableColumn
lldpXdot1dcbxLocETSConPriority = _LldpXdot1dcbxLocETSConPriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 1, 2, 1, 1),
    _LldpXdot1dcbxLocETSConPriority_Type()
)
lldpXdot1dcbxLocETSConPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocETSConPriority.setStatus("current")
_LldpXdot1dcbxLocETSConPriTrafficClass_Type = LldpXdot1dcbxTrafficClassValue
_LldpXdot1dcbxLocETSConPriTrafficClass_Object = MibTableColumn
lldpXdot1dcbxLocETSConPriTrafficClass = _LldpXdot1dcbxLocETSConPriTrafficClass_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 1, 2, 1, 2),
    _LldpXdot1dcbxLocETSConPriTrafficClass_Type()
)
lldpXdot1dcbxLocETSConPriTrafficClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocETSConPriTrafficClass.setStatus("current")
_LldpXdot1dcbxLocETSConTrafficClassBandwidthTable_Object = MibTable
lldpXdot1dcbxLocETSConTrafficClassBandwidthTable = _LldpXdot1dcbxLocETSConTrafficClassBandwidthTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocETSConTrafficClassBandwidthTable.setStatus("current")
_LldpXdot1dcbxLocETSConTrafficClassBandwidthEntry_Object = MibTableRow
lldpXdot1dcbxLocETSConTrafficClassBandwidthEntry = _LldpXdot1dcbxLocETSConTrafficClassBandwidthEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 1, 3, 1)
)
lldpXdot1dcbxLocETSConTrafficClassBandwidthEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
    (0, "LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxLocETSConTrafficClass"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocETSConTrafficClassBandwidthEntry.setStatus("current")
_LldpXdot1dcbxLocETSConTrafficClass_Type = LldpXdot1dcbxTrafficClassValue
_LldpXdot1dcbxLocETSConTrafficClass_Object = MibTableColumn
lldpXdot1dcbxLocETSConTrafficClass = _LldpXdot1dcbxLocETSConTrafficClass_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 1, 3, 1, 1),
    _LldpXdot1dcbxLocETSConTrafficClass_Type()
)
lldpXdot1dcbxLocETSConTrafficClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocETSConTrafficClass.setStatus("current")
_LldpXdot1dcbxLocETSConTrafficClassBandwidth_Type = LldpXdot1dcbxTrafficClassBandwidthValue
_LldpXdot1dcbxLocETSConTrafficClassBandwidth_Object = MibTableColumn
lldpXdot1dcbxLocETSConTrafficClassBandwidth = _LldpXdot1dcbxLocETSConTrafficClassBandwidth_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 1, 3, 1, 2),
    _LldpXdot1dcbxLocETSConTrafficClassBandwidth_Type()
)
lldpXdot1dcbxLocETSConTrafficClassBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocETSConTrafficClassBandwidth.setStatus("current")
_LldpXdot1dcbxLocETSConTrafficSelectionAlgorithmTable_Object = MibTable
lldpXdot1dcbxLocETSConTrafficSelectionAlgorithmTable = _LldpXdot1dcbxLocETSConTrafficSelectionAlgorithmTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 1, 4)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocETSConTrafficSelectionAlgorithmTable.setStatus("current")
_LldpXdot1dcbxLocETSConTrafficSelectionAlgorithmEntry_Object = MibTableRow
lldpXdot1dcbxLocETSConTrafficSelectionAlgorithmEntry = _LldpXdot1dcbxLocETSConTrafficSelectionAlgorithmEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 1, 4, 1)
)
lldpXdot1dcbxLocETSConTrafficSelectionAlgorithmEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
    (0, "LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxLocETSConTSATrafficClass"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocETSConTrafficSelectionAlgorithmEntry.setStatus("current")
_LldpXdot1dcbxLocETSConTSATrafficClass_Type = LldpXdot1dcbxTrafficClassValue
_LldpXdot1dcbxLocETSConTSATrafficClass_Object = MibTableColumn
lldpXdot1dcbxLocETSConTSATrafficClass = _LldpXdot1dcbxLocETSConTSATrafficClass_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 1, 4, 1, 1),
    _LldpXdot1dcbxLocETSConTSATrafficClass_Type()
)
lldpXdot1dcbxLocETSConTSATrafficClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocETSConTSATrafficClass.setStatus("current")
_LldpXdot1dcbxLocETSConTrafficSelectionAlgorithm_Type = LldpXdot1dcbxTrafficSelectionAlgorithm
_LldpXdot1dcbxLocETSConTrafficSelectionAlgorithm_Object = MibTableColumn
lldpXdot1dcbxLocETSConTrafficSelectionAlgorithm = _LldpXdot1dcbxLocETSConTrafficSelectionAlgorithm_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 1, 4, 1, 2),
    _LldpXdot1dcbxLocETSConTrafficSelectionAlgorithm_Type()
)
lldpXdot1dcbxLocETSConTrafficSelectionAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocETSConTrafficSelectionAlgorithm.setStatus("current")
_LldpXdot1dcbxLocETSReco_ObjectIdentity = ObjectIdentity
lldpXdot1dcbxLocETSReco = _LldpXdot1dcbxLocETSReco_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 2)
)
_LldpXdot1dcbxLocETSRecoTrafficClassBandwidthTable_Object = MibTable
lldpXdot1dcbxLocETSRecoTrafficClassBandwidthTable = _LldpXdot1dcbxLocETSRecoTrafficClassBandwidthTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocETSRecoTrafficClassBandwidthTable.setStatus("current")
_LldpXdot1dcbxLocETSRecoTrafficClassBandwidthEntry_Object = MibTableRow
lldpXdot1dcbxLocETSRecoTrafficClassBandwidthEntry = _LldpXdot1dcbxLocETSRecoTrafficClassBandwidthEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 2, 1, 1)
)
lldpXdot1dcbxLocETSRecoTrafficClassBandwidthEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
    (0, "LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxLocETSRecoTrafficClass"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocETSRecoTrafficClassBandwidthEntry.setStatus("current")
_LldpXdot1dcbxLocETSRecoTrafficClass_Type = LldpXdot1dcbxTrafficClassValue
_LldpXdot1dcbxLocETSRecoTrafficClass_Object = MibTableColumn
lldpXdot1dcbxLocETSRecoTrafficClass = _LldpXdot1dcbxLocETSRecoTrafficClass_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 2, 1, 1, 1),
    _LldpXdot1dcbxLocETSRecoTrafficClass_Type()
)
lldpXdot1dcbxLocETSRecoTrafficClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocETSRecoTrafficClass.setStatus("current")
_LldpXdot1dcbxLocETSRecoTrafficClassBandwidth_Type = LldpXdot1dcbxTrafficClassBandwidthValue
_LldpXdot1dcbxLocETSRecoTrafficClassBandwidth_Object = MibTableColumn
lldpXdot1dcbxLocETSRecoTrafficClassBandwidth = _LldpXdot1dcbxLocETSRecoTrafficClassBandwidth_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 2, 1, 1, 2),
    _LldpXdot1dcbxLocETSRecoTrafficClassBandwidth_Type()
)
lldpXdot1dcbxLocETSRecoTrafficClassBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocETSRecoTrafficClassBandwidth.setStatus("current")
_LldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithmTable_Object = MibTable
lldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithmTable = _LldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithmTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithmTable.setStatus("current")
_LldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithmEntry_Object = MibTableRow
lldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithmEntry = _LldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithmEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 2, 2, 1)
)
lldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithmEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
    (0, "LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxLocETSRecoTSATrafficClass"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithmEntry.setStatus("current")
_LldpXdot1dcbxLocETSRecoTSATrafficClass_Type = LldpXdot1dcbxTrafficClassValue
_LldpXdot1dcbxLocETSRecoTSATrafficClass_Object = MibTableColumn
lldpXdot1dcbxLocETSRecoTSATrafficClass = _LldpXdot1dcbxLocETSRecoTSATrafficClass_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 2, 2, 1, 1),
    _LldpXdot1dcbxLocETSRecoTSATrafficClass_Type()
)
lldpXdot1dcbxLocETSRecoTSATrafficClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocETSRecoTSATrafficClass.setStatus("current")
_LldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithm_Type = LldpXdot1dcbxTrafficSelectionAlgorithm
_LldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithm_Object = MibTableColumn
lldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithm = _LldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithm_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 2, 2, 1, 2),
    _LldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithm_Type()
)
lldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithm.setStatus("current")
_LldpXdot1dcbxLocPFC_ObjectIdentity = ObjectIdentity
lldpXdot1dcbxLocPFC = _LldpXdot1dcbxLocPFC_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 3)
)
_LldpXdot1dcbxLocPFCBasicTable_Object = MibTable
lldpXdot1dcbxLocPFCBasicTable = _LldpXdot1dcbxLocPFCBasicTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocPFCBasicTable.setStatus("current")
_LldpXdot1dcbxLocPFCBasicEntry_Object = MibTableRow
lldpXdot1dcbxLocPFCBasicEntry = _LldpXdot1dcbxLocPFCBasicEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 3, 1, 1)
)
lldpXdot1dcbxLocPFCBasicEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocPFCBasicEntry.setStatus("current")
_LldpXdot1dcbxLocPFCWilling_Type = TruthValue
_LldpXdot1dcbxLocPFCWilling_Object = MibTableColumn
lldpXdot1dcbxLocPFCWilling = _LldpXdot1dcbxLocPFCWilling_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 3, 1, 1, 1),
    _LldpXdot1dcbxLocPFCWilling_Type()
)
lldpXdot1dcbxLocPFCWilling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocPFCWilling.setStatus("current")
_LldpXdot1dcbxLocPFCMBC_Type = TruthValue
_LldpXdot1dcbxLocPFCMBC_Object = MibTableColumn
lldpXdot1dcbxLocPFCMBC = _LldpXdot1dcbxLocPFCMBC_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 3, 1, 1, 2),
    _LldpXdot1dcbxLocPFCMBC_Type()
)
lldpXdot1dcbxLocPFCMBC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocPFCMBC.setStatus("current")
_LldpXdot1dcbxLocPFCCap_Type = LldpXdot1dcbxSupportedCapacity
_LldpXdot1dcbxLocPFCCap_Object = MibTableColumn
lldpXdot1dcbxLocPFCCap = _LldpXdot1dcbxLocPFCCap_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 3, 1, 1, 3),
    _LldpXdot1dcbxLocPFCCap_Type()
)
lldpXdot1dcbxLocPFCCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocPFCCap.setStatus("current")
_LldpXdot1dcbxLocPFCEnableTable_Object = MibTable
lldpXdot1dcbxLocPFCEnableTable = _LldpXdot1dcbxLocPFCEnableTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocPFCEnableTable.setStatus("current")
_LldpXdot1dcbxLocPFCEnableEntry_Object = MibTableRow
lldpXdot1dcbxLocPFCEnableEntry = _LldpXdot1dcbxLocPFCEnableEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 3, 2, 1)
)
lldpXdot1dcbxLocPFCEnableEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
    (0, "LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxLocPFCEnablePriority"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocPFCEnableEntry.setStatus("current")
_LldpXdot1dcbxLocPFCEnablePriority_Type = IEEE8021PriorityValue
_LldpXdot1dcbxLocPFCEnablePriority_Object = MibTableColumn
lldpXdot1dcbxLocPFCEnablePriority = _LldpXdot1dcbxLocPFCEnablePriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 3, 2, 1, 1),
    _LldpXdot1dcbxLocPFCEnablePriority_Type()
)
lldpXdot1dcbxLocPFCEnablePriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocPFCEnablePriority.setStatus("current")
_LldpXdot1dcbxLocPFCEnableEnabled_Type = TruthValue
_LldpXdot1dcbxLocPFCEnableEnabled_Object = MibTableColumn
lldpXdot1dcbxLocPFCEnableEnabled = _LldpXdot1dcbxLocPFCEnableEnabled_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 3, 2, 1, 2),
    _LldpXdot1dcbxLocPFCEnableEnabled_Type()
)
lldpXdot1dcbxLocPFCEnableEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocPFCEnableEnabled.setStatus("current")
_LldpXdot1dcbxLocApplicationPriorityAppTable_Object = MibTable
lldpXdot1dcbxLocApplicationPriorityAppTable = _LldpXdot1dcbxLocApplicationPriorityAppTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 4)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocApplicationPriorityAppTable.setStatus("current")
_LldpXdot1dcbxLocApplicationPriorityAppEntry_Object = MibTableRow
lldpXdot1dcbxLocApplicationPriorityAppEntry = _LldpXdot1dcbxLocApplicationPriorityAppEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 4, 1)
)
lldpXdot1dcbxLocApplicationPriorityAppEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
    (0, "LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxLocApplicationPriorityAESelector"),
    (0, "LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxLocApplicationPriorityAEProtocol"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocApplicationPriorityAppEntry.setStatus("current")
_LldpXdot1dcbxLocApplicationPriorityAESelector_Type = LldpXdot1dcbxAppSelector
_LldpXdot1dcbxLocApplicationPriorityAESelector_Object = MibTableColumn
lldpXdot1dcbxLocApplicationPriorityAESelector = _LldpXdot1dcbxLocApplicationPriorityAESelector_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 4, 1, 1),
    _LldpXdot1dcbxLocApplicationPriorityAESelector_Type()
)
lldpXdot1dcbxLocApplicationPriorityAESelector.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocApplicationPriorityAESelector.setStatus("current")
_LldpXdot1dcbxLocApplicationPriorityAEProtocol_Type = LldpXdot1dcbxAppProtocol
_LldpXdot1dcbxLocApplicationPriorityAEProtocol_Object = MibTableColumn
lldpXdot1dcbxLocApplicationPriorityAEProtocol = _LldpXdot1dcbxLocApplicationPriorityAEProtocol_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 4, 1, 2),
    _LldpXdot1dcbxLocApplicationPriorityAEProtocol_Type()
)
lldpXdot1dcbxLocApplicationPriorityAEProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocApplicationPriorityAEProtocol.setStatus("current")
_LldpXdot1dcbxLocApplicationPriorityAEPriority_Type = IEEE8021PriorityValue
_LldpXdot1dcbxLocApplicationPriorityAEPriority_Object = MibTableColumn
lldpXdot1dcbxLocApplicationPriorityAEPriority = _LldpXdot1dcbxLocApplicationPriorityAEPriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 4, 1, 3),
    _LldpXdot1dcbxLocApplicationPriorityAEPriority_Type()
)
lldpXdot1dcbxLocApplicationPriorityAEPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocApplicationPriorityAEPriority.setStatus("current")
_LldpXdot1dcbxLocApplicationVlanAppTable_Object = MibTable
lldpXdot1dcbxLocApplicationVlanAppTable = _LldpXdot1dcbxLocApplicationVlanAppTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 5)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocApplicationVlanAppTable.setStatus("current")
_LldpXdot1dcbxLocApplicationVlanAppEntry_Object = MibTableRow
lldpXdot1dcbxLocApplicationVlanAppEntry = _LldpXdot1dcbxLocApplicationVlanAppEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 5, 1)
)
lldpXdot1dcbxLocApplicationVlanAppEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
    (0, "LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxLocApplicationVlanAESelector"),
    (0, "LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxLocApplicationVlanAEProtocol"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocApplicationVlanAppEntry.setStatus("current")
_LldpXdot1dcbxLocApplicationVlanAESelector_Type = LldpXdot1dcbxAppSelector
_LldpXdot1dcbxLocApplicationVlanAESelector_Object = MibTableColumn
lldpXdot1dcbxLocApplicationVlanAESelector = _LldpXdot1dcbxLocApplicationVlanAESelector_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 5, 1, 1),
    _LldpXdot1dcbxLocApplicationVlanAESelector_Type()
)
lldpXdot1dcbxLocApplicationVlanAESelector.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocApplicationVlanAESelector.setStatus("current")
_LldpXdot1dcbxLocApplicationVlanAEProtocol_Type = LldpXdot1dcbxAppProtocol
_LldpXdot1dcbxLocApplicationVlanAEProtocol_Object = MibTableColumn
lldpXdot1dcbxLocApplicationVlanAEProtocol = _LldpXdot1dcbxLocApplicationVlanAEProtocol_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 5, 1, 2),
    _LldpXdot1dcbxLocApplicationVlanAEProtocol_Type()
)
lldpXdot1dcbxLocApplicationVlanAEProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocApplicationVlanAEProtocol.setStatus("current")
_LldpXdot1dcbxLocApplicationVlanAEVlanId_Type = VlanId
_LldpXdot1dcbxLocApplicationVlanAEVlanId_Object = MibTableColumn
lldpXdot1dcbxLocApplicationVlanAEVlanId = _LldpXdot1dcbxLocApplicationVlanAEVlanId_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 5, 1, 3),
    _LldpXdot1dcbxLocApplicationVlanAEVlanId_Type()
)
lldpXdot1dcbxLocApplicationVlanAEVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocApplicationVlanAEVlanId.setStatus("current")
_LldpXdot1dcbxRemoteData_ObjectIdentity = ObjectIdentity
lldpXdot1dcbxRemoteData = _LldpXdot1dcbxRemoteData_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3)
)
_LldpXdot1dcbxRemETSConfiguration_ObjectIdentity = ObjectIdentity
lldpXdot1dcbxRemETSConfiguration = _LldpXdot1dcbxRemETSConfiguration_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 1)
)
_LldpXdot1dcbxRemETSBasicConfigurationTable_Object = MibTable
lldpXdot1dcbxRemETSBasicConfigurationTable = _LldpXdot1dcbxRemETSBasicConfigurationTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemETSBasicConfigurationTable.setStatus("current")
_LldpXdot1dcbxRemETSBasicConfigurationEntry_Object = MibTableRow
lldpXdot1dcbxRemETSBasicConfigurationEntry = _LldpXdot1dcbxRemETSBasicConfigurationEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 1, 1, 1)
)
lldpXdot1dcbxRemETSBasicConfigurationEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2RemTimeMark"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"),
    (0, "LLDP-V2-MIB", "lldpV2RemIndex"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemETSBasicConfigurationEntry.setStatus("current")
_LldpXdot1dcbxRemETSConCreditBasedShaperSupport_Type = TruthValue
_LldpXdot1dcbxRemETSConCreditBasedShaperSupport_Object = MibTableColumn
lldpXdot1dcbxRemETSConCreditBasedShaperSupport = _LldpXdot1dcbxRemETSConCreditBasedShaperSupport_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 1, 1, 1, 1),
    _LldpXdot1dcbxRemETSConCreditBasedShaperSupport_Type()
)
lldpXdot1dcbxRemETSConCreditBasedShaperSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemETSConCreditBasedShaperSupport.setStatus("current")
_LldpXdot1dcbxRemETSConTrafficClassesSupported_Type = LldpXdot1dcbxSupportedCapacity
_LldpXdot1dcbxRemETSConTrafficClassesSupported_Object = MibTableColumn
lldpXdot1dcbxRemETSConTrafficClassesSupported = _LldpXdot1dcbxRemETSConTrafficClassesSupported_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 1, 1, 1, 2),
    _LldpXdot1dcbxRemETSConTrafficClassesSupported_Type()
)
lldpXdot1dcbxRemETSConTrafficClassesSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemETSConTrafficClassesSupported.setStatus("current")
_LldpXdot1dcbxRemETSConWilling_Type = TruthValue
_LldpXdot1dcbxRemETSConWilling_Object = MibTableColumn
lldpXdot1dcbxRemETSConWilling = _LldpXdot1dcbxRemETSConWilling_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 1, 1, 1, 3),
    _LldpXdot1dcbxRemETSConWilling_Type()
)
lldpXdot1dcbxRemETSConWilling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemETSConWilling.setStatus("current")
_LldpXdot1dcbxRemETSConPriorityAssignmentTable_Object = MibTable
lldpXdot1dcbxRemETSConPriorityAssignmentTable = _LldpXdot1dcbxRemETSConPriorityAssignmentTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemETSConPriorityAssignmentTable.setStatus("current")
_LldpXdot1dcbxRemETSConPriorityAssignmentEntry_Object = MibTableRow
lldpXdot1dcbxRemETSConPriorityAssignmentEntry = _LldpXdot1dcbxRemETSConPriorityAssignmentEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 1, 2, 1)
)
lldpXdot1dcbxRemETSConPriorityAssignmentEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2RemTimeMark"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"),
    (0, "LLDP-V2-MIB", "lldpV2RemIndex"),
    (0, "LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxRemETSConPriority"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemETSConPriorityAssignmentEntry.setStatus("current")
_LldpXdot1dcbxRemETSConPriority_Type = IEEE8021PriorityValue
_LldpXdot1dcbxRemETSConPriority_Object = MibTableColumn
lldpXdot1dcbxRemETSConPriority = _LldpXdot1dcbxRemETSConPriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 1, 2, 1, 1),
    _LldpXdot1dcbxRemETSConPriority_Type()
)
lldpXdot1dcbxRemETSConPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemETSConPriority.setStatus("current")
_LldpXdot1dcbxRemETSConPriTrafficClass_Type = LldpXdot1dcbxTrafficClassValue
_LldpXdot1dcbxRemETSConPriTrafficClass_Object = MibTableColumn
lldpXdot1dcbxRemETSConPriTrafficClass = _LldpXdot1dcbxRemETSConPriTrafficClass_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 1, 2, 1, 2),
    _LldpXdot1dcbxRemETSConPriTrafficClass_Type()
)
lldpXdot1dcbxRemETSConPriTrafficClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemETSConPriTrafficClass.setStatus("current")
_LldpXdot1dcbxRemETSConTrafficClassBandwidthTable_Object = MibTable
lldpXdot1dcbxRemETSConTrafficClassBandwidthTable = _LldpXdot1dcbxRemETSConTrafficClassBandwidthTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 1, 3)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemETSConTrafficClassBandwidthTable.setStatus("current")
_LldpXdot1dcbxRemETSConTrafficClassBandwidthEntry_Object = MibTableRow
lldpXdot1dcbxRemETSConTrafficClassBandwidthEntry = _LldpXdot1dcbxRemETSConTrafficClassBandwidthEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 1, 3, 1)
)
lldpXdot1dcbxRemETSConTrafficClassBandwidthEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2RemTimeMark"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"),
    (0, "LLDP-V2-MIB", "lldpV2RemIndex"),
    (0, "LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxRemETSConTrafficClass"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemETSConTrafficClassBandwidthEntry.setStatus("current")
_LldpXdot1dcbxRemETSConTrafficClass_Type = LldpXdot1dcbxTrafficClassValue
_LldpXdot1dcbxRemETSConTrafficClass_Object = MibTableColumn
lldpXdot1dcbxRemETSConTrafficClass = _LldpXdot1dcbxRemETSConTrafficClass_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 1, 3, 1, 1),
    _LldpXdot1dcbxRemETSConTrafficClass_Type()
)
lldpXdot1dcbxRemETSConTrafficClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemETSConTrafficClass.setStatus("current")
_LldpXdot1dcbxRemETSConTrafficClassBandwidth_Type = LldpXdot1dcbxTrafficClassBandwidthValue
_LldpXdot1dcbxRemETSConTrafficClassBandwidth_Object = MibTableColumn
lldpXdot1dcbxRemETSConTrafficClassBandwidth = _LldpXdot1dcbxRemETSConTrafficClassBandwidth_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 1, 3, 1, 2),
    _LldpXdot1dcbxRemETSConTrafficClassBandwidth_Type()
)
lldpXdot1dcbxRemETSConTrafficClassBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemETSConTrafficClassBandwidth.setStatus("current")
_LldpXdot1dcbxRemETSConTrafficSelectionAlgorithmTable_Object = MibTable
lldpXdot1dcbxRemETSConTrafficSelectionAlgorithmTable = _LldpXdot1dcbxRemETSConTrafficSelectionAlgorithmTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 1, 4)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemETSConTrafficSelectionAlgorithmTable.setStatus("current")
_LldpXdot1dcbxRemETSConTrafficSelectionAlgorithmEntry_Object = MibTableRow
lldpXdot1dcbxRemETSConTrafficSelectionAlgorithmEntry = _LldpXdot1dcbxRemETSConTrafficSelectionAlgorithmEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 1, 4, 1)
)
lldpXdot1dcbxRemETSConTrafficSelectionAlgorithmEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2RemTimeMark"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"),
    (0, "LLDP-V2-MIB", "lldpV2RemIndex"),
    (0, "LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxRemETSConTSATrafficClass"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemETSConTrafficSelectionAlgorithmEntry.setStatus("current")
_LldpXdot1dcbxRemETSConTSATrafficClass_Type = LldpXdot1dcbxTrafficClassValue
_LldpXdot1dcbxRemETSConTSATrafficClass_Object = MibTableColumn
lldpXdot1dcbxRemETSConTSATrafficClass = _LldpXdot1dcbxRemETSConTSATrafficClass_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 1, 4, 1, 1),
    _LldpXdot1dcbxRemETSConTSATrafficClass_Type()
)
lldpXdot1dcbxRemETSConTSATrafficClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemETSConTSATrafficClass.setStatus("current")
_LldpXdot1dcbxRemETSConTrafficSelectionAlgorithm_Type = LldpXdot1dcbxTrafficSelectionAlgorithm
_LldpXdot1dcbxRemETSConTrafficSelectionAlgorithm_Object = MibTableColumn
lldpXdot1dcbxRemETSConTrafficSelectionAlgorithm = _LldpXdot1dcbxRemETSConTrafficSelectionAlgorithm_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 1, 4, 1, 2),
    _LldpXdot1dcbxRemETSConTrafficSelectionAlgorithm_Type()
)
lldpXdot1dcbxRemETSConTrafficSelectionAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemETSConTrafficSelectionAlgorithm.setStatus("current")
_LldpXdot1dcbxRemETSReco_ObjectIdentity = ObjectIdentity
lldpXdot1dcbxRemETSReco = _LldpXdot1dcbxRemETSReco_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 2)
)
_LldpXdot1dcbxRemETSRecoTrafficClassBandwidthTable_Object = MibTable
lldpXdot1dcbxRemETSRecoTrafficClassBandwidthTable = _LldpXdot1dcbxRemETSRecoTrafficClassBandwidthTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemETSRecoTrafficClassBandwidthTable.setStatus("current")
_LldpXdot1dcbxRemETSRecoTrafficClassBandwidthEntry_Object = MibTableRow
lldpXdot1dcbxRemETSRecoTrafficClassBandwidthEntry = _LldpXdot1dcbxRemETSRecoTrafficClassBandwidthEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 2, 1, 1)
)
lldpXdot1dcbxRemETSRecoTrafficClassBandwidthEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2RemTimeMark"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"),
    (0, "LLDP-V2-MIB", "lldpV2RemIndex"),
    (0, "LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxRemETSRecoTrafficClass"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemETSRecoTrafficClassBandwidthEntry.setStatus("current")
_LldpXdot1dcbxRemETSRecoTrafficClass_Type = LldpXdot1dcbxTrafficClassValue
_LldpXdot1dcbxRemETSRecoTrafficClass_Object = MibTableColumn
lldpXdot1dcbxRemETSRecoTrafficClass = _LldpXdot1dcbxRemETSRecoTrafficClass_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 2, 1, 1, 1),
    _LldpXdot1dcbxRemETSRecoTrafficClass_Type()
)
lldpXdot1dcbxRemETSRecoTrafficClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemETSRecoTrafficClass.setStatus("current")
_LldpXdot1dcbxRemETSRecoTrafficClassBandwidth_Type = LldpXdot1dcbxTrafficClassBandwidthValue
_LldpXdot1dcbxRemETSRecoTrafficClassBandwidth_Object = MibTableColumn
lldpXdot1dcbxRemETSRecoTrafficClassBandwidth = _LldpXdot1dcbxRemETSRecoTrafficClassBandwidth_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 2, 1, 1, 2),
    _LldpXdot1dcbxRemETSRecoTrafficClassBandwidth_Type()
)
lldpXdot1dcbxRemETSRecoTrafficClassBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemETSRecoTrafficClassBandwidth.setStatus("current")
_LldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithmTable_Object = MibTable
lldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithmTable = _LldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithmTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithmTable.setStatus("current")
_LldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithmEntry_Object = MibTableRow
lldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithmEntry = _LldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithmEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 2, 2, 1)
)
lldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithmEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2RemTimeMark"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"),
    (0, "LLDP-V2-MIB", "lldpV2RemIndex"),
    (0, "LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxRemETSRecoTSATrafficClass"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithmEntry.setStatus("current")
_LldpXdot1dcbxRemETSRecoTSATrafficClass_Type = LldpXdot1dcbxTrafficClassValue
_LldpXdot1dcbxRemETSRecoTSATrafficClass_Object = MibTableColumn
lldpXdot1dcbxRemETSRecoTSATrafficClass = _LldpXdot1dcbxRemETSRecoTSATrafficClass_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 2, 2, 1, 1),
    _LldpXdot1dcbxRemETSRecoTSATrafficClass_Type()
)
lldpXdot1dcbxRemETSRecoTSATrafficClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemETSRecoTSATrafficClass.setStatus("current")
_LldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithm_Type = LldpXdot1dcbxTrafficSelectionAlgorithm
_LldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithm_Object = MibTableColumn
lldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithm = _LldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithm_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 2, 2, 1, 2),
    _LldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithm_Type()
)
lldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithm.setStatus("current")
_LldpXdot1dcbxRemPFC_ObjectIdentity = ObjectIdentity
lldpXdot1dcbxRemPFC = _LldpXdot1dcbxRemPFC_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 3)
)
_LldpXdot1dcbxRemPFCBasicTable_Object = MibTable
lldpXdot1dcbxRemPFCBasicTable = _LldpXdot1dcbxRemPFCBasicTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemPFCBasicTable.setStatus("current")
_LldpXdot1dcbxRemPFCBasicEntry_Object = MibTableRow
lldpXdot1dcbxRemPFCBasicEntry = _LldpXdot1dcbxRemPFCBasicEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 3, 1, 1)
)
lldpXdot1dcbxRemPFCBasicEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2RemTimeMark"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"),
    (0, "LLDP-V2-MIB", "lldpV2RemIndex"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemPFCBasicEntry.setStatus("current")
_LldpXdot1dcbxRemPFCWilling_Type = TruthValue
_LldpXdot1dcbxRemPFCWilling_Object = MibTableColumn
lldpXdot1dcbxRemPFCWilling = _LldpXdot1dcbxRemPFCWilling_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 3, 1, 1, 1),
    _LldpXdot1dcbxRemPFCWilling_Type()
)
lldpXdot1dcbxRemPFCWilling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemPFCWilling.setStatus("current")
_LldpXdot1dcbxRemPFCMBC_Type = TruthValue
_LldpXdot1dcbxRemPFCMBC_Object = MibTableColumn
lldpXdot1dcbxRemPFCMBC = _LldpXdot1dcbxRemPFCMBC_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 3, 1, 1, 2),
    _LldpXdot1dcbxRemPFCMBC_Type()
)
lldpXdot1dcbxRemPFCMBC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemPFCMBC.setStatus("current")
_LldpXdot1dcbxRemPFCCap_Type = LldpXdot1dcbxSupportedCapacity
_LldpXdot1dcbxRemPFCCap_Object = MibTableColumn
lldpXdot1dcbxRemPFCCap = _LldpXdot1dcbxRemPFCCap_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 3, 1, 1, 3),
    _LldpXdot1dcbxRemPFCCap_Type()
)
lldpXdot1dcbxRemPFCCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemPFCCap.setStatus("current")
_LldpXdot1dcbxRemPFCEnableTable_Object = MibTable
lldpXdot1dcbxRemPFCEnableTable = _LldpXdot1dcbxRemPFCEnableTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 3, 2)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemPFCEnableTable.setStatus("current")
_LldpXdot1dcbxRemPFCEnableEntry_Object = MibTableRow
lldpXdot1dcbxRemPFCEnableEntry = _LldpXdot1dcbxRemPFCEnableEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 3, 2, 1)
)
lldpXdot1dcbxRemPFCEnableEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2RemTimeMark"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"),
    (0, "LLDP-V2-MIB", "lldpV2RemIndex"),
    (0, "LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxRemPFCEnablePriority"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemPFCEnableEntry.setStatus("current")
_LldpXdot1dcbxRemPFCEnablePriority_Type = IEEE8021PriorityValue
_LldpXdot1dcbxRemPFCEnablePriority_Object = MibTableColumn
lldpXdot1dcbxRemPFCEnablePriority = _LldpXdot1dcbxRemPFCEnablePriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 3, 2, 1, 1),
    _LldpXdot1dcbxRemPFCEnablePriority_Type()
)
lldpXdot1dcbxRemPFCEnablePriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemPFCEnablePriority.setStatus("current")
_LldpXdot1dcbxRemPFCEnableEnabled_Type = TruthValue
_LldpXdot1dcbxRemPFCEnableEnabled_Object = MibTableColumn
lldpXdot1dcbxRemPFCEnableEnabled = _LldpXdot1dcbxRemPFCEnableEnabled_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 3, 2, 1, 2),
    _LldpXdot1dcbxRemPFCEnableEnabled_Type()
)
lldpXdot1dcbxRemPFCEnableEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemPFCEnableEnabled.setStatus("current")
_LldpXdot1dcbxRemApplicationPriorityAppTable_Object = MibTable
lldpXdot1dcbxRemApplicationPriorityAppTable = _LldpXdot1dcbxRemApplicationPriorityAppTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 4)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemApplicationPriorityAppTable.setStatus("current")
_LldpXdot1dcbxRemApplicationPriorityAppEntry_Object = MibTableRow
lldpXdot1dcbxRemApplicationPriorityAppEntry = _LldpXdot1dcbxRemApplicationPriorityAppEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 4, 1)
)
lldpXdot1dcbxRemApplicationPriorityAppEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2RemTimeMark"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"),
    (0, "LLDP-V2-MIB", "lldpV2RemIndex"),
    (0, "LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxRemApplicationPriorityAESelector"),
    (0, "LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxRemApplicationPriorityAEProtocol"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemApplicationPriorityAppEntry.setStatus("current")
_LldpXdot1dcbxRemApplicationPriorityAESelector_Type = LldpXdot1dcbxAppSelector
_LldpXdot1dcbxRemApplicationPriorityAESelector_Object = MibTableColumn
lldpXdot1dcbxRemApplicationPriorityAESelector = _LldpXdot1dcbxRemApplicationPriorityAESelector_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 4, 1, 1),
    _LldpXdot1dcbxRemApplicationPriorityAESelector_Type()
)
lldpXdot1dcbxRemApplicationPriorityAESelector.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemApplicationPriorityAESelector.setStatus("current")
_LldpXdot1dcbxRemApplicationPriorityAEProtocol_Type = LldpXdot1dcbxAppProtocol
_LldpXdot1dcbxRemApplicationPriorityAEProtocol_Object = MibTableColumn
lldpXdot1dcbxRemApplicationPriorityAEProtocol = _LldpXdot1dcbxRemApplicationPriorityAEProtocol_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 4, 1, 2),
    _LldpXdot1dcbxRemApplicationPriorityAEProtocol_Type()
)
lldpXdot1dcbxRemApplicationPriorityAEProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemApplicationPriorityAEProtocol.setStatus("current")
_LldpXdot1dcbxRemApplicationPriorityAEPriority_Type = IEEE8021PriorityValue
_LldpXdot1dcbxRemApplicationPriorityAEPriority_Object = MibTableColumn
lldpXdot1dcbxRemApplicationPriorityAEPriority = _LldpXdot1dcbxRemApplicationPriorityAEPriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 4, 1, 3),
    _LldpXdot1dcbxRemApplicationPriorityAEPriority_Type()
)
lldpXdot1dcbxRemApplicationPriorityAEPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemApplicationPriorityAEPriority.setStatus("current")
_LldpXdot1dcbxRemApplicationVlanAppTable_Object = MibTable
lldpXdot1dcbxRemApplicationVlanAppTable = _LldpXdot1dcbxRemApplicationVlanAppTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 5)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemApplicationVlanAppTable.setStatus("current")
_LldpXdot1dcbxRemApplicationVlanAppEntry_Object = MibTableRow
lldpXdot1dcbxRemApplicationVlanAppEntry = _LldpXdot1dcbxRemApplicationVlanAppEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 5, 1)
)
lldpXdot1dcbxRemApplicationVlanAppEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2RemTimeMark"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"),
    (0, "LLDP-V2-MIB", "lldpV2RemIndex"),
    (0, "LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxRemApplicationVlanAESelector"),
    (0, "LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxRemApplicationVlanAEProtocol"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemApplicationVlanAppEntry.setStatus("current")
_LldpXdot1dcbxRemApplicationVlanAESelector_Type = LldpXdot1dcbxAppSelector
_LldpXdot1dcbxRemApplicationVlanAESelector_Object = MibTableColumn
lldpXdot1dcbxRemApplicationVlanAESelector = _LldpXdot1dcbxRemApplicationVlanAESelector_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 5, 1, 1),
    _LldpXdot1dcbxRemApplicationVlanAESelector_Type()
)
lldpXdot1dcbxRemApplicationVlanAESelector.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemApplicationVlanAESelector.setStatus("current")
_LldpXdot1dcbxRemApplicationVlanAEProtocol_Type = LldpXdot1dcbxAppProtocol
_LldpXdot1dcbxRemApplicationVlanAEProtocol_Object = MibTableColumn
lldpXdot1dcbxRemApplicationVlanAEProtocol = _LldpXdot1dcbxRemApplicationVlanAEProtocol_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 5, 1, 2),
    _LldpXdot1dcbxRemApplicationVlanAEProtocol_Type()
)
lldpXdot1dcbxRemApplicationVlanAEProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemApplicationVlanAEProtocol.setStatus("current")
_LldpXdot1dcbxRemApplicationVlanAEVlanId_Type = VlanId
_LldpXdot1dcbxRemApplicationVlanAEVlanId_Object = MibTableColumn
lldpXdot1dcbxRemApplicationVlanAEVlanId = _LldpXdot1dcbxRemApplicationVlanAEVlanId_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 5, 1, 3),
    _LldpXdot1dcbxRemApplicationVlanAEVlanId_Type()
)
lldpXdot1dcbxRemApplicationVlanAEVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemApplicationVlanAEVlanId.setStatus("current")
_LldpXdot1dcbxAdminData_ObjectIdentity = ObjectIdentity
lldpXdot1dcbxAdminData = _LldpXdot1dcbxAdminData_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4)
)
_LldpXdot1dcbxAdminETSConfiguration_ObjectIdentity = ObjectIdentity
lldpXdot1dcbxAdminETSConfiguration = _LldpXdot1dcbxAdminETSConfiguration_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 1)
)
_LldpXdot1dcbxAdminETSBasicConfigurationTable_Object = MibTable
lldpXdot1dcbxAdminETSBasicConfigurationTable = _LldpXdot1dcbxAdminETSBasicConfigurationTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminETSBasicConfigurationTable.setStatus("current")
_LldpXdot1dcbxAdminETSBasicConfigurationEntry_Object = MibTableRow
lldpXdot1dcbxAdminETSBasicConfigurationEntry = _LldpXdot1dcbxAdminETSBasicConfigurationEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 1, 1, 1)
)
lldpXdot1dcbxAdminETSBasicConfigurationEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminETSBasicConfigurationEntry.setStatus("current")
_LldpXdot1dcbxAdminETSConCreditBasedShaperSupport_Type = TruthValue
_LldpXdot1dcbxAdminETSConCreditBasedShaperSupport_Object = MibTableColumn
lldpXdot1dcbxAdminETSConCreditBasedShaperSupport = _LldpXdot1dcbxAdminETSConCreditBasedShaperSupport_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 1, 1, 1, 1),
    _LldpXdot1dcbxAdminETSConCreditBasedShaperSupport_Type()
)
lldpXdot1dcbxAdminETSConCreditBasedShaperSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminETSConCreditBasedShaperSupport.setStatus("current")
_LldpXdot1dcbxAdminETSConTrafficClassesSupported_Type = LldpXdot1dcbxSupportedCapacity
_LldpXdot1dcbxAdminETSConTrafficClassesSupported_Object = MibTableColumn
lldpXdot1dcbxAdminETSConTrafficClassesSupported = _LldpXdot1dcbxAdminETSConTrafficClassesSupported_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 1, 1, 1, 2),
    _LldpXdot1dcbxAdminETSConTrafficClassesSupported_Type()
)
lldpXdot1dcbxAdminETSConTrafficClassesSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminETSConTrafficClassesSupported.setStatus("current")


class _LldpXdot1dcbxAdminETSConWilling_Type(TruthValue):
    """Custom type lldpXdot1dcbxAdminETSConWilling based on TruthValue"""


_LldpXdot1dcbxAdminETSConWilling_Object = MibTableColumn
lldpXdot1dcbxAdminETSConWilling = _LldpXdot1dcbxAdminETSConWilling_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 1, 1, 1, 3),
    _LldpXdot1dcbxAdminETSConWilling_Type()
)
lldpXdot1dcbxAdminETSConWilling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminETSConWilling.setStatus("current")
_LldpXdot1dcbxAdminETSConPriorityAssignmentTable_Object = MibTable
lldpXdot1dcbxAdminETSConPriorityAssignmentTable = _LldpXdot1dcbxAdminETSConPriorityAssignmentTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminETSConPriorityAssignmentTable.setStatus("current")
_LldpXdot1dcbxAdminETSConPriorityAssignmentEntry_Object = MibTableRow
lldpXdot1dcbxAdminETSConPriorityAssignmentEntry = _LldpXdot1dcbxAdminETSConPriorityAssignmentEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 1, 2, 1)
)
lldpXdot1dcbxAdminETSConPriorityAssignmentEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
    (0, "LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxAdminETSConPriority"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminETSConPriorityAssignmentEntry.setStatus("current")
_LldpXdot1dcbxAdminETSConPriority_Type = IEEE8021PriorityValue
_LldpXdot1dcbxAdminETSConPriority_Object = MibTableColumn
lldpXdot1dcbxAdminETSConPriority = _LldpXdot1dcbxAdminETSConPriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 1, 2, 1, 1),
    _LldpXdot1dcbxAdminETSConPriority_Type()
)
lldpXdot1dcbxAdminETSConPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminETSConPriority.setStatus("current")


class _LldpXdot1dcbxAdminETSConPriTrafficClass_Type(LldpXdot1dcbxTrafficClassValue):
    """Custom type lldpXdot1dcbxAdminETSConPriTrafficClass based on LldpXdot1dcbxTrafficClassValue"""
    defaultValue = 0


_LldpXdot1dcbxAdminETSConPriTrafficClass_Object = MibTableColumn
lldpXdot1dcbxAdminETSConPriTrafficClass = _LldpXdot1dcbxAdminETSConPriTrafficClass_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 1, 2, 1, 2),
    _LldpXdot1dcbxAdminETSConPriTrafficClass_Type()
)
lldpXdot1dcbxAdminETSConPriTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminETSConPriTrafficClass.setStatus("current")
_LldpXdot1dcbxAdminETSConTrafficClassBandwidthTable_Object = MibTable
lldpXdot1dcbxAdminETSConTrafficClassBandwidthTable = _LldpXdot1dcbxAdminETSConTrafficClassBandwidthTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 1, 3)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminETSConTrafficClassBandwidthTable.setStatus("current")
_LldpXdot1dcbxAdminETSConTrafficClassBandwidthEntry_Object = MibTableRow
lldpXdot1dcbxAdminETSConTrafficClassBandwidthEntry = _LldpXdot1dcbxAdminETSConTrafficClassBandwidthEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 1, 3, 1)
)
lldpXdot1dcbxAdminETSConTrafficClassBandwidthEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
    (0, "LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxAdminETSConTrafficClass"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminETSConTrafficClassBandwidthEntry.setStatus("current")
_LldpXdot1dcbxAdminETSConTrafficClass_Type = LldpXdot1dcbxTrafficClassValue
_LldpXdot1dcbxAdminETSConTrafficClass_Object = MibTableColumn
lldpXdot1dcbxAdminETSConTrafficClass = _LldpXdot1dcbxAdminETSConTrafficClass_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 1, 3, 1, 1),
    _LldpXdot1dcbxAdminETSConTrafficClass_Type()
)
lldpXdot1dcbxAdminETSConTrafficClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminETSConTrafficClass.setStatus("current")
_LldpXdot1dcbxAdminETSConTrafficClassBandwidth_Type = LldpXdot1dcbxTrafficClassBandwidthValue
_LldpXdot1dcbxAdminETSConTrafficClassBandwidth_Object = MibTableColumn
lldpXdot1dcbxAdminETSConTrafficClassBandwidth = _LldpXdot1dcbxAdminETSConTrafficClassBandwidth_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 1, 3, 1, 2),
    _LldpXdot1dcbxAdminETSConTrafficClassBandwidth_Type()
)
lldpXdot1dcbxAdminETSConTrafficClassBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminETSConTrafficClassBandwidth.setStatus("current")
_LldpXdot1dcbxAdminETSConTrafficSelectionAlgorithmTable_Object = MibTable
lldpXdot1dcbxAdminETSConTrafficSelectionAlgorithmTable = _LldpXdot1dcbxAdminETSConTrafficSelectionAlgorithmTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 1, 4)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminETSConTrafficSelectionAlgorithmTable.setStatus("current")
_LldpXdot1dcbxAdminETSConTrafficSelectionAlgorithmEntry_Object = MibTableRow
lldpXdot1dcbxAdminETSConTrafficSelectionAlgorithmEntry = _LldpXdot1dcbxAdminETSConTrafficSelectionAlgorithmEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 1, 4, 1)
)
lldpXdot1dcbxAdminETSConTrafficSelectionAlgorithmEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
    (0, "LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxAdminETSConTSATrafficClass"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminETSConTrafficSelectionAlgorithmEntry.setStatus("current")
_LldpXdot1dcbxAdminETSConTSATrafficClass_Type = LldpXdot1dcbxTrafficClassValue
_LldpXdot1dcbxAdminETSConTSATrafficClass_Object = MibTableColumn
lldpXdot1dcbxAdminETSConTSATrafficClass = _LldpXdot1dcbxAdminETSConTSATrafficClass_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 1, 4, 1, 1),
    _LldpXdot1dcbxAdminETSConTSATrafficClass_Type()
)
lldpXdot1dcbxAdminETSConTSATrafficClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminETSConTSATrafficClass.setStatus("current")
_LldpXdot1dcbxAdminETSConTrafficSelectionAlgorithm_Type = LldpXdot1dcbxTrafficSelectionAlgorithm
_LldpXdot1dcbxAdminETSConTrafficSelectionAlgorithm_Object = MibTableColumn
lldpXdot1dcbxAdminETSConTrafficSelectionAlgorithm = _LldpXdot1dcbxAdminETSConTrafficSelectionAlgorithm_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 1, 4, 1, 2),
    _LldpXdot1dcbxAdminETSConTrafficSelectionAlgorithm_Type()
)
lldpXdot1dcbxAdminETSConTrafficSelectionAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminETSConTrafficSelectionAlgorithm.setStatus("current")
_LldpXdot1dcbxAdminETSReco_ObjectIdentity = ObjectIdentity
lldpXdot1dcbxAdminETSReco = _LldpXdot1dcbxAdminETSReco_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 2)
)
_LldpXdot1dcbxAdminETSRecoTrafficClassBandwidthTable_Object = MibTable
lldpXdot1dcbxAdminETSRecoTrafficClassBandwidthTable = _LldpXdot1dcbxAdminETSRecoTrafficClassBandwidthTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminETSRecoTrafficClassBandwidthTable.setStatus("current")
_LldpXdot1dcbxAdminETSRecoTrafficClassBandwidthEntry_Object = MibTableRow
lldpXdot1dcbxAdminETSRecoTrafficClassBandwidthEntry = _LldpXdot1dcbxAdminETSRecoTrafficClassBandwidthEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 2, 1, 1)
)
lldpXdot1dcbxAdminETSRecoTrafficClassBandwidthEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
    (0, "LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxAdminETSRecoTrafficClass"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminETSRecoTrafficClassBandwidthEntry.setStatus("current")
_LldpXdot1dcbxAdminETSRecoTrafficClass_Type = LldpXdot1dcbxTrafficClassValue
_LldpXdot1dcbxAdminETSRecoTrafficClass_Object = MibTableColumn
lldpXdot1dcbxAdminETSRecoTrafficClass = _LldpXdot1dcbxAdminETSRecoTrafficClass_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 2, 1, 1, 1),
    _LldpXdot1dcbxAdminETSRecoTrafficClass_Type()
)
lldpXdot1dcbxAdminETSRecoTrafficClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminETSRecoTrafficClass.setStatus("current")
_LldpXdot1dcbxAdminETSRecoTrafficClassBandwidth_Type = LldpXdot1dcbxTrafficClassBandwidthValue
_LldpXdot1dcbxAdminETSRecoTrafficClassBandwidth_Object = MibTableColumn
lldpXdot1dcbxAdminETSRecoTrafficClassBandwidth = _LldpXdot1dcbxAdminETSRecoTrafficClassBandwidth_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 2, 1, 1, 2),
    _LldpXdot1dcbxAdminETSRecoTrafficClassBandwidth_Type()
)
lldpXdot1dcbxAdminETSRecoTrafficClassBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminETSRecoTrafficClassBandwidth.setStatus("current")
_LldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithmTable_Object = MibTable
lldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithmTable = _LldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithmTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 2, 2)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithmTable.setStatus("current")
_LldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithmEntry_Object = MibTableRow
lldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithmEntry = _LldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithmEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 2, 2, 1)
)
lldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithmEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
    (0, "LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxAdminETSRecoTSATrafficClass"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithmEntry.setStatus("current")
_LldpXdot1dcbxAdminETSRecoTSATrafficClass_Type = LldpXdot1dcbxTrafficClassValue
_LldpXdot1dcbxAdminETSRecoTSATrafficClass_Object = MibTableColumn
lldpXdot1dcbxAdminETSRecoTSATrafficClass = _LldpXdot1dcbxAdminETSRecoTSATrafficClass_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 2, 2, 1, 1),
    _LldpXdot1dcbxAdminETSRecoTSATrafficClass_Type()
)
lldpXdot1dcbxAdminETSRecoTSATrafficClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminETSRecoTSATrafficClass.setStatus("current")
_LldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithm_Type = LldpXdot1dcbxTrafficSelectionAlgorithm
_LldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithm_Object = MibTableColumn
lldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithm = _LldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithm_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 2, 2, 1, 2),
    _LldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithm_Type()
)
lldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithm.setStatus("current")
_LldpXdot1dcbxAdminPFC_ObjectIdentity = ObjectIdentity
lldpXdot1dcbxAdminPFC = _LldpXdot1dcbxAdminPFC_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 3)
)
_LldpXdot1dcbxAdminPFCBasicTable_Object = MibTable
lldpXdot1dcbxAdminPFCBasicTable = _LldpXdot1dcbxAdminPFCBasicTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminPFCBasicTable.setStatus("current")
_LldpXdot1dcbxAdminPFCBasicEntry_Object = MibTableRow
lldpXdot1dcbxAdminPFCBasicEntry = _LldpXdot1dcbxAdminPFCBasicEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 3, 1, 1)
)
lldpXdot1dcbxAdminPFCBasicEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminPFCBasicEntry.setStatus("current")


class _LldpXdot1dcbxAdminPFCWilling_Type(TruthValue):
    """Custom type lldpXdot1dcbxAdminPFCWilling based on TruthValue"""


_LldpXdot1dcbxAdminPFCWilling_Object = MibTableColumn
lldpXdot1dcbxAdminPFCWilling = _LldpXdot1dcbxAdminPFCWilling_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 3, 1, 1, 1),
    _LldpXdot1dcbxAdminPFCWilling_Type()
)
lldpXdot1dcbxAdminPFCWilling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminPFCWilling.setStatus("current")
_LldpXdot1dcbxAdminPFCMBC_Type = TruthValue
_LldpXdot1dcbxAdminPFCMBC_Object = MibTableColumn
lldpXdot1dcbxAdminPFCMBC = _LldpXdot1dcbxAdminPFCMBC_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 3, 1, 1, 2),
    _LldpXdot1dcbxAdminPFCMBC_Type()
)
lldpXdot1dcbxAdminPFCMBC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminPFCMBC.setStatus("current")
_LldpXdot1dcbxAdminPFCCap_Type = LldpXdot1dcbxSupportedCapacity
_LldpXdot1dcbxAdminPFCCap_Object = MibTableColumn
lldpXdot1dcbxAdminPFCCap = _LldpXdot1dcbxAdminPFCCap_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 3, 1, 1, 3),
    _LldpXdot1dcbxAdminPFCCap_Type()
)
lldpXdot1dcbxAdminPFCCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminPFCCap.setStatus("current")
_LldpXdot1dcbxAdminPFCEnableTable_Object = MibTable
lldpXdot1dcbxAdminPFCEnableTable = _LldpXdot1dcbxAdminPFCEnableTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 3, 2)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminPFCEnableTable.setStatus("current")
_LldpXdot1dcbxAdminPFCEnableEntry_Object = MibTableRow
lldpXdot1dcbxAdminPFCEnableEntry = _LldpXdot1dcbxAdminPFCEnableEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 3, 2, 1)
)
lldpXdot1dcbxAdminPFCEnableEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
    (0, "LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxAdminPFCEnablePriority"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminPFCEnableEntry.setStatus("current")
_LldpXdot1dcbxAdminPFCEnablePriority_Type = IEEE8021PriorityValue
_LldpXdot1dcbxAdminPFCEnablePriority_Object = MibTableColumn
lldpXdot1dcbxAdminPFCEnablePriority = _LldpXdot1dcbxAdminPFCEnablePriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 3, 2, 1, 1),
    _LldpXdot1dcbxAdminPFCEnablePriority_Type()
)
lldpXdot1dcbxAdminPFCEnablePriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminPFCEnablePriority.setStatus("current")


class _LldpXdot1dcbxAdminPFCEnableEnabled_Type(TruthValue):
    """Custom type lldpXdot1dcbxAdminPFCEnableEnabled based on TruthValue"""


_LldpXdot1dcbxAdminPFCEnableEnabled_Object = MibTableColumn
lldpXdot1dcbxAdminPFCEnableEnabled = _LldpXdot1dcbxAdminPFCEnableEnabled_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 3, 2, 1, 2),
    _LldpXdot1dcbxAdminPFCEnableEnabled_Type()
)
lldpXdot1dcbxAdminPFCEnableEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminPFCEnableEnabled.setStatus("current")
_LldpXdot1dcbxAdminApplicationPriorityAppTable_Object = MibTable
lldpXdot1dcbxAdminApplicationPriorityAppTable = _LldpXdot1dcbxAdminApplicationPriorityAppTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 4)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminApplicationPriorityAppTable.setStatus("current")
_LldpXdot1dcbxAdminApplicationPriorityAppEntry_Object = MibTableRow
lldpXdot1dcbxAdminApplicationPriorityAppEntry = _LldpXdot1dcbxAdminApplicationPriorityAppEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 4, 1)
)
lldpXdot1dcbxAdminApplicationPriorityAppEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
    (0, "LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxAdminApplicationPriorityAESelector"),
    (0, "LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxAdminApplicationPriorityAEProtocol"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminApplicationPriorityAppEntry.setStatus("current")
_LldpXdot1dcbxAdminApplicationPriorityAESelector_Type = LldpXdot1dcbxAppSelector
_LldpXdot1dcbxAdminApplicationPriorityAESelector_Object = MibTableColumn
lldpXdot1dcbxAdminApplicationPriorityAESelector = _LldpXdot1dcbxAdminApplicationPriorityAESelector_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 4, 1, 1),
    _LldpXdot1dcbxAdminApplicationPriorityAESelector_Type()
)
lldpXdot1dcbxAdminApplicationPriorityAESelector.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminApplicationPriorityAESelector.setStatus("current")
_LldpXdot1dcbxAdminApplicationPriorityAEProtocol_Type = LldpXdot1dcbxAppProtocol
_LldpXdot1dcbxAdminApplicationPriorityAEProtocol_Object = MibTableColumn
lldpXdot1dcbxAdminApplicationPriorityAEProtocol = _LldpXdot1dcbxAdminApplicationPriorityAEProtocol_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 4, 1, 2),
    _LldpXdot1dcbxAdminApplicationPriorityAEProtocol_Type()
)
lldpXdot1dcbxAdminApplicationPriorityAEProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminApplicationPriorityAEProtocol.setStatus("current")
_LldpXdot1dcbxAdminApplicationPriorityAEPriority_Type = IEEE8021PriorityValue
_LldpXdot1dcbxAdminApplicationPriorityAEPriority_Object = MibTableColumn
lldpXdot1dcbxAdminApplicationPriorityAEPriority = _LldpXdot1dcbxAdminApplicationPriorityAEPriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 4, 1, 3),
    _LldpXdot1dcbxAdminApplicationPriorityAEPriority_Type()
)
lldpXdot1dcbxAdminApplicationPriorityAEPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminApplicationPriorityAEPriority.setStatus("current")
_LldpXdot1dcbxAdminApplicationVlanAppTable_Object = MibTable
lldpXdot1dcbxAdminApplicationVlanAppTable = _LldpXdot1dcbxAdminApplicationVlanAppTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 5)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminApplicationVlanAppTable.setStatus("current")
_LldpXdot1dcbxAdminApplicationVlanAppEntry_Object = MibTableRow
lldpXdot1dcbxAdminApplicationVlanAppEntry = _LldpXdot1dcbxAdminApplicationVlanAppEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 5, 1)
)
lldpXdot1dcbxAdminApplicationVlanAppEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
    (0, "LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxAdminApplicationVlanAESelector"),
    (0, "LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxAdminApplicationVlanAEProtocol"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminApplicationVlanAppEntry.setStatus("current")
_LldpXdot1dcbxAdminApplicationVlanAESelector_Type = LldpXdot1dcbxAppSelector
_LldpXdot1dcbxAdminApplicationVlanAESelector_Object = MibTableColumn
lldpXdot1dcbxAdminApplicationVlanAESelector = _LldpXdot1dcbxAdminApplicationVlanAESelector_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 5, 1, 1),
    _LldpXdot1dcbxAdminApplicationVlanAESelector_Type()
)
lldpXdot1dcbxAdminApplicationVlanAESelector.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminApplicationVlanAESelector.setStatus("current")
_LldpXdot1dcbxAdminApplicationVlanAEProtocol_Type = LldpXdot1dcbxAppProtocol
_LldpXdot1dcbxAdminApplicationVlanAEProtocol_Object = MibTableColumn
lldpXdot1dcbxAdminApplicationVlanAEProtocol = _LldpXdot1dcbxAdminApplicationVlanAEProtocol_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 5, 1, 2),
    _LldpXdot1dcbxAdminApplicationVlanAEProtocol_Type()
)
lldpXdot1dcbxAdminApplicationVlanAEProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminApplicationVlanAEProtocol.setStatus("current")
_LldpXdot1dcbxAdminApplicationVlanAEVlanId_Type = VlanId
_LldpXdot1dcbxAdminApplicationVlanAEVlanId_Object = MibTableColumn
lldpXdot1dcbxAdminApplicationVlanAEVlanId = _LldpXdot1dcbxAdminApplicationVlanAEVlanId_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 5, 1, 3),
    _LldpXdot1dcbxAdminApplicationVlanAEVlanId_Type()
)
lldpXdot1dcbxAdminApplicationVlanAEVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminApplicationVlanAEVlanId.setStatus("current")
_LldpXdot1dcbxConformance_ObjectIdentity = ObjectIdentity
lldpXdot1dcbxConformance = _LldpXdot1dcbxConformance_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 6)
)
_LldpXdot1dcbxCompliances_ObjectIdentity = ObjectIdentity
lldpXdot1dcbxCompliances = _LldpXdot1dcbxCompliances_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 6, 1)
)
_LldpXdot1dcbxGroups_ObjectIdentity = ObjectIdentity
lldpXdot1dcbxGroups = _LldpXdot1dcbxGroups_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 6, 2)
)
lldpV2PortConfigEntry.registerAugmentions(
    ("LLDP-EXT-DOT1-V2-MIB",
     "lldpV2Xdot1ConfigPortVlanEntry")
)
lldpV2Xdot1ConfigPortVlanEntry.setIndexNames(*lldpV2PortConfigEntry.getIndexNames())
lldpV2Xdot1LocVlanNameEntry.registerAugmentions(
    ("LLDP-EXT-DOT1-V2-MIB",
     "lldpV2Xdot1ConfigVlanNameEntry")
)
lldpV2Xdot1ConfigVlanNameEntry.setIndexNames(*lldpV2Xdot1LocVlanNameEntry.getIndexNames())
lldpV2Xdot1LocProtoVlanEntry.registerAugmentions(
    ("LLDP-EXT-DOT1-V2-MIB",
     "lldpV2Xdot1ConfigProtoVlanEntry")
)
lldpV2Xdot1ConfigProtoVlanEntry.setIndexNames(*lldpV2Xdot1LocProtoVlanEntry.getIndexNames())
lldpV2Xdot1LocProtocolEntry.registerAugmentions(
    ("LLDP-EXT-DOT1-V2-MIB",
     "lldpV2Xdot1ConfigProtocolEntry")
)
lldpV2Xdot1ConfigProtocolEntry.setIndexNames(*lldpV2Xdot1LocProtocolEntry.getIndexNames())
lldpV2Xdot1LocVidUsageDigestEntry.registerAugmentions(
    ("LLDP-EXT-DOT1-V2-MIB",
     "lldpV2Xdot1ConfigVidUsageDigestEntry")
)
lldpV2Xdot1ConfigVidUsageDigestEntry.setIndexNames(*lldpV2Xdot1LocVidUsageDigestEntry.getIndexNames())
lldpV2Xdot1LocManVidEntry.registerAugmentions(
    ("LLDP-EXT-DOT1-V2-MIB",
     "lldpV2Xdot1ConfigManVidEntry")
)
lldpV2Xdot1ConfigManVidEntry.setIndexNames(*lldpV2Xdot1LocManVidEntry.getIndexNames())
lldpV2PortConfigEntry.registerAugmentions(
    ("LLDP-EXT-DOT1-V2-MIB",
     "lldpXdot1CnConfigCnEntry")
)
lldpXdot1CnConfigCnEntry.setIndexNames(*lldpV2PortConfigEntry.getIndexNames())
lldpV2PortConfigEntry.registerAugmentions(
    ("LLDP-EXT-DOT1-V2-MIB",
     "lldpXdot1dcbxConfigETSConfigurationEntry")
)
lldpXdot1dcbxConfigETSConfigurationEntry.setIndexNames(*lldpV2PortConfigEntry.getIndexNames())
lldpV2PortConfigEntry.registerAugmentions(
    ("LLDP-EXT-DOT1-V2-MIB",
     "lldpXdot1dcbxConfigETSRecommendationEntry")
)
lldpXdot1dcbxConfigETSRecommendationEntry.setIndexNames(*lldpV2PortConfigEntry.getIndexNames())
lldpV2PortConfigEntry.registerAugmentions(
    ("LLDP-EXT-DOT1-V2-MIB",
     "lldpXdot1dcbxConfigPFCEntry")
)
lldpXdot1dcbxConfigPFCEntry.setIndexNames(*lldpV2PortConfigEntry.getIndexNames())
lldpV2PortConfigEntry.registerAugmentions(
    ("LLDP-EXT-DOT1-V2-MIB",
     "lldpXdot1dcbxConfigApplicationPriorityEntry")
)
lldpXdot1dcbxConfigApplicationPriorityEntry.setIndexNames(*lldpV2PortConfigEntry.getIndexNames())
lldpV2PortConfigEntry.registerAugmentions(
    ("LLDP-EXT-DOT1-V2-MIB",
     "lldpXdot1dcbxConfigApplicationVlanEntry")
)
lldpXdot1dcbxConfigApplicationVlanEntry.setIndexNames(*lldpV2PortConfigEntry.getIndexNames())

# Managed Objects groups

lldpV2Xdot1ConfigGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 2, 2, 1)
)
lldpV2Xdot1ConfigGroup.setObjects(
      *(("LLDP-EXT-DOT1-V2-MIB", "lldpV2Xdot1ConfigPortVlanTxEnable"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpV2Xdot1ConfigVlanNameTxEnable"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpV2Xdot1ConfigProtoVlanTxEnable"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpV2Xdot1ConfigProtocolTxEnable"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpV2Xdot1ConfigVidUsageDigestTxEnable"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpV2Xdot1ConfigManVidTxEnable"))
)
if mibBuilder.loadTexts:
    lldpV2Xdot1ConfigGroup.setStatus("current")

lldpV2Xdot1LocSysGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 2, 2, 2)
)
lldpV2Xdot1LocSysGroup.setObjects(
      *(("LLDP-EXT-DOT1-V2-MIB", "lldpV2Xdot1LocPortVlanId"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpV2Xdot1LocProtoVlanSupported"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpV2Xdot1LocProtoVlanEnabled"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpV2Xdot1LocVlanName"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpV2Xdot1LocProtocolId"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpV2Xdot1LocVidUsageDigest"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpV2Xdot1LocManVid"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpV2Xdot1LocLinkAggStatus"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpV2Xdot1LocLinkAggPortId"))
)
if mibBuilder.loadTexts:
    lldpV2Xdot1LocSysGroup.setStatus("current")

lldpV2Xdot1RemSysGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 2, 2, 3)
)
lldpV2Xdot1RemSysGroup.setObjects(
      *(("LLDP-EXT-DOT1-V2-MIB", "lldpV2Xdot1RemPortVlanId"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpV2Xdot1RemProtoVlanSupported"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpV2Xdot1RemProtoVlanEnabled"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpV2Xdot1RemVlanName"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpV2Xdot1RemProtocolId"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpV2Xdot1RemVidUsageDigest"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpV2Xdot1RemManVid"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpV2Xdot1RemLinkAggStatus"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpV2Xdot1RemLinkAggPortId"))
)
if mibBuilder.loadTexts:
    lldpV2Xdot1RemSysGroup.setStatus("deprecated")

lldpV2Xdot1RemSysV2Group = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 2, 2, 4)
)
lldpV2Xdot1RemSysV2Group.setObjects(
      *(("LLDP-EXT-DOT1-V2-MIB", "lldpV2Xdot1RemPortVlanId"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpV2Xdot1RemProtoVlanSupported"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpV2Xdot1RemProtoVlanEnabled"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpV2Xdot1RemVlanName"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpV2Xdot1RemProtocolId"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpV2Xdot1RemVidUsageDigestV2"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpV2Xdot1RemManVidV2"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpV2Xdot1RemLinkAggStatus"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpV2Xdot1RemLinkAggPortId"))
)
if mibBuilder.loadTexts:
    lldpV2Xdot1RemSysV2Group.setStatus("current")

lldpXdot1CnGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 4, 2, 1)
)
lldpXdot1CnGroup.setObjects(
      *(("LLDP-EXT-DOT1-V2-MIB", "lldpXdot1CnConfigCnTxEnable"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpV2Xdot1LocCNPVIndicators"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpV2Xdot1LocReadyIndicators"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpV2Xdot1RemCNPVIndicators"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpV2Xdot1RemReadyIndicators"))
)
if mibBuilder.loadTexts:
    lldpXdot1CnGroup.setStatus("current")

lldpXdot1dcbxETSGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 6, 2, 1)
)
lldpXdot1dcbxETSGroup.setObjects(
      *(("LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxConfigETSConfigurationTxEnable"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxConfigETSRecommendationTxEnable"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxLocETSConCreditBasedShaperSupport"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxLocETSConTrafficClassesSupported"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxLocETSConWilling"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxLocETSConPriTrafficClass"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxLocETSConTrafficClassBandwidth"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxLocETSConTrafficSelectionAlgorithm"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxLocETSRecoTrafficClassBandwidth"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithm"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxRemETSConCreditBasedShaperSupport"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxRemETSConTrafficClassesSupported"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxRemETSConWilling"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxRemETSConPriTrafficClass"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxRemETSConTrafficClassBandwidth"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxRemETSConTrafficSelectionAlgorithm"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxRemETSRecoTrafficClassBandwidth"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithm"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxAdminETSConCreditBasedShaperSupport"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxAdminETSConTrafficClassesSupported"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxAdminETSConWilling"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxAdminETSConPriTrafficClass"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxAdminETSConTrafficClassBandwidth"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxAdminETSConTrafficSelectionAlgorithm"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxAdminETSRecoTrafficClassBandwidth"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithm"))
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxETSGroup.setStatus("current")

lldpXdot1dcbxPFCGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 6, 2, 2)
)
lldpXdot1dcbxPFCGroup.setObjects(
      *(("LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxConfigPFCTxEnable"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxLocPFCWilling"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxLocPFCMBC"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxLocPFCCap"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxLocPFCEnableEnabled"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxRemPFCWilling"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxRemPFCMBC"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxRemPFCCap"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxRemPFCEnableEnabled"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxAdminPFCWilling"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxAdminPFCMBC"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxAdminPFCCap"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxAdminPFCEnableEnabled"))
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxPFCGroup.setStatus("current")

lldpXdot1dcbxApplicationPriorityGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 6, 2, 3)
)
lldpXdot1dcbxApplicationPriorityGroup.setObjects(
      *(("LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxConfigApplicationPriorityTxEnable"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxLocApplicationPriorityAEPriority"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxRemApplicationPriorityAEPriority"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxAdminApplicationPriorityAEPriority"))
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxApplicationPriorityGroup.setStatus("current")

lldpXdot1dcbxApplicationVlanGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 6, 2, 4)
)
lldpXdot1dcbxApplicationVlanGroup.setObjects(
      *(("LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxConfigApplicationVlanTxEnable"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxLocApplicationVlanAEVlanId"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxRemApplicationVlanAEVlanId"),
        ("LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxAdminApplicationVlanAEVlanId"))
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxApplicationVlanGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lldpV2Xdot1TxRxCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 2, 1, 1)
)
if mibBuilder.loadTexts:
    lldpV2Xdot1TxRxCompliance.setStatus(
        "current"
    )

lldpV2Xdot1TxCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 2, 1, 2)
)
if mibBuilder.loadTexts:
    lldpV2Xdot1TxCompliance.setStatus(
        "current"
    )

lldpV2Xdot1RxCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 2, 1, 3)
)
if mibBuilder.loadTexts:
    lldpV2Xdot1RxCompliance.setStatus(
        "deprecated"
    )

lldpV2Xdot1RxComplianceV2 = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 2, 1, 4)
)
if mibBuilder.loadTexts:
    lldpV2Xdot1RxComplianceV2.setStatus(
        "current"
    )

lldpXdot1CnCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 4, 1, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1CnCompliance.setStatus(
        "current"
    )

lldpXdot1dcbxCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 6, 1, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LLDP-EXT-DOT1-V2-MIB",
    **{"LldpV2XLinkAggStatusMap": LldpV2XLinkAggStatusMap,
       "LldpV2CnBitVector": LldpV2CnBitVector,
       "LldpXdot1dcbxTrafficClassValue": LldpXdot1dcbxTrafficClassValue,
       "LldpXdot1dcbxTrafficClassBandwidthValue": LldpXdot1dcbxTrafficClassBandwidthValue,
       "LldpXdot1dcbxAppSelector": LldpXdot1dcbxAppSelector,
       "LldpXdot1dcbxAppProtocol": LldpXdot1dcbxAppProtocol,
       "LldpXdot1dcbxSupportedCapacity": LldpXdot1dcbxSupportedCapacity,
       "LldpXdot1dcbxTrafficSelectionAlgorithm": LldpXdot1dcbxTrafficSelectionAlgorithm,
       "lldpV2Xdot1MIB": lldpV2Xdot1MIB,
       "lldpV2Xdot1Objects": lldpV2Xdot1Objects,
       "lldpV2Xdot1Config": lldpV2Xdot1Config,
       "lldpV2Xdot1ConfigPortVlanTable": lldpV2Xdot1ConfigPortVlanTable,
       "lldpV2Xdot1ConfigPortVlanEntry": lldpV2Xdot1ConfigPortVlanEntry,
       "lldpV2Xdot1ConfigPortVlanTxEnable": lldpV2Xdot1ConfigPortVlanTxEnable,
       "lldpV2Xdot1ConfigVlanNameTable": lldpV2Xdot1ConfigVlanNameTable,
       "lldpV2Xdot1ConfigVlanNameEntry": lldpV2Xdot1ConfigVlanNameEntry,
       "lldpV2Xdot1ConfigVlanNameTxEnable": lldpV2Xdot1ConfigVlanNameTxEnable,
       "lldpV2Xdot1ConfigProtoVlanTable": lldpV2Xdot1ConfigProtoVlanTable,
       "lldpV2Xdot1ConfigProtoVlanEntry": lldpV2Xdot1ConfigProtoVlanEntry,
       "lldpV2Xdot1ConfigProtoVlanTxEnable": lldpV2Xdot1ConfigProtoVlanTxEnable,
       "lldpV2Xdot1ConfigProtocolTable": lldpV2Xdot1ConfigProtocolTable,
       "lldpV2Xdot1ConfigProtocolEntry": lldpV2Xdot1ConfigProtocolEntry,
       "lldpV2Xdot1ConfigProtocolTxEnable": lldpV2Xdot1ConfigProtocolTxEnable,
       "lldpV2Xdot1ConfigVidUsageDigestTable": lldpV2Xdot1ConfigVidUsageDigestTable,
       "lldpV2Xdot1ConfigVidUsageDigestEntry": lldpV2Xdot1ConfigVidUsageDigestEntry,
       "lldpV2Xdot1ConfigVidUsageDigestTxEnable": lldpV2Xdot1ConfigVidUsageDigestTxEnable,
       "lldpV2Xdot1ConfigManVidTable": lldpV2Xdot1ConfigManVidTable,
       "lldpV2Xdot1ConfigManVidEntry": lldpV2Xdot1ConfigManVidEntry,
       "lldpV2Xdot1ConfigManVidTxEnable": lldpV2Xdot1ConfigManVidTxEnable,
       "lldpV2Xdot1LocalData": lldpV2Xdot1LocalData,
       "lldpV2Xdot1LocTable": lldpV2Xdot1LocTable,
       "lldpV2Xdot1LocEntry": lldpV2Xdot1LocEntry,
       "lldpV2Xdot1LocPortVlanId": lldpV2Xdot1LocPortVlanId,
       "lldpV2Xdot1LocProtoVlanTable": lldpV2Xdot1LocProtoVlanTable,
       "lldpV2Xdot1LocProtoVlanEntry": lldpV2Xdot1LocProtoVlanEntry,
       "lldpV2Xdot1LocProtoVlanId": lldpV2Xdot1LocProtoVlanId,
       "lldpV2Xdot1LocProtoVlanSupported": lldpV2Xdot1LocProtoVlanSupported,
       "lldpV2Xdot1LocProtoVlanEnabled": lldpV2Xdot1LocProtoVlanEnabled,
       "lldpV2Xdot1LocVlanNameTable": lldpV2Xdot1LocVlanNameTable,
       "lldpV2Xdot1LocVlanNameEntry": lldpV2Xdot1LocVlanNameEntry,
       "lldpV2Xdot1LocVlanId": lldpV2Xdot1LocVlanId,
       "lldpV2Xdot1LocVlanName": lldpV2Xdot1LocVlanName,
       "lldpV2Xdot1LocProtocolTable": lldpV2Xdot1LocProtocolTable,
       "lldpV2Xdot1LocProtocolEntry": lldpV2Xdot1LocProtocolEntry,
       "lldpV2Xdot1LocProtocolIndex": lldpV2Xdot1LocProtocolIndex,
       "lldpV2Xdot1LocProtocolId": lldpV2Xdot1LocProtocolId,
       "lldpV2Xdot1LocVidUsageDigestTable": lldpV2Xdot1LocVidUsageDigestTable,
       "lldpV2Xdot1LocVidUsageDigestEntry": lldpV2Xdot1LocVidUsageDigestEntry,
       "lldpV2Xdot1LocVidUsageDigest": lldpV2Xdot1LocVidUsageDigest,
       "lldpV2Xdot1LocManVidTable": lldpV2Xdot1LocManVidTable,
       "lldpV2Xdot1LocManVidEntry": lldpV2Xdot1LocManVidEntry,
       "lldpV2Xdot1LocManVid": lldpV2Xdot1LocManVid,
       "lldpV2Xdot1LocLinkAggTable": lldpV2Xdot1LocLinkAggTable,
       "lldpV2Xdot1LocLinkAggEntry": lldpV2Xdot1LocLinkAggEntry,
       "lldpV2Xdot1LocLinkAggStatus": lldpV2Xdot1LocLinkAggStatus,
       "lldpV2Xdot1LocLinkAggPortId": lldpV2Xdot1LocLinkAggPortId,
       "lldpV2Xdot1RemoteData": lldpV2Xdot1RemoteData,
       "lldpV2Xdot1RemTable": lldpV2Xdot1RemTable,
       "lldpV2Xdot1RemEntry": lldpV2Xdot1RemEntry,
       "lldpV2Xdot1RemPortVlanId": lldpV2Xdot1RemPortVlanId,
       "lldpV2Xdot1RemProtoVlanTable": lldpV2Xdot1RemProtoVlanTable,
       "lldpV2Xdot1RemProtoVlanEntry": lldpV2Xdot1RemProtoVlanEntry,
       "lldpV2Xdot1RemProtoVlanId": lldpV2Xdot1RemProtoVlanId,
       "lldpV2Xdot1RemProtoVlanSupported": lldpV2Xdot1RemProtoVlanSupported,
       "lldpV2Xdot1RemProtoVlanEnabled": lldpV2Xdot1RemProtoVlanEnabled,
       "lldpV2Xdot1RemVlanNameTable": lldpV2Xdot1RemVlanNameTable,
       "lldpV2Xdot1RemVlanNameEntry": lldpV2Xdot1RemVlanNameEntry,
       "lldpV2Xdot1RemVlanId": lldpV2Xdot1RemVlanId,
       "lldpV2Xdot1RemVlanName": lldpV2Xdot1RemVlanName,
       "lldpV2Xdot1RemProtocolTable": lldpV2Xdot1RemProtocolTable,
       "lldpV2Xdot1RemProtocolEntry": lldpV2Xdot1RemProtocolEntry,
       "lldpV2Xdot1RemProtocolIndex": lldpV2Xdot1RemProtocolIndex,
       "lldpV2Xdot1RemProtocolId": lldpV2Xdot1RemProtocolId,
       "lldpV2Xdot1RemVidUsageDigestTable": lldpV2Xdot1RemVidUsageDigestTable,
       "lldpV2Xdot1RemVidUsageDigestEntry": lldpV2Xdot1RemVidUsageDigestEntry,
       "lldpV2Xdot1RemVidUsageDigest": lldpV2Xdot1RemVidUsageDigest,
       "lldpV2Xdot1RemManVidTable": lldpV2Xdot1RemManVidTable,
       "lldpV2Xdot1RemManVidEntry": lldpV2Xdot1RemManVidEntry,
       "lldpV2Xdot1RemManVid": lldpV2Xdot1RemManVid,
       "lldpV2Xdot1RemLinkAggTable": lldpV2Xdot1RemLinkAggTable,
       "lldpV2Xdot1RemLinkAggEntry": lldpV2Xdot1RemLinkAggEntry,
       "lldpV2Xdot1RemLinkAggStatus": lldpV2Xdot1RemLinkAggStatus,
       "lldpV2Xdot1RemLinkAggPortId": lldpV2Xdot1RemLinkAggPortId,
       "lldpV2Xdot1RemVidUsageDigestV2Table": lldpV2Xdot1RemVidUsageDigestV2Table,
       "lldpV2Xdot1RemVidUsageDigestV2Entry": lldpV2Xdot1RemVidUsageDigestV2Entry,
       "lldpV2Xdot1RemVidUsageDigestV2": lldpV2Xdot1RemVidUsageDigestV2,
       "lldpV2Xdot1RemManVidV2Table": lldpV2Xdot1RemManVidV2Table,
       "lldpV2Xdot1RemManVidV2Entry": lldpV2Xdot1RemManVidV2Entry,
       "lldpV2Xdot1RemManVidV2": lldpV2Xdot1RemManVidV2,
       "lldpV2Xdot1Conformance": lldpV2Xdot1Conformance,
       "lldpV2Xdot1Compliances": lldpV2Xdot1Compliances,
       "lldpV2Xdot1TxRxCompliance": lldpV2Xdot1TxRxCompliance,
       "lldpV2Xdot1TxCompliance": lldpV2Xdot1TxCompliance,
       "lldpV2Xdot1RxCompliance": lldpV2Xdot1RxCompliance,
       "lldpV2Xdot1RxComplianceV2": lldpV2Xdot1RxComplianceV2,
       "lldpV2Xdot1Groups": lldpV2Xdot1Groups,
       "lldpV2Xdot1ConfigGroup": lldpV2Xdot1ConfigGroup,
       "lldpV2Xdot1LocSysGroup": lldpV2Xdot1LocSysGroup,
       "lldpV2Xdot1RemSysGroup": lldpV2Xdot1RemSysGroup,
       "lldpV2Xdot1RemSysV2Group": lldpV2Xdot1RemSysV2Group,
       "lldpXdot1CnMIB": lldpXdot1CnMIB,
       "lldpXdot1CnObjects": lldpXdot1CnObjects,
       "lldpXdot1CnConfig": lldpXdot1CnConfig,
       "lldpXdot1CnConfigCnTable": lldpXdot1CnConfigCnTable,
       "lldpXdot1CnConfigCnEntry": lldpXdot1CnConfigCnEntry,
       "lldpXdot1CnConfigCnTxEnable": lldpXdot1CnConfigCnTxEnable,
       "lldpXdot1CnLocalData": lldpXdot1CnLocalData,
       "lldpV2Xdot1LocCnTable": lldpV2Xdot1LocCnTable,
       "lldpV2Xdot1LocCnEntry": lldpV2Xdot1LocCnEntry,
       "lldpV2Xdot1LocCNPVIndicators": lldpV2Xdot1LocCNPVIndicators,
       "lldpV2Xdot1LocReadyIndicators": lldpV2Xdot1LocReadyIndicators,
       "lldpXdot1CnRemoteData": lldpXdot1CnRemoteData,
       "lldpV2Xdot1RemCnTable": lldpV2Xdot1RemCnTable,
       "lldpV2Xdot1RemCnEntry": lldpV2Xdot1RemCnEntry,
       "lldpV2Xdot1RemCNPVIndicators": lldpV2Xdot1RemCNPVIndicators,
       "lldpV2Xdot1RemReadyIndicators": lldpV2Xdot1RemReadyIndicators,
       "lldpXdot1CnConformance": lldpXdot1CnConformance,
       "lldpXdot1CnCompliances": lldpXdot1CnCompliances,
       "lldpXdot1CnCompliance": lldpXdot1CnCompliance,
       "lldpXdot1CnGroups": lldpXdot1CnGroups,
       "lldpXdot1CnGroup": lldpXdot1CnGroup,
       "lldpXdot1dcbxMIB": lldpXdot1dcbxMIB,
       "lldpXdot1dcbxObjects": lldpXdot1dcbxObjects,
       "lldpXdot1dcbxConfig": lldpXdot1dcbxConfig,
       "lldpXdot1dcbxConfigETSConfigurationTable": lldpXdot1dcbxConfigETSConfigurationTable,
       "lldpXdot1dcbxConfigETSConfigurationEntry": lldpXdot1dcbxConfigETSConfigurationEntry,
       "lldpXdot1dcbxConfigETSConfigurationTxEnable": lldpXdot1dcbxConfigETSConfigurationTxEnable,
       "lldpXdot1dcbxConfigETSRecommendationTable": lldpXdot1dcbxConfigETSRecommendationTable,
       "lldpXdot1dcbxConfigETSRecommendationEntry": lldpXdot1dcbxConfigETSRecommendationEntry,
       "lldpXdot1dcbxConfigETSRecommendationTxEnable": lldpXdot1dcbxConfigETSRecommendationTxEnable,
       "lldpXdot1dcbxConfigPFCTable": lldpXdot1dcbxConfigPFCTable,
       "lldpXdot1dcbxConfigPFCEntry": lldpXdot1dcbxConfigPFCEntry,
       "lldpXdot1dcbxConfigPFCTxEnable": lldpXdot1dcbxConfigPFCTxEnable,
       "lldpXdot1dcbxConfigApplicationPriorityTable": lldpXdot1dcbxConfigApplicationPriorityTable,
       "lldpXdot1dcbxConfigApplicationPriorityEntry": lldpXdot1dcbxConfigApplicationPriorityEntry,
       "lldpXdot1dcbxConfigApplicationPriorityTxEnable": lldpXdot1dcbxConfigApplicationPriorityTxEnable,
       "lldpXdot1dcbxConfigApplicationVlanTable": lldpXdot1dcbxConfigApplicationVlanTable,
       "lldpXdot1dcbxConfigApplicationVlanEntry": lldpXdot1dcbxConfigApplicationVlanEntry,
       "lldpXdot1dcbxConfigApplicationVlanTxEnable": lldpXdot1dcbxConfigApplicationVlanTxEnable,
       "lldpXdot1dcbxLocalData": lldpXdot1dcbxLocalData,
       "lldpXdot1dcbxLocETSConfiguration": lldpXdot1dcbxLocETSConfiguration,
       "lldpXdot1dcbxLocETSBasicConfigurationTable": lldpXdot1dcbxLocETSBasicConfigurationTable,
       "lldpXdot1dcbxLocETSBasicConfigurationEntry": lldpXdot1dcbxLocETSBasicConfigurationEntry,
       "lldpXdot1dcbxLocETSConCreditBasedShaperSupport": lldpXdot1dcbxLocETSConCreditBasedShaperSupport,
       "lldpXdot1dcbxLocETSConTrafficClassesSupported": lldpXdot1dcbxLocETSConTrafficClassesSupported,
       "lldpXdot1dcbxLocETSConWilling": lldpXdot1dcbxLocETSConWilling,
       "lldpXdot1dcbxLocETSConPriorityAssignmentTable": lldpXdot1dcbxLocETSConPriorityAssignmentTable,
       "lldpXdot1dcbxLocETSConPriorityAssignmentEntry": lldpXdot1dcbxLocETSConPriorityAssignmentEntry,
       "lldpXdot1dcbxLocETSConPriority": lldpXdot1dcbxLocETSConPriority,
       "lldpXdot1dcbxLocETSConPriTrafficClass": lldpXdot1dcbxLocETSConPriTrafficClass,
       "lldpXdot1dcbxLocETSConTrafficClassBandwidthTable": lldpXdot1dcbxLocETSConTrafficClassBandwidthTable,
       "lldpXdot1dcbxLocETSConTrafficClassBandwidthEntry": lldpXdot1dcbxLocETSConTrafficClassBandwidthEntry,
       "lldpXdot1dcbxLocETSConTrafficClass": lldpXdot1dcbxLocETSConTrafficClass,
       "lldpXdot1dcbxLocETSConTrafficClassBandwidth": lldpXdot1dcbxLocETSConTrafficClassBandwidth,
       "lldpXdot1dcbxLocETSConTrafficSelectionAlgorithmTable": lldpXdot1dcbxLocETSConTrafficSelectionAlgorithmTable,
       "lldpXdot1dcbxLocETSConTrafficSelectionAlgorithmEntry": lldpXdot1dcbxLocETSConTrafficSelectionAlgorithmEntry,
       "lldpXdot1dcbxLocETSConTSATrafficClass": lldpXdot1dcbxLocETSConTSATrafficClass,
       "lldpXdot1dcbxLocETSConTrafficSelectionAlgorithm": lldpXdot1dcbxLocETSConTrafficSelectionAlgorithm,
       "lldpXdot1dcbxLocETSReco": lldpXdot1dcbxLocETSReco,
       "lldpXdot1dcbxLocETSRecoTrafficClassBandwidthTable": lldpXdot1dcbxLocETSRecoTrafficClassBandwidthTable,
       "lldpXdot1dcbxLocETSRecoTrafficClassBandwidthEntry": lldpXdot1dcbxLocETSRecoTrafficClassBandwidthEntry,
       "lldpXdot1dcbxLocETSRecoTrafficClass": lldpXdot1dcbxLocETSRecoTrafficClass,
       "lldpXdot1dcbxLocETSRecoTrafficClassBandwidth": lldpXdot1dcbxLocETSRecoTrafficClassBandwidth,
       "lldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithmTable": lldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithmTable,
       "lldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithmEntry": lldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithmEntry,
       "lldpXdot1dcbxLocETSRecoTSATrafficClass": lldpXdot1dcbxLocETSRecoTSATrafficClass,
       "lldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithm": lldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithm,
       "lldpXdot1dcbxLocPFC": lldpXdot1dcbxLocPFC,
       "lldpXdot1dcbxLocPFCBasicTable": lldpXdot1dcbxLocPFCBasicTable,
       "lldpXdot1dcbxLocPFCBasicEntry": lldpXdot1dcbxLocPFCBasicEntry,
       "lldpXdot1dcbxLocPFCWilling": lldpXdot1dcbxLocPFCWilling,
       "lldpXdot1dcbxLocPFCMBC": lldpXdot1dcbxLocPFCMBC,
       "lldpXdot1dcbxLocPFCCap": lldpXdot1dcbxLocPFCCap,
       "lldpXdot1dcbxLocPFCEnableTable": lldpXdot1dcbxLocPFCEnableTable,
       "lldpXdot1dcbxLocPFCEnableEntry": lldpXdot1dcbxLocPFCEnableEntry,
       "lldpXdot1dcbxLocPFCEnablePriority": lldpXdot1dcbxLocPFCEnablePriority,
       "lldpXdot1dcbxLocPFCEnableEnabled": lldpXdot1dcbxLocPFCEnableEnabled,
       "lldpXdot1dcbxLocApplicationPriorityAppTable": lldpXdot1dcbxLocApplicationPriorityAppTable,
       "lldpXdot1dcbxLocApplicationPriorityAppEntry": lldpXdot1dcbxLocApplicationPriorityAppEntry,
       "lldpXdot1dcbxLocApplicationPriorityAESelector": lldpXdot1dcbxLocApplicationPriorityAESelector,
       "lldpXdot1dcbxLocApplicationPriorityAEProtocol": lldpXdot1dcbxLocApplicationPriorityAEProtocol,
       "lldpXdot1dcbxLocApplicationPriorityAEPriority": lldpXdot1dcbxLocApplicationPriorityAEPriority,
       "lldpXdot1dcbxLocApplicationVlanAppTable": lldpXdot1dcbxLocApplicationVlanAppTable,
       "lldpXdot1dcbxLocApplicationVlanAppEntry": lldpXdot1dcbxLocApplicationVlanAppEntry,
       "lldpXdot1dcbxLocApplicationVlanAESelector": lldpXdot1dcbxLocApplicationVlanAESelector,
       "lldpXdot1dcbxLocApplicationVlanAEProtocol": lldpXdot1dcbxLocApplicationVlanAEProtocol,
       "lldpXdot1dcbxLocApplicationVlanAEVlanId": lldpXdot1dcbxLocApplicationVlanAEVlanId,
       "lldpXdot1dcbxRemoteData": lldpXdot1dcbxRemoteData,
       "lldpXdot1dcbxRemETSConfiguration": lldpXdot1dcbxRemETSConfiguration,
       "lldpXdot1dcbxRemETSBasicConfigurationTable": lldpXdot1dcbxRemETSBasicConfigurationTable,
       "lldpXdot1dcbxRemETSBasicConfigurationEntry": lldpXdot1dcbxRemETSBasicConfigurationEntry,
       "lldpXdot1dcbxRemETSConCreditBasedShaperSupport": lldpXdot1dcbxRemETSConCreditBasedShaperSupport,
       "lldpXdot1dcbxRemETSConTrafficClassesSupported": lldpXdot1dcbxRemETSConTrafficClassesSupported,
       "lldpXdot1dcbxRemETSConWilling": lldpXdot1dcbxRemETSConWilling,
       "lldpXdot1dcbxRemETSConPriorityAssignmentTable": lldpXdot1dcbxRemETSConPriorityAssignmentTable,
       "lldpXdot1dcbxRemETSConPriorityAssignmentEntry": lldpXdot1dcbxRemETSConPriorityAssignmentEntry,
       "lldpXdot1dcbxRemETSConPriority": lldpXdot1dcbxRemETSConPriority,
       "lldpXdot1dcbxRemETSConPriTrafficClass": lldpXdot1dcbxRemETSConPriTrafficClass,
       "lldpXdot1dcbxRemETSConTrafficClassBandwidthTable": lldpXdot1dcbxRemETSConTrafficClassBandwidthTable,
       "lldpXdot1dcbxRemETSConTrafficClassBandwidthEntry": lldpXdot1dcbxRemETSConTrafficClassBandwidthEntry,
       "lldpXdot1dcbxRemETSConTrafficClass": lldpXdot1dcbxRemETSConTrafficClass,
       "lldpXdot1dcbxRemETSConTrafficClassBandwidth": lldpXdot1dcbxRemETSConTrafficClassBandwidth,
       "lldpXdot1dcbxRemETSConTrafficSelectionAlgorithmTable": lldpXdot1dcbxRemETSConTrafficSelectionAlgorithmTable,
       "lldpXdot1dcbxRemETSConTrafficSelectionAlgorithmEntry": lldpXdot1dcbxRemETSConTrafficSelectionAlgorithmEntry,
       "lldpXdot1dcbxRemETSConTSATrafficClass": lldpXdot1dcbxRemETSConTSATrafficClass,
       "lldpXdot1dcbxRemETSConTrafficSelectionAlgorithm": lldpXdot1dcbxRemETSConTrafficSelectionAlgorithm,
       "lldpXdot1dcbxRemETSReco": lldpXdot1dcbxRemETSReco,
       "lldpXdot1dcbxRemETSRecoTrafficClassBandwidthTable": lldpXdot1dcbxRemETSRecoTrafficClassBandwidthTable,
       "lldpXdot1dcbxRemETSRecoTrafficClassBandwidthEntry": lldpXdot1dcbxRemETSRecoTrafficClassBandwidthEntry,
       "lldpXdot1dcbxRemETSRecoTrafficClass": lldpXdot1dcbxRemETSRecoTrafficClass,
       "lldpXdot1dcbxRemETSRecoTrafficClassBandwidth": lldpXdot1dcbxRemETSRecoTrafficClassBandwidth,
       "lldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithmTable": lldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithmTable,
       "lldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithmEntry": lldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithmEntry,
       "lldpXdot1dcbxRemETSRecoTSATrafficClass": lldpXdot1dcbxRemETSRecoTSATrafficClass,
       "lldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithm": lldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithm,
       "lldpXdot1dcbxRemPFC": lldpXdot1dcbxRemPFC,
       "lldpXdot1dcbxRemPFCBasicTable": lldpXdot1dcbxRemPFCBasicTable,
       "lldpXdot1dcbxRemPFCBasicEntry": lldpXdot1dcbxRemPFCBasicEntry,
       "lldpXdot1dcbxRemPFCWilling": lldpXdot1dcbxRemPFCWilling,
       "lldpXdot1dcbxRemPFCMBC": lldpXdot1dcbxRemPFCMBC,
       "lldpXdot1dcbxRemPFCCap": lldpXdot1dcbxRemPFCCap,
       "lldpXdot1dcbxRemPFCEnableTable": lldpXdot1dcbxRemPFCEnableTable,
       "lldpXdot1dcbxRemPFCEnableEntry": lldpXdot1dcbxRemPFCEnableEntry,
       "lldpXdot1dcbxRemPFCEnablePriority": lldpXdot1dcbxRemPFCEnablePriority,
       "lldpXdot1dcbxRemPFCEnableEnabled": lldpXdot1dcbxRemPFCEnableEnabled,
       "lldpXdot1dcbxRemApplicationPriorityAppTable": lldpXdot1dcbxRemApplicationPriorityAppTable,
       "lldpXdot1dcbxRemApplicationPriorityAppEntry": lldpXdot1dcbxRemApplicationPriorityAppEntry,
       "lldpXdot1dcbxRemApplicationPriorityAESelector": lldpXdot1dcbxRemApplicationPriorityAESelector,
       "lldpXdot1dcbxRemApplicationPriorityAEProtocol": lldpXdot1dcbxRemApplicationPriorityAEProtocol,
       "lldpXdot1dcbxRemApplicationPriorityAEPriority": lldpXdot1dcbxRemApplicationPriorityAEPriority,
       "lldpXdot1dcbxRemApplicationVlanAppTable": lldpXdot1dcbxRemApplicationVlanAppTable,
       "lldpXdot1dcbxRemApplicationVlanAppEntry": lldpXdot1dcbxRemApplicationVlanAppEntry,
       "lldpXdot1dcbxRemApplicationVlanAESelector": lldpXdot1dcbxRemApplicationVlanAESelector,
       "lldpXdot1dcbxRemApplicationVlanAEProtocol": lldpXdot1dcbxRemApplicationVlanAEProtocol,
       "lldpXdot1dcbxRemApplicationVlanAEVlanId": lldpXdot1dcbxRemApplicationVlanAEVlanId,
       "lldpXdot1dcbxAdminData": lldpXdot1dcbxAdminData,
       "lldpXdot1dcbxAdminETSConfiguration": lldpXdot1dcbxAdminETSConfiguration,
       "lldpXdot1dcbxAdminETSBasicConfigurationTable": lldpXdot1dcbxAdminETSBasicConfigurationTable,
       "lldpXdot1dcbxAdminETSBasicConfigurationEntry": lldpXdot1dcbxAdminETSBasicConfigurationEntry,
       "lldpXdot1dcbxAdminETSConCreditBasedShaperSupport": lldpXdot1dcbxAdminETSConCreditBasedShaperSupport,
       "lldpXdot1dcbxAdminETSConTrafficClassesSupported": lldpXdot1dcbxAdminETSConTrafficClassesSupported,
       "lldpXdot1dcbxAdminETSConWilling": lldpXdot1dcbxAdminETSConWilling,
       "lldpXdot1dcbxAdminETSConPriorityAssignmentTable": lldpXdot1dcbxAdminETSConPriorityAssignmentTable,
       "lldpXdot1dcbxAdminETSConPriorityAssignmentEntry": lldpXdot1dcbxAdminETSConPriorityAssignmentEntry,
       "lldpXdot1dcbxAdminETSConPriority": lldpXdot1dcbxAdminETSConPriority,
       "lldpXdot1dcbxAdminETSConPriTrafficClass": lldpXdot1dcbxAdminETSConPriTrafficClass,
       "lldpXdot1dcbxAdminETSConTrafficClassBandwidthTable": lldpXdot1dcbxAdminETSConTrafficClassBandwidthTable,
       "lldpXdot1dcbxAdminETSConTrafficClassBandwidthEntry": lldpXdot1dcbxAdminETSConTrafficClassBandwidthEntry,
       "lldpXdot1dcbxAdminETSConTrafficClass": lldpXdot1dcbxAdminETSConTrafficClass,
       "lldpXdot1dcbxAdminETSConTrafficClassBandwidth": lldpXdot1dcbxAdminETSConTrafficClassBandwidth,
       "lldpXdot1dcbxAdminETSConTrafficSelectionAlgorithmTable": lldpXdot1dcbxAdminETSConTrafficSelectionAlgorithmTable,
       "lldpXdot1dcbxAdminETSConTrafficSelectionAlgorithmEntry": lldpXdot1dcbxAdminETSConTrafficSelectionAlgorithmEntry,
       "lldpXdot1dcbxAdminETSConTSATrafficClass": lldpXdot1dcbxAdminETSConTSATrafficClass,
       "lldpXdot1dcbxAdminETSConTrafficSelectionAlgorithm": lldpXdot1dcbxAdminETSConTrafficSelectionAlgorithm,
       "lldpXdot1dcbxAdminETSReco": lldpXdot1dcbxAdminETSReco,
       "lldpXdot1dcbxAdminETSRecoTrafficClassBandwidthTable": lldpXdot1dcbxAdminETSRecoTrafficClassBandwidthTable,
       "lldpXdot1dcbxAdminETSRecoTrafficClassBandwidthEntry": lldpXdot1dcbxAdminETSRecoTrafficClassBandwidthEntry,
       "lldpXdot1dcbxAdminETSRecoTrafficClass": lldpXdot1dcbxAdminETSRecoTrafficClass,
       "lldpXdot1dcbxAdminETSRecoTrafficClassBandwidth": lldpXdot1dcbxAdminETSRecoTrafficClassBandwidth,
       "lldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithmTable": lldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithmTable,
       "lldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithmEntry": lldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithmEntry,
       "lldpXdot1dcbxAdminETSRecoTSATrafficClass": lldpXdot1dcbxAdminETSRecoTSATrafficClass,
       "lldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithm": lldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithm,
       "lldpXdot1dcbxAdminPFC": lldpXdot1dcbxAdminPFC,
       "lldpXdot1dcbxAdminPFCBasicTable": lldpXdot1dcbxAdminPFCBasicTable,
       "lldpXdot1dcbxAdminPFCBasicEntry": lldpXdot1dcbxAdminPFCBasicEntry,
       "lldpXdot1dcbxAdminPFCWilling": lldpXdot1dcbxAdminPFCWilling,
       "lldpXdot1dcbxAdminPFCMBC": lldpXdot1dcbxAdminPFCMBC,
       "lldpXdot1dcbxAdminPFCCap": lldpXdot1dcbxAdminPFCCap,
       "lldpXdot1dcbxAdminPFCEnableTable": lldpXdot1dcbxAdminPFCEnableTable,
       "lldpXdot1dcbxAdminPFCEnableEntry": lldpXdot1dcbxAdminPFCEnableEntry,
       "lldpXdot1dcbxAdminPFCEnablePriority": lldpXdot1dcbxAdminPFCEnablePriority,
       "lldpXdot1dcbxAdminPFCEnableEnabled": lldpXdot1dcbxAdminPFCEnableEnabled,
       "lldpXdot1dcbxAdminApplicationPriorityAppTable": lldpXdot1dcbxAdminApplicationPriorityAppTable,
       "lldpXdot1dcbxAdminApplicationPriorityAppEntry": lldpXdot1dcbxAdminApplicationPriorityAppEntry,
       "lldpXdot1dcbxAdminApplicationPriorityAESelector": lldpXdot1dcbxAdminApplicationPriorityAESelector,
       "lldpXdot1dcbxAdminApplicationPriorityAEProtocol": lldpXdot1dcbxAdminApplicationPriorityAEProtocol,
       "lldpXdot1dcbxAdminApplicationPriorityAEPriority": lldpXdot1dcbxAdminApplicationPriorityAEPriority,
       "lldpXdot1dcbxAdminApplicationVlanAppTable": lldpXdot1dcbxAdminApplicationVlanAppTable,
       "lldpXdot1dcbxAdminApplicationVlanAppEntry": lldpXdot1dcbxAdminApplicationVlanAppEntry,
       "lldpXdot1dcbxAdminApplicationVlanAESelector": lldpXdot1dcbxAdminApplicationVlanAESelector,
       "lldpXdot1dcbxAdminApplicationVlanAEProtocol": lldpXdot1dcbxAdminApplicationVlanAEProtocol,
       "lldpXdot1dcbxAdminApplicationVlanAEVlanId": lldpXdot1dcbxAdminApplicationVlanAEVlanId,
       "lldpXdot1dcbxConformance": lldpXdot1dcbxConformance,
       "lldpXdot1dcbxCompliances": lldpXdot1dcbxCompliances,
       "lldpXdot1dcbxCompliance": lldpXdot1dcbxCompliance,
       "lldpXdot1dcbxGroups": lldpXdot1dcbxGroups,
       "lldpXdot1dcbxETSGroup": lldpXdot1dcbxETSGroup,
       "lldpXdot1dcbxPFCGroup": lldpXdot1dcbxPFCGroup,
       "lldpXdot1dcbxApplicationPriorityGroup": lldpXdot1dcbxApplicationPriorityGroup,
       "lldpXdot1dcbxApplicationVlanGroup": lldpXdot1dcbxApplicationVlanGroup}
)
