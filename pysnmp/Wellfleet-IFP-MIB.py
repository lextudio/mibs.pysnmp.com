# SNMP MIB module (Wellfleet-IFP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-IFP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:22 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(wfIfpGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfIfpGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfIfpDrvCfgTable_Object = MibTable
wfIfpDrvCfgTable = _WfIfpDrvCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 1)
)
if mibBuilder.loadTexts:
    wfIfpDrvCfgTable.setStatus("mandatory")
_WfIfpDrvCfgEntry_Object = MibTableRow
wfIfpDrvCfgEntry = _WfIfpDrvCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 1, 1)
)
wfIfpDrvCfgEntry.setIndexNames(
    (0, "Wellfleet-IFP-MIB", "wfIfpDrvCfgSlot"),
)
if mibBuilder.loadTexts:
    wfIfpDrvCfgEntry.setStatus("mandatory")


class _WfIfpDrvCfgState_Type(Integer32):
    """Custom type wfIfpDrvCfgState based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              20)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("init", 3),
          ("notpresent", 20),
          ("up", 1))
    )


_WfIfpDrvCfgState_Type.__name__ = "Integer32"
_WfIfpDrvCfgState_Object = MibTableColumn
wfIfpDrvCfgState = _WfIfpDrvCfgState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 1, 1, 1),
    _WfIfpDrvCfgState_Type()
)
wfIfpDrvCfgState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIfpDrvCfgState.setStatus("mandatory")


class _WfIfpDrvCfgSlot_Type(Integer32):
    """Custom type wfIfpDrvCfgSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_WfIfpDrvCfgSlot_Type.__name__ = "Integer32"
_WfIfpDrvCfgSlot_Object = MibTableColumn
wfIfpDrvCfgSlot = _WfIfpDrvCfgSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 1, 1, 2),
    _WfIfpDrvCfgSlot_Type()
)
wfIfpDrvCfgSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpDrvCfgSlot.setStatus("mandatory")


class _WfIfpDrvCfgHeartbeatPeriod_Type(Integer32):
    """Custom type wfIfpDrvCfgHeartbeatPeriod based on Integer32"""
    defaultValue = 3


_WfIfpDrvCfgHeartbeatPeriod_Object = MibTableColumn
wfIfpDrvCfgHeartbeatPeriod = _WfIfpDrvCfgHeartbeatPeriod_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 1, 1, 3),
    _WfIfpDrvCfgHeartbeatPeriod_Type()
)
wfIfpDrvCfgHeartbeatPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIfpDrvCfgHeartbeatPeriod.setStatus("mandatory")


class _WfIfpDrvCfgHiPriQueRdEnable_Type(Integer32):
    """Custom type wfIfpDrvCfgHiPriQueRdEnable based on Integer32"""
    defaultValue = 1023

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64,
              128,
              256,
              512,
              1023)
        )
    )
    namedValues = NamedValues(
        *(("enablehiall", 1023),
          ("enablehiatmp120", 128),
          ("enablehiatmp121", 256),
          ("enablehicap1", 1),
          ("enablehicap2", 2),
          ("enablehicap3", 4),
          ("enablehicap4", 8),
          ("enablehicap5", 16),
          ("enablehimcast", 512),
          ("enablehissp0", 32),
          ("enablehissp1", 64))
    )


_WfIfpDrvCfgHiPriQueRdEnable_Type.__name__ = "Integer32"
_WfIfpDrvCfgHiPriQueRdEnable_Object = MibTableColumn
wfIfpDrvCfgHiPriQueRdEnable = _WfIfpDrvCfgHiPriQueRdEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 1, 1, 4),
    _WfIfpDrvCfgHiPriQueRdEnable_Type()
)
wfIfpDrvCfgHiPriQueRdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIfpDrvCfgHiPriQueRdEnable.setStatus("mandatory")


class _WfIfpDrvCfgLoPriQueRdEnable_Type(Integer32):
    """Custom type wfIfpDrvCfgLoPriQueRdEnable based on Integer32"""
    defaultValue = 1023

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64,
              128,
              256,
              512,
              1023)
        )
    )
    namedValues = NamedValues(
        *(("enableloall", 1023),
          ("enableloatm0", 128),
          ("enableloatm1", 256),
          ("enablelocap1", 1),
          ("enablelocap2", 2),
          ("enablelocap3", 4),
          ("enablelocap4", 8),
          ("enablelocap5", 16),
          ("enablelomcast", 512),
          ("enablelossp0", 32),
          ("enablelossp1", 64))
    )


_WfIfpDrvCfgLoPriQueRdEnable_Type.__name__ = "Integer32"
_WfIfpDrvCfgLoPriQueRdEnable_Object = MibTableColumn
wfIfpDrvCfgLoPriQueRdEnable = _WfIfpDrvCfgLoPriQueRdEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 1, 1, 5),
    _WfIfpDrvCfgLoPriQueRdEnable_Type()
)
wfIfpDrvCfgLoPriQueRdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIfpDrvCfgLoPriQueRdEnable.setStatus("mandatory")


class _WfIfpDrvCfgPortDrainEnable_Type(Integer32):
    """Custom type wfIfpDrvCfgPortDrainEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64,
              128,
              256,
              512,
              1023)
        )
    )
    namedValues = NamedValues(
        *(("enabledrainalll", 1023),
          ("enabledrainatm0", 128),
          ("enabledrainatm1", 256),
          ("enabledraincap1", 1),
          ("enabledraincap2", 2),
          ("enabledraincap3", 4),
          ("enabledraincap4", 8),
          ("enabledraincap5", 16),
          ("enabledrainmcast", 512),
          ("enabledrainssp0", 32),
          ("enabledrainssp1", 64))
    )


_WfIfpDrvCfgPortDrainEnable_Type.__name__ = "Integer32"
_WfIfpDrvCfgPortDrainEnable_Object = MibTableColumn
wfIfpDrvCfgPortDrainEnable = _WfIfpDrvCfgPortDrainEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 1, 1, 6),
    _WfIfpDrvCfgPortDrainEnable_Type()
)
wfIfpDrvCfgPortDrainEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIfpDrvCfgPortDrainEnable.setStatus("mandatory")


class _WfIfpDrvCfgSspPktTypeI_Type(Integer32):
    """Custom type wfIfpDrvCfgSspPktTypeI based on Integer32"""
    defaultValue = 33

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_WfIfpDrvCfgSspPktTypeI_Type.__name__ = "Integer32"
_WfIfpDrvCfgSspPktTypeI_Object = MibTableColumn
wfIfpDrvCfgSspPktTypeI = _WfIfpDrvCfgSspPktTypeI_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 1, 1, 7),
    _WfIfpDrvCfgSspPktTypeI_Type()
)
wfIfpDrvCfgSspPktTypeI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIfpDrvCfgSspPktTypeI.setStatus("mandatory")


class _WfIfpDrvCfgSspPktTypeII_Type(Integer32):
    """Custom type wfIfpDrvCfgSspPktTypeII based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_WfIfpDrvCfgSspPktTypeII_Type.__name__ = "Integer32"
_WfIfpDrvCfgSspPktTypeII_Object = MibTableColumn
wfIfpDrvCfgSspPktTypeII = _WfIfpDrvCfgSspPktTypeII_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 1, 1, 8),
    _WfIfpDrvCfgSspPktTypeII_Type()
)
wfIfpDrvCfgSspPktTypeII.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIfpDrvCfgSspPktTypeII.setStatus("mandatory")


class _WfIfpDrvCfgCap0PktTypeI_Type(Integer32):
    """Custom type wfIfpDrvCfgCap0PktTypeI based on Integer32"""
    defaultValue = 33

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_WfIfpDrvCfgCap0PktTypeI_Type.__name__ = "Integer32"
_WfIfpDrvCfgCap0PktTypeI_Object = MibTableColumn
wfIfpDrvCfgCap0PktTypeI = _WfIfpDrvCfgCap0PktTypeI_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 1, 1, 9),
    _WfIfpDrvCfgCap0PktTypeI_Type()
)
wfIfpDrvCfgCap0PktTypeI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIfpDrvCfgCap0PktTypeI.setStatus("mandatory")


class _WfIfpDrvCfgCap0PktTypeII_Type(Integer32):
    """Custom type wfIfpDrvCfgCap0PktTypeII based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_WfIfpDrvCfgCap0PktTypeII_Type.__name__ = "Integer32"
_WfIfpDrvCfgCap0PktTypeII_Object = MibTableColumn
wfIfpDrvCfgCap0PktTypeII = _WfIfpDrvCfgCap0PktTypeII_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 1, 1, 10),
    _WfIfpDrvCfgCap0PktTypeII_Type()
)
wfIfpDrvCfgCap0PktTypeII.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIfpDrvCfgCap0PktTypeII.setStatus("mandatory")


class _WfIfpDrvCfgCap1PktTypeI_Type(Integer32):
    """Custom type wfIfpDrvCfgCap1PktTypeI based on Integer32"""
    defaultValue = 33

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_WfIfpDrvCfgCap1PktTypeI_Type.__name__ = "Integer32"
_WfIfpDrvCfgCap1PktTypeI_Object = MibTableColumn
wfIfpDrvCfgCap1PktTypeI = _WfIfpDrvCfgCap1PktTypeI_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 1, 1, 11),
    _WfIfpDrvCfgCap1PktTypeI_Type()
)
wfIfpDrvCfgCap1PktTypeI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIfpDrvCfgCap1PktTypeI.setStatus("mandatory")


class _WfIfpDrvCfgCap1PktTypeII_Type(Integer32):
    """Custom type wfIfpDrvCfgCap1PktTypeII based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_WfIfpDrvCfgCap1PktTypeII_Type.__name__ = "Integer32"
_WfIfpDrvCfgCap1PktTypeII_Object = MibTableColumn
wfIfpDrvCfgCap1PktTypeII = _WfIfpDrvCfgCap1PktTypeII_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 1, 1, 12),
    _WfIfpDrvCfgCap1PktTypeII_Type()
)
wfIfpDrvCfgCap1PktTypeII.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIfpDrvCfgCap1PktTypeII.setStatus("mandatory")


class _WfIfpDrvCfgAtmPktTypeI_Type(Integer32):
    """Custom type wfIfpDrvCfgAtmPktTypeI based on Integer32"""
    defaultValue = 2048

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_WfIfpDrvCfgAtmPktTypeI_Type.__name__ = "Integer32"
_WfIfpDrvCfgAtmPktTypeI_Object = MibTableColumn
wfIfpDrvCfgAtmPktTypeI = _WfIfpDrvCfgAtmPktTypeI_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 1, 1, 13),
    _WfIfpDrvCfgAtmPktTypeI_Type()
)
wfIfpDrvCfgAtmPktTypeI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIfpDrvCfgAtmPktTypeI.setStatus("mandatory")


class _WfIfpDrvCfgAtmPktTypeII_Type(Integer32):
    """Custom type wfIfpDrvCfgAtmPktTypeII based on Integer32"""
    defaultValue = 34525

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_WfIfpDrvCfgAtmPktTypeII_Type.__name__ = "Integer32"
_WfIfpDrvCfgAtmPktTypeII_Object = MibTableColumn
wfIfpDrvCfgAtmPktTypeII = _WfIfpDrvCfgAtmPktTypeII_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 1, 1, 14),
    _WfIfpDrvCfgAtmPktTypeII_Type()
)
wfIfpDrvCfgAtmPktTypeII.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIfpDrvCfgAtmPktTypeII.setStatus("mandatory")


class _WfIfpDrvCfgMax2kBufferCnt_Type(Integer32):
    """Custom type wfIfpDrvCfgMax2kBufferCnt based on Integer32"""
    defaultValue = 1536

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_WfIfpDrvCfgMax2kBufferCnt_Type.__name__ = "Integer32"
_WfIfpDrvCfgMax2kBufferCnt_Object = MibTableColumn
wfIfpDrvCfgMax2kBufferCnt = _WfIfpDrvCfgMax2kBufferCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 1, 1, 15),
    _WfIfpDrvCfgMax2kBufferCnt_Type()
)
wfIfpDrvCfgMax2kBufferCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIfpDrvCfgMax2kBufferCnt.setStatus("mandatory")


class _WfIfpDrvCfgMax8kBufferCnt_Type(Integer32):
    """Custom type wfIfpDrvCfgMax8kBufferCnt based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_WfIfpDrvCfgMax8kBufferCnt_Type.__name__ = "Integer32"
_WfIfpDrvCfgMax8kBufferCnt_Object = MibTableColumn
wfIfpDrvCfgMax8kBufferCnt = _WfIfpDrvCfgMax8kBufferCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 1, 1, 16),
    _WfIfpDrvCfgMax8kBufferCnt_Type()
)
wfIfpDrvCfgMax8kBufferCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIfpDrvCfgMax8kBufferCnt.setStatus("mandatory")


class _WfIfpDrvCfgBufferOffset_Type(Integer32):
    """Custom type wfIfpDrvCfgBufferOffset based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_WfIfpDrvCfgBufferOffset_Type.__name__ = "Integer32"
_WfIfpDrvCfgBufferOffset_Object = MibTableColumn
wfIfpDrvCfgBufferOffset = _WfIfpDrvCfgBufferOffset_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 1, 1, 17),
    _WfIfpDrvCfgBufferOffset_Type()
)
wfIfpDrvCfgBufferOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIfpDrvCfgBufferOffset.setStatus("mandatory")


class _WfIfpDrvCfgCapHiPriQueClip_Type(Integer32):
    """Custom type wfIfpDrvCfgCapHiPriQueClip based on Integer32"""
    defaultValue = 1023

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_WfIfpDrvCfgCapHiPriQueClip_Type.__name__ = "Integer32"
_WfIfpDrvCfgCapHiPriQueClip_Object = MibTableColumn
wfIfpDrvCfgCapHiPriQueClip = _WfIfpDrvCfgCapHiPriQueClip_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 1, 1, 18),
    _WfIfpDrvCfgCapHiPriQueClip_Type()
)
wfIfpDrvCfgCapHiPriQueClip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIfpDrvCfgCapHiPriQueClip.setStatus("mandatory")


class _WfIfpDrvCfgCapLoPriQueClip_Type(Integer32):
    """Custom type wfIfpDrvCfgCapLoPriQueClip based on Integer32"""
    defaultValue = 1023

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_WfIfpDrvCfgCapLoPriQueClip_Type.__name__ = "Integer32"
_WfIfpDrvCfgCapLoPriQueClip_Object = MibTableColumn
wfIfpDrvCfgCapLoPriQueClip = _WfIfpDrvCfgCapLoPriQueClip_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 1, 1, 19),
    _WfIfpDrvCfgCapLoPriQueClip_Type()
)
wfIfpDrvCfgCapLoPriQueClip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIfpDrvCfgCapLoPriQueClip.setStatus("mandatory")


class _WfIfpDrvCfgAtmHiPriQueClip_Type(Integer32):
    """Custom type wfIfpDrvCfgAtmHiPriQueClip based on Integer32"""
    defaultValue = 1023

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_WfIfpDrvCfgAtmHiPriQueClip_Type.__name__ = "Integer32"
_WfIfpDrvCfgAtmHiPriQueClip_Object = MibTableColumn
wfIfpDrvCfgAtmHiPriQueClip = _WfIfpDrvCfgAtmHiPriQueClip_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 1, 1, 20),
    _WfIfpDrvCfgAtmHiPriQueClip_Type()
)
wfIfpDrvCfgAtmHiPriQueClip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIfpDrvCfgAtmHiPriQueClip.setStatus("mandatory")


class _WfIfpDrvCfgAtmLoPriQueClip_Type(Integer32):
    """Custom type wfIfpDrvCfgAtmLoPriQueClip based on Integer32"""
    defaultValue = 1023

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_WfIfpDrvCfgAtmLoPriQueClip_Type.__name__ = "Integer32"
_WfIfpDrvCfgAtmLoPriQueClip_Object = MibTableColumn
wfIfpDrvCfgAtmLoPriQueClip = _WfIfpDrvCfgAtmLoPriQueClip_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 1, 1, 21),
    _WfIfpDrvCfgAtmLoPriQueClip_Type()
)
wfIfpDrvCfgAtmLoPriQueClip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIfpDrvCfgAtmLoPriQueClip.setStatus("mandatory")


class _WfIfpDrvCfgSspHiPriQueClip_Type(Integer32):
    """Custom type wfIfpDrvCfgSspHiPriQueClip based on Integer32"""
    defaultValue = 1023

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_WfIfpDrvCfgSspHiPriQueClip_Type.__name__ = "Integer32"
_WfIfpDrvCfgSspHiPriQueClip_Object = MibTableColumn
wfIfpDrvCfgSspHiPriQueClip = _WfIfpDrvCfgSspHiPriQueClip_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 1, 1, 22),
    _WfIfpDrvCfgSspHiPriQueClip_Type()
)
wfIfpDrvCfgSspHiPriQueClip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIfpDrvCfgSspHiPriQueClip.setStatus("mandatory")


class _WfIfpDrvCfgSspLoPriQueClip_Type(Integer32):
    """Custom type wfIfpDrvCfgSspLoPriQueClip based on Integer32"""
    defaultValue = 1023

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_WfIfpDrvCfgSspLoPriQueClip_Type.__name__ = "Integer32"
_WfIfpDrvCfgSspLoPriQueClip_Object = MibTableColumn
wfIfpDrvCfgSspLoPriQueClip = _WfIfpDrvCfgSspLoPriQueClip_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 1, 1, 23),
    _WfIfpDrvCfgSspLoPriQueClip_Type()
)
wfIfpDrvCfgSspLoPriQueClip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIfpDrvCfgSspLoPriQueClip.setStatus("mandatory")


class _WfIfpDrvCfgMcastHiPriClip_Type(Integer32):
    """Custom type wfIfpDrvCfgMcastHiPriClip based on Integer32"""
    defaultValue = 2047

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2047),
    )


_WfIfpDrvCfgMcastHiPriClip_Type.__name__ = "Integer32"
_WfIfpDrvCfgMcastHiPriClip_Object = MibTableColumn
wfIfpDrvCfgMcastHiPriClip = _WfIfpDrvCfgMcastHiPriClip_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 1, 1, 24),
    _WfIfpDrvCfgMcastHiPriClip_Type()
)
wfIfpDrvCfgMcastHiPriClip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIfpDrvCfgMcastHiPriClip.setStatus("mandatory")


class _WfIfpDrvCfgMcastLoPriClip_Type(Integer32):
    """Custom type wfIfpDrvCfgMcastLoPriClip based on Integer32"""
    defaultValue = 2047

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2047),
    )


_WfIfpDrvCfgMcastLoPriClip_Type.__name__ = "Integer32"
_WfIfpDrvCfgMcastLoPriClip_Object = MibTableColumn
wfIfpDrvCfgMcastLoPriClip = _WfIfpDrvCfgMcastLoPriClip_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 1, 1, 25),
    _WfIfpDrvCfgMcastLoPriClip_Type()
)
wfIfpDrvCfgMcastLoPriClip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIfpDrvCfgMcastLoPriClip.setStatus("mandatory")


class _WfIfpDrvCfgRspActiveStreamMask_Type(Integer32):
    """Custom type wfIfpDrvCfgRspActiveStreamMask based on Integer32"""
    defaultValue = -1


_WfIfpDrvCfgRspActiveStreamMask_Object = MibTableColumn
wfIfpDrvCfgRspActiveStreamMask = _WfIfpDrvCfgRspActiveStreamMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 1, 1, 26),
    _WfIfpDrvCfgRspActiveStreamMask_Type()
)
wfIfpDrvCfgRspActiveStreamMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIfpDrvCfgRspActiveStreamMask.setStatus("mandatory")


class _WfIfpDrvCfgToSspLoPriInterval_Type(Integer32):
    """Custom type wfIfpDrvCfgToSspLoPriInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_WfIfpDrvCfgToSspLoPriInterval_Type.__name__ = "Integer32"
_WfIfpDrvCfgToSspLoPriInterval_Object = MibTableColumn
wfIfpDrvCfgToSspLoPriInterval = _WfIfpDrvCfgToSspLoPriInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 1, 1, 27),
    _WfIfpDrvCfgToSspLoPriInterval_Type()
)
wfIfpDrvCfgToSspLoPriInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIfpDrvCfgToSspLoPriInterval.setStatus("mandatory")


class _WfIfpDrvCfgToSspLoPriPktCnt_Type(Integer32):
    """Custom type wfIfpDrvCfgToSspLoPriPktCnt based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_WfIfpDrvCfgToSspLoPriPktCnt_Type.__name__ = "Integer32"
_WfIfpDrvCfgToSspLoPriPktCnt_Object = MibTableColumn
wfIfpDrvCfgToSspLoPriPktCnt = _WfIfpDrvCfgToSspLoPriPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 1, 1, 28),
    _WfIfpDrvCfgToSspLoPriPktCnt_Type()
)
wfIfpDrvCfgToSspLoPriPktCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIfpDrvCfgToSspLoPriPktCnt.setStatus("mandatory")
_WfIfpStatsTable_Object = MibTable
wfIfpStatsTable = _WfIfpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2)
)
if mibBuilder.loadTexts:
    wfIfpStatsTable.setStatus("mandatory")
_WfIfpStatsEntry_Object = MibTableRow
wfIfpStatsEntry = _WfIfpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1)
)
wfIfpStatsEntry.setIndexNames(
    (0, "Wellfleet-IFP-MIB", "wfIfpStatsSlot"),
)
if mibBuilder.loadTexts:
    wfIfpStatsEntry.setStatus("mandatory")


class _WfIfpStatsSlot_Type(Integer32):
    """Custom type wfIfpStatsSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_WfIfpStatsSlot_Type.__name__ = "Integer32"
_WfIfpStatsSlot_Object = MibTableColumn
wfIfpStatsSlot = _WfIfpStatsSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 1),
    _WfIfpStatsSlot_Type()
)
wfIfpStatsSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsSlot.setStatus("mandatory")
_WfIfpStatsCap0HiPriQueDepth_Type = Counter32
_WfIfpStatsCap0HiPriQueDepth_Object = MibTableColumn
wfIfpStatsCap0HiPriQueDepth = _WfIfpStatsCap0HiPriQueDepth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 2),
    _WfIfpStatsCap0HiPriQueDepth_Type()
)
wfIfpStatsCap0HiPriQueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsCap0HiPriQueDepth.setStatus("mandatory")
_WfIfpStatsCap0LoPriQueDepth_Type = Counter32
_WfIfpStatsCap0LoPriQueDepth_Object = MibTableColumn
wfIfpStatsCap0LoPriQueDepth = _WfIfpStatsCap0LoPriQueDepth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 3),
    _WfIfpStatsCap0LoPriQueDepth_Type()
)
wfIfpStatsCap0LoPriQueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsCap0LoPriQueDepth.setStatus("mandatory")
_WfIfpStatsCap1HiPriQueDepth_Type = Counter32
_WfIfpStatsCap1HiPriQueDepth_Object = MibTableColumn
wfIfpStatsCap1HiPriQueDepth = _WfIfpStatsCap1HiPriQueDepth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 4),
    _WfIfpStatsCap1HiPriQueDepth_Type()
)
wfIfpStatsCap1HiPriQueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsCap1HiPriQueDepth.setStatus("mandatory")
_WfIfpStatsCap1LoPriQueDepth_Type = Counter32
_WfIfpStatsCap1LoPriQueDepth_Object = MibTableColumn
wfIfpStatsCap1LoPriQueDepth = _WfIfpStatsCap1LoPriQueDepth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 5),
    _WfIfpStatsCap1LoPriQueDepth_Type()
)
wfIfpStatsCap1LoPriQueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsCap1LoPriQueDepth.setStatus("mandatory")
_WfIfpStatsCap2HiPriQueDepth_Type = Counter32
_WfIfpStatsCap2HiPriQueDepth_Object = MibTableColumn
wfIfpStatsCap2HiPriQueDepth = _WfIfpStatsCap2HiPriQueDepth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 6),
    _WfIfpStatsCap2HiPriQueDepth_Type()
)
wfIfpStatsCap2HiPriQueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsCap2HiPriQueDepth.setStatus("mandatory")
_WfIfpStatsCap2LoPriQueDepth_Type = Counter32
_WfIfpStatsCap2LoPriQueDepth_Object = MibTableColumn
wfIfpStatsCap2LoPriQueDepth = _WfIfpStatsCap2LoPriQueDepth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 7),
    _WfIfpStatsCap2LoPriQueDepth_Type()
)
wfIfpStatsCap2LoPriQueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsCap2LoPriQueDepth.setStatus("mandatory")
_WfIfpStatsCap3HiPriQueDepth_Type = Counter32
_WfIfpStatsCap3HiPriQueDepth_Object = MibTableColumn
wfIfpStatsCap3HiPriQueDepth = _WfIfpStatsCap3HiPriQueDepth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 8),
    _WfIfpStatsCap3HiPriQueDepth_Type()
)
wfIfpStatsCap3HiPriQueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsCap3HiPriQueDepth.setStatus("mandatory")
_WfIfpStatsCap3LoPriQueDepth_Type = Counter32
_WfIfpStatsCap3LoPriQueDepth_Object = MibTableColumn
wfIfpStatsCap3LoPriQueDepth = _WfIfpStatsCap3LoPriQueDepth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 9),
    _WfIfpStatsCap3LoPriQueDepth_Type()
)
wfIfpStatsCap3LoPriQueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsCap3LoPriQueDepth.setStatus("mandatory")
_WfIfpStatsCap4HiPriQueDepth_Type = Counter32
_WfIfpStatsCap4HiPriQueDepth_Object = MibTableColumn
wfIfpStatsCap4HiPriQueDepth = _WfIfpStatsCap4HiPriQueDepth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 10),
    _WfIfpStatsCap4HiPriQueDepth_Type()
)
wfIfpStatsCap4HiPriQueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsCap4HiPriQueDepth.setStatus("mandatory")
_WfIfpStatsCap4LoPriQueDepth_Type = Counter32
_WfIfpStatsCap4LoPriQueDepth_Object = MibTableColumn
wfIfpStatsCap4LoPriQueDepth = _WfIfpStatsCap4LoPriQueDepth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 11),
    _WfIfpStatsCap4LoPriQueDepth_Type()
)
wfIfpStatsCap4LoPriQueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsCap4LoPriQueDepth.setStatus("mandatory")
_WfIfpStatsAtm0HiPriQueDepth_Type = Counter32
_WfIfpStatsAtm0HiPriQueDepth_Object = MibTableColumn
wfIfpStatsAtm0HiPriQueDepth = _WfIfpStatsAtm0HiPriQueDepth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 12),
    _WfIfpStatsAtm0HiPriQueDepth_Type()
)
wfIfpStatsAtm0HiPriQueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsAtm0HiPriQueDepth.setStatus("mandatory")
_WfIfpStatsAtm0LoPriQueDepth_Type = Counter32
_WfIfpStatsAtm0LoPriQueDepth_Object = MibTableColumn
wfIfpStatsAtm0LoPriQueDepth = _WfIfpStatsAtm0LoPriQueDepth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 13),
    _WfIfpStatsAtm0LoPriQueDepth_Type()
)
wfIfpStatsAtm0LoPriQueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsAtm0LoPriQueDepth.setStatus("mandatory")
_WfIfpStatsAtm1HiPriQueDepth_Type = Counter32
_WfIfpStatsAtm1HiPriQueDepth_Object = MibTableColumn
wfIfpStatsAtm1HiPriQueDepth = _WfIfpStatsAtm1HiPriQueDepth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 14),
    _WfIfpStatsAtm1HiPriQueDepth_Type()
)
wfIfpStatsAtm1HiPriQueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsAtm1HiPriQueDepth.setStatus("mandatory")
_WfIfpStatsAtm1LoPriQueDepth_Type = Counter32
_WfIfpStatsAtm1LoPriQueDepth_Object = MibTableColumn
wfIfpStatsAtm1LoPriQueDepth = _WfIfpStatsAtm1LoPriQueDepth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 15),
    _WfIfpStatsAtm1LoPriQueDepth_Type()
)
wfIfpStatsAtm1LoPriQueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsAtm1LoPriQueDepth.setStatus("mandatory")
_WfIfpStatsSsp0HiPriQueDepth_Type = Counter32
_WfIfpStatsSsp0HiPriQueDepth_Object = MibTableColumn
wfIfpStatsSsp0HiPriQueDepth = _WfIfpStatsSsp0HiPriQueDepth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 16),
    _WfIfpStatsSsp0HiPriQueDepth_Type()
)
wfIfpStatsSsp0HiPriQueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsSsp0HiPriQueDepth.setStatus("mandatory")
_WfIfpStatsSsp0LoPriQueDepth_Type = Counter32
_WfIfpStatsSsp0LoPriQueDepth_Object = MibTableColumn
wfIfpStatsSsp0LoPriQueDepth = _WfIfpStatsSsp0LoPriQueDepth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 17),
    _WfIfpStatsSsp0LoPriQueDepth_Type()
)
wfIfpStatsSsp0LoPriQueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsSsp0LoPriQueDepth.setStatus("mandatory")
_WfIfpStatsSsp1HiPriQueDepth_Type = Counter32
_WfIfpStatsSsp1HiPriQueDepth_Object = MibTableColumn
wfIfpStatsSsp1HiPriQueDepth = _WfIfpStatsSsp1HiPriQueDepth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 18),
    _WfIfpStatsSsp1HiPriQueDepth_Type()
)
wfIfpStatsSsp1HiPriQueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsSsp1HiPriQueDepth.setStatus("mandatory")
_WfIfpStatsSsp1LoPriQueDepth_Type = Counter32
_WfIfpStatsSsp1LoPriQueDepth_Object = MibTableColumn
wfIfpStatsSsp1LoPriQueDepth = _WfIfpStatsSsp1LoPriQueDepth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 19),
    _WfIfpStatsSsp1LoPriQueDepth_Type()
)
wfIfpStatsSsp1LoPriQueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsSsp1LoPriQueDepth.setStatus("mandatory")
_WfIfpStatsMcastHiPriQueDepth_Type = Counter32
_WfIfpStatsMcastHiPriQueDepth_Object = MibTableColumn
wfIfpStatsMcastHiPriQueDepth = _WfIfpStatsMcastHiPriQueDepth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 20),
    _WfIfpStatsMcastHiPriQueDepth_Type()
)
wfIfpStatsMcastHiPriQueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsMcastHiPriQueDepth.setStatus("mandatory")
_WfIfpStatsMcastLoPriQueDepth_Type = Counter32
_WfIfpStatsMcastLoPriQueDepth_Object = MibTableColumn
wfIfpStatsMcastLoPriQueDepth = _WfIfpStatsMcastLoPriQueDepth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 21),
    _WfIfpStatsMcastLoPriQueDepth_Type()
)
wfIfpStatsMcastLoPriQueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsMcastLoPriQueDepth.setStatus("mandatory")
_WfIfpStatsCap0HiPriQueClips_Type = Counter32
_WfIfpStatsCap0HiPriQueClips_Object = MibTableColumn
wfIfpStatsCap0HiPriQueClips = _WfIfpStatsCap0HiPriQueClips_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 22),
    _WfIfpStatsCap0HiPriQueClips_Type()
)
wfIfpStatsCap0HiPriQueClips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsCap0HiPriQueClips.setStatus("mandatory")
_WfIfpStatsCap0LoPriQueClips_Type = Counter32
_WfIfpStatsCap0LoPriQueClips_Object = MibTableColumn
wfIfpStatsCap0LoPriQueClips = _WfIfpStatsCap0LoPriQueClips_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 23),
    _WfIfpStatsCap0LoPriQueClips_Type()
)
wfIfpStatsCap0LoPriQueClips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsCap0LoPriQueClips.setStatus("mandatory")
_WfIfpStatsCap1HiPriQueClips_Type = Counter32
_WfIfpStatsCap1HiPriQueClips_Object = MibTableColumn
wfIfpStatsCap1HiPriQueClips = _WfIfpStatsCap1HiPriQueClips_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 24),
    _WfIfpStatsCap1HiPriQueClips_Type()
)
wfIfpStatsCap1HiPriQueClips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsCap1HiPriQueClips.setStatus("mandatory")
_WfIfpStatsCap1LoPriQueClips_Type = Counter32
_WfIfpStatsCap1LoPriQueClips_Object = MibTableColumn
wfIfpStatsCap1LoPriQueClips = _WfIfpStatsCap1LoPriQueClips_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 25),
    _WfIfpStatsCap1LoPriQueClips_Type()
)
wfIfpStatsCap1LoPriQueClips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsCap1LoPriQueClips.setStatus("mandatory")
_WfIfpStatsCap2HiPriQueClips_Type = Counter32
_WfIfpStatsCap2HiPriQueClips_Object = MibTableColumn
wfIfpStatsCap2HiPriQueClips = _WfIfpStatsCap2HiPriQueClips_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 26),
    _WfIfpStatsCap2HiPriQueClips_Type()
)
wfIfpStatsCap2HiPriQueClips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsCap2HiPriQueClips.setStatus("mandatory")
_WfIfpStatsCap2LoPriQueClips_Type = Counter32
_WfIfpStatsCap2LoPriQueClips_Object = MibTableColumn
wfIfpStatsCap2LoPriQueClips = _WfIfpStatsCap2LoPriQueClips_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 27),
    _WfIfpStatsCap2LoPriQueClips_Type()
)
wfIfpStatsCap2LoPriQueClips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsCap2LoPriQueClips.setStatus("mandatory")
_WfIfpStatsCap3HiPriQueClips_Type = Counter32
_WfIfpStatsCap3HiPriQueClips_Object = MibTableColumn
wfIfpStatsCap3HiPriQueClips = _WfIfpStatsCap3HiPriQueClips_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 28),
    _WfIfpStatsCap3HiPriQueClips_Type()
)
wfIfpStatsCap3HiPriQueClips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsCap3HiPriQueClips.setStatus("mandatory")
_WfIfpStatsCap3LoPriQueClips_Type = Counter32
_WfIfpStatsCap3LoPriQueClips_Object = MibTableColumn
wfIfpStatsCap3LoPriQueClips = _WfIfpStatsCap3LoPriQueClips_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 29),
    _WfIfpStatsCap3LoPriQueClips_Type()
)
wfIfpStatsCap3LoPriQueClips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsCap3LoPriQueClips.setStatus("mandatory")
_WfIfpStatsCap4HiPriQueClips_Type = Counter32
_WfIfpStatsCap4HiPriQueClips_Object = MibTableColumn
wfIfpStatsCap4HiPriQueClips = _WfIfpStatsCap4HiPriQueClips_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 30),
    _WfIfpStatsCap4HiPriQueClips_Type()
)
wfIfpStatsCap4HiPriQueClips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsCap4HiPriQueClips.setStatus("mandatory")
_WfIfpStatsCap4LoPriQueClips_Type = Counter32
_WfIfpStatsCap4LoPriQueClips_Object = MibTableColumn
wfIfpStatsCap4LoPriQueClips = _WfIfpStatsCap4LoPriQueClips_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 31),
    _WfIfpStatsCap4LoPriQueClips_Type()
)
wfIfpStatsCap4LoPriQueClips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsCap4LoPriQueClips.setStatus("mandatory")
_WfIfpStatsAtm0HiPriQueClips_Type = Counter32
_WfIfpStatsAtm0HiPriQueClips_Object = MibTableColumn
wfIfpStatsAtm0HiPriQueClips = _WfIfpStatsAtm0HiPriQueClips_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 32),
    _WfIfpStatsAtm0HiPriQueClips_Type()
)
wfIfpStatsAtm0HiPriQueClips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsAtm0HiPriQueClips.setStatus("mandatory")
_WfIfpStatsAtm0LoPriQueClips_Type = Counter32
_WfIfpStatsAtm0LoPriQueClips_Object = MibTableColumn
wfIfpStatsAtm0LoPriQueClips = _WfIfpStatsAtm0LoPriQueClips_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 33),
    _WfIfpStatsAtm0LoPriQueClips_Type()
)
wfIfpStatsAtm0LoPriQueClips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsAtm0LoPriQueClips.setStatus("mandatory")
_WfIfpStatsAtm1HiPriQueClips_Type = Counter32
_WfIfpStatsAtm1HiPriQueClips_Object = MibTableColumn
wfIfpStatsAtm1HiPriQueClips = _WfIfpStatsAtm1HiPriQueClips_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 34),
    _WfIfpStatsAtm1HiPriQueClips_Type()
)
wfIfpStatsAtm1HiPriQueClips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsAtm1HiPriQueClips.setStatus("mandatory")
_WfIfpStatsAtm1LoPriQueClips_Type = Counter32
_WfIfpStatsAtm1LoPriQueClips_Object = MibTableColumn
wfIfpStatsAtm1LoPriQueClips = _WfIfpStatsAtm1LoPriQueClips_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 35),
    _WfIfpStatsAtm1LoPriQueClips_Type()
)
wfIfpStatsAtm1LoPriQueClips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsAtm1LoPriQueClips.setStatus("mandatory")
_WfIfpStatsSsp0HiPriQueClips_Type = Counter32
_WfIfpStatsSsp0HiPriQueClips_Object = MibTableColumn
wfIfpStatsSsp0HiPriQueClips = _WfIfpStatsSsp0HiPriQueClips_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 36),
    _WfIfpStatsSsp0HiPriQueClips_Type()
)
wfIfpStatsSsp0HiPriQueClips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsSsp0HiPriQueClips.setStatus("mandatory")
_WfIfpStatsSsp0LoPriQueClips_Type = Counter32
_WfIfpStatsSsp0LoPriQueClips_Object = MibTableColumn
wfIfpStatsSsp0LoPriQueClips = _WfIfpStatsSsp0LoPriQueClips_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 37),
    _WfIfpStatsSsp0LoPriQueClips_Type()
)
wfIfpStatsSsp0LoPriQueClips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsSsp0LoPriQueClips.setStatus("mandatory")
_WfIfpStatsSsp1HiPriQueClips_Type = Counter32
_WfIfpStatsSsp1HiPriQueClips_Object = MibTableColumn
wfIfpStatsSsp1HiPriQueClips = _WfIfpStatsSsp1HiPriQueClips_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 38),
    _WfIfpStatsSsp1HiPriQueClips_Type()
)
wfIfpStatsSsp1HiPriQueClips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsSsp1HiPriQueClips.setStatus("mandatory")
_WfIfpStatsSsp1LoPriQueClips_Type = Counter32
_WfIfpStatsSsp1LoPriQueClips_Object = MibTableColumn
wfIfpStatsSsp1LoPriQueClips = _WfIfpStatsSsp1LoPriQueClips_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 39),
    _WfIfpStatsSsp1LoPriQueClips_Type()
)
wfIfpStatsSsp1LoPriQueClips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsSsp1LoPriQueClips.setStatus("mandatory")
_WfIfpStatsMcastHiPriQueClips_Type = Counter32
_WfIfpStatsMcastHiPriQueClips_Object = MibTableColumn
wfIfpStatsMcastHiPriQueClips = _WfIfpStatsMcastHiPriQueClips_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 40),
    _WfIfpStatsMcastHiPriQueClips_Type()
)
wfIfpStatsMcastHiPriQueClips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsMcastHiPriQueClips.setStatus("mandatory")
_WfIfpStatsMcastLoPriQueClips_Type = Counter32
_WfIfpStatsMcastLoPriQueClips_Object = MibTableColumn
wfIfpStatsMcastLoPriQueClips = _WfIfpStatsMcastLoPriQueClips_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 41),
    _WfIfpStatsMcastLoPriQueClips_Type()
)
wfIfpStatsMcastLoPriQueClips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsMcastLoPriQueClips.setStatus("mandatory")
_WfIfpStatsSspLoPriDrops_Type = Counter32
_WfIfpStatsSspLoPriDrops_Object = MibTableColumn
wfIfpStatsSspLoPriDrops = _WfIfpStatsSspLoPriDrops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 42),
    _WfIfpStatsSspLoPriDrops_Type()
)
wfIfpStatsSspLoPriDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsSspLoPriDrops.setStatus("mandatory")
_WfIfpStatsRecvCrcErrors_Type = Counter32
_WfIfpStatsRecvCrcErrors_Object = MibTableColumn
wfIfpStatsRecvCrcErrors = _WfIfpStatsRecvCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 43),
    _WfIfpStatsRecvCrcErrors_Type()
)
wfIfpStatsRecvCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsRecvCrcErrors.setStatus("mandatory")
_WfIfpStatsBuf2kStackPtr_Type = Counter32
_WfIfpStatsBuf2kStackPtr_Object = MibTableColumn
wfIfpStatsBuf2kStackPtr = _WfIfpStatsBuf2kStackPtr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 44),
    _WfIfpStatsBuf2kStackPtr_Type()
)
wfIfpStatsBuf2kStackPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsBuf2kStackPtr.setStatus("mandatory")
_WfIfpStatsBuf8kStackPtr_Type = Counter32
_WfIfpStatsBuf8kStackPtr_Object = MibTableColumn
wfIfpStatsBuf8kStackPtr = _WfIfpStatsBuf8kStackPtr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 45),
    _WfIfpStatsBuf8kStackPtr_Type()
)
wfIfpStatsBuf8kStackPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsBuf8kStackPtr.setStatus("mandatory")
_WfIfpStatsBuf2kStackLimit_Type = Counter32
_WfIfpStatsBuf2kStackLimit_Object = MibTableColumn
wfIfpStatsBuf2kStackLimit = _WfIfpStatsBuf2kStackLimit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 46),
    _WfIfpStatsBuf2kStackLimit_Type()
)
wfIfpStatsBuf2kStackLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsBuf2kStackLimit.setStatus("mandatory")
_WfIfpStatsBuf8kStackLimit_Type = Counter32
_WfIfpStatsBuf8kStackLimit_Object = MibTableColumn
wfIfpStatsBuf8kStackLimit = _WfIfpStatsBuf8kStackLimit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 47),
    _WfIfpStatsBuf8kStackLimit_Type()
)
wfIfpStatsBuf8kStackLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsBuf8kStackLimit.setStatus("mandatory")


class _WfIfpStatsRspState_Type(Integer32):
    """Custom type wfIfpStatsRspState based on Integer32"""
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
        *(("down", 4),
          ("init", 2),
          ("nofwd", 3),
          ("up", 1))
    )


_WfIfpStatsRspState_Type.__name__ = "Integer32"
_WfIfpStatsRspState_Object = MibTableColumn
wfIfpStatsRspState = _WfIfpStatsRspState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 48),
    _WfIfpStatsRspState_Type()
)
wfIfpStatsRspState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsRspState.setStatus("mandatory")
_WfIfpStatsRspActiveStreamMask_Type = Integer32
_WfIfpStatsRspActiveStreamMask_Object = MibTableColumn
wfIfpStatsRspActiveStreamMask = _WfIfpStatsRspActiveStreamMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 49),
    _WfIfpStatsRspActiveStreamMask_Type()
)
wfIfpStatsRspActiveStreamMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsRspActiveStreamMask.setStatus("mandatory")
_WfIfpStatsBadDesc_Type = Counter32
_WfIfpStatsBadDesc_Object = MibTableColumn
wfIfpStatsBadDesc = _WfIfpStatsBadDesc_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 50),
    _WfIfpStatsBadDesc_Type()
)
wfIfpStatsBadDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsBadDesc.setStatus("mandatory")
_WfIfpStatsDispatchMiss_Type = Counter32
_WfIfpStatsDispatchMiss_Object = MibTableColumn
wfIfpStatsDispatchMiss = _WfIfpStatsDispatchMiss_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 51),
    _WfIfpStatsDispatchMiss_Type()
)
wfIfpStatsDispatchMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsDispatchMiss.setStatus("mandatory")
_WfIfpStatsSspDeliversHi_Type = Counter32
_WfIfpStatsSspDeliversHi_Object = MibTableColumn
wfIfpStatsSspDeliversHi = _WfIfpStatsSspDeliversHi_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 52),
    _WfIfpStatsSspDeliversHi_Type()
)
wfIfpStatsSspDeliversHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsSspDeliversHi.setStatus("mandatory")
_WfIfpStatsSspDeliversLo_Type = Counter32
_WfIfpStatsSspDeliversLo_Object = MibTableColumn
wfIfpStatsSspDeliversLo = _WfIfpStatsSspDeliversLo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 53),
    _WfIfpStatsSspDeliversLo_Type()
)
wfIfpStatsSspDeliversLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsSspDeliversLo.setStatus("mandatory")
_WfIfpStatsSspIpDeliversHi_Type = Counter32
_WfIfpStatsSspIpDeliversHi_Object = MibTableColumn
wfIfpStatsSspIpDeliversHi = _WfIfpStatsSspIpDeliversHi_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 54),
    _WfIfpStatsSspIpDeliversHi_Type()
)
wfIfpStatsSspIpDeliversHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsSspIpDeliversHi.setStatus("mandatory")
_WfIfpStatsSspIpDeliversLo_Type = Counter32
_WfIfpStatsSspIpDeliversLo_Object = MibTableColumn
wfIfpStatsSspIpDeliversLo = _WfIfpStatsSspIpDeliversLo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 55),
    _WfIfpStatsSspIpDeliversLo_Type()
)
wfIfpStatsSspIpDeliversLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsSspIpDeliversLo.setStatus("mandatory")
_WfIfpStatsIpBlackHoleDrops_Type = Counter32
_WfIfpStatsIpBlackHoleDrops_Object = MibTableColumn
wfIfpStatsIpBlackHoleDrops = _WfIfpStatsIpBlackHoleDrops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 56),
    _WfIfpStatsIpBlackHoleDrops_Type()
)
wfIfpStatsIpBlackHoleDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsIpBlackHoleDrops.setStatus("mandatory")
_WfIfpStatsRspBypassSent_Type = Counter32
_WfIfpStatsRspBypassSent_Object = MibTableColumn
wfIfpStatsRspBypassSent = _WfIfpStatsRspBypassSent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 57),
    _WfIfpStatsRspBypassSent_Type()
)
wfIfpStatsRspBypassSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsRspBypassSent.setStatus("mandatory")
_WfIfpStatsDpiBoflsSent_Type = Counter32
_WfIfpStatsDpiBoflsSent_Object = MibTableColumn
wfIfpStatsDpiBoflsSent = _WfIfpStatsDpiBoflsSent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 58),
    _WfIfpStatsDpiBoflsSent_Type()
)
wfIfpStatsDpiBoflsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsDpiBoflsSent.setStatus("mandatory")
_WfIfpStatsSspRspQosTx_Type = Counter32
_WfIfpStatsSspRspQosTx_Object = MibTableColumn
wfIfpStatsSspRspQosTx = _WfIfpStatsSspRspQosTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 59),
    _WfIfpStatsSspRspQosTx_Type()
)
wfIfpStatsSspRspQosTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsSspRspQosTx.setStatus("mandatory")
_WfIfpStatsSspRspBcastQosTx_Type = Counter32
_WfIfpStatsSspRspBcastQosTx_Object = MibTableColumn
wfIfpStatsSspRspBcastQosTx = _WfIfpStatsSspRspBcastQosTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 60),
    _WfIfpStatsSspRspBcastQosTx_Type()
)
wfIfpStatsSspRspBcastQosTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsSspRspBcastQosTx.setStatus("mandatory")
_WfIfpStatsCongCtrlClips_Type = Counter32
_WfIfpStatsCongCtrlClips_Object = MibTableColumn
wfIfpStatsCongCtrlClips = _WfIfpStatsCongCtrlClips_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 61),
    _WfIfpStatsCongCtrlClips_Type()
)
wfIfpStatsCongCtrlClips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsCongCtrlClips.setStatus("mandatory")
_WfIfpStatsCap0CrcInterrupts_Type = Counter32
_WfIfpStatsCap0CrcInterrupts_Object = MibTableColumn
wfIfpStatsCap0CrcInterrupts = _WfIfpStatsCap0CrcInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 62),
    _WfIfpStatsCap0CrcInterrupts_Type()
)
wfIfpStatsCap0CrcInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsCap0CrcInterrupts.setStatus("mandatory")
_WfIfpStatsSspCrcInterrupts_Type = Counter32
_WfIfpStatsSspCrcInterrupts_Object = MibTableColumn
wfIfpStatsSspCrcInterrupts = _WfIfpStatsSspCrcInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 63),
    _WfIfpStatsSspCrcInterrupts_Type()
)
wfIfpStatsSspCrcInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsSspCrcInterrupts.setStatus("mandatory")
_WfIfpStatsCap1CrcInterrupts_Type = Counter32
_WfIfpStatsCap1CrcInterrupts_Object = MibTableColumn
wfIfpStatsCap1CrcInterrupts = _WfIfpStatsCap1CrcInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 64),
    _WfIfpStatsCap1CrcInterrupts_Type()
)
wfIfpStatsCap1CrcInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsCap1CrcInterrupts.setStatus("mandatory")
_WfIfpStatsTpCrcInterrupts_Type = Counter32
_WfIfpStatsTpCrcInterrupts_Object = MibTableColumn
wfIfpStatsTpCrcInterrupts = _WfIfpStatsTpCrcInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 65),
    _WfIfpStatsTpCrcInterrupts_Type()
)
wfIfpStatsTpCrcInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsTpCrcInterrupts.setStatus("mandatory")
_WfIfpStatsMaxEofInterrupts_Type = Counter32
_WfIfpStatsMaxEofInterrupts_Object = MibTableColumn
wfIfpStatsMaxEofInterrupts = _WfIfpStatsMaxEofInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 66),
    _WfIfpStatsMaxEofInterrupts_Type()
)
wfIfpStatsMaxEofInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsMaxEofInterrupts.setStatus("mandatory")
_WfIfpStats2kFlowControlInd_Type = Counter32
_WfIfpStats2kFlowControlInd_Object = MibTableColumn
wfIfpStats2kFlowControlInd = _WfIfpStats2kFlowControlInd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 67),
    _WfIfpStats2kFlowControlInd_Type()
)
wfIfpStats2kFlowControlInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStats2kFlowControlInd.setStatus("mandatory")
_WfIfpStats8kFlowControlInd_Type = Counter32
_WfIfpStats8kFlowControlInd_Object = MibTableColumn
wfIfpStats8kFlowControlInd = _WfIfpStats8kFlowControlInd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 68),
    _WfIfpStats8kFlowControlInd_Type()
)
wfIfpStats8kFlowControlInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStats8kFlowControlInd.setStatus("mandatory")
_WfIfpStatsPrimInputSlotMask_Type = Gauge32
_WfIfpStatsPrimInputSlotMask_Object = MibTableColumn
wfIfpStatsPrimInputSlotMask = _WfIfpStatsPrimInputSlotMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 69),
    _WfIfpStatsPrimInputSlotMask_Type()
)
wfIfpStatsPrimInputSlotMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsPrimInputSlotMask.setStatus("mandatory")
_WfIfpStatsSecInputSlotMask_Type = Gauge32
_WfIfpStatsSecInputSlotMask_Object = MibTableColumn
wfIfpStatsSecInputSlotMask = _WfIfpStatsSecInputSlotMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 70),
    _WfIfpStatsSecInputSlotMask_Type()
)
wfIfpStatsSecInputSlotMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsSecInputSlotMask.setStatus("mandatory")
_WfIfpStatsSspLongFlowCtrl_Type = Counter32
_WfIfpStatsSspLongFlowCtrl_Object = MibTableColumn
wfIfpStatsSspLongFlowCtrl = _WfIfpStatsSspLongFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 71),
    _WfIfpStatsSspLongFlowCtrl_Type()
)
wfIfpStatsSspLongFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsSspLongFlowCtrl.setStatus("mandatory")
_WfIfpStatsToSspRateCtrlClips_Type = Counter32
_WfIfpStatsToSspRateCtrlClips_Object = MibTableColumn
wfIfpStatsToSspRateCtrlClips = _WfIfpStatsToSspRateCtrlClips_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 2, 1, 72),
    _WfIfpStatsToSspRateCtrlClips_Type()
)
wfIfpStatsToSspRateCtrlClips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpStatsToSspRateCtrlClips.setStatus("mandatory")
_WfIfpDrvCongCfgTable_Object = MibTable
wfIfpDrvCongCfgTable = _WfIfpDrvCongCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 3)
)
if mibBuilder.loadTexts:
    wfIfpDrvCongCfgTable.setStatus("mandatory")
_WfIfpDrvCongCfgEntry_Object = MibTableRow
wfIfpDrvCongCfgEntry = _WfIfpDrvCongCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 3, 1)
)
wfIfpDrvCongCfgEntry.setIndexNames(
    (0, "Wellfleet-IFP-MIB", "wfIfpDrvCongCfgIndex"),
)
if mibBuilder.loadTexts:
    wfIfpDrvCongCfgEntry.setStatus("mandatory")


class _WfIfpDrvCongCfgDelete_Type(Integer32):
    """Custom type wfIfpDrvCongCfgDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfIfpDrvCongCfgDelete_Type.__name__ = "Integer32"
_WfIfpDrvCongCfgDelete_Object = MibTableColumn
wfIfpDrvCongCfgDelete = _WfIfpDrvCongCfgDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 3, 1, 1),
    _WfIfpDrvCongCfgDelete_Type()
)
wfIfpDrvCongCfgDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIfpDrvCongCfgDelete.setStatus("mandatory")


class _WfIfpDrvCongCfgIndex_Type(Integer32):
    """Custom type wfIfpDrvCongCfgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfIfpDrvCongCfgIndex_Type.__name__ = "Integer32"
_WfIfpDrvCongCfgIndex_Object = MibTableColumn
wfIfpDrvCongCfgIndex = _WfIfpDrvCongCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 3, 1, 2),
    _WfIfpDrvCongCfgIndex_Type()
)
wfIfpDrvCongCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIfpDrvCongCfgIndex.setStatus("mandatory")


class _WfIfpDrvCongCfgInternServClass_Type(Integer32):
    """Custom type wfIfpDrvCongCfgInternServClass based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WfIfpDrvCongCfgInternServClass_Type.__name__ = "Integer32"
_WfIfpDrvCongCfgInternServClass_Object = MibTableColumn
wfIfpDrvCongCfgInternServClass = _WfIfpDrvCongCfgInternServClass_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 3, 1, 3),
    _WfIfpDrvCongCfgInternServClass_Type()
)
wfIfpDrvCongCfgInternServClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIfpDrvCongCfgInternServClass.setStatus("mandatory")


class _WfIfpDrvCongCfgDropPreference_Type(Integer32):
    """Custom type wfIfpDrvCongCfgDropPreference based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_WfIfpDrvCongCfgDropPreference_Type.__name__ = "Integer32"
_WfIfpDrvCongCfgDropPreference_Object = MibTableColumn
wfIfpDrvCongCfgDropPreference = _WfIfpDrvCongCfgDropPreference_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 3, 1, 4),
    _WfIfpDrvCongCfgDropPreference_Type()
)
wfIfpDrvCongCfgDropPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIfpDrvCongCfgDropPreference.setStatus("mandatory")


class _WfIfpDrvCongCfgWmDropThreshold_Type(Integer32):
    """Custom type wfIfpDrvCongCfgWmDropThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WfIfpDrvCongCfgWmDropThreshold_Type.__name__ = "Integer32"
_WfIfpDrvCongCfgWmDropThreshold_Object = MibTableColumn
wfIfpDrvCongCfgWmDropThreshold = _WfIfpDrvCongCfgWmDropThreshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2, 3, 1, 5),
    _WfIfpDrvCongCfgWmDropThreshold_Type()
)
wfIfpDrvCongCfgWmDropThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIfpDrvCongCfgWmDropThreshold.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-IFP-MIB",
    **{"wfIfpDrvCfgTable": wfIfpDrvCfgTable,
       "wfIfpDrvCfgEntry": wfIfpDrvCfgEntry,
       "wfIfpDrvCfgState": wfIfpDrvCfgState,
       "wfIfpDrvCfgSlot": wfIfpDrvCfgSlot,
       "wfIfpDrvCfgHeartbeatPeriod": wfIfpDrvCfgHeartbeatPeriod,
       "wfIfpDrvCfgHiPriQueRdEnable": wfIfpDrvCfgHiPriQueRdEnable,
       "wfIfpDrvCfgLoPriQueRdEnable": wfIfpDrvCfgLoPriQueRdEnable,
       "wfIfpDrvCfgPortDrainEnable": wfIfpDrvCfgPortDrainEnable,
       "wfIfpDrvCfgSspPktTypeI": wfIfpDrvCfgSspPktTypeI,
       "wfIfpDrvCfgSspPktTypeII": wfIfpDrvCfgSspPktTypeII,
       "wfIfpDrvCfgCap0PktTypeI": wfIfpDrvCfgCap0PktTypeI,
       "wfIfpDrvCfgCap0PktTypeII": wfIfpDrvCfgCap0PktTypeII,
       "wfIfpDrvCfgCap1PktTypeI": wfIfpDrvCfgCap1PktTypeI,
       "wfIfpDrvCfgCap1PktTypeII": wfIfpDrvCfgCap1PktTypeII,
       "wfIfpDrvCfgAtmPktTypeI": wfIfpDrvCfgAtmPktTypeI,
       "wfIfpDrvCfgAtmPktTypeII": wfIfpDrvCfgAtmPktTypeII,
       "wfIfpDrvCfgMax2kBufferCnt": wfIfpDrvCfgMax2kBufferCnt,
       "wfIfpDrvCfgMax8kBufferCnt": wfIfpDrvCfgMax8kBufferCnt,
       "wfIfpDrvCfgBufferOffset": wfIfpDrvCfgBufferOffset,
       "wfIfpDrvCfgCapHiPriQueClip": wfIfpDrvCfgCapHiPriQueClip,
       "wfIfpDrvCfgCapLoPriQueClip": wfIfpDrvCfgCapLoPriQueClip,
       "wfIfpDrvCfgAtmHiPriQueClip": wfIfpDrvCfgAtmHiPriQueClip,
       "wfIfpDrvCfgAtmLoPriQueClip": wfIfpDrvCfgAtmLoPriQueClip,
       "wfIfpDrvCfgSspHiPriQueClip": wfIfpDrvCfgSspHiPriQueClip,
       "wfIfpDrvCfgSspLoPriQueClip": wfIfpDrvCfgSspLoPriQueClip,
       "wfIfpDrvCfgMcastHiPriClip": wfIfpDrvCfgMcastHiPriClip,
       "wfIfpDrvCfgMcastLoPriClip": wfIfpDrvCfgMcastLoPriClip,
       "wfIfpDrvCfgRspActiveStreamMask": wfIfpDrvCfgRspActiveStreamMask,
       "wfIfpDrvCfgToSspLoPriInterval": wfIfpDrvCfgToSspLoPriInterval,
       "wfIfpDrvCfgToSspLoPriPktCnt": wfIfpDrvCfgToSspLoPriPktCnt,
       "wfIfpStatsTable": wfIfpStatsTable,
       "wfIfpStatsEntry": wfIfpStatsEntry,
       "wfIfpStatsSlot": wfIfpStatsSlot,
       "wfIfpStatsCap0HiPriQueDepth": wfIfpStatsCap0HiPriQueDepth,
       "wfIfpStatsCap0LoPriQueDepth": wfIfpStatsCap0LoPriQueDepth,
       "wfIfpStatsCap1HiPriQueDepth": wfIfpStatsCap1HiPriQueDepth,
       "wfIfpStatsCap1LoPriQueDepth": wfIfpStatsCap1LoPriQueDepth,
       "wfIfpStatsCap2HiPriQueDepth": wfIfpStatsCap2HiPriQueDepth,
       "wfIfpStatsCap2LoPriQueDepth": wfIfpStatsCap2LoPriQueDepth,
       "wfIfpStatsCap3HiPriQueDepth": wfIfpStatsCap3HiPriQueDepth,
       "wfIfpStatsCap3LoPriQueDepth": wfIfpStatsCap3LoPriQueDepth,
       "wfIfpStatsCap4HiPriQueDepth": wfIfpStatsCap4HiPriQueDepth,
       "wfIfpStatsCap4LoPriQueDepth": wfIfpStatsCap4LoPriQueDepth,
       "wfIfpStatsAtm0HiPriQueDepth": wfIfpStatsAtm0HiPriQueDepth,
       "wfIfpStatsAtm0LoPriQueDepth": wfIfpStatsAtm0LoPriQueDepth,
       "wfIfpStatsAtm1HiPriQueDepth": wfIfpStatsAtm1HiPriQueDepth,
       "wfIfpStatsAtm1LoPriQueDepth": wfIfpStatsAtm1LoPriQueDepth,
       "wfIfpStatsSsp0HiPriQueDepth": wfIfpStatsSsp0HiPriQueDepth,
       "wfIfpStatsSsp0LoPriQueDepth": wfIfpStatsSsp0LoPriQueDepth,
       "wfIfpStatsSsp1HiPriQueDepth": wfIfpStatsSsp1HiPriQueDepth,
       "wfIfpStatsSsp1LoPriQueDepth": wfIfpStatsSsp1LoPriQueDepth,
       "wfIfpStatsMcastHiPriQueDepth": wfIfpStatsMcastHiPriQueDepth,
       "wfIfpStatsMcastLoPriQueDepth": wfIfpStatsMcastLoPriQueDepth,
       "wfIfpStatsCap0HiPriQueClips": wfIfpStatsCap0HiPriQueClips,
       "wfIfpStatsCap0LoPriQueClips": wfIfpStatsCap0LoPriQueClips,
       "wfIfpStatsCap1HiPriQueClips": wfIfpStatsCap1HiPriQueClips,
       "wfIfpStatsCap1LoPriQueClips": wfIfpStatsCap1LoPriQueClips,
       "wfIfpStatsCap2HiPriQueClips": wfIfpStatsCap2HiPriQueClips,
       "wfIfpStatsCap2LoPriQueClips": wfIfpStatsCap2LoPriQueClips,
       "wfIfpStatsCap3HiPriQueClips": wfIfpStatsCap3HiPriQueClips,
       "wfIfpStatsCap3LoPriQueClips": wfIfpStatsCap3LoPriQueClips,
       "wfIfpStatsCap4HiPriQueClips": wfIfpStatsCap4HiPriQueClips,
       "wfIfpStatsCap4LoPriQueClips": wfIfpStatsCap4LoPriQueClips,
       "wfIfpStatsAtm0HiPriQueClips": wfIfpStatsAtm0HiPriQueClips,
       "wfIfpStatsAtm0LoPriQueClips": wfIfpStatsAtm0LoPriQueClips,
       "wfIfpStatsAtm1HiPriQueClips": wfIfpStatsAtm1HiPriQueClips,
       "wfIfpStatsAtm1LoPriQueClips": wfIfpStatsAtm1LoPriQueClips,
       "wfIfpStatsSsp0HiPriQueClips": wfIfpStatsSsp0HiPriQueClips,
       "wfIfpStatsSsp0LoPriQueClips": wfIfpStatsSsp0LoPriQueClips,
       "wfIfpStatsSsp1HiPriQueClips": wfIfpStatsSsp1HiPriQueClips,
       "wfIfpStatsSsp1LoPriQueClips": wfIfpStatsSsp1LoPriQueClips,
       "wfIfpStatsMcastHiPriQueClips": wfIfpStatsMcastHiPriQueClips,
       "wfIfpStatsMcastLoPriQueClips": wfIfpStatsMcastLoPriQueClips,
       "wfIfpStatsSspLoPriDrops": wfIfpStatsSspLoPriDrops,
       "wfIfpStatsRecvCrcErrors": wfIfpStatsRecvCrcErrors,
       "wfIfpStatsBuf2kStackPtr": wfIfpStatsBuf2kStackPtr,
       "wfIfpStatsBuf8kStackPtr": wfIfpStatsBuf8kStackPtr,
       "wfIfpStatsBuf2kStackLimit": wfIfpStatsBuf2kStackLimit,
       "wfIfpStatsBuf8kStackLimit": wfIfpStatsBuf8kStackLimit,
       "wfIfpStatsRspState": wfIfpStatsRspState,
       "wfIfpStatsRspActiveStreamMask": wfIfpStatsRspActiveStreamMask,
       "wfIfpStatsBadDesc": wfIfpStatsBadDesc,
       "wfIfpStatsDispatchMiss": wfIfpStatsDispatchMiss,
       "wfIfpStatsSspDeliversHi": wfIfpStatsSspDeliversHi,
       "wfIfpStatsSspDeliversLo": wfIfpStatsSspDeliversLo,
       "wfIfpStatsSspIpDeliversHi": wfIfpStatsSspIpDeliversHi,
       "wfIfpStatsSspIpDeliversLo": wfIfpStatsSspIpDeliversLo,
       "wfIfpStatsIpBlackHoleDrops": wfIfpStatsIpBlackHoleDrops,
       "wfIfpStatsRspBypassSent": wfIfpStatsRspBypassSent,
       "wfIfpStatsDpiBoflsSent": wfIfpStatsDpiBoflsSent,
       "wfIfpStatsSspRspQosTx": wfIfpStatsSspRspQosTx,
       "wfIfpStatsSspRspBcastQosTx": wfIfpStatsSspRspBcastQosTx,
       "wfIfpStatsCongCtrlClips": wfIfpStatsCongCtrlClips,
       "wfIfpStatsCap0CrcInterrupts": wfIfpStatsCap0CrcInterrupts,
       "wfIfpStatsSspCrcInterrupts": wfIfpStatsSspCrcInterrupts,
       "wfIfpStatsCap1CrcInterrupts": wfIfpStatsCap1CrcInterrupts,
       "wfIfpStatsTpCrcInterrupts": wfIfpStatsTpCrcInterrupts,
       "wfIfpStatsMaxEofInterrupts": wfIfpStatsMaxEofInterrupts,
       "wfIfpStats2kFlowControlInd": wfIfpStats2kFlowControlInd,
       "wfIfpStats8kFlowControlInd": wfIfpStats8kFlowControlInd,
       "wfIfpStatsPrimInputSlotMask": wfIfpStatsPrimInputSlotMask,
       "wfIfpStatsSecInputSlotMask": wfIfpStatsSecInputSlotMask,
       "wfIfpStatsSspLongFlowCtrl": wfIfpStatsSspLongFlowCtrl,
       "wfIfpStatsToSspRateCtrlClips": wfIfpStatsToSspRateCtrlClips,
       "wfIfpDrvCongCfgTable": wfIfpDrvCongCfgTable,
       "wfIfpDrvCongCfgEntry": wfIfpDrvCongCfgEntry,
       "wfIfpDrvCongCfgDelete": wfIfpDrvCongCfgDelete,
       "wfIfpDrvCongCfgIndex": wfIfpDrvCongCfgIndex,
       "wfIfpDrvCongCfgInternServClass": wfIfpDrvCongCfgInternServClass,
       "wfIfpDrvCongCfgDropPreference": wfIfpDrvCongCfgDropPreference,
       "wfIfpDrvCongCfgWmDropThreshold": wfIfpDrvCongCfgWmDropThreshold}
)
