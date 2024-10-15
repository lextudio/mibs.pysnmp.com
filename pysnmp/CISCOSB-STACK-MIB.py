# SNMP MIB module (CISCOSB-STACK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCOSB-STACK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:14:55 2024
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

(MacAddress,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "MacAddress")

(switch001,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "switch001")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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

rlStack = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107)
)
rlStack.setRevisions(
        ("2005-04-14 00:00",)
)


# Types definitions



class StackMode(Integer32):
    """Custom type StackMode based on Integer32"""
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
        *(("advanced-hybrid", 4),
          ("advanced-hybrid-XG", 5),
          ("basic-hybrid", 3),
          ("native", 2),
          ("standalone", 1))
    )





class PortsPair(Integer32):
    """Custom type PortsPair based on Integer32"""
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
        *(("pair-lionXg", 5),
          ("pair-s1s2", 1),
          ("pair-s1s25G", 3),
          ("pair-s1s2Xg", 4),
          ("pair-s3s4", 2))
    )





class HybridStackPortSpeed(Integer32):
    """Custom type HybridStackPortSpeed based on Integer32"""
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
        *(("port-speed-10G", 3),
          ("port-speed-1G", 1),
          ("port-speed-5G", 2),
          ("port-speed-auto", 4),
          ("port-speed-down", 5))
    )





class HybridStackDeviceMode(Integer32):
    """Custom type HybridStackDeviceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mode-L2", 1),
          ("mode-L3", 2))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlStackActiveUnitIdTable_Object = MibTable
rlStackActiveUnitIdTable = _RlStackActiveUnitIdTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 1)
)
if mibBuilder.loadTexts:
    rlStackActiveUnitIdTable.setStatus("current")
_RlStackActiveUnitIdEntry_Object = MibTableRow
rlStackActiveUnitIdEntry = _RlStackActiveUnitIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 1, 1)
)
rlStackActiveUnitIdEntry.setIndexNames(
    (0, "CISCOSB-STACK-MIB", "rlStackCurrentUnitId"),
)
if mibBuilder.loadTexts:
    rlStackActiveUnitIdEntry.setStatus("current")
_RlStackCurrentUnitId_Type = Integer32
_RlStackCurrentUnitId_Object = MibTableColumn
rlStackCurrentUnitId = _RlStackCurrentUnitId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 1, 1, 1),
    _RlStackCurrentUnitId_Type()
)
rlStackCurrentUnitId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlStackCurrentUnitId.setStatus("current")


class _RlStackActiveUnitIdAfterReset_Type(Integer32):
    """Custom type rlStackActiveUnitIdAfterReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RlStackActiveUnitIdAfterReset_Type.__name__ = "Integer32"
_RlStackActiveUnitIdAfterReset_Object = MibTableColumn
rlStackActiveUnitIdAfterReset = _RlStackActiveUnitIdAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 1, 1, 2),
    _RlStackActiveUnitIdAfterReset_Type()
)
rlStackActiveUnitIdAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStackActiveUnitIdAfterReset.setStatus("current")


class _RlStackUnitModeAfterReset_Type(Integer32):
    """Custom type rlStackUnitModeAfterReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stack", 2),
          ("standalone", 1))
    )


_RlStackUnitModeAfterReset_Type.__name__ = "Integer32"
_RlStackUnitModeAfterReset_Object = MibScalar
rlStackUnitModeAfterReset = _RlStackUnitModeAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 2),
    _RlStackUnitModeAfterReset_Type()
)
rlStackUnitModeAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStackUnitModeAfterReset.setStatus("current")


class _RlStackUnitMode_Type(Integer32):
    """Custom type rlStackUnitMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stack", 2),
          ("standalone", 1))
    )


_RlStackUnitMode_Type.__name__ = "Integer32"
_RlStackUnitMode_Object = MibScalar
rlStackUnitMode = _RlStackUnitMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 3),
    _RlStackUnitMode_Type()
)
rlStackUnitMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStackUnitMode.setStatus("current")
_RlStackUnitMacAddressAfterReset_Type = MacAddress
_RlStackUnitMacAddressAfterReset_Object = MibScalar
rlStackUnitMacAddressAfterReset = _RlStackUnitMacAddressAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 4),
    _RlStackUnitMacAddressAfterReset_Type()
)
rlStackUnitMacAddressAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStackUnitMacAddressAfterReset.setStatus("current")
_RlStackHybridTable_Object = MibTable
rlStackHybridTable = _RlStackHybridTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5)
)
if mibBuilder.loadTexts:
    rlStackHybridTable.setStatus("current")
_RlStackHybridEntry_Object = MibTableRow
rlStackHybridEntry = _RlStackHybridEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1)
)
rlStackHybridEntry.setIndexNames(
    (0, "CISCOSB-STACK-MIB", "rlStackHybridUnitId"),
)
if mibBuilder.loadTexts:
    rlStackHybridEntry.setStatus("current")


class _RlStackHybridUnitId_Type(Integer32):
    """Custom type rlStackHybridUnitId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RlStackHybridUnitId_Type.__name__ = "Integer32"
_RlStackHybridUnitId_Object = MibTableColumn
rlStackHybridUnitId = _RlStackHybridUnitId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1, 1),
    _RlStackHybridUnitId_Type()
)
rlStackHybridUnitId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlStackHybridUnitId.setStatus("current")
_RlStackHybridStackMode_Type = StackMode
_RlStackHybridStackMode_Object = MibTableColumn
rlStackHybridStackMode = _RlStackHybridStackMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1, 2),
    _RlStackHybridStackMode_Type()
)
rlStackHybridStackMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStackHybridStackMode.setStatus("current")
_RlStackHybridPortsPair_Type = PortsPair
_RlStackHybridPortsPair_Object = MibTableColumn
rlStackHybridPortsPair = _RlStackHybridPortsPair_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1, 3),
    _RlStackHybridPortsPair_Type()
)
rlStackHybridPortsPair.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStackHybridPortsPair.setStatus("current")
_RlStackHybridPortNo1speed_Type = HybridStackPortSpeed
_RlStackHybridPortNo1speed_Object = MibTableColumn
rlStackHybridPortNo1speed = _RlStackHybridPortNo1speed_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1, 4),
    _RlStackHybridPortNo1speed_Type()
)
rlStackHybridPortNo1speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStackHybridPortNo1speed.setStatus("current")
_RlStackHybridPortNo2speed_Type = HybridStackPortSpeed
_RlStackHybridPortNo2speed_Object = MibTableColumn
rlStackHybridPortNo2speed = _RlStackHybridPortNo2speed_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1, 5),
    _RlStackHybridPortNo2speed_Type()
)
rlStackHybridPortNo2speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStackHybridPortNo2speed.setStatus("current")


class _RlStackHybridUnitIdAfterReset_Type(Integer32):
    """Custom type rlStackHybridUnitIdAfterReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_RlStackHybridUnitIdAfterReset_Type.__name__ = "Integer32"
_RlStackHybridUnitIdAfterReset_Object = MibTableColumn
rlStackHybridUnitIdAfterReset = _RlStackHybridUnitIdAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1, 6),
    _RlStackHybridUnitIdAfterReset_Type()
)
rlStackHybridUnitIdAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStackHybridUnitIdAfterReset.setStatus("current")
_RlStackHybridStackModeAfterReset_Type = StackMode
_RlStackHybridStackModeAfterReset_Object = MibTableColumn
rlStackHybridStackModeAfterReset = _RlStackHybridStackModeAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1, 7),
    _RlStackHybridStackModeAfterReset_Type()
)
rlStackHybridStackModeAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStackHybridStackModeAfterReset.setStatus("current")
_RlStackHybridPortsPairAfterReset_Type = PortsPair
_RlStackHybridPortsPairAfterReset_Object = MibTableColumn
rlStackHybridPortsPairAfterReset = _RlStackHybridPortsPairAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1, 8),
    _RlStackHybridPortsPairAfterReset_Type()
)
rlStackHybridPortsPairAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStackHybridPortsPairAfterReset.setStatus("current")
_RlStackHybridPortNo1speedAfterReset_Type = HybridStackPortSpeed
_RlStackHybridPortNo1speedAfterReset_Object = MibTableColumn
rlStackHybridPortNo1speedAfterReset = _RlStackHybridPortNo1speedAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1, 9),
    _RlStackHybridPortNo1speedAfterReset_Type()
)
rlStackHybridPortNo1speedAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStackHybridPortNo1speedAfterReset.setStatus("current")
_RlStackHybridPortNo2speedAfterReset_Type = HybridStackPortSpeed
_RlStackHybridPortNo2speedAfterReset_Object = MibTableColumn
rlStackHybridPortNo2speedAfterReset = _RlStackHybridPortNo2speedAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1, 10),
    _RlStackHybridPortNo2speedAfterReset_Type()
)
rlStackHybridPortNo2speedAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStackHybridPortNo2speedAfterReset.setStatus("current")
_RlStackHybridDeleteStartupAfterReset_Type = TruthValue
_RlStackHybridDeleteStartupAfterReset_Object = MibTableColumn
rlStackHybridDeleteStartupAfterReset = _RlStackHybridDeleteStartupAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1, 11),
    _RlStackHybridDeleteStartupAfterReset_Type()
)
rlStackHybridDeleteStartupAfterReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStackHybridDeleteStartupAfterReset.setStatus("current")
_RlStackHybridDeviceModeAfterReset_Type = HybridStackDeviceMode
_RlStackHybridDeviceModeAfterReset_Object = MibTableColumn
rlStackHybridDeviceModeAfterReset = _RlStackHybridDeviceModeAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1, 12),
    _RlStackHybridDeviceModeAfterReset_Type()
)
rlStackHybridDeviceModeAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStackHybridDeviceModeAfterReset.setStatus("current")


class _RlStackHybridXgPortNo1Num_Type(Integer32):
    """Custom type rlStackHybridXgPortNo1Num based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_RlStackHybridXgPortNo1Num_Type.__name__ = "Integer32"
_RlStackHybridXgPortNo1Num_Object = MibTableColumn
rlStackHybridXgPortNo1Num = _RlStackHybridXgPortNo1Num_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1, 13),
    _RlStackHybridXgPortNo1Num_Type()
)
rlStackHybridXgPortNo1Num.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStackHybridXgPortNo1Num.setStatus("current")


class _RlStackHybridXgPortNo1NumAfterReset_Type(Integer32):
    """Custom type rlStackHybridXgPortNo1NumAfterReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_RlStackHybridXgPortNo1NumAfterReset_Type.__name__ = "Integer32"
_RlStackHybridXgPortNo1NumAfterReset_Object = MibTableColumn
rlStackHybridXgPortNo1NumAfterReset = _RlStackHybridXgPortNo1NumAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1, 14),
    _RlStackHybridXgPortNo1NumAfterReset_Type()
)
rlStackHybridXgPortNo1NumAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStackHybridXgPortNo1NumAfterReset.setStatus("current")


class _RlStackHybridXgPortNo2Num_Type(Integer32):
    """Custom type rlStackHybridXgPortNo2Num based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_RlStackHybridXgPortNo2Num_Type.__name__ = "Integer32"
_RlStackHybridXgPortNo2Num_Object = MibTableColumn
rlStackHybridXgPortNo2Num = _RlStackHybridXgPortNo2Num_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1, 15),
    _RlStackHybridXgPortNo2Num_Type()
)
rlStackHybridXgPortNo2Num.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStackHybridXgPortNo2Num.setStatus("current")


class _RlStackHybridXgPortNo2NumAfterReset_Type(Integer32):
    """Custom type rlStackHybridXgPortNo2NumAfterReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_RlStackHybridXgPortNo2NumAfterReset_Type.__name__ = "Integer32"
_RlStackHybridXgPortNo2NumAfterReset_Object = MibTableColumn
rlStackHybridXgPortNo2NumAfterReset = _RlStackHybridXgPortNo2NumAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1, 16),
    _RlStackHybridXgPortNo2NumAfterReset_Type()
)
rlStackHybridXgPortNo2NumAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStackHybridXgPortNo2NumAfterReset.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-STACK-MIB",
    **{"StackMode": StackMode,
       "PortsPair": PortsPair,
       "HybridStackPortSpeed": HybridStackPortSpeed,
       "HybridStackDeviceMode": HybridStackDeviceMode,
       "rlStack": rlStack,
       "rlStackActiveUnitIdTable": rlStackActiveUnitIdTable,
       "rlStackActiveUnitIdEntry": rlStackActiveUnitIdEntry,
       "rlStackCurrentUnitId": rlStackCurrentUnitId,
       "rlStackActiveUnitIdAfterReset": rlStackActiveUnitIdAfterReset,
       "rlStackUnitModeAfterReset": rlStackUnitModeAfterReset,
       "rlStackUnitMode": rlStackUnitMode,
       "rlStackUnitMacAddressAfterReset": rlStackUnitMacAddressAfterReset,
       "rlStackHybridTable": rlStackHybridTable,
       "rlStackHybridEntry": rlStackHybridEntry,
       "rlStackHybridUnitId": rlStackHybridUnitId,
       "rlStackHybridStackMode": rlStackHybridStackMode,
       "rlStackHybridPortsPair": rlStackHybridPortsPair,
       "rlStackHybridPortNo1speed": rlStackHybridPortNo1speed,
       "rlStackHybridPortNo2speed": rlStackHybridPortNo2speed,
       "rlStackHybridUnitIdAfterReset": rlStackHybridUnitIdAfterReset,
       "rlStackHybridStackModeAfterReset": rlStackHybridStackModeAfterReset,
       "rlStackHybridPortsPairAfterReset": rlStackHybridPortsPairAfterReset,
       "rlStackHybridPortNo1speedAfterReset": rlStackHybridPortNo1speedAfterReset,
       "rlStackHybridPortNo2speedAfterReset": rlStackHybridPortNo2speedAfterReset,
       "rlStackHybridDeleteStartupAfterReset": rlStackHybridDeleteStartupAfterReset,
       "rlStackHybridDeviceModeAfterReset": rlStackHybridDeviceModeAfterReset,
       "rlStackHybridXgPortNo1Num": rlStackHybridXgPortNo1Num,
       "rlStackHybridXgPortNo1NumAfterReset": rlStackHybridXgPortNo1NumAfterReset,
       "rlStackHybridXgPortNo2Num": rlStackHybridXgPortNo2Num,
       "rlStackHybridXgPortNo2NumAfterReset": rlStackHybridXgPortNo2NumAfterReset}
)
