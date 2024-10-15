# SNMP MIB module (SONUS-DS1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONUS-DS1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:56:54 2024
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(sonusDs1Index,
 sonusDs3Index,
 sonusEventClass,
 sonusEventDescription,
 sonusEventLevel,
 sonusPortIndex,
 sonusShelfIndex,
 sonusSlotIndex) = mibBuilder.importSymbols(
    "SONUS-COMMON-MIB",
    "sonusDs1Index",
    "sonusDs3Index",
    "sonusEventClass",
    "sonusEventDescription",
    "sonusEventLevel",
    "sonusPortIndex",
    "sonusShelfIndex",
    "sonusSlotIndex")

(sonusCircuitMIBs,) = mibBuilder.importSymbols(
    "SONUS-SMI",
    "sonusCircuitMIBs")

(SonusAdminAction,
 SonusAdminState,
 SonusName,
 SonusServiceState) = mibBuilder.importSymbols(
    "SONUS-TC",
    "SonusAdminAction",
    "SonusAdminState",
    "SonusName",
    "SonusServiceState")


# MODULE-IDENTITY

sonusDsx1MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonusDsx1MIBObjects_ObjectIdentity = ObjectIdentity
sonusDsx1MIBObjects = _SonusDsx1MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1)
)
_SonusDsx1Admn_ObjectIdentity = ObjectIdentity
sonusDsx1Admn = _SonusDsx1Admn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1)
)
_SonusDsx1AdmnNextIndex_ObjectIdentity = ObjectIdentity
sonusDsx1AdmnNextIndex = _SonusDsx1AdmnNextIndex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 1)
)
_SonusDsx1AdmnTable_Object = MibTable
sonusDsx1AdmnTable = _SonusDsx1AdmnTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    sonusDsx1AdmnTable.setStatus("current")
_SonusDsx1AdmnEntry_Object = MibTableRow
sonusDsx1AdmnEntry = _SonusDsx1AdmnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 2, 1)
)
sonusDsx1AdmnEntry.setIndexNames(
    (0, "SONUS-DS1-MIB", "sonusDsx1AdmnShelfIndex"),
    (0, "SONUS-DS1-MIB", "sonusDsx1AdmnSlotIndex"),
    (0, "SONUS-DS1-MIB", "sonusDsx1AdmnPortIndex"),
    (0, "SONUS-DS1-MIB", "sonusDsx1AdmnDs3Index"),
    (0, "SONUS-DS1-MIB", "sonusDsx1AdmnDs1Index"),
)
if mibBuilder.loadTexts:
    sonusDsx1AdmnEntry.setStatus("current")
_SonusDsx1AdmnRowStatus_Type = RowStatus
_SonusDsx1AdmnRowStatus_Object = MibTableColumn
sonusDsx1AdmnRowStatus = _SonusDsx1AdmnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 2, 1, 1),
    _SonusDsx1AdmnRowStatus_Type()
)
sonusDsx1AdmnRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsx1AdmnRowStatus.setStatus("current")
_SonusDsx1AdmnName_Type = SonusName
_SonusDsx1AdmnName_Object = MibTableColumn
sonusDsx1AdmnName = _SonusDsx1AdmnName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 2, 1, 2),
    _SonusDsx1AdmnName_Type()
)
sonusDsx1AdmnName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsx1AdmnName.setStatus("current")


class _SonusDsx1AdmnProfileName_Type(DisplayString):
    """Custom type sonusDsx1AdmnProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 23),
    )


_SonusDsx1AdmnProfileName_Type.__name__ = "DisplayString"
_SonusDsx1AdmnProfileName_Object = MibTableColumn
sonusDsx1AdmnProfileName = _SonusDsx1AdmnProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 2, 1, 3),
    _SonusDsx1AdmnProfileName_Type()
)
sonusDsx1AdmnProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsx1AdmnProfileName.setStatus("current")
_SonusDsx1AdmnShelfIndex_Type = Integer32
_SonusDsx1AdmnShelfIndex_Object = MibTableColumn
sonusDsx1AdmnShelfIndex = _SonusDsx1AdmnShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 2, 1, 4),
    _SonusDsx1AdmnShelfIndex_Type()
)
sonusDsx1AdmnShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx1AdmnShelfIndex.setStatus("current")
_SonusDsx1AdmnSlotIndex_Type = Integer32
_SonusDsx1AdmnSlotIndex_Object = MibTableColumn
sonusDsx1AdmnSlotIndex = _SonusDsx1AdmnSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 2, 1, 5),
    _SonusDsx1AdmnSlotIndex_Type()
)
sonusDsx1AdmnSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx1AdmnSlotIndex.setStatus("current")
_SonusDsx1AdmnPortIndex_Type = Integer32
_SonusDsx1AdmnPortIndex_Object = MibTableColumn
sonusDsx1AdmnPortIndex = _SonusDsx1AdmnPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 2, 1, 6),
    _SonusDsx1AdmnPortIndex_Type()
)
sonusDsx1AdmnPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx1AdmnPortIndex.setStatus("current")
_SonusDsx1AdmnDs3Index_Type = Integer32
_SonusDsx1AdmnDs3Index_Object = MibTableColumn
sonusDsx1AdmnDs3Index = _SonusDsx1AdmnDs3Index_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 2, 1, 7),
    _SonusDsx1AdmnDs3Index_Type()
)
sonusDsx1AdmnDs3Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx1AdmnDs3Index.setStatus("current")
_SonusDsx1AdmnDs1Index_Type = Integer32
_SonusDsx1AdmnDs1Index_Object = MibTableColumn
sonusDsx1AdmnDs1Index = _SonusDsx1AdmnDs1Index_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 2, 1, 8),
    _SonusDsx1AdmnDs1Index_Type()
)
sonusDsx1AdmnDs1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx1AdmnDs1Index.setStatus("current")
_SonusDsx1AdmnIfIndex_Type = Integer32
_SonusDsx1AdmnIfIndex_Object = MibTableColumn
sonusDsx1AdmnIfIndex = _SonusDsx1AdmnIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 2, 1, 9),
    _SonusDsx1AdmnIfIndex_Type()
)
sonusDsx1AdmnIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx1AdmnIfIndex.setStatus("current")


class _SonusDsx1AdmnState_Type(SonusAdminState):
    """Custom type sonusDsx1AdmnState based on SonusAdminState"""


_SonusDsx1AdmnState_Object = MibTableColumn
sonusDsx1AdmnState = _SonusDsx1AdmnState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 2, 1, 10),
    _SonusDsx1AdmnState_Type()
)
sonusDsx1AdmnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsx1AdmnState.setStatus("current")


class _SonusDsx1AdmnLineBuildOut_Type(Integer32):
    """Custom type sonusDsx1AdmnLineBuildOut based on Integer32"""
    defaultValue = 2

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
              8)
        )
    )
    namedValues = NamedValues(
        *(("buildOut0to110", 1),
          ("buildOut110to220", 2),
          ("buildOut120Ohms", 7),
          ("buildOut220to330", 3),
          ("buildOut330to440", 4),
          ("buildOut440to550", 5),
          ("buildOut550to660", 6),
          ("buildOut75Ohms", 8))
    )


_SonusDsx1AdmnLineBuildOut_Type.__name__ = "Integer32"
_SonusDsx1AdmnLineBuildOut_Object = MibTableColumn
sonusDsx1AdmnLineBuildOut = _SonusDsx1AdmnLineBuildOut_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 2, 1, 11),
    _SonusDsx1AdmnLineBuildOut_Type()
)
sonusDsx1AdmnLineBuildOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsx1AdmnLineBuildOut.setStatus("current")


class _SonusDsx1AdmnTimeout_Type(Integer32):
    """Custom type sonusDsx1AdmnTimeout based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_SonusDsx1AdmnTimeout_Type.__name__ = "Integer32"
_SonusDsx1AdmnTimeout_Object = MibTableColumn
sonusDsx1AdmnTimeout = _SonusDsx1AdmnTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 2, 1, 12),
    _SonusDsx1AdmnTimeout_Type()
)
sonusDsx1AdmnTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsx1AdmnTimeout.setStatus("current")


class _SonusDsx1AdmnMode_Type(SonusServiceState):
    """Custom type sonusDsx1AdmnMode based on SonusServiceState"""


_SonusDsx1AdmnMode_Object = MibTableColumn
sonusDsx1AdmnMode = _SonusDsx1AdmnMode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 2, 1, 13),
    _SonusDsx1AdmnMode_Type()
)
sonusDsx1AdmnMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsx1AdmnMode.setStatus("current")


class _SonusDsx1AdmnAction_Type(SonusAdminAction):
    """Custom type sonusDsx1AdmnAction based on SonusAdminAction"""


_SonusDsx1AdmnAction_Object = MibTableColumn
sonusDsx1AdmnAction = _SonusDsx1AdmnAction_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 2, 1, 14),
    _SonusDsx1AdmnAction_Type()
)
sonusDsx1AdmnAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsx1AdmnAction.setStatus("current")


class _SonusDsx1AdmnIdleCode_Type(Integer32):
    """Custom type sonusDsx1AdmnIdleCode based on Integer32"""
    defaultValue = 127

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SonusDsx1AdmnIdleCode_Type.__name__ = "Integer32"
_SonusDsx1AdmnIdleCode_Object = MibTableColumn
sonusDsx1AdmnIdleCode = _SonusDsx1AdmnIdleCode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 2, 1, 15),
    _SonusDsx1AdmnIdleCode_Type()
)
sonusDsx1AdmnIdleCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsx1AdmnIdleCode.setStatus("current")


class _SonusDsx1AdmnAvailChannels_Type(Bits):
    """Custom type sonusDsx1AdmnAvailChannels based on Bits"""
    namedValues = NamedValues(
        *(("channel1", 0),
          ("channel10", 9),
          ("channel11", 10),
          ("channel12", 11),
          ("channel13", 12),
          ("channel14", 13),
          ("channel15", 14),
          ("channel16", 15),
          ("channel17", 16),
          ("channel18", 17),
          ("channel19", 18),
          ("channel2", 1),
          ("channel20", 19),
          ("channel21", 20),
          ("channel22", 21),
          ("channel23", 22),
          ("channel24", 23),
          ("channel25", 24),
          ("channel26", 25),
          ("channel27", 26),
          ("channel28", 27),
          ("channel29", 28),
          ("channel3", 2),
          ("channel30", 29),
          ("channel31", 30),
          ("channel32", 31),
          ("channel4", 3),
          ("channel5", 4),
          ("channel6", 5),
          ("channel7", 6),
          ("channel8", 7),
          ("channel9", 8))
    )

_SonusDsx1AdmnAvailChannels_Type.__name__ = "Bits"
_SonusDsx1AdmnAvailChannels_Object = MibTableColumn
sonusDsx1AdmnAvailChannels = _SonusDsx1AdmnAvailChannels_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 2, 1, 16),
    _SonusDsx1AdmnAvailChannels_Type()
)
sonusDsx1AdmnAvailChannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsx1AdmnAvailChannels.setStatus("current")


class _SonusDsx1AdmnType_Type(Integer32):
    """Custom type sonusDsx1AdmnType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e1", 2),
          ("t1", 1))
    )


_SonusDsx1AdmnType_Type.__name__ = "Integer32"
_SonusDsx1AdmnType_Object = MibTableColumn
sonusDsx1AdmnType = _SonusDsx1AdmnType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 2, 1, 17),
    _SonusDsx1AdmnType_Type()
)
sonusDsx1AdmnType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsx1AdmnType.setStatus("current")


class _SonusDsx1AdmnESThreshold_Type(Integer32):
    """Custom type sonusDsx1AdmnESThreshold based on Integer32"""
    defaultValue = 65

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_SonusDsx1AdmnESThreshold_Type.__name__ = "Integer32"
_SonusDsx1AdmnESThreshold_Object = MibTableColumn
sonusDsx1AdmnESThreshold = _SonusDsx1AdmnESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 2, 1, 18),
    _SonusDsx1AdmnESThreshold_Type()
)
sonusDsx1AdmnESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsx1AdmnESThreshold.setStatus("current")


class _SonusDsx1AdmnSESThreshold_Type(Integer32):
    """Custom type sonusDsx1AdmnSESThreshold based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_SonusDsx1AdmnSESThreshold_Type.__name__ = "Integer32"
_SonusDsx1AdmnSESThreshold_Object = MibTableColumn
sonusDsx1AdmnSESThreshold = _SonusDsx1AdmnSESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 2, 1, 19),
    _SonusDsx1AdmnSESThreshold_Type()
)
sonusDsx1AdmnSESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsx1AdmnSESThreshold.setStatus("current")


class _SonusDsx1AdmnCSSThreshold_Type(Integer32):
    """Custom type sonusDsx1AdmnCSSThreshold based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_SonusDsx1AdmnCSSThreshold_Type.__name__ = "Integer32"
_SonusDsx1AdmnCSSThreshold_Object = MibTableColumn
sonusDsx1AdmnCSSThreshold = _SonusDsx1AdmnCSSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 2, 1, 20),
    _SonusDsx1AdmnCSSThreshold_Type()
)
sonusDsx1AdmnCSSThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsx1AdmnCSSThreshold.setStatus("current")


class _SonusDsx1AdmnDayESThreshold_Type(Integer32):
    """Custom type sonusDsx1AdmnDayESThreshold based on Integer32"""
    defaultValue = 648

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonusDsx1AdmnDayESThreshold_Type.__name__ = "Integer32"
_SonusDsx1AdmnDayESThreshold_Object = MibTableColumn
sonusDsx1AdmnDayESThreshold = _SonusDsx1AdmnDayESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 2, 1, 21),
    _SonusDsx1AdmnDayESThreshold_Type()
)
sonusDsx1AdmnDayESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsx1AdmnDayESThreshold.setStatus("current")


class _SonusDsx1AdmnDaySESThreshold_Type(Integer32):
    """Custom type sonusDsx1AdmnDaySESThreshold based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonusDsx1AdmnDaySESThreshold_Type.__name__ = "Integer32"
_SonusDsx1AdmnDaySESThreshold_Object = MibTableColumn
sonusDsx1AdmnDaySESThreshold = _SonusDsx1AdmnDaySESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 2, 1, 22),
    _SonusDsx1AdmnDaySESThreshold_Type()
)
sonusDsx1AdmnDaySESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsx1AdmnDaySESThreshold.setStatus("current")


class _SonusDsx1AdmnDayCSSThreshold_Type(Integer32):
    """Custom type sonusDsx1AdmnDayCSSThreshold based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonusDsx1AdmnDayCSSThreshold_Type.__name__ = "Integer32"
_SonusDsx1AdmnDayCSSThreshold_Object = MibTableColumn
sonusDsx1AdmnDayCSSThreshold = _SonusDsx1AdmnDayCSSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 2, 1, 23),
    _SonusDsx1AdmnDayCSSThreshold_Type()
)
sonusDsx1AdmnDayCSSThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsx1AdmnDayCSSThreshold.setStatus("current")


class _SonusDsx1AdmnFarESThreshold_Type(Integer32):
    """Custom type sonusDsx1AdmnFarESThreshold based on Integer32"""
    defaultValue = 65

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_SonusDsx1AdmnFarESThreshold_Type.__name__ = "Integer32"
_SonusDsx1AdmnFarESThreshold_Object = MibTableColumn
sonusDsx1AdmnFarESThreshold = _SonusDsx1AdmnFarESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 2, 1, 24),
    _SonusDsx1AdmnFarESThreshold_Type()
)
sonusDsx1AdmnFarESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsx1AdmnFarESThreshold.setStatus("current")


class _SonusDsx1AdmnFarSESThreshold_Type(Integer32):
    """Custom type sonusDsx1AdmnFarSESThreshold based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_SonusDsx1AdmnFarSESThreshold_Type.__name__ = "Integer32"
_SonusDsx1AdmnFarSESThreshold_Object = MibTableColumn
sonusDsx1AdmnFarSESThreshold = _SonusDsx1AdmnFarSESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 2, 1, 25),
    _SonusDsx1AdmnFarSESThreshold_Type()
)
sonusDsx1AdmnFarSESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsx1AdmnFarSESThreshold.setStatus("current")


class _SonusDsx1AdmnFarDayESThreshold_Type(Integer32):
    """Custom type sonusDsx1AdmnFarDayESThreshold based on Integer32"""
    defaultValue = 648

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonusDsx1AdmnFarDayESThreshold_Type.__name__ = "Integer32"
_SonusDsx1AdmnFarDayESThreshold_Object = MibTableColumn
sonusDsx1AdmnFarDayESThreshold = _SonusDsx1AdmnFarDayESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 2, 1, 26),
    _SonusDsx1AdmnFarDayESThreshold_Type()
)
sonusDsx1AdmnFarDayESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsx1AdmnFarDayESThreshold.setStatus("current")


class _SonusDsx1AdmnFarDaySESThreshold_Type(Integer32):
    """Custom type sonusDsx1AdmnFarDaySESThreshold based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonusDsx1AdmnFarDaySESThreshold_Type.__name__ = "Integer32"
_SonusDsx1AdmnFarDaySESThreshold_Object = MibTableColumn
sonusDsx1AdmnFarDaySESThreshold = _SonusDsx1AdmnFarDaySESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 2, 1, 27),
    _SonusDsx1AdmnFarDaySESThreshold_Type()
)
sonusDsx1AdmnFarDaySESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsx1AdmnFarDaySESThreshold.setStatus("current")


class _SonusDsx1AdmnPCVThreshold_Type(Integer32):
    """Custom type sonusDsx1AdmnPCVThreshold based on Integer32"""
    defaultValue = 13296

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_SonusDsx1AdmnPCVThreshold_Type.__name__ = "Integer32"
_SonusDsx1AdmnPCVThreshold_Object = MibTableColumn
sonusDsx1AdmnPCVThreshold = _SonusDsx1AdmnPCVThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 2, 1, 28),
    _SonusDsx1AdmnPCVThreshold_Type()
)
sonusDsx1AdmnPCVThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsx1AdmnPCVThreshold.setStatus("current")


class _SonusDsx1AdmnLCVThreshold_Type(Integer32):
    """Custom type sonusDsx1AdmnLCVThreshold based on Integer32"""
    defaultValue = 13340

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_SonusDsx1AdmnLCVThreshold_Type.__name__ = "Integer32"
_SonusDsx1AdmnLCVThreshold_Object = MibTableColumn
sonusDsx1AdmnLCVThreshold = _SonusDsx1AdmnLCVThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 2, 1, 29),
    _SonusDsx1AdmnLCVThreshold_Type()
)
sonusDsx1AdmnLCVThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsx1AdmnLCVThreshold.setStatus("current")


class _SonusDsx1AdmnUASThreshold_Type(Integer32):
    """Custom type sonusDsx1AdmnUASThreshold based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_SonusDsx1AdmnUASThreshold_Type.__name__ = "Integer32"
_SonusDsx1AdmnUASThreshold_Object = MibTableColumn
sonusDsx1AdmnUASThreshold = _SonusDsx1AdmnUASThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 2, 1, 30),
    _SonusDsx1AdmnUASThreshold_Type()
)
sonusDsx1AdmnUASThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsx1AdmnUASThreshold.setStatus("current")


class _SonusDsx1AdmnFarPCVThreshold_Type(Integer32):
    """Custom type sonusDsx1AdmnFarPCVThreshold based on Integer32"""
    defaultValue = 72

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_SonusDsx1AdmnFarPCVThreshold_Type.__name__ = "Integer32"
_SonusDsx1AdmnFarPCVThreshold_Object = MibTableColumn
sonusDsx1AdmnFarPCVThreshold = _SonusDsx1AdmnFarPCVThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 2, 1, 31),
    _SonusDsx1AdmnFarPCVThreshold_Type()
)
sonusDsx1AdmnFarPCVThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsx1AdmnFarPCVThreshold.setStatus("current")


class _SonusDsx1AdmnFarLCVThreshold_Type(Integer32):
    """Custom type sonusDsx1AdmnFarLCVThreshold based on Integer32"""
    defaultValue = 72

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_SonusDsx1AdmnFarLCVThreshold_Type.__name__ = "Integer32"
_SonusDsx1AdmnFarLCVThreshold_Object = MibTableColumn
sonusDsx1AdmnFarLCVThreshold = _SonusDsx1AdmnFarLCVThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 2, 1, 32),
    _SonusDsx1AdmnFarLCVThreshold_Type()
)
sonusDsx1AdmnFarLCVThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsx1AdmnFarLCVThreshold.setStatus("current")


class _SonusDsx1AdmnFarUASThreshold_Type(Integer32):
    """Custom type sonusDsx1AdmnFarUASThreshold based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_SonusDsx1AdmnFarUASThreshold_Type.__name__ = "Integer32"
_SonusDsx1AdmnFarUASThreshold_Object = MibTableColumn
sonusDsx1AdmnFarUASThreshold = _SonusDsx1AdmnFarUASThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 2, 1, 33),
    _SonusDsx1AdmnFarUASThreshold_Type()
)
sonusDsx1AdmnFarUASThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsx1AdmnFarUASThreshold.setStatus("current")


class _SonusDsx1AdmnDayPCVThreshold_Type(Integer32):
    """Custom type sonusDsx1AdmnDayPCVThreshold based on Integer32"""
    defaultValue = 132960

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1048575),
    )


_SonusDsx1AdmnDayPCVThreshold_Type.__name__ = "Integer32"
_SonusDsx1AdmnDayPCVThreshold_Object = MibTableColumn
sonusDsx1AdmnDayPCVThreshold = _SonusDsx1AdmnDayPCVThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 2, 1, 34),
    _SonusDsx1AdmnDayPCVThreshold_Type()
)
sonusDsx1AdmnDayPCVThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsx1AdmnDayPCVThreshold.setStatus("current")


class _SonusDsx1AdmnDayLCVThreshold_Type(Integer32):
    """Custom type sonusDsx1AdmnDayLCVThreshold based on Integer32"""
    defaultValue = 133400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1048575),
    )


_SonusDsx1AdmnDayLCVThreshold_Type.__name__ = "Integer32"
_SonusDsx1AdmnDayLCVThreshold_Object = MibTableColumn
sonusDsx1AdmnDayLCVThreshold = _SonusDsx1AdmnDayLCVThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 2, 1, 35),
    _SonusDsx1AdmnDayLCVThreshold_Type()
)
sonusDsx1AdmnDayLCVThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsx1AdmnDayLCVThreshold.setStatus("current")


class _SonusDsx1AdmnDayUASThreshold_Type(Integer32):
    """Custom type sonusDsx1AdmnDayUASThreshold based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonusDsx1AdmnDayUASThreshold_Type.__name__ = "Integer32"
_SonusDsx1AdmnDayUASThreshold_Object = MibTableColumn
sonusDsx1AdmnDayUASThreshold = _SonusDsx1AdmnDayUASThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 2, 1, 36),
    _SonusDsx1AdmnDayUASThreshold_Type()
)
sonusDsx1AdmnDayUASThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsx1AdmnDayUASThreshold.setStatus("current")


class _SonusDsx1AdmnFarDayPCVThreshold_Type(Integer32):
    """Custom type sonusDsx1AdmnFarDayPCVThreshold based on Integer32"""
    defaultValue = 691

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1048575),
    )


_SonusDsx1AdmnFarDayPCVThreshold_Type.__name__ = "Integer32"
_SonusDsx1AdmnFarDayPCVThreshold_Object = MibTableColumn
sonusDsx1AdmnFarDayPCVThreshold = _SonusDsx1AdmnFarDayPCVThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 2, 1, 37),
    _SonusDsx1AdmnFarDayPCVThreshold_Type()
)
sonusDsx1AdmnFarDayPCVThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsx1AdmnFarDayPCVThreshold.setStatus("current")


class _SonusDsx1AdmnFarDayLCVThreshold_Type(Integer32):
    """Custom type sonusDsx1AdmnFarDayLCVThreshold based on Integer32"""
    defaultValue = 691

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1048575),
    )


_SonusDsx1AdmnFarDayLCVThreshold_Type.__name__ = "Integer32"
_SonusDsx1AdmnFarDayLCVThreshold_Object = MibTableColumn
sonusDsx1AdmnFarDayLCVThreshold = _SonusDsx1AdmnFarDayLCVThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 2, 1, 38),
    _SonusDsx1AdmnFarDayLCVThreshold_Type()
)
sonusDsx1AdmnFarDayLCVThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsx1AdmnFarDayLCVThreshold.setStatus("current")


class _SonusDsx1AdmnFarDayUASThreshold_Type(Integer32):
    """Custom type sonusDsx1AdmnFarDayUASThreshold based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonusDsx1AdmnFarDayUASThreshold_Type.__name__ = "Integer32"
_SonusDsx1AdmnFarDayUASThreshold_Object = MibTableColumn
sonusDsx1AdmnFarDayUASThreshold = _SonusDsx1AdmnFarDayUASThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 2, 1, 39),
    _SonusDsx1AdmnFarDayUASThreshold_Type()
)
sonusDsx1AdmnFarDayUASThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsx1AdmnFarDayUASThreshold.setStatus("current")


class _SonusDsx1AdmnInitCounters_Type(SonusAdminState):
    """Custom type sonusDsx1AdmnInitCounters based on SonusAdminState"""


_SonusDsx1AdmnInitCounters_Object = MibTableColumn
sonusDsx1AdmnInitCounters = _SonusDsx1AdmnInitCounters_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 2, 1, 40),
    _SonusDsx1AdmnInitCounters_Type()
)
sonusDsx1AdmnInitCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsx1AdmnInitCounters.setStatus("current")


class _SonusDsx1AdmnEchoProfileName_Type(DisplayString):
    """Custom type sonusDsx1AdmnEchoProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 23),
    )


_SonusDsx1AdmnEchoProfileName_Type.__name__ = "DisplayString"
_SonusDsx1AdmnEchoProfileName_Object = MibTableColumn
sonusDsx1AdmnEchoProfileName = _SonusDsx1AdmnEchoProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 2, 1, 41),
    _SonusDsx1AdmnEchoProfileName_Type()
)
sonusDsx1AdmnEchoProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsx1AdmnEchoProfileName.setStatus("current")


class _SonusDsx1AdmnEchoCancellorMaxTail_Type(Integer32):
    """Custom type sonusDsx1AdmnEchoCancellorMaxTail based on Integer32"""
    defaultValue = 4

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
        *(("millisec24", 1),
          ("millisec32", 2),
          ("millisec48", 3),
          ("millisec64", 4))
    )


_SonusDsx1AdmnEchoCancellorMaxTail_Type.__name__ = "Integer32"
_SonusDsx1AdmnEchoCancellorMaxTail_Object = MibTableColumn
sonusDsx1AdmnEchoCancellorMaxTail = _SonusDsx1AdmnEchoCancellorMaxTail_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 2, 1, 42),
    _SonusDsx1AdmnEchoCancellorMaxTail_Type()
)
sonusDsx1AdmnEchoCancellorMaxTail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx1AdmnEchoCancellorMaxTail.setStatus("current")


class _SonusDsx1AdmnEchoCancellorAudioType_Type(Integer32):
    """Custom type sonusDsx1AdmnEchoCancellorAudioType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aLaw", 2),
          ("uLaw", 1))
    )


_SonusDsx1AdmnEchoCancellorAudioType_Type.__name__ = "Integer32"
_SonusDsx1AdmnEchoCancellorAudioType_Object = MibTableColumn
sonusDsx1AdmnEchoCancellorAudioType = _SonusDsx1AdmnEchoCancellorAudioType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 2, 1, 43),
    _SonusDsx1AdmnEchoCancellorAudioType_Type()
)
sonusDsx1AdmnEchoCancellorAudioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx1AdmnEchoCancellorAudioType.setStatus("current")


class _SonusDsx1AdmnEchoCancellorSignallingTone_Type(Integer32):
    """Custom type sonusDsx1AdmnEchoCancellorSignallingTone based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("c5", 2),
          ("none", 1))
    )


_SonusDsx1AdmnEchoCancellorSignallingTone_Type.__name__ = "Integer32"
_SonusDsx1AdmnEchoCancellorSignallingTone_Object = MibTableColumn
sonusDsx1AdmnEchoCancellorSignallingTone = _SonusDsx1AdmnEchoCancellorSignallingTone_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 2, 1, 44),
    _SonusDsx1AdmnEchoCancellorSignallingTone_Type()
)
sonusDsx1AdmnEchoCancellorSignallingTone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx1AdmnEchoCancellorSignallingTone.setStatus("current")


class _SonusDsx1AdmnEchoCancellorNlpDisable_Type(Integer32):
    """Custom type sonusDsx1AdmnEchoCancellorNlpDisable based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_SonusDsx1AdmnEchoCancellorNlpDisable_Type.__name__ = "Integer32"
_SonusDsx1AdmnEchoCancellorNlpDisable_Object = MibTableColumn
sonusDsx1AdmnEchoCancellorNlpDisable = _SonusDsx1AdmnEchoCancellorNlpDisable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 2, 1, 45),
    _SonusDsx1AdmnEchoCancellorNlpDisable_Type()
)
sonusDsx1AdmnEchoCancellorNlpDisable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx1AdmnEchoCancellorNlpDisable.setStatus("current")


class _SonusDsx1AdmnEchoCancellorNlpEnable_Type(Integer32):
    """Custom type sonusDsx1AdmnEchoCancellorNlpEnable based on Integer32"""
    defaultValue = 75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 80),
    )


_SonusDsx1AdmnEchoCancellorNlpEnable_Type.__name__ = "Integer32"
_SonusDsx1AdmnEchoCancellorNlpEnable_Object = MibTableColumn
sonusDsx1AdmnEchoCancellorNlpEnable = _SonusDsx1AdmnEchoCancellorNlpEnable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 2, 1, 46),
    _SonusDsx1AdmnEchoCancellorNlpEnable_Type()
)
sonusDsx1AdmnEchoCancellorNlpEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx1AdmnEchoCancellorNlpEnable.setStatus("current")


class _SonusDsx1AdmnEchoCancellorReturnLoss_Type(Integer32):
    """Custom type sonusDsx1AdmnEchoCancellorReturnLoss based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dB0", 3),
          ("dB3", 2),
          ("dB6", 1))
    )


_SonusDsx1AdmnEchoCancellorReturnLoss_Type.__name__ = "Integer32"
_SonusDsx1AdmnEchoCancellorReturnLoss_Object = MibTableColumn
sonusDsx1AdmnEchoCancellorReturnLoss = _SonusDsx1AdmnEchoCancellorReturnLoss_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 2, 1, 47),
    _SonusDsx1AdmnEchoCancellorReturnLoss_Type()
)
sonusDsx1AdmnEchoCancellorReturnLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx1AdmnEchoCancellorReturnLoss.setStatus("current")


class _SonusDsx1AdmnEchoCancellorResidualEcho_Type(Integer32):
    """Custom type sonusDsx1AdmnEchoCancellorResidualEcho based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("cancelOnly", 1),
          ("comfortNoise", 4),
          ("suppressResidual", 2))
    )


_SonusDsx1AdmnEchoCancellorResidualEcho_Type.__name__ = "Integer32"
_SonusDsx1AdmnEchoCancellorResidualEcho_Object = MibTableColumn
sonusDsx1AdmnEchoCancellorResidualEcho = _SonusDsx1AdmnEchoCancellorResidualEcho_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 2, 1, 48),
    _SonusDsx1AdmnEchoCancellorResidualEcho_Type()
)
sonusDsx1AdmnEchoCancellorResidualEcho.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx1AdmnEchoCancellorResidualEcho.setStatus("current")


class _SonusDsx1AdmnEchoCancellorHiLevelComp_Type(Integer32):
    """Custom type sonusDsx1AdmnEchoCancellorHiLevelComp based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dB6", 2),
          ("none", 1))
    )


_SonusDsx1AdmnEchoCancellorHiLevelComp_Type.__name__ = "Integer32"
_SonusDsx1AdmnEchoCancellorHiLevelComp_Object = MibTableColumn
sonusDsx1AdmnEchoCancellorHiLevelComp = _SonusDsx1AdmnEchoCancellorHiLevelComp_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 2, 1, 49),
    _SonusDsx1AdmnEchoCancellorHiLevelComp_Type()
)
sonusDsx1AdmnEchoCancellorHiLevelComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx1AdmnEchoCancellorHiLevelComp.setStatus("current")


class _SonusDsx1AdmnEchoCancellorModemDisable_Type(Integer32):
    """Custom type sonusDsx1AdmnEchoCancellorModemDisable based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("g164", 2),
          ("g165", 4),
          ("ignore2100Hz", 1))
    )


_SonusDsx1AdmnEchoCancellorModemDisable_Type.__name__ = "Integer32"
_SonusDsx1AdmnEchoCancellorModemDisable_Object = MibTableColumn
sonusDsx1AdmnEchoCancellorModemDisable = _SonusDsx1AdmnEchoCancellorModemDisable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 2, 1, 50),
    _SonusDsx1AdmnEchoCancellorModemDisable_Type()
)
sonusDsx1AdmnEchoCancellorModemDisable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx1AdmnEchoCancellorModemDisable.setStatus("current")


class _SonusDsx1AdmnZeroSuppression_Type(Integer32):
    """Custom type sonusDsx1AdmnZeroSuppression based on Integer32"""
    defaultValue = 1

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
        *(("bellZeroSuppression", 5),
          ("gteZeroSuppression", 4),
          ("jamBit8", 2),
          ("none", 1),
          ("signalFrameOnlyJamBit8", 3))
    )


_SonusDsx1AdmnZeroSuppression_Type.__name__ = "Integer32"
_SonusDsx1AdmnZeroSuppression_Object = MibTableColumn
sonusDsx1AdmnZeroSuppression = _SonusDsx1AdmnZeroSuppression_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 2, 1, 51),
    _SonusDsx1AdmnZeroSuppression_Type()
)
sonusDsx1AdmnZeroSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsx1AdmnZeroSuppression.setStatus("current")


class _SonusDsx1AdmnCircuitId_Type(DisplayString):
    """Custom type sonusDsx1AdmnCircuitId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 23),
    )


_SonusDsx1AdmnCircuitId_Type.__name__ = "DisplayString"
_SonusDsx1AdmnCircuitId_Object = MibTableColumn
sonusDsx1AdmnCircuitId = _SonusDsx1AdmnCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 2, 1, 52),
    _SonusDsx1AdmnCircuitId_Type()
)
sonusDsx1AdmnCircuitId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsx1AdmnCircuitId.setStatus("current")


class _SonusDsx1AdmnEchoCancellorNarrowbandDetection_Type(Integer32):
    """Custom type sonusDsx1AdmnEchoCancellorNarrowbandDetection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_SonusDsx1AdmnEchoCancellorNarrowbandDetection_Type.__name__ = "Integer32"
_SonusDsx1AdmnEchoCancellorNarrowbandDetection_Object = MibTableColumn
sonusDsx1AdmnEchoCancellorNarrowbandDetection = _SonusDsx1AdmnEchoCancellorNarrowbandDetection_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 1, 2, 1, 53),
    _SonusDsx1AdmnEchoCancellorNarrowbandDetection_Type()
)
sonusDsx1AdmnEchoCancellorNarrowbandDetection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx1AdmnEchoCancellorNarrowbandDetection.setStatus("current")
_SonusDsx1StatTable_Object = MibTable
sonusDsx1StatTable = _SonusDsx1StatTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 2)
)
if mibBuilder.loadTexts:
    sonusDsx1StatTable.setStatus("current")
_SonusDsx1StatEntry_Object = MibTableRow
sonusDsx1StatEntry = _SonusDsx1StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 2, 1)
)
sonusDsx1StatEntry.setIndexNames(
    (0, "SONUS-DS1-MIB", "sonusDsx1StatShelfIndex"),
    (0, "SONUS-DS1-MIB", "sonusDsx1StatSlotIndex"),
    (0, "SONUS-DS1-MIB", "sonusDsx1StatPortIndex"),
    (0, "SONUS-DS1-MIB", "sonusDsx1StatDs3Index"),
    (0, "SONUS-DS1-MIB", "sonusDsx1StatDs1Index"),
)
if mibBuilder.loadTexts:
    sonusDsx1StatEntry.setStatus("current")
_SonusDsx1StatShelfIndex_Type = Integer32
_SonusDsx1StatShelfIndex_Object = MibTableColumn
sonusDsx1StatShelfIndex = _SonusDsx1StatShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 2, 1, 1),
    _SonusDsx1StatShelfIndex_Type()
)
sonusDsx1StatShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx1StatShelfIndex.setStatus("current")
_SonusDsx1StatSlotIndex_Type = Integer32
_SonusDsx1StatSlotIndex_Object = MibTableColumn
sonusDsx1StatSlotIndex = _SonusDsx1StatSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 2, 1, 2),
    _SonusDsx1StatSlotIndex_Type()
)
sonusDsx1StatSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx1StatSlotIndex.setStatus("current")
_SonusDsx1StatPortIndex_Type = Integer32
_SonusDsx1StatPortIndex_Object = MibTableColumn
sonusDsx1StatPortIndex = _SonusDsx1StatPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 2, 1, 3),
    _SonusDsx1StatPortIndex_Type()
)
sonusDsx1StatPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx1StatPortIndex.setStatus("current")
_SonusDsx1StatDs3Index_Type = Integer32
_SonusDsx1StatDs3Index_Object = MibTableColumn
sonusDsx1StatDs3Index = _SonusDsx1StatDs3Index_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 2, 1, 4),
    _SonusDsx1StatDs3Index_Type()
)
sonusDsx1StatDs3Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx1StatDs3Index.setStatus("current")
_SonusDsx1StatDs1Index_Type = Integer32
_SonusDsx1StatDs1Index_Object = MibTableColumn
sonusDsx1StatDs1Index = _SonusDsx1StatDs1Index_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 2, 1, 5),
    _SonusDsx1StatDs1Index_Type()
)
sonusDsx1StatDs1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx1StatDs1Index.setStatus("current")
_SonusDsx1StatValidInt_Type = Integer32
_SonusDsx1StatValidInt_Object = MibTableColumn
sonusDsx1StatValidInt = _SonusDsx1StatValidInt_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 2, 1, 6),
    _SonusDsx1StatValidInt_Type()
)
sonusDsx1StatValidInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx1StatValidInt.setStatus("current")
_SonusDsx1StatRxSlips_Type = Integer32
_SonusDsx1StatRxSlips_Object = MibTableColumn
sonusDsx1StatRxSlips = _SonusDsx1StatRxSlips_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 2, 1, 7),
    _SonusDsx1StatRxSlips_Type()
)
sonusDsx1StatRxSlips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx1StatRxSlips.setStatus("current")
_SonusDsx1StatTxSlips_Type = Integer32
_SonusDsx1StatTxSlips_Object = MibTableColumn
sonusDsx1StatTxSlips = _SonusDsx1StatTxSlips_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 2, 1, 8),
    _SonusDsx1StatTxSlips_Type()
)
sonusDsx1StatTxSlips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx1StatTxSlips.setStatus("current")
_SonusDsx1StatLOF_Type = Integer32
_SonusDsx1StatLOF_Object = MibTableColumn
sonusDsx1StatLOF = _SonusDsx1StatLOF_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 2, 1, 9),
    _SonusDsx1StatLOF_Type()
)
sonusDsx1StatLOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx1StatLOF.setStatus("current")
_SonusDsx1StatAIS_Type = Integer32
_SonusDsx1StatAIS_Object = MibTableColumn
sonusDsx1StatAIS = _SonusDsx1StatAIS_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 2, 1, 10),
    _SonusDsx1StatAIS_Type()
)
sonusDsx1StatAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx1StatAIS.setStatus("current")
_SonusDsx1StatRAI_Type = Integer32
_SonusDsx1StatRAI_Object = MibTableColumn
sonusDsx1StatRAI = _SonusDsx1StatRAI_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 2, 1, 11),
    _SonusDsx1StatRAI_Type()
)
sonusDsx1StatRAI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx1StatRAI.setStatus("current")
_SonusDsx1StatRED_Type = Integer32
_SonusDsx1StatRED_Object = MibTableColumn
sonusDsx1StatRED = _SonusDsx1StatRED_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 2, 1, 12),
    _SonusDsx1StatRED_Type()
)
sonusDsx1StatRED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx1StatRED.setStatus("current")
_SonusDsx1StatCRC_Type = Integer32
_SonusDsx1StatCRC_Object = MibTableColumn
sonusDsx1StatCRC = _SonusDsx1StatCRC_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 2, 1, 13),
    _SonusDsx1StatCRC_Type()
)
sonusDsx1StatCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx1StatCRC.setStatus("current")
_SonusDsx1StatCOFA_Type = Integer32
_SonusDsx1StatCOFA_Object = MibTableColumn
sonusDsx1StatCOFA = _SonusDsx1StatCOFA_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 2, 1, 14),
    _SonusDsx1StatCOFA_Type()
)
sonusDsx1StatCOFA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx1StatCOFA.setStatus("current")
_SonusDsx1StatFBE_Type = Integer32
_SonusDsx1StatFBE_Object = MibTableColumn
sonusDsx1StatFBE = _SonusDsx1StatFBE_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 2, 1, 15),
    _SonusDsx1StatFBE_Type()
)
sonusDsx1StatFBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx1StatFBE.setStatus("current")
_SonusDsx1StatStatus_Type = DisplayString
_SonusDsx1StatStatus_Object = MibTableColumn
sonusDsx1StatStatus = _SonusDsx1StatStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 2, 1, 16),
    _SonusDsx1StatStatus_Type()
)
sonusDsx1StatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx1StatStatus.setStatus("deprecated")
_SonusDsx1StatAllocChannels_Type = DisplayString
_SonusDsx1StatAllocChannels_Object = MibTableColumn
sonusDsx1StatAllocChannels = _SonusDsx1StatAllocChannels_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 2, 1, 17),
    _SonusDsx1StatAllocChannels_Type()
)
sonusDsx1StatAllocChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx1StatAllocChannels.setStatus("current")
_SonusDsx1StatEnabChannels_Type = DisplayString
_SonusDsx1StatEnabChannels_Object = MibTableColumn
sonusDsx1StatEnabChannels = _SonusDsx1StatEnabChannels_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 2, 1, 18),
    _SonusDsx1StatEnabChannels_Type()
)
sonusDsx1StatEnabChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx1StatEnabChannels.setStatus("current")
_SonusE1StatLOMF_Type = Integer32
_SonusE1StatLOMF_Object = MibTableColumn
sonusE1StatLOMF = _SonusE1StatLOMF_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 2, 1, 19),
    _SonusE1StatLOMF_Type()
)
sonusE1StatLOMF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusE1StatLOMF.setStatus("current")
_SonusE1StatMFError_Type = Integer32
_SonusE1StatMFError_Object = MibTableColumn
sonusE1StatMFError = _SonusE1StatMFError_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 2, 1, 20),
    _SonusE1StatMFError_Type()
)
sonusE1StatMFError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusE1StatMFError.setStatus("current")
_SonusE1StatFEBE_Type = Integer32
_SonusE1StatFEBE_Object = MibTableColumn
sonusE1StatFEBE = _SonusE1StatFEBE_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 2, 1, 21),
    _SonusE1StatFEBE_Type()
)
sonusE1StatFEBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusE1StatFEBE.setStatus("current")
_SonusE1StatOOOF_Type = Integer32
_SonusE1StatOOOF_Object = MibTableColumn
sonusE1StatOOOF = _SonusE1StatOOOF_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 2, 1, 22),
    _SonusE1StatOOOF_Type()
)
sonusE1StatOOOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusE1StatOOOF.setStatus("current")
_SonusE1StatC2NCIWCK_Type = Integer32
_SonusE1StatC2NCIWCK_Object = MibTableColumn
sonusE1StatC2NCIWCK = _SonusE1StatC2NCIWCK_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 2, 1, 23),
    _SonusE1StatC2NCIWCK_Type()
)
sonusE1StatC2NCIWCK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusE1StatC2NCIWCK.setStatus("current")
_SonusE1StatRAIContCRC_Type = Integer32
_SonusE1StatRAIContCRC_Object = MibTableColumn
sonusE1StatRAIContCRC = _SonusE1StatRAIContCRC_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 2, 1, 24),
    _SonusE1StatRAIContCRC_Type()
)
sonusE1StatRAIContCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusE1StatRAIContCRC.setStatus("current")
_SonusE1StatContFEBE_Type = Integer32
_SonusE1StatContFEBE_Object = MibTableColumn
sonusE1StatContFEBE = _SonusE1StatContFEBE_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 2, 1, 25),
    _SonusE1StatContFEBE_Type()
)
sonusE1StatContFEBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusE1StatContFEBE.setStatus("current")
_SonusE1StatExcessCRC_Type = Integer32
_SonusE1StatExcessCRC_Object = MibTableColumn
sonusE1StatExcessCRC = _SonusE1StatExcessCRC_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 2, 1, 26),
    _SonusE1StatExcessCRC_Type()
)
sonusE1StatExcessCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusE1StatExcessCRC.setStatus("current")
_SonusE1StatFASErr_Type = Integer32
_SonusE1StatFASErr_Object = MibTableColumn
sonusE1StatFASErr = _SonusE1StatFASErr_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 2, 1, 27),
    _SonusE1StatFASErr_Type()
)
sonusE1StatFASErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusE1StatFASErr.setStatus("current")


class _SonusDsx1StatSendPattern_Type(Integer32):
    """Custom type sonusDsx1StatSendPattern based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("dsx1Send3in24Pattern", 7),
          ("dsx1Send511Pattern", 6),
          ("dsx1SendLineCode", 2),
          ("dsx1SendNoCode", 1),
          ("dsx1SendOtherTestPattern", 8),
          ("dsx1SendPayloadCode", 3),
          ("dsx1SendQRS", 5),
          ("dsx1SendResetCode", 4))
    )


_SonusDsx1StatSendPattern_Type.__name__ = "Integer32"
_SonusDsx1StatSendPattern_Object = MibTableColumn
sonusDsx1StatSendPattern = _SonusDsx1StatSendPattern_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 2, 1, 28),
    _SonusDsx1StatSendPattern_Type()
)
sonusDsx1StatSendPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx1StatSendPattern.setStatus("current")


class _SonusDsx1StatStatusCode_Type(Integer32):
    """Custom type sonusDsx1StatStatusCode based on Integer32"""
    defaultValue = 1

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
        *(("dsx1StatStatusCodeAisAlarm", 4),
          ("dsx1StatStatusCodeDspFailure", 5),
          ("dsx1StatStatusCodeLoopback", 6),
          ("dsx1StatStatusCodeNoAlarm", 1),
          ("dsx1StatStatusCodeRedAlarm", 2),
          ("dsx1StatStatusCodeYellowAlarm", 3))
    )


_SonusDsx1StatStatusCode_Type.__name__ = "Integer32"
_SonusDsx1StatStatusCode_Object = MibTableColumn
sonusDsx1StatStatusCode = _SonusDsx1StatStatusCode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 2, 1, 29),
    _SonusDsx1StatStatusCode_Type()
)
sonusDsx1StatStatusCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx1StatStatusCode.setStatus("current")


class _SonusDsx1StatLoopbackStatus_Type(Integer32):
    """Custom type sonusDsx1StatLoopbackStatus based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("dsx1StatLoopbackStatusFeLineLoopback", 6),
          ("dsx1StatLoopbackStatusFePayloadLoopback", 7),
          ("dsx1StatLoopbackStatusNeDualLoopback", 5),
          ("dsx1StatLoopbackStatusNeInwardLoopback", 4),
          ("dsx1StatLoopbackStatusNeLineLoopback", 2),
          ("dsx1StatLoopbackStatusNePayloadLoopback", 3),
          ("dsx1StatLoopbackStatusNoLoopback", 1))
    )


_SonusDsx1StatLoopbackStatus_Type.__name__ = "Integer32"
_SonusDsx1StatLoopbackStatus_Object = MibTableColumn
sonusDsx1StatLoopbackStatus = _SonusDsx1StatLoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 2, 1, 30),
    _SonusDsx1StatLoopbackStatus_Type()
)
sonusDsx1StatLoopbackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx1StatLoopbackStatus.setStatus("current")


class _SonusDsx1StatOperStatus_Type(Integer32):
    """Custom type sonusDsx1StatOperStatus based on Integer32"""
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
          ("dryingUp", 3),
          ("up", 1))
    )


_SonusDsx1StatOperStatus_Type.__name__ = "Integer32"
_SonusDsx1StatOperStatus_Object = MibTableColumn
sonusDsx1StatOperStatus = _SonusDsx1StatOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 2, 1, 31),
    _SonusDsx1StatOperStatus_Type()
)
sonusDsx1StatOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsx1StatOperStatus.setStatus("current")
_SonusDs0AdmnTable_Object = MibTable
sonusDs0AdmnTable = _SonusDs0AdmnTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 3)
)
if mibBuilder.loadTexts:
    sonusDs0AdmnTable.setStatus("current")
_SonusDs0AdmnEntry_Object = MibTableRow
sonusDs0AdmnEntry = _SonusDs0AdmnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 3, 1)
)
sonusDs0AdmnEntry.setIndexNames(
    (0, "SONUS-DS1-MIB", "sonusDs0AdmnShelfIndex"),
    (0, "SONUS-DS1-MIB", "sonusDs0AdmnSlotIndex"),
    (0, "SONUS-DS1-MIB", "sonusDs0AdmnPortIndex"),
    (0, "SONUS-DS1-MIB", "sonusDs0AdmnDs3Index"),
    (0, "SONUS-DS1-MIB", "sonusDs0AdmnDs1Index"),
    (0, "SONUS-DS1-MIB", "sonusDs0AdmnDs0Index"),
)
if mibBuilder.loadTexts:
    sonusDs0AdmnEntry.setStatus("current")
_SonusDs0AdmnShelfIndex_Type = Integer32
_SonusDs0AdmnShelfIndex_Object = MibTableColumn
sonusDs0AdmnShelfIndex = _SonusDs0AdmnShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 3, 1, 1),
    _SonusDs0AdmnShelfIndex_Type()
)
sonusDs0AdmnShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDs0AdmnShelfIndex.setStatus("current")
_SonusDs0AdmnSlotIndex_Type = Integer32
_SonusDs0AdmnSlotIndex_Object = MibTableColumn
sonusDs0AdmnSlotIndex = _SonusDs0AdmnSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 3, 1, 2),
    _SonusDs0AdmnSlotIndex_Type()
)
sonusDs0AdmnSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDs0AdmnSlotIndex.setStatus("current")
_SonusDs0AdmnPortIndex_Type = Integer32
_SonusDs0AdmnPortIndex_Object = MibTableColumn
sonusDs0AdmnPortIndex = _SonusDs0AdmnPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 3, 1, 3),
    _SonusDs0AdmnPortIndex_Type()
)
sonusDs0AdmnPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDs0AdmnPortIndex.setStatus("current")
_SonusDs0AdmnDs3Index_Type = Integer32
_SonusDs0AdmnDs3Index_Object = MibTableColumn
sonusDs0AdmnDs3Index = _SonusDs0AdmnDs3Index_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 3, 1, 4),
    _SonusDs0AdmnDs3Index_Type()
)
sonusDs0AdmnDs3Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDs0AdmnDs3Index.setStatus("current")
_SonusDs0AdmnDs1Index_Type = Integer32
_SonusDs0AdmnDs1Index_Object = MibTableColumn
sonusDs0AdmnDs1Index = _SonusDs0AdmnDs1Index_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 3, 1, 5),
    _SonusDs0AdmnDs1Index_Type()
)
sonusDs0AdmnDs1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDs0AdmnDs1Index.setStatus("current")
_SonusDs0AdmnDs0Index_Type = Integer32
_SonusDs0AdmnDs0Index_Object = MibTableColumn
sonusDs0AdmnDs0Index = _SonusDs0AdmnDs0Index_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 3, 1, 6),
    _SonusDs0AdmnDs0Index_Type()
)
sonusDs0AdmnDs0Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDs0AdmnDs0Index.setStatus("current")


class _SonusDs0AdmnTimeout_Type(Integer32):
    """Custom type sonusDs0AdmnTimeout based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_SonusDs0AdmnTimeout_Type.__name__ = "Integer32"
_SonusDs0AdmnTimeout_Object = MibTableColumn
sonusDs0AdmnTimeout = _SonusDs0AdmnTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 3, 1, 7),
    _SonusDs0AdmnTimeout_Type()
)
sonusDs0AdmnTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs0AdmnTimeout.setStatus("current")


class _SonusDs0AdmnMode_Type(SonusServiceState):
    """Custom type sonusDs0AdmnMode based on SonusServiceState"""


_SonusDs0AdmnMode_Object = MibTableColumn
sonusDs0AdmnMode = _SonusDs0AdmnMode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 3, 1, 8),
    _SonusDs0AdmnMode_Type()
)
sonusDs0AdmnMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs0AdmnMode.setStatus("current")


class _SonusDs0AdmnAction_Type(SonusAdminAction):
    """Custom type sonusDs0AdmnAction based on SonusAdminAction"""


_SonusDs0AdmnAction_Object = MibTableColumn
sonusDs0AdmnAction = _SonusDs0AdmnAction_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 3, 1, 9),
    _SonusDs0AdmnAction_Type()
)
sonusDs0AdmnAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs0AdmnAction.setStatus("current")


class _SonusDs0AdmnState_Type(Integer32):
    """Custom type sonusDs0AdmnState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 2),
          ("unavailable", 1))
    )


_SonusDs0AdmnState_Type.__name__ = "Integer32"
_SonusDs0AdmnState_Object = MibTableColumn
sonusDs0AdmnState = _SonusDs0AdmnState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 3, 1, 10),
    _SonusDs0AdmnState_Type()
)
sonusDs0AdmnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs0AdmnState.setStatus("current")


class _SonusDs0AdmnIdleCode_Type(Integer32):
    """Custom type sonusDs0AdmnIdleCode based on Integer32"""
    defaultValue = 127

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SonusDs0AdmnIdleCode_Type.__name__ = "Integer32"
_SonusDs0AdmnIdleCode_Object = MibTableColumn
sonusDs0AdmnIdleCode = _SonusDs0AdmnIdleCode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 3, 1, 11),
    _SonusDs0AdmnIdleCode_Type()
)
sonusDs0AdmnIdleCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs0AdmnIdleCode.setStatus("current")


class _SonusDs0AdmnTone_Type(Integer32):
    """Custom type sonusDs0AdmnTone based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dmw", 2),
          ("none", 1))
    )


_SonusDs0AdmnTone_Type.__name__ = "Integer32"
_SonusDs0AdmnTone_Object = MibTableColumn
sonusDs0AdmnTone = _SonusDs0AdmnTone_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 3, 1, 12),
    _SonusDs0AdmnTone_Type()
)
sonusDs0AdmnTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs0AdmnTone.setStatus("current")


class _SonusDs0AdmnLoopback_Type(Integer32):
    """Custom type sonusDs0AdmnLoopback based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SonusDs0AdmnLoopback_Type.__name__ = "Integer32"
_SonusDs0AdmnLoopback_Object = MibTableColumn
sonusDs0AdmnLoopback = _SonusDs0AdmnLoopback_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 3, 1, 13),
    _SonusDs0AdmnLoopback_Type()
)
sonusDs0AdmnLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs0AdmnLoopback.setStatus("current")
_SonusDs1Profile_ObjectIdentity = ObjectIdentity
sonusDs1Profile = _SonusDs1Profile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4)
)
_SonusDs1ProfileNextIndex_Type = Integer32
_SonusDs1ProfileNextIndex_Object = MibScalar
sonusDs1ProfileNextIndex = _SonusDs1ProfileNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 1),
    _SonusDs1ProfileNextIndex_Type()
)
sonusDs1ProfileNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDs1ProfileNextIndex.setStatus("current")
_SonusDs1ProfileTable_Object = MibTable
sonusDs1ProfileTable = _SonusDs1ProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    sonusDs1ProfileTable.setStatus("current")
_SonusDs1ProfileEntry_Object = MibTableRow
sonusDs1ProfileEntry = _SonusDs1ProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1)
)
sonusDs1ProfileEntry.setIndexNames(
    (0, "SONUS-DS1-MIB", "sonusDs1ProfileIndex"),
)
if mibBuilder.loadTexts:
    sonusDs1ProfileEntry.setStatus("current")
_SonusDs1ProfileRowStatus_Type = RowStatus
_SonusDs1ProfileRowStatus_Object = MibTableColumn
sonusDs1ProfileRowStatus = _SonusDs1ProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 1),
    _SonusDs1ProfileRowStatus_Type()
)
sonusDs1ProfileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileRowStatus.setStatus("current")
_SonusDs1ProfileName_Type = SonusName
_SonusDs1ProfileName_Object = MibTableColumn
sonusDs1ProfileName = _SonusDs1ProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 2),
    _SonusDs1ProfileName_Type()
)
sonusDs1ProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileName.setStatus("current")
_SonusDs1ProfileIndex_Type = Integer32
_SonusDs1ProfileIndex_Object = MibTableColumn
sonusDs1ProfileIndex = _SonusDs1ProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 3),
    _SonusDs1ProfileIndex_Type()
)
sonusDs1ProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDs1ProfileIndex.setStatus("current")


class _SonusDs1ProfileState_Type(SonusAdminState):
    """Custom type sonusDs1ProfileState based on SonusAdminState"""


_SonusDs1ProfileState_Object = MibTableColumn
sonusDs1ProfileState = _SonusDs1ProfileState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 4),
    _SonusDs1ProfileState_Type()
)
sonusDs1ProfileState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileState.setStatus("current")


class _SonusDs1ProfileDs1LineBO_Type(Integer32):
    """Custom type sonusDs1ProfileDs1LineBO based on Integer32"""
    defaultValue = 2

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
              8)
        )
    )
    namedValues = NamedValues(
        *(("buildOut0to110", 1),
          ("buildOut110to220", 2),
          ("buildOut120Ohms", 7),
          ("buildOut220to330", 3),
          ("buildOut330to440", 4),
          ("buildOut440to550", 5),
          ("buildOut550to660", 6),
          ("buildOut75Ohms", 8))
    )


_SonusDs1ProfileDs1LineBO_Type.__name__ = "Integer32"
_SonusDs1ProfileDs1LineBO_Object = MibTableColumn
sonusDs1ProfileDs1LineBO = _SonusDs1ProfileDs1LineBO_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 5),
    _SonusDs1ProfileDs1LineBO_Type()
)
sonusDs1ProfileDs1LineBO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileDs1LineBO.setStatus("current")


class _SonusDs1ProfileDs1LineType_Type(Integer32):
    """Custom type sonusDs1ProfileDs1LineType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("d4", 3),
          ("e1", 4),
          ("e1crc", 5),
          ("esf", 2))
    )


_SonusDs1ProfileDs1LineType_Type.__name__ = "Integer32"
_SonusDs1ProfileDs1LineType_Object = MibTableColumn
sonusDs1ProfileDs1LineType = _SonusDs1ProfileDs1LineType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 6),
    _SonusDs1ProfileDs1LineType_Type()
)
sonusDs1ProfileDs1LineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileDs1LineType.setStatus("current")


class _SonusDs1ProfileDs1LineCoding_Type(Integer32):
    """Custom type sonusDs1ProfileDs1LineCoding based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ami", 5),
          ("b8zs", 2),
          ("hdb3", 3))
    )


_SonusDs1ProfileDs1LineCoding_Type.__name__ = "Integer32"
_SonusDs1ProfileDs1LineCoding_Object = MibTableColumn
sonusDs1ProfileDs1LineCoding = _SonusDs1ProfileDs1LineCoding_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 7),
    _SonusDs1ProfileDs1LineCoding_Type()
)
sonusDs1ProfileDs1LineCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileDs1LineCoding.setStatus("current")


class _SonusDs1ProfileDs1SignalMode_Type(Integer32):
    """Custom type sonusDs1ProfileDs1SignalMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("none", 1)
    )


_SonusDs1ProfileDs1SignalMode_Type.__name__ = "Integer32"
_SonusDs1ProfileDs1SignalMode_Object = MibTableColumn
sonusDs1ProfileDs1SignalMode = _SonusDs1ProfileDs1SignalMode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 8),
    _SonusDs1ProfileDs1SignalMode_Type()
)
sonusDs1ProfileDs1SignalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileDs1SignalMode.setStatus("current")


class _SonusDs1ProfileDs1Fdl_Type(Integer32):
    """Custom type sonusDs1ProfileDs1Fdl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ansi", 2),
          ("none", 8))
    )


_SonusDs1ProfileDs1Fdl_Type.__name__ = "Integer32"
_SonusDs1ProfileDs1Fdl_Object = MibTableColumn
sonusDs1ProfileDs1Fdl = _SonusDs1ProfileDs1Fdl_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 9),
    _SonusDs1ProfileDs1Fdl_Type()
)
sonusDs1ProfileDs1Fdl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileDs1Fdl.setStatus("current")


class _SonusDs1ProfileDs0IdleCode_Type(Integer32):
    """Custom type sonusDs1ProfileDs0IdleCode based on Integer32"""
    defaultValue = 127

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SonusDs1ProfileDs0IdleCode_Type.__name__ = "Integer32"
_SonusDs1ProfileDs0IdleCode_Object = MibTableColumn
sonusDs1ProfileDs0IdleCode = _SonusDs1ProfileDs0IdleCode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 10),
    _SonusDs1ProfileDs0IdleCode_Type()
)
sonusDs1ProfileDs0IdleCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileDs0IdleCode.setStatus("current")


class _SonusDs1ProfileAvailChannels_Type(Bits):
    """Custom type sonusDs1ProfileAvailChannels based on Bits"""
    namedValues = NamedValues(
        *(("channel1", 0),
          ("channel10", 9),
          ("channel11", 10),
          ("channel12", 11),
          ("channel13", 12),
          ("channel14", 13),
          ("channel15", 14),
          ("channel16", 15),
          ("channel17", 16),
          ("channel18", 17),
          ("channel19", 18),
          ("channel2", 1),
          ("channel20", 19),
          ("channel21", 20),
          ("channel22", 21),
          ("channel23", 22),
          ("channel24", 23),
          ("channel25", 24),
          ("channel26", 25),
          ("channel27", 26),
          ("channel28", 27),
          ("channel29", 28),
          ("channel3", 2),
          ("channel30", 29),
          ("channel31", 30),
          ("channel4", 3),
          ("channel5", 4),
          ("channel6", 5),
          ("channel7", 6),
          ("channel8", 7),
          ("channel9", 8))
    )

_SonusDs1ProfileAvailChannels_Type.__name__ = "Bits"
_SonusDs1ProfileAvailChannels_Object = MibTableColumn
sonusDs1ProfileAvailChannels = _SonusDs1ProfileAvailChannels_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 11),
    _SonusDs1ProfileAvailChannels_Type()
)
sonusDs1ProfileAvailChannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileAvailChannels.setStatus("current")


class _SonusDs1ProfileDs1LineBOState_Type(SonusAdminState):
    """Custom type sonusDs1ProfileDs1LineBOState based on SonusAdminState"""


_SonusDs1ProfileDs1LineBOState_Object = MibTableColumn
sonusDs1ProfileDs1LineBOState = _SonusDs1ProfileDs1LineBOState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 12),
    _SonusDs1ProfileDs1LineBOState_Type()
)
sonusDs1ProfileDs1LineBOState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileDs1LineBOState.setStatus("current")


class _SonusDs1ProfileDs1LineTypeState_Type(SonusAdminState):
    """Custom type sonusDs1ProfileDs1LineTypeState based on SonusAdminState"""


_SonusDs1ProfileDs1LineTypeState_Object = MibTableColumn
sonusDs1ProfileDs1LineTypeState = _SonusDs1ProfileDs1LineTypeState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 13),
    _SonusDs1ProfileDs1LineTypeState_Type()
)
sonusDs1ProfileDs1LineTypeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileDs1LineTypeState.setStatus("current")


class _SonusDs1ProfileDs1LineCodingState_Type(SonusAdminState):
    """Custom type sonusDs1ProfileDs1LineCodingState based on SonusAdminState"""


_SonusDs1ProfileDs1LineCodingState_Object = MibTableColumn
sonusDs1ProfileDs1LineCodingState = _SonusDs1ProfileDs1LineCodingState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 14),
    _SonusDs1ProfileDs1LineCodingState_Type()
)
sonusDs1ProfileDs1LineCodingState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileDs1LineCodingState.setStatus("current")


class _SonusDs1ProfileDs1SignalModeState_Type(SonusAdminState):
    """Custom type sonusDs1ProfileDs1SignalModeState based on SonusAdminState"""


_SonusDs1ProfileDs1SignalModeState_Object = MibTableColumn
sonusDs1ProfileDs1SignalModeState = _SonusDs1ProfileDs1SignalModeState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 15),
    _SonusDs1ProfileDs1SignalModeState_Type()
)
sonusDs1ProfileDs1SignalModeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileDs1SignalModeState.setStatus("current")


class _SonusDs1ProfileDs1FdlState_Type(SonusAdminState):
    """Custom type sonusDs1ProfileDs1FdlState based on SonusAdminState"""


_SonusDs1ProfileDs1FdlState_Object = MibTableColumn
sonusDs1ProfileDs1FdlState = _SonusDs1ProfileDs1FdlState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 16),
    _SonusDs1ProfileDs1FdlState_Type()
)
sonusDs1ProfileDs1FdlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileDs1FdlState.setStatus("current")


class _SonusDs1ProfileDs0IdleCodeState_Type(SonusAdminState):
    """Custom type sonusDs1ProfileDs0IdleCodeState based on SonusAdminState"""


_SonusDs1ProfileDs0IdleCodeState_Object = MibTableColumn
sonusDs1ProfileDs0IdleCodeState = _SonusDs1ProfileDs0IdleCodeState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 17),
    _SonusDs1ProfileDs0IdleCodeState_Type()
)
sonusDs1ProfileDs0IdleCodeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileDs0IdleCodeState.setStatus("current")


class _SonusDs1ProfileAvailChannelsState_Type(SonusAdminState):
    """Custom type sonusDs1ProfileAvailChannelsState based on SonusAdminState"""


_SonusDs1ProfileAvailChannelsState_Object = MibTableColumn
sonusDs1ProfileAvailChannelsState = _SonusDs1ProfileAvailChannelsState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 18),
    _SonusDs1ProfileAvailChannelsState_Type()
)
sonusDs1ProfileAvailChannelsState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileAvailChannelsState.setStatus("current")


class _SonusDs1ProfileType_Type(Integer32):
    """Custom type sonusDs1ProfileType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e1", 2),
          ("t1", 1))
    )


_SonusDs1ProfileType_Type.__name__ = "Integer32"
_SonusDs1ProfileType_Object = MibTableColumn
sonusDs1ProfileType = _SonusDs1ProfileType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 19),
    _SonusDs1ProfileType_Type()
)
sonusDs1ProfileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileType.setStatus("current")


class _SonusDs1ProfileESThreshold_Type(Integer32):
    """Custom type sonusDs1ProfileESThreshold based on Integer32"""
    defaultValue = 65

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_SonusDs1ProfileESThreshold_Type.__name__ = "Integer32"
_SonusDs1ProfileESThreshold_Object = MibTableColumn
sonusDs1ProfileESThreshold = _SonusDs1ProfileESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 20),
    _SonusDs1ProfileESThreshold_Type()
)
sonusDs1ProfileESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileESThreshold.setStatus("current")


class _SonusDs1ProfileSESThreshold_Type(Integer32):
    """Custom type sonusDs1ProfileSESThreshold based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_SonusDs1ProfileSESThreshold_Type.__name__ = "Integer32"
_SonusDs1ProfileSESThreshold_Object = MibTableColumn
sonusDs1ProfileSESThreshold = _SonusDs1ProfileSESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 21),
    _SonusDs1ProfileSESThreshold_Type()
)
sonusDs1ProfileSESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileSESThreshold.setStatus("current")


class _SonusDs1ProfileCSSThreshold_Type(Integer32):
    """Custom type sonusDs1ProfileCSSThreshold based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_SonusDs1ProfileCSSThreshold_Type.__name__ = "Integer32"
_SonusDs1ProfileCSSThreshold_Object = MibTableColumn
sonusDs1ProfileCSSThreshold = _SonusDs1ProfileCSSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 22),
    _SonusDs1ProfileCSSThreshold_Type()
)
sonusDs1ProfileCSSThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileCSSThreshold.setStatus("current")


class _SonusDs1ProfileDayESThreshold_Type(Integer32):
    """Custom type sonusDs1ProfileDayESThreshold based on Integer32"""
    defaultValue = 648

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonusDs1ProfileDayESThreshold_Type.__name__ = "Integer32"
_SonusDs1ProfileDayESThreshold_Object = MibTableColumn
sonusDs1ProfileDayESThreshold = _SonusDs1ProfileDayESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 23),
    _SonusDs1ProfileDayESThreshold_Type()
)
sonusDs1ProfileDayESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileDayESThreshold.setStatus("current")


class _SonusDs1ProfileDaySESThreshold_Type(Integer32):
    """Custom type sonusDs1ProfileDaySESThreshold based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonusDs1ProfileDaySESThreshold_Type.__name__ = "Integer32"
_SonusDs1ProfileDaySESThreshold_Object = MibTableColumn
sonusDs1ProfileDaySESThreshold = _SonusDs1ProfileDaySESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 24),
    _SonusDs1ProfileDaySESThreshold_Type()
)
sonusDs1ProfileDaySESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileDaySESThreshold.setStatus("current")


class _SonusDs1ProfileDayCSSThreshold_Type(Integer32):
    """Custom type sonusDs1ProfileDayCSSThreshold based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonusDs1ProfileDayCSSThreshold_Type.__name__ = "Integer32"
_SonusDs1ProfileDayCSSThreshold_Object = MibTableColumn
sonusDs1ProfileDayCSSThreshold = _SonusDs1ProfileDayCSSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 25),
    _SonusDs1ProfileDayCSSThreshold_Type()
)
sonusDs1ProfileDayCSSThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileDayCSSThreshold.setStatus("current")


class _SonusDs1ProfileFarESThreshold_Type(Integer32):
    """Custom type sonusDs1ProfileFarESThreshold based on Integer32"""
    defaultValue = 65

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_SonusDs1ProfileFarESThreshold_Type.__name__ = "Integer32"
_SonusDs1ProfileFarESThreshold_Object = MibTableColumn
sonusDs1ProfileFarESThreshold = _SonusDs1ProfileFarESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 26),
    _SonusDs1ProfileFarESThreshold_Type()
)
sonusDs1ProfileFarESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileFarESThreshold.setStatus("current")


class _SonusDs1ProfileFarSESThreshold_Type(Integer32):
    """Custom type sonusDs1ProfileFarSESThreshold based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_SonusDs1ProfileFarSESThreshold_Type.__name__ = "Integer32"
_SonusDs1ProfileFarSESThreshold_Object = MibTableColumn
sonusDs1ProfileFarSESThreshold = _SonusDs1ProfileFarSESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 27),
    _SonusDs1ProfileFarSESThreshold_Type()
)
sonusDs1ProfileFarSESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileFarSESThreshold.setStatus("current")


class _SonusDs1ProfileFarDayESThreshold_Type(Integer32):
    """Custom type sonusDs1ProfileFarDayESThreshold based on Integer32"""
    defaultValue = 648

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonusDs1ProfileFarDayESThreshold_Type.__name__ = "Integer32"
_SonusDs1ProfileFarDayESThreshold_Object = MibTableColumn
sonusDs1ProfileFarDayESThreshold = _SonusDs1ProfileFarDayESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 28),
    _SonusDs1ProfileFarDayESThreshold_Type()
)
sonusDs1ProfileFarDayESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileFarDayESThreshold.setStatus("current")


class _SonusDs1ProfileFarDaySESThreshold_Type(Integer32):
    """Custom type sonusDs1ProfileFarDaySESThreshold based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonusDs1ProfileFarDaySESThreshold_Type.__name__ = "Integer32"
_SonusDs1ProfileFarDaySESThreshold_Object = MibTableColumn
sonusDs1ProfileFarDaySESThreshold = _SonusDs1ProfileFarDaySESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 29),
    _SonusDs1ProfileFarDaySESThreshold_Type()
)
sonusDs1ProfileFarDaySESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileFarDaySESThreshold.setStatus("current")


class _SonusDs1ProfilePCVThreshold_Type(Integer32):
    """Custom type sonusDs1ProfilePCVThreshold based on Integer32"""
    defaultValue = 13296

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_SonusDs1ProfilePCVThreshold_Type.__name__ = "Integer32"
_SonusDs1ProfilePCVThreshold_Object = MibTableColumn
sonusDs1ProfilePCVThreshold = _SonusDs1ProfilePCVThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 30),
    _SonusDs1ProfilePCVThreshold_Type()
)
sonusDs1ProfilePCVThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfilePCVThreshold.setStatus("current")


class _SonusDs1ProfileLCVThreshold_Type(Integer32):
    """Custom type sonusDs1ProfileLCVThreshold based on Integer32"""
    defaultValue = 13340

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_SonusDs1ProfileLCVThreshold_Type.__name__ = "Integer32"
_SonusDs1ProfileLCVThreshold_Object = MibTableColumn
sonusDs1ProfileLCVThreshold = _SonusDs1ProfileLCVThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 31),
    _SonusDs1ProfileLCVThreshold_Type()
)
sonusDs1ProfileLCVThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileLCVThreshold.setStatus("current")


class _SonusDs1ProfileUASThreshold_Type(Integer32):
    """Custom type sonusDs1ProfileUASThreshold based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_SonusDs1ProfileUASThreshold_Type.__name__ = "Integer32"
_SonusDs1ProfileUASThreshold_Object = MibTableColumn
sonusDs1ProfileUASThreshold = _SonusDs1ProfileUASThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 32),
    _SonusDs1ProfileUASThreshold_Type()
)
sonusDs1ProfileUASThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileUASThreshold.setStatus("current")


class _SonusDs1ProfileFarPCVThreshold_Type(Integer32):
    """Custom type sonusDs1ProfileFarPCVThreshold based on Integer32"""
    defaultValue = 72

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_SonusDs1ProfileFarPCVThreshold_Type.__name__ = "Integer32"
_SonusDs1ProfileFarPCVThreshold_Object = MibTableColumn
sonusDs1ProfileFarPCVThreshold = _SonusDs1ProfileFarPCVThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 33),
    _SonusDs1ProfileFarPCVThreshold_Type()
)
sonusDs1ProfileFarPCVThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileFarPCVThreshold.setStatus("current")


class _SonusDs1ProfileFarLCVThreshold_Type(Integer32):
    """Custom type sonusDs1ProfileFarLCVThreshold based on Integer32"""
    defaultValue = 72

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_SonusDs1ProfileFarLCVThreshold_Type.__name__ = "Integer32"
_SonusDs1ProfileFarLCVThreshold_Object = MibTableColumn
sonusDs1ProfileFarLCVThreshold = _SonusDs1ProfileFarLCVThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 34),
    _SonusDs1ProfileFarLCVThreshold_Type()
)
sonusDs1ProfileFarLCVThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileFarLCVThreshold.setStatus("current")


class _SonusDs1ProfileFarUASThreshold_Type(Integer32):
    """Custom type sonusDs1ProfileFarUASThreshold based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_SonusDs1ProfileFarUASThreshold_Type.__name__ = "Integer32"
_SonusDs1ProfileFarUASThreshold_Object = MibTableColumn
sonusDs1ProfileFarUASThreshold = _SonusDs1ProfileFarUASThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 35),
    _SonusDs1ProfileFarUASThreshold_Type()
)
sonusDs1ProfileFarUASThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileFarUASThreshold.setStatus("current")


class _SonusDs1ProfileDayPCVThreshold_Type(Integer32):
    """Custom type sonusDs1ProfileDayPCVThreshold based on Integer32"""
    defaultValue = 132960

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1048575),
    )


_SonusDs1ProfileDayPCVThreshold_Type.__name__ = "Integer32"
_SonusDs1ProfileDayPCVThreshold_Object = MibTableColumn
sonusDs1ProfileDayPCVThreshold = _SonusDs1ProfileDayPCVThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 36),
    _SonusDs1ProfileDayPCVThreshold_Type()
)
sonusDs1ProfileDayPCVThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileDayPCVThreshold.setStatus("current")


class _SonusDs1ProfileDayLCVThreshold_Type(Integer32):
    """Custom type sonusDs1ProfileDayLCVThreshold based on Integer32"""
    defaultValue = 133400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1048575),
    )


_SonusDs1ProfileDayLCVThreshold_Type.__name__ = "Integer32"
_SonusDs1ProfileDayLCVThreshold_Object = MibTableColumn
sonusDs1ProfileDayLCVThreshold = _SonusDs1ProfileDayLCVThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 37),
    _SonusDs1ProfileDayLCVThreshold_Type()
)
sonusDs1ProfileDayLCVThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileDayLCVThreshold.setStatus("current")


class _SonusDs1ProfileDayUASThreshold_Type(Integer32):
    """Custom type sonusDs1ProfileDayUASThreshold based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonusDs1ProfileDayUASThreshold_Type.__name__ = "Integer32"
_SonusDs1ProfileDayUASThreshold_Object = MibTableColumn
sonusDs1ProfileDayUASThreshold = _SonusDs1ProfileDayUASThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 38),
    _SonusDs1ProfileDayUASThreshold_Type()
)
sonusDs1ProfileDayUASThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileDayUASThreshold.setStatus("current")


class _SonusDs1ProfileFarDayPCVThreshold_Type(Integer32):
    """Custom type sonusDs1ProfileFarDayPCVThreshold based on Integer32"""
    defaultValue = 691

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1048575),
    )


_SonusDs1ProfileFarDayPCVThreshold_Type.__name__ = "Integer32"
_SonusDs1ProfileFarDayPCVThreshold_Object = MibTableColumn
sonusDs1ProfileFarDayPCVThreshold = _SonusDs1ProfileFarDayPCVThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 39),
    _SonusDs1ProfileFarDayPCVThreshold_Type()
)
sonusDs1ProfileFarDayPCVThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileFarDayPCVThreshold.setStatus("current")


class _SonusDs1ProfileFarDayLCVThreshold_Type(Integer32):
    """Custom type sonusDs1ProfileFarDayLCVThreshold based on Integer32"""
    defaultValue = 691

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1048575),
    )


_SonusDs1ProfileFarDayLCVThreshold_Type.__name__ = "Integer32"
_SonusDs1ProfileFarDayLCVThreshold_Object = MibTableColumn
sonusDs1ProfileFarDayLCVThreshold = _SonusDs1ProfileFarDayLCVThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 40),
    _SonusDs1ProfileFarDayLCVThreshold_Type()
)
sonusDs1ProfileFarDayLCVThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileFarDayLCVThreshold.setStatus("current")


class _SonusDs1ProfileFarDayUASThreshold_Type(Integer32):
    """Custom type sonusDs1ProfileFarDayUASThreshold based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonusDs1ProfileFarDayUASThreshold_Type.__name__ = "Integer32"
_SonusDs1ProfileFarDayUASThreshold_Object = MibTableColumn
sonusDs1ProfileFarDayUASThreshold = _SonusDs1ProfileFarDayUASThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 41),
    _SonusDs1ProfileFarDayUASThreshold_Type()
)
sonusDs1ProfileFarDayUASThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileFarDayUASThreshold.setStatus("current")


class _SonusDs1ProfileESThresholdState_Type(SonusAdminState):
    """Custom type sonusDs1ProfileESThresholdState based on SonusAdminState"""


_SonusDs1ProfileESThresholdState_Object = MibTableColumn
sonusDs1ProfileESThresholdState = _SonusDs1ProfileESThresholdState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 42),
    _SonusDs1ProfileESThresholdState_Type()
)
sonusDs1ProfileESThresholdState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileESThresholdState.setStatus("current")


class _SonusDs1ProfileSESThresholdState_Type(SonusAdminState):
    """Custom type sonusDs1ProfileSESThresholdState based on SonusAdminState"""


_SonusDs1ProfileSESThresholdState_Object = MibTableColumn
sonusDs1ProfileSESThresholdState = _SonusDs1ProfileSESThresholdState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 43),
    _SonusDs1ProfileSESThresholdState_Type()
)
sonusDs1ProfileSESThresholdState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileSESThresholdState.setStatus("current")


class _SonusDs1ProfileCSSThresholdState_Type(SonusAdminState):
    """Custom type sonusDs1ProfileCSSThresholdState based on SonusAdminState"""


_SonusDs1ProfileCSSThresholdState_Object = MibTableColumn
sonusDs1ProfileCSSThresholdState = _SonusDs1ProfileCSSThresholdState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 44),
    _SonusDs1ProfileCSSThresholdState_Type()
)
sonusDs1ProfileCSSThresholdState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileCSSThresholdState.setStatus("current")


class _SonusDs1ProfileDayESThresholdState_Type(SonusAdminState):
    """Custom type sonusDs1ProfileDayESThresholdState based on SonusAdminState"""


_SonusDs1ProfileDayESThresholdState_Object = MibTableColumn
sonusDs1ProfileDayESThresholdState = _SonusDs1ProfileDayESThresholdState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 45),
    _SonusDs1ProfileDayESThresholdState_Type()
)
sonusDs1ProfileDayESThresholdState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileDayESThresholdState.setStatus("current")


class _SonusDs1ProfileDaySESThresholdState_Type(SonusAdminState):
    """Custom type sonusDs1ProfileDaySESThresholdState based on SonusAdminState"""


_SonusDs1ProfileDaySESThresholdState_Object = MibTableColumn
sonusDs1ProfileDaySESThresholdState = _SonusDs1ProfileDaySESThresholdState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 46),
    _SonusDs1ProfileDaySESThresholdState_Type()
)
sonusDs1ProfileDaySESThresholdState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileDaySESThresholdState.setStatus("current")


class _SonusDs1ProfileDayCSSThresholdState_Type(SonusAdminState):
    """Custom type sonusDs1ProfileDayCSSThresholdState based on SonusAdminState"""


_SonusDs1ProfileDayCSSThresholdState_Object = MibTableColumn
sonusDs1ProfileDayCSSThresholdState = _SonusDs1ProfileDayCSSThresholdState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 47),
    _SonusDs1ProfileDayCSSThresholdState_Type()
)
sonusDs1ProfileDayCSSThresholdState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileDayCSSThresholdState.setStatus("current")


class _SonusDs1ProfileFarESThresholdState_Type(SonusAdminState):
    """Custom type sonusDs1ProfileFarESThresholdState based on SonusAdminState"""


_SonusDs1ProfileFarESThresholdState_Object = MibTableColumn
sonusDs1ProfileFarESThresholdState = _SonusDs1ProfileFarESThresholdState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 48),
    _SonusDs1ProfileFarESThresholdState_Type()
)
sonusDs1ProfileFarESThresholdState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileFarESThresholdState.setStatus("current")


class _SonusDs1ProfileFarSESThresholdState_Type(SonusAdminState):
    """Custom type sonusDs1ProfileFarSESThresholdState based on SonusAdminState"""


_SonusDs1ProfileFarSESThresholdState_Object = MibTableColumn
sonusDs1ProfileFarSESThresholdState = _SonusDs1ProfileFarSESThresholdState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 49),
    _SonusDs1ProfileFarSESThresholdState_Type()
)
sonusDs1ProfileFarSESThresholdState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileFarSESThresholdState.setStatus("current")


class _SonusDs1ProfileFarDayESThresholdState_Type(SonusAdminState):
    """Custom type sonusDs1ProfileFarDayESThresholdState based on SonusAdminState"""


_SonusDs1ProfileFarDayESThresholdState_Object = MibTableColumn
sonusDs1ProfileFarDayESThresholdState = _SonusDs1ProfileFarDayESThresholdState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 50),
    _SonusDs1ProfileFarDayESThresholdState_Type()
)
sonusDs1ProfileFarDayESThresholdState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileFarDayESThresholdState.setStatus("current")


class _SonusDs1ProfileFarDaySESThresholdState_Type(SonusAdminState):
    """Custom type sonusDs1ProfileFarDaySESThresholdState based on SonusAdminState"""


_SonusDs1ProfileFarDaySESThresholdState_Object = MibTableColumn
sonusDs1ProfileFarDaySESThresholdState = _SonusDs1ProfileFarDaySESThresholdState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 51),
    _SonusDs1ProfileFarDaySESThresholdState_Type()
)
sonusDs1ProfileFarDaySESThresholdState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileFarDaySESThresholdState.setStatus("current")


class _SonusDs1ProfilePCVThresholdState_Type(SonusAdminState):
    """Custom type sonusDs1ProfilePCVThresholdState based on SonusAdminState"""


_SonusDs1ProfilePCVThresholdState_Object = MibTableColumn
sonusDs1ProfilePCVThresholdState = _SonusDs1ProfilePCVThresholdState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 52),
    _SonusDs1ProfilePCVThresholdState_Type()
)
sonusDs1ProfilePCVThresholdState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfilePCVThresholdState.setStatus("current")


class _SonusDs1ProfileLCVThresholdState_Type(SonusAdminState):
    """Custom type sonusDs1ProfileLCVThresholdState based on SonusAdminState"""


_SonusDs1ProfileLCVThresholdState_Object = MibTableColumn
sonusDs1ProfileLCVThresholdState = _SonusDs1ProfileLCVThresholdState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 53),
    _SonusDs1ProfileLCVThresholdState_Type()
)
sonusDs1ProfileLCVThresholdState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileLCVThresholdState.setStatus("current")


class _SonusDs1ProfileUASThresholdState_Type(SonusAdminState):
    """Custom type sonusDs1ProfileUASThresholdState based on SonusAdminState"""


_SonusDs1ProfileUASThresholdState_Object = MibTableColumn
sonusDs1ProfileUASThresholdState = _SonusDs1ProfileUASThresholdState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 54),
    _SonusDs1ProfileUASThresholdState_Type()
)
sonusDs1ProfileUASThresholdState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileUASThresholdState.setStatus("current")


class _SonusDs1ProfileFarPCVThresholdState_Type(SonusAdminState):
    """Custom type sonusDs1ProfileFarPCVThresholdState based on SonusAdminState"""


_SonusDs1ProfileFarPCVThresholdState_Object = MibTableColumn
sonusDs1ProfileFarPCVThresholdState = _SonusDs1ProfileFarPCVThresholdState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 55),
    _SonusDs1ProfileFarPCVThresholdState_Type()
)
sonusDs1ProfileFarPCVThresholdState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileFarPCVThresholdState.setStatus("current")


class _SonusDs1ProfileFarLCVThresholdState_Type(SonusAdminState):
    """Custom type sonusDs1ProfileFarLCVThresholdState based on SonusAdminState"""


_SonusDs1ProfileFarLCVThresholdState_Object = MibTableColumn
sonusDs1ProfileFarLCVThresholdState = _SonusDs1ProfileFarLCVThresholdState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 56),
    _SonusDs1ProfileFarLCVThresholdState_Type()
)
sonusDs1ProfileFarLCVThresholdState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileFarLCVThresholdState.setStatus("current")


class _SonusDs1ProfileFarUASThresholdState_Type(SonusAdminState):
    """Custom type sonusDs1ProfileFarUASThresholdState based on SonusAdminState"""


_SonusDs1ProfileFarUASThresholdState_Object = MibTableColumn
sonusDs1ProfileFarUASThresholdState = _SonusDs1ProfileFarUASThresholdState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 57),
    _SonusDs1ProfileFarUASThresholdState_Type()
)
sonusDs1ProfileFarUASThresholdState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileFarUASThresholdState.setStatus("current")


class _SonusDs1ProfileDayPCVThresholdState_Type(SonusAdminState):
    """Custom type sonusDs1ProfileDayPCVThresholdState based on SonusAdminState"""


_SonusDs1ProfileDayPCVThresholdState_Object = MibTableColumn
sonusDs1ProfileDayPCVThresholdState = _SonusDs1ProfileDayPCVThresholdState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 58),
    _SonusDs1ProfileDayPCVThresholdState_Type()
)
sonusDs1ProfileDayPCVThresholdState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileDayPCVThresholdState.setStatus("current")


class _SonusDs1ProfileDayLCVThresholdState_Type(SonusAdminState):
    """Custom type sonusDs1ProfileDayLCVThresholdState based on SonusAdminState"""


_SonusDs1ProfileDayLCVThresholdState_Object = MibTableColumn
sonusDs1ProfileDayLCVThresholdState = _SonusDs1ProfileDayLCVThresholdState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 59),
    _SonusDs1ProfileDayLCVThresholdState_Type()
)
sonusDs1ProfileDayLCVThresholdState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileDayLCVThresholdState.setStatus("current")


class _SonusDs1ProfileDayUASThresholdState_Type(SonusAdminState):
    """Custom type sonusDs1ProfileDayUASThresholdState based on SonusAdminState"""


_SonusDs1ProfileDayUASThresholdState_Object = MibTableColumn
sonusDs1ProfileDayUASThresholdState = _SonusDs1ProfileDayUASThresholdState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 60),
    _SonusDs1ProfileDayUASThresholdState_Type()
)
sonusDs1ProfileDayUASThresholdState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileDayUASThresholdState.setStatus("current")


class _SonusDs1ProfileFarDayPCVThresholdState_Type(SonusAdminState):
    """Custom type sonusDs1ProfileFarDayPCVThresholdState based on SonusAdminState"""


_SonusDs1ProfileFarDayPCVThresholdState_Object = MibTableColumn
sonusDs1ProfileFarDayPCVThresholdState = _SonusDs1ProfileFarDayPCVThresholdState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 61),
    _SonusDs1ProfileFarDayPCVThresholdState_Type()
)
sonusDs1ProfileFarDayPCVThresholdState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileFarDayPCVThresholdState.setStatus("current")


class _SonusDs1ProfileFarDayLCVThresholdState_Type(SonusAdminState):
    """Custom type sonusDs1ProfileFarDayLCVThresholdState based on SonusAdminState"""


_SonusDs1ProfileFarDayLCVThresholdState_Object = MibTableColumn
sonusDs1ProfileFarDayLCVThresholdState = _SonusDs1ProfileFarDayLCVThresholdState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 62),
    _SonusDs1ProfileFarDayLCVThresholdState_Type()
)
sonusDs1ProfileFarDayLCVThresholdState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileFarDayLCVThresholdState.setStatus("current")


class _SonusDs1ProfileFarDayUASThresholdState_Type(SonusAdminState):
    """Custom type sonusDs1ProfileFarDayUASThresholdState based on SonusAdminState"""


_SonusDs1ProfileFarDayUASThresholdState_Object = MibTableColumn
sonusDs1ProfileFarDayUASThresholdState = _SonusDs1ProfileFarDayUASThresholdState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 1, 4, 2, 1, 63),
    _SonusDs1ProfileFarDayUASThresholdState_Type()
)
sonusDs1ProfileFarDayUASThresholdState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDs1ProfileFarDayUASThresholdState.setStatus("current")
_SonusDsx1MIBNotifications_ObjectIdentity = ObjectIdentity
sonusDsx1MIBNotifications = _SonusDsx1MIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 2)
)
_SonusDsx1MIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
sonusDsx1MIBNotificationsPrefix = _SonusDsx1MIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 2, 0)
)
_SonusDsx1MIBNotificationsObjects_ObjectIdentity = ObjectIdentity
sonusDsx1MIBNotificationsObjects = _SonusDsx1MIBNotificationsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 2, 1)
)


class _SonusDs1OutOfServiceReason_Type(Integer32):
    """Custom type sonusDs1OutOfServiceReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("maintenance", 1)
    )


_SonusDs1OutOfServiceReason_Type.__name__ = "Integer32"
_SonusDs1OutOfServiceReason_Object = MibScalar
sonusDs1OutOfServiceReason = _SonusDs1OutOfServiceReason_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 2, 1, 1),
    _SonusDs1OutOfServiceReason_Type()
)
sonusDs1OutOfServiceReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDs1OutOfServiceReason.setStatus("current")


class _SonusDs1OutOfServiceType_Type(Integer32):
    """Custom type sonusDs1OutOfServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("admin", 1),
          ("hwFailure", 2))
    )


_SonusDs1OutOfServiceType_Type.__name__ = "Integer32"
_SonusDs1OutOfServiceType_Object = MibScalar
sonusDs1OutOfServiceType = _SonusDs1OutOfServiceType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 2, 1, 2),
    _SonusDs1OutOfServiceType_Type()
)
sonusDs1OutOfServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDs1OutOfServiceType.setStatus("current")


class _SonusDs1ThresholdType_Type(Integer32):
    """Custom type sonusDs1ThresholdType based on Integer32"""
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
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("currentControlledSlips", 4),
          ("currentErroredSeconds", 5),
          ("currentFarEndErroredSeconds", 15),
          ("currentFarEndSeverelyErrSeconds", 16),
          ("currentFarEndUnavailableSeconds", 19),
          ("currentLineCodeViolation", 1),
          ("currentPathCodeViolation", 2),
          ("currentPathCodeViolationFarEnd", 3),
          ("currentSeverelyErrSeconds", 6),
          ("currentUnavailableSeconds", 7),
          ("totalControlledSlips", 11),
          ("totalErroredSeconds", 12),
          ("totalFarEndCurrentSeverelyErrSeconds", 18),
          ("totalFarEndErroredSeconds", 17),
          ("totalFarEndUnavailableSeconds", 20),
          ("totalLineCodeViolation", 8),
          ("totalPathCodeViolation", 9),
          ("totalPathCodeViolationFarEnd", 10),
          ("totalSeverelyErrSeconds", 13),
          ("totalUnavailableSeconds", 14))
    )


_SonusDs1ThresholdType_Type.__name__ = "Integer32"
_SonusDs1ThresholdType_Object = MibScalar
sonusDs1ThresholdType = _SonusDs1ThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 2, 1, 3),
    _SonusDs1ThresholdType_Type()
)
sonusDs1ThresholdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDs1ThresholdType.setStatus("current")


class _SonusDs1LineState_Type(Integer32):
    """Custom type sonusDs1LineState based on Integer32"""
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
        *(("ais", 4),
          ("green", 1),
          ("hwfailure", 5),
          ("red", 2),
          ("yellow", 3))
    )


_SonusDs1LineState_Type.__name__ = "Integer32"
_SonusDs1LineState_Object = MibScalar
sonusDs1LineState = _SonusDs1LineState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 2, 1, 4),
    _SonusDs1LineState_Type()
)
sonusDs1LineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDs1LineState.setStatus("current")


class _SonusDs1AdmnState_Type(Integer32):
    """Custom type sonusDs1AdmnState based on Integer32"""
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
        *(("deleted", 3),
          ("disabled", 1),
          ("dryingUp", 5),
          ("enabled", 2),
          ("inservice", 4))
    )


_SonusDs1AdmnState_Type.__name__ = "Integer32"
_SonusDs1AdmnState_Object = MibScalar
sonusDs1AdmnState = _SonusDs1AdmnState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 2, 1, 5),
    _SonusDs1AdmnState_Type()
)
sonusDs1AdmnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDs1AdmnState.setStatus("current")

# Managed Objects groups


# Notification objects

sonusDsx1AdminChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 2, 0, 1)
)
sonusDsx1AdminChangeNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusPortIndex"),
        ("SONUS-COMMON-MIB", "sonusDs3Index"),
        ("SONUS-COMMON-MIB", "sonusDs1Index"),
        ("SONUS-DS1-MIB", "sonusDs1AdmnState"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusDsx1AdminChangeNotification.setStatus(
        "current"
    )

sonusDsx1OutOfServiceNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 2, 0, 2)
)
sonusDsx1OutOfServiceNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusPortIndex"),
        ("SONUS-COMMON-MIB", "sonusDs3Index"),
        ("SONUS-COMMON-MIB", "sonusDs1Index"),
        ("SONUS-DS1-MIB", "sonusDs1OutOfServiceReason"),
        ("SONUS-DS1-MIB", "sonusDs1OutOfServiceType"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusDsx1OutOfServiceNotification.setStatus(
        "current"
    )

sonusDsx1ThresholdCrossingNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 2, 0, 3)
)
sonusDsx1ThresholdCrossingNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusPortIndex"),
        ("SONUS-COMMON-MIB", "sonusDs3Index"),
        ("SONUS-COMMON-MIB", "sonusDs1Index"),
        ("SONUS-DS1-MIB", "sonusDs1ThresholdType"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusDsx1ThresholdCrossingNotification.setStatus(
        "current"
    )

sonusDsx1LineStatusChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4, 1, 2, 0, 4)
)
sonusDsx1LineStatusChangeNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusPortIndex"),
        ("SONUS-COMMON-MIB", "sonusDs3Index"),
        ("SONUS-COMMON-MIB", "sonusDs1Index"),
        ("SONUS-DS1-MIB", "sonusDs1LineState"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusDsx1LineStatusChangeNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONUS-DS1-MIB",
    **{"sonusDsx1MIB": sonusDsx1MIB,
       "sonusDsx1MIBObjects": sonusDsx1MIBObjects,
       "sonusDsx1Admn": sonusDsx1Admn,
       "sonusDsx1AdmnNextIndex": sonusDsx1AdmnNextIndex,
       "sonusDsx1AdmnTable": sonusDsx1AdmnTable,
       "sonusDsx1AdmnEntry": sonusDsx1AdmnEntry,
       "sonusDsx1AdmnRowStatus": sonusDsx1AdmnRowStatus,
       "sonusDsx1AdmnName": sonusDsx1AdmnName,
       "sonusDsx1AdmnProfileName": sonusDsx1AdmnProfileName,
       "sonusDsx1AdmnShelfIndex": sonusDsx1AdmnShelfIndex,
       "sonusDsx1AdmnSlotIndex": sonusDsx1AdmnSlotIndex,
       "sonusDsx1AdmnPortIndex": sonusDsx1AdmnPortIndex,
       "sonusDsx1AdmnDs3Index": sonusDsx1AdmnDs3Index,
       "sonusDsx1AdmnDs1Index": sonusDsx1AdmnDs1Index,
       "sonusDsx1AdmnIfIndex": sonusDsx1AdmnIfIndex,
       "sonusDsx1AdmnState": sonusDsx1AdmnState,
       "sonusDsx1AdmnLineBuildOut": sonusDsx1AdmnLineBuildOut,
       "sonusDsx1AdmnTimeout": sonusDsx1AdmnTimeout,
       "sonusDsx1AdmnMode": sonusDsx1AdmnMode,
       "sonusDsx1AdmnAction": sonusDsx1AdmnAction,
       "sonusDsx1AdmnIdleCode": sonusDsx1AdmnIdleCode,
       "sonusDsx1AdmnAvailChannels": sonusDsx1AdmnAvailChannels,
       "sonusDsx1AdmnType": sonusDsx1AdmnType,
       "sonusDsx1AdmnESThreshold": sonusDsx1AdmnESThreshold,
       "sonusDsx1AdmnSESThreshold": sonusDsx1AdmnSESThreshold,
       "sonusDsx1AdmnCSSThreshold": sonusDsx1AdmnCSSThreshold,
       "sonusDsx1AdmnDayESThreshold": sonusDsx1AdmnDayESThreshold,
       "sonusDsx1AdmnDaySESThreshold": sonusDsx1AdmnDaySESThreshold,
       "sonusDsx1AdmnDayCSSThreshold": sonusDsx1AdmnDayCSSThreshold,
       "sonusDsx1AdmnFarESThreshold": sonusDsx1AdmnFarESThreshold,
       "sonusDsx1AdmnFarSESThreshold": sonusDsx1AdmnFarSESThreshold,
       "sonusDsx1AdmnFarDayESThreshold": sonusDsx1AdmnFarDayESThreshold,
       "sonusDsx1AdmnFarDaySESThreshold": sonusDsx1AdmnFarDaySESThreshold,
       "sonusDsx1AdmnPCVThreshold": sonusDsx1AdmnPCVThreshold,
       "sonusDsx1AdmnLCVThreshold": sonusDsx1AdmnLCVThreshold,
       "sonusDsx1AdmnUASThreshold": sonusDsx1AdmnUASThreshold,
       "sonusDsx1AdmnFarPCVThreshold": sonusDsx1AdmnFarPCVThreshold,
       "sonusDsx1AdmnFarLCVThreshold": sonusDsx1AdmnFarLCVThreshold,
       "sonusDsx1AdmnFarUASThreshold": sonusDsx1AdmnFarUASThreshold,
       "sonusDsx1AdmnDayPCVThreshold": sonusDsx1AdmnDayPCVThreshold,
       "sonusDsx1AdmnDayLCVThreshold": sonusDsx1AdmnDayLCVThreshold,
       "sonusDsx1AdmnDayUASThreshold": sonusDsx1AdmnDayUASThreshold,
       "sonusDsx1AdmnFarDayPCVThreshold": sonusDsx1AdmnFarDayPCVThreshold,
       "sonusDsx1AdmnFarDayLCVThreshold": sonusDsx1AdmnFarDayLCVThreshold,
       "sonusDsx1AdmnFarDayUASThreshold": sonusDsx1AdmnFarDayUASThreshold,
       "sonusDsx1AdmnInitCounters": sonusDsx1AdmnInitCounters,
       "sonusDsx1AdmnEchoProfileName": sonusDsx1AdmnEchoProfileName,
       "sonusDsx1AdmnEchoCancellorMaxTail": sonusDsx1AdmnEchoCancellorMaxTail,
       "sonusDsx1AdmnEchoCancellorAudioType": sonusDsx1AdmnEchoCancellorAudioType,
       "sonusDsx1AdmnEchoCancellorSignallingTone": sonusDsx1AdmnEchoCancellorSignallingTone,
       "sonusDsx1AdmnEchoCancellorNlpDisable": sonusDsx1AdmnEchoCancellorNlpDisable,
       "sonusDsx1AdmnEchoCancellorNlpEnable": sonusDsx1AdmnEchoCancellorNlpEnable,
       "sonusDsx1AdmnEchoCancellorReturnLoss": sonusDsx1AdmnEchoCancellorReturnLoss,
       "sonusDsx1AdmnEchoCancellorResidualEcho": sonusDsx1AdmnEchoCancellorResidualEcho,
       "sonusDsx1AdmnEchoCancellorHiLevelComp": sonusDsx1AdmnEchoCancellorHiLevelComp,
       "sonusDsx1AdmnEchoCancellorModemDisable": sonusDsx1AdmnEchoCancellorModemDisable,
       "sonusDsx1AdmnZeroSuppression": sonusDsx1AdmnZeroSuppression,
       "sonusDsx1AdmnCircuitId": sonusDsx1AdmnCircuitId,
       "sonusDsx1AdmnEchoCancellorNarrowbandDetection": sonusDsx1AdmnEchoCancellorNarrowbandDetection,
       "sonusDsx1StatTable": sonusDsx1StatTable,
       "sonusDsx1StatEntry": sonusDsx1StatEntry,
       "sonusDsx1StatShelfIndex": sonusDsx1StatShelfIndex,
       "sonusDsx1StatSlotIndex": sonusDsx1StatSlotIndex,
       "sonusDsx1StatPortIndex": sonusDsx1StatPortIndex,
       "sonusDsx1StatDs3Index": sonusDsx1StatDs3Index,
       "sonusDsx1StatDs1Index": sonusDsx1StatDs1Index,
       "sonusDsx1StatValidInt": sonusDsx1StatValidInt,
       "sonusDsx1StatRxSlips": sonusDsx1StatRxSlips,
       "sonusDsx1StatTxSlips": sonusDsx1StatTxSlips,
       "sonusDsx1StatLOF": sonusDsx1StatLOF,
       "sonusDsx1StatAIS": sonusDsx1StatAIS,
       "sonusDsx1StatRAI": sonusDsx1StatRAI,
       "sonusDsx1StatRED": sonusDsx1StatRED,
       "sonusDsx1StatCRC": sonusDsx1StatCRC,
       "sonusDsx1StatCOFA": sonusDsx1StatCOFA,
       "sonusDsx1StatFBE": sonusDsx1StatFBE,
       "sonusDsx1StatStatus": sonusDsx1StatStatus,
       "sonusDsx1StatAllocChannels": sonusDsx1StatAllocChannels,
       "sonusDsx1StatEnabChannels": sonusDsx1StatEnabChannels,
       "sonusE1StatLOMF": sonusE1StatLOMF,
       "sonusE1StatMFError": sonusE1StatMFError,
       "sonusE1StatFEBE": sonusE1StatFEBE,
       "sonusE1StatOOOF": sonusE1StatOOOF,
       "sonusE1StatC2NCIWCK": sonusE1StatC2NCIWCK,
       "sonusE1StatRAIContCRC": sonusE1StatRAIContCRC,
       "sonusE1StatContFEBE": sonusE1StatContFEBE,
       "sonusE1StatExcessCRC": sonusE1StatExcessCRC,
       "sonusE1StatFASErr": sonusE1StatFASErr,
       "sonusDsx1StatSendPattern": sonusDsx1StatSendPattern,
       "sonusDsx1StatStatusCode": sonusDsx1StatStatusCode,
       "sonusDsx1StatLoopbackStatus": sonusDsx1StatLoopbackStatus,
       "sonusDsx1StatOperStatus": sonusDsx1StatOperStatus,
       "sonusDs0AdmnTable": sonusDs0AdmnTable,
       "sonusDs0AdmnEntry": sonusDs0AdmnEntry,
       "sonusDs0AdmnShelfIndex": sonusDs0AdmnShelfIndex,
       "sonusDs0AdmnSlotIndex": sonusDs0AdmnSlotIndex,
       "sonusDs0AdmnPortIndex": sonusDs0AdmnPortIndex,
       "sonusDs0AdmnDs3Index": sonusDs0AdmnDs3Index,
       "sonusDs0AdmnDs1Index": sonusDs0AdmnDs1Index,
       "sonusDs0AdmnDs0Index": sonusDs0AdmnDs0Index,
       "sonusDs0AdmnTimeout": sonusDs0AdmnTimeout,
       "sonusDs0AdmnMode": sonusDs0AdmnMode,
       "sonusDs0AdmnAction": sonusDs0AdmnAction,
       "sonusDs0AdmnState": sonusDs0AdmnState,
       "sonusDs0AdmnIdleCode": sonusDs0AdmnIdleCode,
       "sonusDs0AdmnTone": sonusDs0AdmnTone,
       "sonusDs0AdmnLoopback": sonusDs0AdmnLoopback,
       "sonusDs1Profile": sonusDs1Profile,
       "sonusDs1ProfileNextIndex": sonusDs1ProfileNextIndex,
       "sonusDs1ProfileTable": sonusDs1ProfileTable,
       "sonusDs1ProfileEntry": sonusDs1ProfileEntry,
       "sonusDs1ProfileRowStatus": sonusDs1ProfileRowStatus,
       "sonusDs1ProfileName": sonusDs1ProfileName,
       "sonusDs1ProfileIndex": sonusDs1ProfileIndex,
       "sonusDs1ProfileState": sonusDs1ProfileState,
       "sonusDs1ProfileDs1LineBO": sonusDs1ProfileDs1LineBO,
       "sonusDs1ProfileDs1LineType": sonusDs1ProfileDs1LineType,
       "sonusDs1ProfileDs1LineCoding": sonusDs1ProfileDs1LineCoding,
       "sonusDs1ProfileDs1SignalMode": sonusDs1ProfileDs1SignalMode,
       "sonusDs1ProfileDs1Fdl": sonusDs1ProfileDs1Fdl,
       "sonusDs1ProfileDs0IdleCode": sonusDs1ProfileDs0IdleCode,
       "sonusDs1ProfileAvailChannels": sonusDs1ProfileAvailChannels,
       "sonusDs1ProfileDs1LineBOState": sonusDs1ProfileDs1LineBOState,
       "sonusDs1ProfileDs1LineTypeState": sonusDs1ProfileDs1LineTypeState,
       "sonusDs1ProfileDs1LineCodingState": sonusDs1ProfileDs1LineCodingState,
       "sonusDs1ProfileDs1SignalModeState": sonusDs1ProfileDs1SignalModeState,
       "sonusDs1ProfileDs1FdlState": sonusDs1ProfileDs1FdlState,
       "sonusDs1ProfileDs0IdleCodeState": sonusDs1ProfileDs0IdleCodeState,
       "sonusDs1ProfileAvailChannelsState": sonusDs1ProfileAvailChannelsState,
       "sonusDs1ProfileType": sonusDs1ProfileType,
       "sonusDs1ProfileESThreshold": sonusDs1ProfileESThreshold,
       "sonusDs1ProfileSESThreshold": sonusDs1ProfileSESThreshold,
       "sonusDs1ProfileCSSThreshold": sonusDs1ProfileCSSThreshold,
       "sonusDs1ProfileDayESThreshold": sonusDs1ProfileDayESThreshold,
       "sonusDs1ProfileDaySESThreshold": sonusDs1ProfileDaySESThreshold,
       "sonusDs1ProfileDayCSSThreshold": sonusDs1ProfileDayCSSThreshold,
       "sonusDs1ProfileFarESThreshold": sonusDs1ProfileFarESThreshold,
       "sonusDs1ProfileFarSESThreshold": sonusDs1ProfileFarSESThreshold,
       "sonusDs1ProfileFarDayESThreshold": sonusDs1ProfileFarDayESThreshold,
       "sonusDs1ProfileFarDaySESThreshold": sonusDs1ProfileFarDaySESThreshold,
       "sonusDs1ProfilePCVThreshold": sonusDs1ProfilePCVThreshold,
       "sonusDs1ProfileLCVThreshold": sonusDs1ProfileLCVThreshold,
       "sonusDs1ProfileUASThreshold": sonusDs1ProfileUASThreshold,
       "sonusDs1ProfileFarPCVThreshold": sonusDs1ProfileFarPCVThreshold,
       "sonusDs1ProfileFarLCVThreshold": sonusDs1ProfileFarLCVThreshold,
       "sonusDs1ProfileFarUASThreshold": sonusDs1ProfileFarUASThreshold,
       "sonusDs1ProfileDayPCVThreshold": sonusDs1ProfileDayPCVThreshold,
       "sonusDs1ProfileDayLCVThreshold": sonusDs1ProfileDayLCVThreshold,
       "sonusDs1ProfileDayUASThreshold": sonusDs1ProfileDayUASThreshold,
       "sonusDs1ProfileFarDayPCVThreshold": sonusDs1ProfileFarDayPCVThreshold,
       "sonusDs1ProfileFarDayLCVThreshold": sonusDs1ProfileFarDayLCVThreshold,
       "sonusDs1ProfileFarDayUASThreshold": sonusDs1ProfileFarDayUASThreshold,
       "sonusDs1ProfileESThresholdState": sonusDs1ProfileESThresholdState,
       "sonusDs1ProfileSESThresholdState": sonusDs1ProfileSESThresholdState,
       "sonusDs1ProfileCSSThresholdState": sonusDs1ProfileCSSThresholdState,
       "sonusDs1ProfileDayESThresholdState": sonusDs1ProfileDayESThresholdState,
       "sonusDs1ProfileDaySESThresholdState": sonusDs1ProfileDaySESThresholdState,
       "sonusDs1ProfileDayCSSThresholdState": sonusDs1ProfileDayCSSThresholdState,
       "sonusDs1ProfileFarESThresholdState": sonusDs1ProfileFarESThresholdState,
       "sonusDs1ProfileFarSESThresholdState": sonusDs1ProfileFarSESThresholdState,
       "sonusDs1ProfileFarDayESThresholdState": sonusDs1ProfileFarDayESThresholdState,
       "sonusDs1ProfileFarDaySESThresholdState": sonusDs1ProfileFarDaySESThresholdState,
       "sonusDs1ProfilePCVThresholdState": sonusDs1ProfilePCVThresholdState,
       "sonusDs1ProfileLCVThresholdState": sonusDs1ProfileLCVThresholdState,
       "sonusDs1ProfileUASThresholdState": sonusDs1ProfileUASThresholdState,
       "sonusDs1ProfileFarPCVThresholdState": sonusDs1ProfileFarPCVThresholdState,
       "sonusDs1ProfileFarLCVThresholdState": sonusDs1ProfileFarLCVThresholdState,
       "sonusDs1ProfileFarUASThresholdState": sonusDs1ProfileFarUASThresholdState,
       "sonusDs1ProfileDayPCVThresholdState": sonusDs1ProfileDayPCVThresholdState,
       "sonusDs1ProfileDayLCVThresholdState": sonusDs1ProfileDayLCVThresholdState,
       "sonusDs1ProfileDayUASThresholdState": sonusDs1ProfileDayUASThresholdState,
       "sonusDs1ProfileFarDayPCVThresholdState": sonusDs1ProfileFarDayPCVThresholdState,
       "sonusDs1ProfileFarDayLCVThresholdState": sonusDs1ProfileFarDayLCVThresholdState,
       "sonusDs1ProfileFarDayUASThresholdState": sonusDs1ProfileFarDayUASThresholdState,
       "sonusDsx1MIBNotifications": sonusDsx1MIBNotifications,
       "sonusDsx1MIBNotificationsPrefix": sonusDsx1MIBNotificationsPrefix,
       "sonusDsx1AdminChangeNotification": sonusDsx1AdminChangeNotification,
       "sonusDsx1OutOfServiceNotification": sonusDsx1OutOfServiceNotification,
       "sonusDsx1ThresholdCrossingNotification": sonusDsx1ThresholdCrossingNotification,
       "sonusDsx1LineStatusChangeNotification": sonusDsx1LineStatusChangeNotification,
       "sonusDsx1MIBNotificationsObjects": sonusDsx1MIBNotificationsObjects,
       "sonusDs1OutOfServiceReason": sonusDs1OutOfServiceReason,
       "sonusDs1OutOfServiceType": sonusDs1OutOfServiceType,
       "sonusDs1ThresholdType": sonusDs1ThresholdType,
       "sonusDs1LineState": sonusDs1LineState,
       "sonusDs1AdmnState": sonusDs1AdmnState}
)
