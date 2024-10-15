# SNMP MIB module (SNA-SDLC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SNA-SDLC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:29:03 2024
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

(ifAdminStatus,
 ifIndex,
 ifOperStatus) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifAdminStatus",
    "ifIndex",
    "ifOperStatus")

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
 TextualConvention,
 TimeInterval) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeInterval")


# MODULE-IDENTITY

snaDLC = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 41)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sdlc_ObjectIdentity = ObjectIdentity
sdlc = _Sdlc_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 41, 1)
)
_SdlcPortGroup_ObjectIdentity = ObjectIdentity
sdlcPortGroup = _SdlcPortGroup_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 41, 1, 1)
)
_SdlcPortAdminTable_Object = MibTable
sdlcPortAdminTable = _SdlcPortAdminTable_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 1, 1)
)
if mibBuilder.loadTexts:
    sdlcPortAdminTable.setStatus("current")
_SdlcPortAdminEntry_Object = MibTableRow
sdlcPortAdminEntry = _SdlcPortAdminEntry_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 1, 1, 1)
)
sdlcPortAdminEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    sdlcPortAdminEntry.setStatus("current")


class _SdlcPortAdminName_Type(DisplayString):
    """Custom type sdlcPortAdminName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_SdlcPortAdminName_Type.__name__ = "DisplayString"
_SdlcPortAdminName_Object = MibTableColumn
sdlcPortAdminName = _SdlcPortAdminName_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 1, 1, 1, 1),
    _SdlcPortAdminName_Type()
)
sdlcPortAdminName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdlcPortAdminName.setStatus("current")


class _SdlcPortAdminRole_Type(Integer32):
    """Custom type sdlcPortAdminRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("negotiable", 3),
          ("primary", 1),
          ("secondary", 2))
    )


_SdlcPortAdminRole_Type.__name__ = "Integer32"
_SdlcPortAdminRole_Object = MibTableColumn
sdlcPortAdminRole = _SdlcPortAdminRole_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 1, 1, 1, 2),
    _SdlcPortAdminRole_Type()
)
sdlcPortAdminRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdlcPortAdminRole.setStatus("current")


class _SdlcPortAdminType_Type(Integer32):
    """Custom type sdlcPortAdminType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("leased", 1),
          ("switched", 2))
    )


_SdlcPortAdminType_Type.__name__ = "Integer32"
_SdlcPortAdminType_Object = MibTableColumn
sdlcPortAdminType = _SdlcPortAdminType_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 1, 1, 1, 3),
    _SdlcPortAdminType_Type()
)
sdlcPortAdminType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdlcPortAdminType.setStatus("current")


class _SdlcPortAdminTopology_Type(Integer32):
    """Custom type sdlcPortAdminTopology based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multipoint", 2),
          ("pointToPoint", 1))
    )


_SdlcPortAdminTopology_Type.__name__ = "Integer32"
_SdlcPortAdminTopology_Object = MibTableColumn
sdlcPortAdminTopology = _SdlcPortAdminTopology_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 1, 1, 1, 4),
    _SdlcPortAdminTopology_Type()
)
sdlcPortAdminTopology.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdlcPortAdminTopology.setStatus("current")


class _SdlcPortAdminISTATUS_Type(Integer32):
    """Custom type sdlcPortAdminISTATUS based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_SdlcPortAdminISTATUS_Type.__name__ = "Integer32"
_SdlcPortAdminISTATUS_Object = MibTableColumn
sdlcPortAdminISTATUS = _SdlcPortAdminISTATUS_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 1, 1, 1, 5),
    _SdlcPortAdminISTATUS_Type()
)
sdlcPortAdminISTATUS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdlcPortAdminISTATUS.setStatus("current")


class _SdlcPortAdminACTIVTO_Type(TimeInterval):
    """Custom type sdlcPortAdminACTIVTO based on TimeInterval"""
    defaultValue = 0


_SdlcPortAdminACTIVTO_Object = MibTableColumn
sdlcPortAdminACTIVTO = _SdlcPortAdminACTIVTO_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 1, 1, 1, 6),
    _SdlcPortAdminACTIVTO_Type()
)
sdlcPortAdminACTIVTO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdlcPortAdminACTIVTO.setStatus("current")


class _SdlcPortAdminPAUSE_Type(TimeInterval):
    """Custom type sdlcPortAdminPAUSE based on TimeInterval"""
    defaultValue = 200


_SdlcPortAdminPAUSE_Object = MibTableColumn
sdlcPortAdminPAUSE = _SdlcPortAdminPAUSE_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 1, 1, 1, 7),
    _SdlcPortAdminPAUSE_Type()
)
sdlcPortAdminPAUSE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdlcPortAdminPAUSE.setStatus("current")


class _SdlcPortAdminSERVLIM_Type(Integer32):
    """Custom type sdlcPortAdminSERVLIM based on Integer32"""
    defaultValue = 20


_SdlcPortAdminSERVLIM_Object = MibTableColumn
sdlcPortAdminSERVLIM = _SdlcPortAdminSERVLIM_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 1, 1, 1, 8),
    _SdlcPortAdminSERVLIM_Type()
)
sdlcPortAdminSERVLIM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdlcPortAdminSERVLIM.setStatus("current")


class _SdlcPortAdminSlowPollTimer_Type(TimeInterval):
    """Custom type sdlcPortAdminSlowPollTimer based on TimeInterval"""
    defaultValue = 2000


_SdlcPortAdminSlowPollTimer_Object = MibTableColumn
sdlcPortAdminSlowPollTimer = _SdlcPortAdminSlowPollTimer_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 1, 1, 1, 9),
    _SdlcPortAdminSlowPollTimer_Type()
)
sdlcPortAdminSlowPollTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdlcPortAdminSlowPollTimer.setStatus("current")
_SdlcPortOperTable_Object = MibTable
sdlcPortOperTable = _SdlcPortOperTable_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 1, 2)
)
if mibBuilder.loadTexts:
    sdlcPortOperTable.setStatus("current")
_SdlcPortOperEntry_Object = MibTableRow
sdlcPortOperEntry = _SdlcPortOperEntry_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 1, 2, 1)
)
sdlcPortOperEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    sdlcPortOperEntry.setStatus("current")


class _SdlcPortOperName_Type(DisplayString):
    """Custom type sdlcPortOperName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_SdlcPortOperName_Type.__name__ = "DisplayString"
_SdlcPortOperName_Object = MibTableColumn
sdlcPortOperName = _SdlcPortOperName_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 1, 2, 1, 1),
    _SdlcPortOperName_Type()
)
sdlcPortOperName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPortOperName.setStatus("current")


class _SdlcPortOperRole_Type(Integer32):
    """Custom type sdlcPortOperRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2),
          ("undefined", 3))
    )


_SdlcPortOperRole_Type.__name__ = "Integer32"
_SdlcPortOperRole_Object = MibTableColumn
sdlcPortOperRole = _SdlcPortOperRole_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 1, 2, 1, 2),
    _SdlcPortOperRole_Type()
)
sdlcPortOperRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPortOperRole.setStatus("current")


class _SdlcPortOperType_Type(Integer32):
    """Custom type sdlcPortOperType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("leased", 1),
          ("switched", 2))
    )


_SdlcPortOperType_Type.__name__ = "Integer32"
_SdlcPortOperType_Object = MibTableColumn
sdlcPortOperType = _SdlcPortOperType_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 1, 2, 1, 3),
    _SdlcPortOperType_Type()
)
sdlcPortOperType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPortOperType.setStatus("current")


class _SdlcPortOperTopology_Type(Integer32):
    """Custom type sdlcPortOperTopology based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multipoint", 2),
          ("pointToPoint", 1))
    )


_SdlcPortOperTopology_Type.__name__ = "Integer32"
_SdlcPortOperTopology_Object = MibTableColumn
sdlcPortOperTopology = _SdlcPortOperTopology_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 1, 2, 1, 4),
    _SdlcPortOperTopology_Type()
)
sdlcPortOperTopology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPortOperTopology.setStatus("current")


class _SdlcPortOperISTATUS_Type(Integer32):
    """Custom type sdlcPortOperISTATUS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_SdlcPortOperISTATUS_Type.__name__ = "Integer32"
_SdlcPortOperISTATUS_Object = MibTableColumn
sdlcPortOperISTATUS = _SdlcPortOperISTATUS_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 1, 2, 1, 5),
    _SdlcPortOperISTATUS_Type()
)
sdlcPortOperISTATUS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPortOperISTATUS.setStatus("current")
_SdlcPortOperACTIVTO_Type = TimeInterval
_SdlcPortOperACTIVTO_Object = MibTableColumn
sdlcPortOperACTIVTO = _SdlcPortOperACTIVTO_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 1, 2, 1, 6),
    _SdlcPortOperACTIVTO_Type()
)
sdlcPortOperACTIVTO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPortOperACTIVTO.setStatus("current")
_SdlcPortOperPAUSE_Type = TimeInterval
_SdlcPortOperPAUSE_Object = MibTableColumn
sdlcPortOperPAUSE = _SdlcPortOperPAUSE_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 1, 2, 1, 7),
    _SdlcPortOperPAUSE_Type()
)
sdlcPortOperPAUSE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPortOperPAUSE.setStatus("current")


class _SdlcPortOperSlowPollMethod_Type(Integer32):
    """Custom type sdlcPortOperSlowPollMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 3),
          ("pollpause", 2),
          ("servlim", 1))
    )


_SdlcPortOperSlowPollMethod_Type.__name__ = "Integer32"
_SdlcPortOperSlowPollMethod_Object = MibTableColumn
sdlcPortOperSlowPollMethod = _SdlcPortOperSlowPollMethod_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 1, 2, 1, 8),
    _SdlcPortOperSlowPollMethod_Type()
)
sdlcPortOperSlowPollMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPortOperSlowPollMethod.setStatus("current")
_SdlcPortOperSERVLIM_Type = Integer32
_SdlcPortOperSERVLIM_Object = MibTableColumn
sdlcPortOperSERVLIM = _SdlcPortOperSERVLIM_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 1, 2, 1, 9),
    _SdlcPortOperSERVLIM_Type()
)
sdlcPortOperSERVLIM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPortOperSERVLIM.setStatus("current")
_SdlcPortOperSlowPollTimer_Type = TimeInterval
_SdlcPortOperSlowPollTimer_Object = MibTableColumn
sdlcPortOperSlowPollTimer = _SdlcPortOperSlowPollTimer_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 1, 2, 1, 10),
    _SdlcPortOperSlowPollTimer_Type()
)
sdlcPortOperSlowPollTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPortOperSlowPollTimer.setStatus("current")
_SdlcPortOperLastModifyTime_Type = TimeTicks
_SdlcPortOperLastModifyTime_Object = MibTableColumn
sdlcPortOperLastModifyTime = _SdlcPortOperLastModifyTime_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 1, 2, 1, 11),
    _SdlcPortOperLastModifyTime_Type()
)
sdlcPortOperLastModifyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPortOperLastModifyTime.setStatus("current")
_SdlcPortOperLastFailTime_Type = TimeTicks
_SdlcPortOperLastFailTime_Object = MibTableColumn
sdlcPortOperLastFailTime = _SdlcPortOperLastFailTime_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 1, 2, 1, 12),
    _SdlcPortOperLastFailTime_Type()
)
sdlcPortOperLastFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPortOperLastFailTime.setStatus("current")


class _SdlcPortOperLastFailCause_Type(Integer32):
    """Custom type sdlcPortOperLastFailCause based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("physical", 2),
          ("undefined", 1))
    )


_SdlcPortOperLastFailCause_Type.__name__ = "Integer32"
_SdlcPortOperLastFailCause_Object = MibTableColumn
sdlcPortOperLastFailCause = _SdlcPortOperLastFailCause_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 1, 2, 1, 13),
    _SdlcPortOperLastFailCause_Type()
)
sdlcPortOperLastFailCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPortOperLastFailCause.setStatus("current")
_SdlcPortStatsTable_Object = MibTable
sdlcPortStatsTable = _SdlcPortStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 1, 3)
)
if mibBuilder.loadTexts:
    sdlcPortStatsTable.setStatus("current")
_SdlcPortStatsEntry_Object = MibTableRow
sdlcPortStatsEntry = _SdlcPortStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1)
)
sdlcPortStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    sdlcPortStatsEntry.setStatus("current")
_SdlcPortStatsPhysicalFailures_Type = Counter32
_SdlcPortStatsPhysicalFailures_Object = MibTableColumn
sdlcPortStatsPhysicalFailures = _SdlcPortStatsPhysicalFailures_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 1),
    _SdlcPortStatsPhysicalFailures_Type()
)
sdlcPortStatsPhysicalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPortStatsPhysicalFailures.setStatus("current")
_SdlcPortStatsInvalidAddresses_Type = Counter32
_SdlcPortStatsInvalidAddresses_Object = MibTableColumn
sdlcPortStatsInvalidAddresses = _SdlcPortStatsInvalidAddresses_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 2),
    _SdlcPortStatsInvalidAddresses_Type()
)
sdlcPortStatsInvalidAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPortStatsInvalidAddresses.setStatus("current")
_SdlcPortStatsDwarfFrames_Type = Counter32
_SdlcPortStatsDwarfFrames_Object = MibTableColumn
sdlcPortStatsDwarfFrames = _SdlcPortStatsDwarfFrames_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 3),
    _SdlcPortStatsDwarfFrames_Type()
)
sdlcPortStatsDwarfFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPortStatsDwarfFrames.setStatus("current")
_SdlcPortStatsPollsIn_Type = Counter32
_SdlcPortStatsPollsIn_Object = MibTableColumn
sdlcPortStatsPollsIn = _SdlcPortStatsPollsIn_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 4),
    _SdlcPortStatsPollsIn_Type()
)
sdlcPortStatsPollsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPortStatsPollsIn.setStatus("current")
_SdlcPortStatsPollsOut_Type = Counter32
_SdlcPortStatsPollsOut_Object = MibTableColumn
sdlcPortStatsPollsOut = _SdlcPortStatsPollsOut_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 5),
    _SdlcPortStatsPollsOut_Type()
)
sdlcPortStatsPollsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPortStatsPollsOut.setStatus("current")
_SdlcPortStatsPollRspsIn_Type = Counter32
_SdlcPortStatsPollRspsIn_Object = MibTableColumn
sdlcPortStatsPollRspsIn = _SdlcPortStatsPollRspsIn_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 6),
    _SdlcPortStatsPollRspsIn_Type()
)
sdlcPortStatsPollRspsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPortStatsPollRspsIn.setStatus("current")
_SdlcPortStatsPollRspsOut_Type = Counter32
_SdlcPortStatsPollRspsOut_Object = MibTableColumn
sdlcPortStatsPollRspsOut = _SdlcPortStatsPollRspsOut_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 7),
    _SdlcPortStatsPollRspsOut_Type()
)
sdlcPortStatsPollRspsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPortStatsPollRspsOut.setStatus("current")
_SdlcPortStatsLocalBusies_Type = Counter32
_SdlcPortStatsLocalBusies_Object = MibTableColumn
sdlcPortStatsLocalBusies = _SdlcPortStatsLocalBusies_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 8),
    _SdlcPortStatsLocalBusies_Type()
)
sdlcPortStatsLocalBusies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPortStatsLocalBusies.setStatus("current")
_SdlcPortStatsRemoteBusies_Type = Counter32
_SdlcPortStatsRemoteBusies_Object = MibTableColumn
sdlcPortStatsRemoteBusies = _SdlcPortStatsRemoteBusies_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 9),
    _SdlcPortStatsRemoteBusies_Type()
)
sdlcPortStatsRemoteBusies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPortStatsRemoteBusies.setStatus("current")
_SdlcPortStatsIFramesIn_Type = Counter32
_SdlcPortStatsIFramesIn_Object = MibTableColumn
sdlcPortStatsIFramesIn = _SdlcPortStatsIFramesIn_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 10),
    _SdlcPortStatsIFramesIn_Type()
)
sdlcPortStatsIFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPortStatsIFramesIn.setStatus("current")
_SdlcPortStatsIFramesOut_Type = Counter32
_SdlcPortStatsIFramesOut_Object = MibTableColumn
sdlcPortStatsIFramesOut = _SdlcPortStatsIFramesOut_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 11),
    _SdlcPortStatsIFramesOut_Type()
)
sdlcPortStatsIFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPortStatsIFramesOut.setStatus("current")
_SdlcPortStatsOctetsIn_Type = Counter32
_SdlcPortStatsOctetsIn_Object = MibTableColumn
sdlcPortStatsOctetsIn = _SdlcPortStatsOctetsIn_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 12),
    _SdlcPortStatsOctetsIn_Type()
)
sdlcPortStatsOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPortStatsOctetsIn.setStatus("current")
_SdlcPortStatsOctetsOut_Type = Counter32
_SdlcPortStatsOctetsOut_Object = MibTableColumn
sdlcPortStatsOctetsOut = _SdlcPortStatsOctetsOut_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 13),
    _SdlcPortStatsOctetsOut_Type()
)
sdlcPortStatsOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPortStatsOctetsOut.setStatus("current")
_SdlcPortStatsProtocolErrs_Type = Counter32
_SdlcPortStatsProtocolErrs_Object = MibTableColumn
sdlcPortStatsProtocolErrs = _SdlcPortStatsProtocolErrs_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 14),
    _SdlcPortStatsProtocolErrs_Type()
)
sdlcPortStatsProtocolErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPortStatsProtocolErrs.setStatus("current")
_SdlcPortStatsActivityTOs_Type = Counter32
_SdlcPortStatsActivityTOs_Object = MibTableColumn
sdlcPortStatsActivityTOs = _SdlcPortStatsActivityTOs_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 15),
    _SdlcPortStatsActivityTOs_Type()
)
sdlcPortStatsActivityTOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPortStatsActivityTOs.setStatus("current")
_SdlcPortStatsRNRLIMITs_Type = Counter32
_SdlcPortStatsRNRLIMITs_Object = MibTableColumn
sdlcPortStatsRNRLIMITs = _SdlcPortStatsRNRLIMITs_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 16),
    _SdlcPortStatsRNRLIMITs_Type()
)
sdlcPortStatsRNRLIMITs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPortStatsRNRLIMITs.setStatus("current")
_SdlcPortStatsRetriesExps_Type = Counter32
_SdlcPortStatsRetriesExps_Object = MibTableColumn
sdlcPortStatsRetriesExps = _SdlcPortStatsRetriesExps_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 17),
    _SdlcPortStatsRetriesExps_Type()
)
sdlcPortStatsRetriesExps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPortStatsRetriesExps.setStatus("current")
_SdlcPortStatsRetransmitsIn_Type = Counter32
_SdlcPortStatsRetransmitsIn_Object = MibTableColumn
sdlcPortStatsRetransmitsIn = _SdlcPortStatsRetransmitsIn_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 18),
    _SdlcPortStatsRetransmitsIn_Type()
)
sdlcPortStatsRetransmitsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPortStatsRetransmitsIn.setStatus("current")
_SdlcPortStatsRetransmitsOut_Type = Counter32
_SdlcPortStatsRetransmitsOut_Object = MibTableColumn
sdlcPortStatsRetransmitsOut = _SdlcPortStatsRetransmitsOut_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 19),
    _SdlcPortStatsRetransmitsOut_Type()
)
sdlcPortStatsRetransmitsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPortStatsRetransmitsOut.setStatus("current")
_SdlcLSGroup_ObjectIdentity = ObjectIdentity
sdlcLSGroup = _SdlcLSGroup_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 41, 1, 2)
)
_SdlcLSAdminTable_Object = MibTable
sdlcLSAdminTable = _SdlcLSAdminTable_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 1)
)
if mibBuilder.loadTexts:
    sdlcLSAdminTable.setStatus("current")
_SdlcLSAdminEntry_Object = MibTableRow
sdlcLSAdminEntry = _SdlcLSAdminEntry_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1)
)
sdlcLSAdminEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SNA-SDLC-MIB", "sdlcLSAddress"),
)
if mibBuilder.loadTexts:
    sdlcLSAdminEntry.setStatus("current")


class _SdlcLSAddress_Type(Integer32):
    """Custom type sdlcLSAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SdlcLSAddress_Type.__name__ = "Integer32"
_SdlcLSAddress_Object = MibTableColumn
sdlcLSAddress = _SdlcLSAddress_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 1),
    _SdlcLSAddress_Type()
)
sdlcLSAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdlcLSAddress.setStatus("current")


class _SdlcLSAdminName_Type(DisplayString):
    """Custom type sdlcLSAdminName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_SdlcLSAdminName_Type.__name__ = "DisplayString"
_SdlcLSAdminName_Object = MibTableColumn
sdlcLSAdminName = _SdlcLSAdminName_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 2),
    _SdlcLSAdminName_Type()
)
sdlcLSAdminName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdlcLSAdminName.setStatus("current")


class _SdlcLSAdminState_Type(Integer32):
    """Custom type sdlcLSAdminState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_SdlcLSAdminState_Type.__name__ = "Integer32"
_SdlcLSAdminState_Object = MibTableColumn
sdlcLSAdminState = _SdlcLSAdminState_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 3),
    _SdlcLSAdminState_Type()
)
sdlcLSAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdlcLSAdminState.setStatus("current")


class _SdlcLSAdminISTATUS_Type(Integer32):
    """Custom type sdlcLSAdminISTATUS based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_SdlcLSAdminISTATUS_Type.__name__ = "Integer32"
_SdlcLSAdminISTATUS_Object = MibTableColumn
sdlcLSAdminISTATUS = _SdlcLSAdminISTATUS_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 4),
    _SdlcLSAdminISTATUS_Type()
)
sdlcLSAdminISTATUS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdlcLSAdminISTATUS.setStatus("current")
_SdlcLSAdminMAXDATASend_Type = Integer32
_SdlcLSAdminMAXDATASend_Object = MibTableColumn
sdlcLSAdminMAXDATASend = _SdlcLSAdminMAXDATASend_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 5),
    _SdlcLSAdminMAXDATASend_Type()
)
sdlcLSAdminMAXDATASend.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdlcLSAdminMAXDATASend.setStatus("current")
_SdlcLSAdminMAXDATARcv_Type = Integer32
_SdlcLSAdminMAXDATARcv_Object = MibTableColumn
sdlcLSAdminMAXDATARcv = _SdlcLSAdminMAXDATARcv_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 6),
    _SdlcLSAdminMAXDATARcv_Type()
)
sdlcLSAdminMAXDATARcv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdlcLSAdminMAXDATARcv.setStatus("current")


class _SdlcLSAdminREPLYTO_Type(TimeInterval):
    """Custom type sdlcLSAdminREPLYTO based on TimeInterval"""
    defaultValue = 100


_SdlcLSAdminREPLYTO_Object = MibTableColumn
sdlcLSAdminREPLYTO = _SdlcLSAdminREPLYTO_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 7),
    _SdlcLSAdminREPLYTO_Type()
)
sdlcLSAdminREPLYTO.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdlcLSAdminREPLYTO.setStatus("current")


class _SdlcLSAdminMAXIN_Type(Integer32):
    """Custom type sdlcLSAdminMAXIN based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_SdlcLSAdminMAXIN_Type.__name__ = "Integer32"
_SdlcLSAdminMAXIN_Object = MibTableColumn
sdlcLSAdminMAXIN = _SdlcLSAdminMAXIN_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 8),
    _SdlcLSAdminMAXIN_Type()
)
sdlcLSAdminMAXIN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdlcLSAdminMAXIN.setStatus("current")


class _SdlcLSAdminMAXOUT_Type(Integer32):
    """Custom type sdlcLSAdminMAXOUT based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_SdlcLSAdminMAXOUT_Type.__name__ = "Integer32"
_SdlcLSAdminMAXOUT_Object = MibTableColumn
sdlcLSAdminMAXOUT = _SdlcLSAdminMAXOUT_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 9),
    _SdlcLSAdminMAXOUT_Type()
)
sdlcLSAdminMAXOUT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdlcLSAdminMAXOUT.setStatus("current")


class _SdlcLSAdminMODULO_Type(Integer32):
    """Custom type sdlcLSAdminMODULO based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(8,
              128)
        )
    )
    namedValues = NamedValues(
        *(("eight", 8),
          ("onetwentyeight", 128))
    )


_SdlcLSAdminMODULO_Type.__name__ = "Integer32"
_SdlcLSAdminMODULO_Object = MibTableColumn
sdlcLSAdminMODULO = _SdlcLSAdminMODULO_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 10),
    _SdlcLSAdminMODULO_Type()
)
sdlcLSAdminMODULO.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdlcLSAdminMODULO.setStatus("current")


class _SdlcLSAdminRETRIESm_Type(Integer32):
    """Custom type sdlcLSAdminRETRIESm based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SdlcLSAdminRETRIESm_Type.__name__ = "Integer32"
_SdlcLSAdminRETRIESm_Object = MibTableColumn
sdlcLSAdminRETRIESm = _SdlcLSAdminRETRIESm_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 11),
    _SdlcLSAdminRETRIESm_Type()
)
sdlcLSAdminRETRIESm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdlcLSAdminRETRIESm.setStatus("current")


class _SdlcLSAdminRETRIESt_Type(TimeInterval):
    """Custom type sdlcLSAdminRETRIESt based on TimeInterval"""
    defaultValue = 0


_SdlcLSAdminRETRIESt_Object = MibTableColumn
sdlcLSAdminRETRIESt = _SdlcLSAdminRETRIESt_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 12),
    _SdlcLSAdminRETRIESt_Type()
)
sdlcLSAdminRETRIESt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdlcLSAdminRETRIESt.setStatus("current")


class _SdlcLSAdminRETRIESn_Type(Integer32):
    """Custom type sdlcLSAdminRETRIESn based on Integer32"""
    defaultValue = 0


_SdlcLSAdminRETRIESn_Object = MibTableColumn
sdlcLSAdminRETRIESn = _SdlcLSAdminRETRIESn_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 13),
    _SdlcLSAdminRETRIESn_Type()
)
sdlcLSAdminRETRIESn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdlcLSAdminRETRIESn.setStatus("current")


class _SdlcLSAdminRNRLIMIT_Type(TimeInterval):
    """Custom type sdlcLSAdminRNRLIMIT based on TimeInterval"""
    defaultValue = 18000


_SdlcLSAdminRNRLIMIT_Object = MibTableColumn
sdlcLSAdminRNRLIMIT = _SdlcLSAdminRNRLIMIT_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 14),
    _SdlcLSAdminRNRLIMIT_Type()
)
sdlcLSAdminRNRLIMIT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdlcLSAdminRNRLIMIT.setStatus("current")


class _SdlcLSAdminDATMODE_Type(Integer32):
    """Custom type sdlcLSAdminDATMODE based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 2),
          ("half", 1))
    )


_SdlcLSAdminDATMODE_Type.__name__ = "Integer32"
_SdlcLSAdminDATMODE_Object = MibTableColumn
sdlcLSAdminDATMODE = _SdlcLSAdminDATMODE_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 15),
    _SdlcLSAdminDATMODE_Type()
)
sdlcLSAdminDATMODE.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdlcLSAdminDATMODE.setStatus("current")


class _SdlcLSAdminGPoll_Type(Integer32):
    """Custom type sdlcLSAdminGPoll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_SdlcLSAdminGPoll_Type.__name__ = "Integer32"
_SdlcLSAdminGPoll_Object = MibTableColumn
sdlcLSAdminGPoll = _SdlcLSAdminGPoll_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 16),
    _SdlcLSAdminGPoll_Type()
)
sdlcLSAdminGPoll.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdlcLSAdminGPoll.setStatus("current")


class _SdlcLSAdminSimRim_Type(Integer32):
    """Custom type sdlcLSAdminSimRim based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_SdlcLSAdminSimRim_Type.__name__ = "Integer32"
_SdlcLSAdminSimRim_Object = MibTableColumn
sdlcLSAdminSimRim = _SdlcLSAdminSimRim_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 17),
    _SdlcLSAdminSimRim_Type()
)
sdlcLSAdminSimRim.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdlcLSAdminSimRim.setStatus("current")


class _SdlcLSAdminXmitRcvCap_Type(Integer32):
    """Custom type sdlcLSAdminXmitRcvCap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("twa", 1),
          ("tws", 2))
    )


_SdlcLSAdminXmitRcvCap_Type.__name__ = "Integer32"
_SdlcLSAdminXmitRcvCap_Object = MibTableColumn
sdlcLSAdminXmitRcvCap = _SdlcLSAdminXmitRcvCap_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 18),
    _SdlcLSAdminXmitRcvCap_Type()
)
sdlcLSAdminXmitRcvCap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdlcLSAdminXmitRcvCap.setStatus("current")
_SdlcLSAdminRowStatus_Type = RowStatus
_SdlcLSAdminRowStatus_Object = MibTableColumn
sdlcLSAdminRowStatus = _SdlcLSAdminRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 19),
    _SdlcLSAdminRowStatus_Type()
)
sdlcLSAdminRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdlcLSAdminRowStatus.setStatus("current")
_SdlcLSOperTable_Object = MibTable
sdlcLSOperTable = _SdlcLSOperTable_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 2)
)
if mibBuilder.loadTexts:
    sdlcLSOperTable.setStatus("current")
_SdlcLSOperEntry_Object = MibTableRow
sdlcLSOperEntry = _SdlcLSOperEntry_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1)
)
sdlcLSOperEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SNA-SDLC-MIB", "sdlcLSAddress"),
)
if mibBuilder.loadTexts:
    sdlcLSOperEntry.setStatus("current")


class _SdlcLSOperName_Type(DisplayString):
    """Custom type sdlcLSOperName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_SdlcLSOperName_Type.__name__ = "DisplayString"
_SdlcLSOperName_Object = MibTableColumn
sdlcLSOperName = _SdlcLSOperName_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 1),
    _SdlcLSOperName_Type()
)
sdlcLSOperName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSOperName.setStatus("current")


class _SdlcLSOperRole_Type(Integer32):
    """Custom type sdlcLSOperRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2),
          ("undefined", 3))
    )


_SdlcLSOperRole_Type.__name__ = "Integer32"
_SdlcLSOperRole_Object = MibTableColumn
sdlcLSOperRole = _SdlcLSOperRole_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 2),
    _SdlcLSOperRole_Type()
)
sdlcLSOperRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSOperRole.setStatus("current")


class _SdlcLSOperState_Type(Integer32):
    """Custom type sdlcLSOperState based on Integer32"""
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
        *(("contactPending", 2),
          ("contacted", 3),
          ("discontactPending", 4),
          ("discontacted", 1))
    )


_SdlcLSOperState_Type.__name__ = "Integer32"
_SdlcLSOperState_Object = MibTableColumn
sdlcLSOperState = _SdlcLSOperState_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 3),
    _SdlcLSOperState_Type()
)
sdlcLSOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSOperState.setStatus("current")
_SdlcLSOperMAXDATASend_Type = Integer32
_SdlcLSOperMAXDATASend_Object = MibTableColumn
sdlcLSOperMAXDATASend = _SdlcLSOperMAXDATASend_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 4),
    _SdlcLSOperMAXDATASend_Type()
)
sdlcLSOperMAXDATASend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSOperMAXDATASend.setStatus("current")
_SdlcLSOperREPLYTO_Type = TimeInterval
_SdlcLSOperREPLYTO_Object = MibTableColumn
sdlcLSOperREPLYTO = _SdlcLSOperREPLYTO_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 5),
    _SdlcLSOperREPLYTO_Type()
)
sdlcLSOperREPLYTO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSOperREPLYTO.setStatus("current")


class _SdlcLSOperMAXIN_Type(Integer32):
    """Custom type sdlcLSOperMAXIN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_SdlcLSOperMAXIN_Type.__name__ = "Integer32"
_SdlcLSOperMAXIN_Object = MibTableColumn
sdlcLSOperMAXIN = _SdlcLSOperMAXIN_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 6),
    _SdlcLSOperMAXIN_Type()
)
sdlcLSOperMAXIN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSOperMAXIN.setStatus("current")


class _SdlcLSOperMAXOUT_Type(Integer32):
    """Custom type sdlcLSOperMAXOUT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_SdlcLSOperMAXOUT_Type.__name__ = "Integer32"
_SdlcLSOperMAXOUT_Object = MibTableColumn
sdlcLSOperMAXOUT = _SdlcLSOperMAXOUT_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 7),
    _SdlcLSOperMAXOUT_Type()
)
sdlcLSOperMAXOUT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSOperMAXOUT.setStatus("current")


class _SdlcLSOperMODULO_Type(Integer32):
    """Custom type sdlcLSOperMODULO based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(8,
              128)
        )
    )
    namedValues = NamedValues(
        *(("eight", 8),
          ("onetwentyeight", 128))
    )


_SdlcLSOperMODULO_Type.__name__ = "Integer32"
_SdlcLSOperMODULO_Object = MibTableColumn
sdlcLSOperMODULO = _SdlcLSOperMODULO_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 8),
    _SdlcLSOperMODULO_Type()
)
sdlcLSOperMODULO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSOperMODULO.setStatus("current")


class _SdlcLSOperRETRIESm_Type(Integer32):
    """Custom type sdlcLSOperRETRIESm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SdlcLSOperRETRIESm_Type.__name__ = "Integer32"
_SdlcLSOperRETRIESm_Object = MibTableColumn
sdlcLSOperRETRIESm = _SdlcLSOperRETRIESm_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 9),
    _SdlcLSOperRETRIESm_Type()
)
sdlcLSOperRETRIESm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSOperRETRIESm.setStatus("current")
_SdlcLSOperRETRIESt_Type = TimeInterval
_SdlcLSOperRETRIESt_Object = MibTableColumn
sdlcLSOperRETRIESt = _SdlcLSOperRETRIESt_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 10),
    _SdlcLSOperRETRIESt_Type()
)
sdlcLSOperRETRIESt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSOperRETRIESt.setStatus("current")


class _SdlcLSOperRETRIESn_Type(Integer32):
    """Custom type sdlcLSOperRETRIESn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SdlcLSOperRETRIESn_Type.__name__ = "Integer32"
_SdlcLSOperRETRIESn_Object = MibTableColumn
sdlcLSOperRETRIESn = _SdlcLSOperRETRIESn_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 11),
    _SdlcLSOperRETRIESn_Type()
)
sdlcLSOperRETRIESn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSOperRETRIESn.setStatus("current")
_SdlcLSOperRNRLIMIT_Type = TimeInterval
_SdlcLSOperRNRLIMIT_Object = MibTableColumn
sdlcLSOperRNRLIMIT = _SdlcLSOperRNRLIMIT_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 12),
    _SdlcLSOperRNRLIMIT_Type()
)
sdlcLSOperRNRLIMIT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSOperRNRLIMIT.setStatus("current")


class _SdlcLSOperDATMODE_Type(Integer32):
    """Custom type sdlcLSOperDATMODE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 2),
          ("half", 1))
    )


_SdlcLSOperDATMODE_Type.__name__ = "Integer32"
_SdlcLSOperDATMODE_Object = MibTableColumn
sdlcLSOperDATMODE = _SdlcLSOperDATMODE_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 13),
    _SdlcLSOperDATMODE_Type()
)
sdlcLSOperDATMODE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSOperDATMODE.setStatus("current")
_SdlcLSOperLastModifyTime_Type = TimeTicks
_SdlcLSOperLastModifyTime_Object = MibTableColumn
sdlcLSOperLastModifyTime = _SdlcLSOperLastModifyTime_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 14),
    _SdlcLSOperLastModifyTime_Type()
)
sdlcLSOperLastModifyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSOperLastModifyTime.setStatus("current")
_SdlcLSOperLastFailTime_Type = TimeTicks
_SdlcLSOperLastFailTime_Object = MibTableColumn
sdlcLSOperLastFailTime = _SdlcLSOperLastFailTime_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 15),
    _SdlcLSOperLastFailTime_Type()
)
sdlcLSOperLastFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSOperLastFailTime.setStatus("current")


class _SdlcLSOperLastFailCause_Type(Integer32):
    """Custom type sdlcLSOperLastFailCause based on Integer32"""
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
        *(("noActivity", 6),
          ("noResponse", 4),
          ("protocolErr", 5),
          ("retriesExpired", 8),
          ("rnrLimit", 7),
          ("rxFRMR", 2),
          ("txFRMR", 3),
          ("undefined", 1))
    )


_SdlcLSOperLastFailCause_Type.__name__ = "Integer32"
_SdlcLSOperLastFailCause_Object = MibTableColumn
sdlcLSOperLastFailCause = _SdlcLSOperLastFailCause_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 16),
    _SdlcLSOperLastFailCause_Type()
)
sdlcLSOperLastFailCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSOperLastFailCause.setStatus("current")


class _SdlcLSOperLastFailCtrlIn_Type(OctetString):
    """Custom type sdlcLSOperLastFailCtrlIn based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2),
    )


_SdlcLSOperLastFailCtrlIn_Type.__name__ = "OctetString"
_SdlcLSOperLastFailCtrlIn_Object = MibTableColumn
sdlcLSOperLastFailCtrlIn = _SdlcLSOperLastFailCtrlIn_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 17),
    _SdlcLSOperLastFailCtrlIn_Type()
)
sdlcLSOperLastFailCtrlIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSOperLastFailCtrlIn.setStatus("current")


class _SdlcLSOperLastFailCtrlOut_Type(OctetString):
    """Custom type sdlcLSOperLastFailCtrlOut based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2),
    )


_SdlcLSOperLastFailCtrlOut_Type.__name__ = "OctetString"
_SdlcLSOperLastFailCtrlOut_Object = MibTableColumn
sdlcLSOperLastFailCtrlOut = _SdlcLSOperLastFailCtrlOut_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 18),
    _SdlcLSOperLastFailCtrlOut_Type()
)
sdlcLSOperLastFailCtrlOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSOperLastFailCtrlOut.setStatus("current")


class _SdlcLSOperLastFailFRMRInfo_Type(OctetString):
    """Custom type sdlcLSOperLastFailFRMRInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_SdlcLSOperLastFailFRMRInfo_Type.__name__ = "OctetString"
_SdlcLSOperLastFailFRMRInfo_Object = MibTableColumn
sdlcLSOperLastFailFRMRInfo = _SdlcLSOperLastFailFRMRInfo_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 19),
    _SdlcLSOperLastFailFRMRInfo_Type()
)
sdlcLSOperLastFailFRMRInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSOperLastFailFRMRInfo.setStatus("current")
_SdlcLSOperLastFailREPLYTOs_Type = Counter32
_SdlcLSOperLastFailREPLYTOs_Object = MibTableColumn
sdlcLSOperLastFailREPLYTOs = _SdlcLSOperLastFailREPLYTOs_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 20),
    _SdlcLSOperLastFailREPLYTOs_Type()
)
sdlcLSOperLastFailREPLYTOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSOperLastFailREPLYTOs.setStatus("current")


class _SdlcLSOperEcho_Type(Integer32):
    """Custom type sdlcLSOperEcho based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_SdlcLSOperEcho_Type.__name__ = "Integer32"
_SdlcLSOperEcho_Object = MibTableColumn
sdlcLSOperEcho = _SdlcLSOperEcho_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 21),
    _SdlcLSOperEcho_Type()
)
sdlcLSOperEcho.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSOperEcho.setStatus("current")


class _SdlcLSOperGPoll_Type(Integer32):
    """Custom type sdlcLSOperGPoll based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_SdlcLSOperGPoll_Type.__name__ = "Integer32"
_SdlcLSOperGPoll_Object = MibTableColumn
sdlcLSOperGPoll = _SdlcLSOperGPoll_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 22),
    _SdlcLSOperGPoll_Type()
)
sdlcLSOperGPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSOperGPoll.setStatus("current")


class _SdlcLSOperSimRim_Type(Integer32):
    """Custom type sdlcLSOperSimRim based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_SdlcLSOperSimRim_Type.__name__ = "Integer32"
_SdlcLSOperSimRim_Object = MibTableColumn
sdlcLSOperSimRim = _SdlcLSOperSimRim_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 23),
    _SdlcLSOperSimRim_Type()
)
sdlcLSOperSimRim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSOperSimRim.setStatus("current")


class _SdlcLSOperXmitRcvCap_Type(Integer32):
    """Custom type sdlcLSOperXmitRcvCap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("twa", 1),
          ("tws", 2))
    )


_SdlcLSOperXmitRcvCap_Type.__name__ = "Integer32"
_SdlcLSOperXmitRcvCap_Object = MibTableColumn
sdlcLSOperXmitRcvCap = _SdlcLSOperXmitRcvCap_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 24),
    _SdlcLSOperXmitRcvCap_Type()
)
sdlcLSOperXmitRcvCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSOperXmitRcvCap.setStatus("current")
_SdlcLSStatsTable_Object = MibTable
sdlcLSStatsTable = _SdlcLSStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 3)
)
if mibBuilder.loadTexts:
    sdlcLSStatsTable.setStatus("current")
_SdlcLSStatsEntry_Object = MibTableRow
sdlcLSStatsEntry = _SdlcLSStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1)
)
sdlcLSStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SNA-SDLC-MIB", "sdlcLSAddress"),
)
if mibBuilder.loadTexts:
    sdlcLSStatsEntry.setStatus("current")
_SdlcLSStatsBLUsIn_Type = Counter32
_SdlcLSStatsBLUsIn_Object = MibTableColumn
sdlcLSStatsBLUsIn = _SdlcLSStatsBLUsIn_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 1),
    _SdlcLSStatsBLUsIn_Type()
)
sdlcLSStatsBLUsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsBLUsIn.setStatus("current")
_SdlcLSStatsBLUsOut_Type = Counter32
_SdlcLSStatsBLUsOut_Object = MibTableColumn
sdlcLSStatsBLUsOut = _SdlcLSStatsBLUsOut_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 2),
    _SdlcLSStatsBLUsOut_Type()
)
sdlcLSStatsBLUsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsBLUsOut.setStatus("current")
_SdlcLSStatsOctetsIn_Type = Counter32
_SdlcLSStatsOctetsIn_Object = MibTableColumn
sdlcLSStatsOctetsIn = _SdlcLSStatsOctetsIn_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 3),
    _SdlcLSStatsOctetsIn_Type()
)
sdlcLSStatsOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsOctetsIn.setStatus("current")
_SdlcLSStatsOctetsOut_Type = Counter32
_SdlcLSStatsOctetsOut_Object = MibTableColumn
sdlcLSStatsOctetsOut = _SdlcLSStatsOctetsOut_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 4),
    _SdlcLSStatsOctetsOut_Type()
)
sdlcLSStatsOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsOctetsOut.setStatus("current")
_SdlcLSStatsPollsIn_Type = Counter32
_SdlcLSStatsPollsIn_Object = MibTableColumn
sdlcLSStatsPollsIn = _SdlcLSStatsPollsIn_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 5),
    _SdlcLSStatsPollsIn_Type()
)
sdlcLSStatsPollsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsPollsIn.setStatus("current")
_SdlcLSStatsPollsOut_Type = Counter32
_SdlcLSStatsPollsOut_Object = MibTableColumn
sdlcLSStatsPollsOut = _SdlcLSStatsPollsOut_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 6),
    _SdlcLSStatsPollsOut_Type()
)
sdlcLSStatsPollsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsPollsOut.setStatus("current")
_SdlcLSStatsPollRspsOut_Type = Counter32
_SdlcLSStatsPollRspsOut_Object = MibTableColumn
sdlcLSStatsPollRspsOut = _SdlcLSStatsPollRspsOut_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 7),
    _SdlcLSStatsPollRspsOut_Type()
)
sdlcLSStatsPollRspsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsPollRspsOut.setStatus("current")
_SdlcLSStatsPollRspsIn_Type = Counter32
_SdlcLSStatsPollRspsIn_Object = MibTableColumn
sdlcLSStatsPollRspsIn = _SdlcLSStatsPollRspsIn_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 8),
    _SdlcLSStatsPollRspsIn_Type()
)
sdlcLSStatsPollRspsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsPollRspsIn.setStatus("current")
_SdlcLSStatsLocalBusies_Type = Counter32
_SdlcLSStatsLocalBusies_Object = MibTableColumn
sdlcLSStatsLocalBusies = _SdlcLSStatsLocalBusies_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 9),
    _SdlcLSStatsLocalBusies_Type()
)
sdlcLSStatsLocalBusies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsLocalBusies.setStatus("current")
_SdlcLSStatsRemoteBusies_Type = Counter32
_SdlcLSStatsRemoteBusies_Object = MibTableColumn
sdlcLSStatsRemoteBusies = _SdlcLSStatsRemoteBusies_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 10),
    _SdlcLSStatsRemoteBusies_Type()
)
sdlcLSStatsRemoteBusies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsRemoteBusies.setStatus("current")
_SdlcLSStatsIFramesIn_Type = Counter32
_SdlcLSStatsIFramesIn_Object = MibTableColumn
sdlcLSStatsIFramesIn = _SdlcLSStatsIFramesIn_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 11),
    _SdlcLSStatsIFramesIn_Type()
)
sdlcLSStatsIFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsIFramesIn.setStatus("current")
_SdlcLSStatsIFramesOut_Type = Counter32
_SdlcLSStatsIFramesOut_Object = MibTableColumn
sdlcLSStatsIFramesOut = _SdlcLSStatsIFramesOut_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 12),
    _SdlcLSStatsIFramesOut_Type()
)
sdlcLSStatsIFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsIFramesOut.setStatus("current")
_SdlcLSStatsUIFramesIn_Type = Counter32
_SdlcLSStatsUIFramesIn_Object = MibTableColumn
sdlcLSStatsUIFramesIn = _SdlcLSStatsUIFramesIn_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 13),
    _SdlcLSStatsUIFramesIn_Type()
)
sdlcLSStatsUIFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsUIFramesIn.setStatus("current")
_SdlcLSStatsUIFramesOut_Type = Counter32
_SdlcLSStatsUIFramesOut_Object = MibTableColumn
sdlcLSStatsUIFramesOut = _SdlcLSStatsUIFramesOut_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 14),
    _SdlcLSStatsUIFramesOut_Type()
)
sdlcLSStatsUIFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsUIFramesOut.setStatus("current")
_SdlcLSStatsXIDsIn_Type = Counter32
_SdlcLSStatsXIDsIn_Object = MibTableColumn
sdlcLSStatsXIDsIn = _SdlcLSStatsXIDsIn_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 15),
    _SdlcLSStatsXIDsIn_Type()
)
sdlcLSStatsXIDsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsXIDsIn.setStatus("current")
_SdlcLSStatsXIDsOut_Type = Counter32
_SdlcLSStatsXIDsOut_Object = MibTableColumn
sdlcLSStatsXIDsOut = _SdlcLSStatsXIDsOut_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 16),
    _SdlcLSStatsXIDsOut_Type()
)
sdlcLSStatsXIDsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsXIDsOut.setStatus("current")
_SdlcLSStatsTESTsIn_Type = Counter32
_SdlcLSStatsTESTsIn_Object = MibTableColumn
sdlcLSStatsTESTsIn = _SdlcLSStatsTESTsIn_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 17),
    _SdlcLSStatsTESTsIn_Type()
)
sdlcLSStatsTESTsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsTESTsIn.setStatus("current")
_SdlcLSStatsTESTsOut_Type = Counter32
_SdlcLSStatsTESTsOut_Object = MibTableColumn
sdlcLSStatsTESTsOut = _SdlcLSStatsTESTsOut_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 18),
    _SdlcLSStatsTESTsOut_Type()
)
sdlcLSStatsTESTsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsTESTsOut.setStatus("current")
_SdlcLSStatsREJsIn_Type = Counter32
_SdlcLSStatsREJsIn_Object = MibTableColumn
sdlcLSStatsREJsIn = _SdlcLSStatsREJsIn_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 19),
    _SdlcLSStatsREJsIn_Type()
)
sdlcLSStatsREJsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsREJsIn.setStatus("current")
_SdlcLSStatsREJsOut_Type = Counter32
_SdlcLSStatsREJsOut_Object = MibTableColumn
sdlcLSStatsREJsOut = _SdlcLSStatsREJsOut_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 20),
    _SdlcLSStatsREJsOut_Type()
)
sdlcLSStatsREJsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsREJsOut.setStatus("current")
_SdlcLSStatsFRMRsIn_Type = Counter32
_SdlcLSStatsFRMRsIn_Object = MibTableColumn
sdlcLSStatsFRMRsIn = _SdlcLSStatsFRMRsIn_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 21),
    _SdlcLSStatsFRMRsIn_Type()
)
sdlcLSStatsFRMRsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsFRMRsIn.setStatus("current")
_SdlcLSStatsFRMRsOut_Type = Counter32
_SdlcLSStatsFRMRsOut_Object = MibTableColumn
sdlcLSStatsFRMRsOut = _SdlcLSStatsFRMRsOut_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 22),
    _SdlcLSStatsFRMRsOut_Type()
)
sdlcLSStatsFRMRsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsFRMRsOut.setStatus("current")
_SdlcLSStatsSIMsIn_Type = Counter32
_SdlcLSStatsSIMsIn_Object = MibTableColumn
sdlcLSStatsSIMsIn = _SdlcLSStatsSIMsIn_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 23),
    _SdlcLSStatsSIMsIn_Type()
)
sdlcLSStatsSIMsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsSIMsIn.setStatus("current")
_SdlcLSStatsSIMsOut_Type = Counter32
_SdlcLSStatsSIMsOut_Object = MibTableColumn
sdlcLSStatsSIMsOut = _SdlcLSStatsSIMsOut_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 24),
    _SdlcLSStatsSIMsOut_Type()
)
sdlcLSStatsSIMsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsSIMsOut.setStatus("current")
_SdlcLSStatsRIMsIn_Type = Counter32
_SdlcLSStatsRIMsIn_Object = MibTableColumn
sdlcLSStatsRIMsIn = _SdlcLSStatsRIMsIn_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 25),
    _SdlcLSStatsRIMsIn_Type()
)
sdlcLSStatsRIMsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsRIMsIn.setStatus("current")
_SdlcLSStatsRIMsOut_Type = Counter32
_SdlcLSStatsRIMsOut_Object = MibTableColumn
sdlcLSStatsRIMsOut = _SdlcLSStatsRIMsOut_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 26),
    _SdlcLSStatsRIMsOut_Type()
)
sdlcLSStatsRIMsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsRIMsOut.setStatus("current")
_SdlcLSStatsDISCIn_Type = Counter32
_SdlcLSStatsDISCIn_Object = MibTableColumn
sdlcLSStatsDISCIn = _SdlcLSStatsDISCIn_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 27),
    _SdlcLSStatsDISCIn_Type()
)
sdlcLSStatsDISCIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsDISCIn.setStatus("current")
_SdlcLSStatsDISCOut_Type = Counter32
_SdlcLSStatsDISCOut_Object = MibTableColumn
sdlcLSStatsDISCOut = _SdlcLSStatsDISCOut_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 28),
    _SdlcLSStatsDISCOut_Type()
)
sdlcLSStatsDISCOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsDISCOut.setStatus("current")
_SdlcLSStatsUAIn_Type = Counter32
_SdlcLSStatsUAIn_Object = MibTableColumn
sdlcLSStatsUAIn = _SdlcLSStatsUAIn_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 29),
    _SdlcLSStatsUAIn_Type()
)
sdlcLSStatsUAIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsUAIn.setStatus("current")
_SdlcLSStatsUAOut_Type = Counter32
_SdlcLSStatsUAOut_Object = MibTableColumn
sdlcLSStatsUAOut = _SdlcLSStatsUAOut_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 30),
    _SdlcLSStatsUAOut_Type()
)
sdlcLSStatsUAOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsUAOut.setStatus("current")
_SdlcLSStatsDMIn_Type = Counter32
_SdlcLSStatsDMIn_Object = MibTableColumn
sdlcLSStatsDMIn = _SdlcLSStatsDMIn_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 31),
    _SdlcLSStatsDMIn_Type()
)
sdlcLSStatsDMIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsDMIn.setStatus("current")
_SdlcLSStatsDMOut_Type = Counter32
_SdlcLSStatsDMOut_Object = MibTableColumn
sdlcLSStatsDMOut = _SdlcLSStatsDMOut_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 32),
    _SdlcLSStatsDMOut_Type()
)
sdlcLSStatsDMOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsDMOut.setStatus("current")
_SdlcLSStatsSNRMIn_Type = Counter32
_SdlcLSStatsSNRMIn_Object = MibTableColumn
sdlcLSStatsSNRMIn = _SdlcLSStatsSNRMIn_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 33),
    _SdlcLSStatsSNRMIn_Type()
)
sdlcLSStatsSNRMIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsSNRMIn.setStatus("current")
_SdlcLSStatsSNRMOut_Type = Counter32
_SdlcLSStatsSNRMOut_Object = MibTableColumn
sdlcLSStatsSNRMOut = _SdlcLSStatsSNRMOut_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 34),
    _SdlcLSStatsSNRMOut_Type()
)
sdlcLSStatsSNRMOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsSNRMOut.setStatus("current")
_SdlcLSStatsProtocolErrs_Type = Counter32
_SdlcLSStatsProtocolErrs_Object = MibTableColumn
sdlcLSStatsProtocolErrs = _SdlcLSStatsProtocolErrs_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 35),
    _SdlcLSStatsProtocolErrs_Type()
)
sdlcLSStatsProtocolErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsProtocolErrs.setStatus("current")
_SdlcLSStatsActivityTOs_Type = Counter32
_SdlcLSStatsActivityTOs_Object = MibTableColumn
sdlcLSStatsActivityTOs = _SdlcLSStatsActivityTOs_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 36),
    _SdlcLSStatsActivityTOs_Type()
)
sdlcLSStatsActivityTOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsActivityTOs.setStatus("current")
_SdlcLSStatsRNRLIMITs_Type = Counter32
_SdlcLSStatsRNRLIMITs_Object = MibTableColumn
sdlcLSStatsRNRLIMITs = _SdlcLSStatsRNRLIMITs_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 37),
    _SdlcLSStatsRNRLIMITs_Type()
)
sdlcLSStatsRNRLIMITs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsRNRLIMITs.setStatus("current")
_SdlcLSStatsRetriesExps_Type = Counter32
_SdlcLSStatsRetriesExps_Object = MibTableColumn
sdlcLSStatsRetriesExps = _SdlcLSStatsRetriesExps_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 38),
    _SdlcLSStatsRetriesExps_Type()
)
sdlcLSStatsRetriesExps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsRetriesExps.setStatus("current")
_SdlcLSStatsRetransmitsIn_Type = Counter32
_SdlcLSStatsRetransmitsIn_Object = MibTableColumn
sdlcLSStatsRetransmitsIn = _SdlcLSStatsRetransmitsIn_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 39),
    _SdlcLSStatsRetransmitsIn_Type()
)
sdlcLSStatsRetransmitsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsRetransmitsIn.setStatus("current")
_SdlcLSStatsRetransmitsOut_Type = Counter32
_SdlcLSStatsRetransmitsOut_Object = MibTableColumn
sdlcLSStatsRetransmitsOut = _SdlcLSStatsRetransmitsOut_Object(
    (1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 40),
    _SdlcLSStatsRetransmitsOut_Type()
)
sdlcLSStatsRetransmitsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsRetransmitsOut.setStatus("current")
_SdlcTraps_ObjectIdentity = ObjectIdentity
sdlcTraps = _SdlcTraps_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 41, 1, 3)
)
_SdlcConformance_ObjectIdentity = ObjectIdentity
sdlcConformance = _SdlcConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 41, 1, 4)
)
_SdlcCompliances_ObjectIdentity = ObjectIdentity
sdlcCompliances = _SdlcCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 41, 1, 4, 1)
)
_SdlcGroups_ObjectIdentity = ObjectIdentity
sdlcGroups = _SdlcGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 41, 1, 4, 2)
)
_SdlcCoreGroups_ObjectIdentity = ObjectIdentity
sdlcCoreGroups = _SdlcCoreGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 41, 1, 4, 2, 1)
)
_SdlcPrimaryGroups_ObjectIdentity = ObjectIdentity
sdlcPrimaryGroups = _SdlcPrimaryGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 41, 1, 4, 2, 2)
)

# Managed Objects groups

sdlcCorePortAdminGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 41, 1, 4, 2, 1, 1)
)
sdlcCorePortAdminGroup.setObjects(
      *(("SNA-SDLC-MIB", "sdlcPortAdminName"),
        ("SNA-SDLC-MIB", "sdlcPortAdminRole"),
        ("SNA-SDLC-MIB", "sdlcPortAdminType"),
        ("SNA-SDLC-MIB", "sdlcPortAdminTopology"),
        ("SNA-SDLC-MIB", "sdlcPortAdminISTATUS"))
)
if mibBuilder.loadTexts:
    sdlcCorePortAdminGroup.setStatus("current")

sdlcCorePortOperGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 41, 1, 4, 2, 1, 2)
)
sdlcCorePortOperGroup.setObjects(
      *(("SNA-SDLC-MIB", "sdlcPortOperName"),
        ("SNA-SDLC-MIB", "sdlcPortOperRole"),
        ("SNA-SDLC-MIB", "sdlcPortOperType"),
        ("SNA-SDLC-MIB", "sdlcPortOperTopology"),
        ("SNA-SDLC-MIB", "sdlcPortOperISTATUS"),
        ("SNA-SDLC-MIB", "sdlcPortOperACTIVTO"),
        ("SNA-SDLC-MIB", "sdlcPortOperLastFailTime"),
        ("SNA-SDLC-MIB", "sdlcPortOperLastFailCause"))
)
if mibBuilder.loadTexts:
    sdlcCorePortOperGroup.setStatus("current")

sdlcCorePortStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 41, 1, 4, 2, 1, 3)
)
sdlcCorePortStatsGroup.setObjects(
      *(("SNA-SDLC-MIB", "sdlcPortStatsPhysicalFailures"),
        ("SNA-SDLC-MIB", "sdlcPortStatsInvalidAddresses"),
        ("SNA-SDLC-MIB", "sdlcPortStatsDwarfFrames"))
)
if mibBuilder.loadTexts:
    sdlcCorePortStatsGroup.setStatus("current")

sdlcCoreLSAdminGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 41, 1, 4, 2, 1, 4)
)
sdlcCoreLSAdminGroup.setObjects(
      *(("SNA-SDLC-MIB", "sdlcLSAddress"),
        ("SNA-SDLC-MIB", "sdlcLSAdminName"),
        ("SNA-SDLC-MIB", "sdlcLSAdminState"),
        ("SNA-SDLC-MIB", "sdlcLSAdminISTATUS"),
        ("SNA-SDLC-MIB", "sdlcLSAdminMAXDATASend"),
        ("SNA-SDLC-MIB", "sdlcLSAdminMAXDATARcv"),
        ("SNA-SDLC-MIB", "sdlcLSAdminMAXIN"),
        ("SNA-SDLC-MIB", "sdlcLSAdminMAXOUT"),
        ("SNA-SDLC-MIB", "sdlcLSAdminMODULO"),
        ("SNA-SDLC-MIB", "sdlcLSAdminRETRIESm"),
        ("SNA-SDLC-MIB", "sdlcLSAdminRETRIESt"),
        ("SNA-SDLC-MIB", "sdlcLSAdminRETRIESn"),
        ("SNA-SDLC-MIB", "sdlcLSAdminRNRLIMIT"),
        ("SNA-SDLC-MIB", "sdlcLSAdminDATMODE"),
        ("SNA-SDLC-MIB", "sdlcLSAdminGPoll"),
        ("SNA-SDLC-MIB", "sdlcLSAdminSimRim"),
        ("SNA-SDLC-MIB", "sdlcLSAdminRowStatus"))
)
if mibBuilder.loadTexts:
    sdlcCoreLSAdminGroup.setStatus("current")

sdlcCoreLSOperGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 41, 1, 4, 2, 1, 5)
)
sdlcCoreLSOperGroup.setObjects(
      *(("SNA-SDLC-MIB", "sdlcLSOperRole"),
        ("SNA-SDLC-MIB", "sdlcLSOperState"),
        ("SNA-SDLC-MIB", "sdlcLSOperMAXDATASend"),
        ("SNA-SDLC-MIB", "sdlcLSOperMAXIN"),
        ("SNA-SDLC-MIB", "sdlcLSOperMAXOUT"),
        ("SNA-SDLC-MIB", "sdlcLSOperMODULO"),
        ("SNA-SDLC-MIB", "sdlcLSOperRETRIESm"),
        ("SNA-SDLC-MIB", "sdlcLSOperRETRIESt"),
        ("SNA-SDLC-MIB", "sdlcLSOperRETRIESn"),
        ("SNA-SDLC-MIB", "sdlcLSOperRNRLIMIT"),
        ("SNA-SDLC-MIB", "sdlcLSOperDATMODE"),
        ("SNA-SDLC-MIB", "sdlcLSOperLastFailTime"),
        ("SNA-SDLC-MIB", "sdlcLSOperLastFailCause"),
        ("SNA-SDLC-MIB", "sdlcLSOperLastFailCtrlIn"),
        ("SNA-SDLC-MIB", "sdlcLSOperLastFailCtrlOut"),
        ("SNA-SDLC-MIB", "sdlcLSOperLastFailFRMRInfo"),
        ("SNA-SDLC-MIB", "sdlcLSOperLastFailREPLYTOs"),
        ("SNA-SDLC-MIB", "sdlcLSOperEcho"),
        ("SNA-SDLC-MIB", "sdlcLSOperGPoll"))
)
if mibBuilder.loadTexts:
    sdlcCoreLSOperGroup.setStatus("current")

sdlcCoreLSStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 41, 1, 4, 2, 1, 6)
)
sdlcCoreLSStatsGroup.setObjects(
      *(("SNA-SDLC-MIB", "sdlcLSStatsBLUsIn"),
        ("SNA-SDLC-MIB", "sdlcLSStatsBLUsOut"),
        ("SNA-SDLC-MIB", "sdlcLSStatsOctetsIn"),
        ("SNA-SDLC-MIB", "sdlcLSStatsOctetsOut"),
        ("SNA-SDLC-MIB", "sdlcLSStatsPollsIn"),
        ("SNA-SDLC-MIB", "sdlcLSStatsPollsOut"),
        ("SNA-SDLC-MIB", "sdlcLSStatsPollRspsIn"),
        ("SNA-SDLC-MIB", "sdlcLSStatsPollRspsOut"),
        ("SNA-SDLC-MIB", "sdlcLSStatsLocalBusies"),
        ("SNA-SDLC-MIB", "sdlcLSStatsRemoteBusies"),
        ("SNA-SDLC-MIB", "sdlcLSStatsIFramesIn"),
        ("SNA-SDLC-MIB", "sdlcLSStatsIFramesOut"),
        ("SNA-SDLC-MIB", "sdlcLSStatsRetransmitsIn"),
        ("SNA-SDLC-MIB", "sdlcLSStatsRetransmitsOut"),
        ("SNA-SDLC-MIB", "sdlcLSStatsUIFramesIn"),
        ("SNA-SDLC-MIB", "sdlcLSStatsUIFramesOut"),
        ("SNA-SDLC-MIB", "sdlcLSStatsXIDsIn"),
        ("SNA-SDLC-MIB", "sdlcLSStatsXIDsOut"),
        ("SNA-SDLC-MIB", "sdlcLSStatsTESTsIn"),
        ("SNA-SDLC-MIB", "sdlcLSStatsTESTsOut"),
        ("SNA-SDLC-MIB", "sdlcLSStatsREJsIn"),
        ("SNA-SDLC-MIB", "sdlcLSStatsREJsOut"),
        ("SNA-SDLC-MIB", "sdlcLSStatsFRMRsIn"),
        ("SNA-SDLC-MIB", "sdlcLSStatsFRMRsOut"),
        ("SNA-SDLC-MIB", "sdlcLSStatsSIMsIn"),
        ("SNA-SDLC-MIB", "sdlcLSStatsSIMsOut"),
        ("SNA-SDLC-MIB", "sdlcLSStatsRIMsIn"),
        ("SNA-SDLC-MIB", "sdlcLSStatsRIMsOut"),
        ("SNA-SDLC-MIB", "sdlcLSStatsProtocolErrs"),
        ("SNA-SDLC-MIB", "sdlcLSStatsRNRLIMITs"),
        ("SNA-SDLC-MIB", "sdlcLSStatsRetriesExps"))
)
if mibBuilder.loadTexts:
    sdlcCoreLSStatsGroup.setStatus("current")

sdlcPrimaryGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 41, 1, 4, 2, 2, 1)
)
sdlcPrimaryGroup.setObjects(
      *(("SNA-SDLC-MIB", "sdlcPortAdminPAUSE"),
        ("SNA-SDLC-MIB", "sdlcPortOperPAUSE"),
        ("SNA-SDLC-MIB", "sdlcLSAdminREPLYTO"),
        ("SNA-SDLC-MIB", "sdlcLSOperREPLYTO"))
)
if mibBuilder.loadTexts:
    sdlcPrimaryGroup.setStatus("current")

sdlcPrimaryMultipointGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 41, 1, 4, 2, 2, 2)
)
sdlcPrimaryMultipointGroup.setObjects(
      *(("SNA-SDLC-MIB", "sdlcPortAdminSERVLIM"),
        ("SNA-SDLC-MIB", "sdlcPortAdminSlowPollTimer"),
        ("SNA-SDLC-MIB", "sdlcPortOperSlowPollMethod"),
        ("SNA-SDLC-MIB", "sdlcPortOperSERVLIM"),
        ("SNA-SDLC-MIB", "sdlcPortOperSlowPollTimer"))
)
if mibBuilder.loadTexts:
    sdlcPrimaryMultipointGroup.setStatus("current")


# Notification objects

sdlcPortStatusChange = NotificationType(
    (1, 3, 6, 1, 2, 1, 41, 1, 3, 1)
)
sdlcPortStatusChange.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifAdminStatus"),
        ("IF-MIB", "ifOperStatus"),
        ("SNA-SDLC-MIB", "sdlcPortOperLastFailTime"),
        ("SNA-SDLC-MIB", "sdlcPortOperLastFailCause"))
)
if mibBuilder.loadTexts:
    sdlcPortStatusChange.setStatus(
        "current"
    )

sdlcLSStatusChange = NotificationType(
    (1, 3, 6, 1, 2, 1, 41, 1, 3, 2)
)
sdlcLSStatusChange.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("SNA-SDLC-MIB", "sdlcLSAddress"),
        ("SNA-SDLC-MIB", "sdlcLSOperState"),
        ("SNA-SDLC-MIB", "sdlcLSAdminState"),
        ("SNA-SDLC-MIB", "sdlcLSOperLastFailTime"),
        ("SNA-SDLC-MIB", "sdlcLSOperLastFailCause"),
        ("SNA-SDLC-MIB", "sdlcLSOperLastFailFRMRInfo"),
        ("SNA-SDLC-MIB", "sdlcLSOperLastFailCtrlIn"),
        ("SNA-SDLC-MIB", "sdlcLSOperLastFailCtrlOut"),
        ("SNA-SDLC-MIB", "sdlcLSOperLastFailREPLYTOs"))
)
if mibBuilder.loadTexts:
    sdlcLSStatusChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

sdlcCoreCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 41, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    sdlcCoreCompliance.setStatus(
        "current"
    )

sdlcPrimaryCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 41, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    sdlcPrimaryCompliance.setStatus(
        "current"
    )

sdlcPrimaryMultipointCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 41, 1, 4, 1, 3)
)
if mibBuilder.loadTexts:
    sdlcPrimaryMultipointCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SNA-SDLC-MIB",
    **{"snaDLC": snaDLC,
       "sdlc": sdlc,
       "sdlcPortGroup": sdlcPortGroup,
       "sdlcPortAdminTable": sdlcPortAdminTable,
       "sdlcPortAdminEntry": sdlcPortAdminEntry,
       "sdlcPortAdminName": sdlcPortAdminName,
       "sdlcPortAdminRole": sdlcPortAdminRole,
       "sdlcPortAdminType": sdlcPortAdminType,
       "sdlcPortAdminTopology": sdlcPortAdminTopology,
       "sdlcPortAdminISTATUS": sdlcPortAdminISTATUS,
       "sdlcPortAdminACTIVTO": sdlcPortAdminACTIVTO,
       "sdlcPortAdminPAUSE": sdlcPortAdminPAUSE,
       "sdlcPortAdminSERVLIM": sdlcPortAdminSERVLIM,
       "sdlcPortAdminSlowPollTimer": sdlcPortAdminSlowPollTimer,
       "sdlcPortOperTable": sdlcPortOperTable,
       "sdlcPortOperEntry": sdlcPortOperEntry,
       "sdlcPortOperName": sdlcPortOperName,
       "sdlcPortOperRole": sdlcPortOperRole,
       "sdlcPortOperType": sdlcPortOperType,
       "sdlcPortOperTopology": sdlcPortOperTopology,
       "sdlcPortOperISTATUS": sdlcPortOperISTATUS,
       "sdlcPortOperACTIVTO": sdlcPortOperACTIVTO,
       "sdlcPortOperPAUSE": sdlcPortOperPAUSE,
       "sdlcPortOperSlowPollMethod": sdlcPortOperSlowPollMethod,
       "sdlcPortOperSERVLIM": sdlcPortOperSERVLIM,
       "sdlcPortOperSlowPollTimer": sdlcPortOperSlowPollTimer,
       "sdlcPortOperLastModifyTime": sdlcPortOperLastModifyTime,
       "sdlcPortOperLastFailTime": sdlcPortOperLastFailTime,
       "sdlcPortOperLastFailCause": sdlcPortOperLastFailCause,
       "sdlcPortStatsTable": sdlcPortStatsTable,
       "sdlcPortStatsEntry": sdlcPortStatsEntry,
       "sdlcPortStatsPhysicalFailures": sdlcPortStatsPhysicalFailures,
       "sdlcPortStatsInvalidAddresses": sdlcPortStatsInvalidAddresses,
       "sdlcPortStatsDwarfFrames": sdlcPortStatsDwarfFrames,
       "sdlcPortStatsPollsIn": sdlcPortStatsPollsIn,
       "sdlcPortStatsPollsOut": sdlcPortStatsPollsOut,
       "sdlcPortStatsPollRspsIn": sdlcPortStatsPollRspsIn,
       "sdlcPortStatsPollRspsOut": sdlcPortStatsPollRspsOut,
       "sdlcPortStatsLocalBusies": sdlcPortStatsLocalBusies,
       "sdlcPortStatsRemoteBusies": sdlcPortStatsRemoteBusies,
       "sdlcPortStatsIFramesIn": sdlcPortStatsIFramesIn,
       "sdlcPortStatsIFramesOut": sdlcPortStatsIFramesOut,
       "sdlcPortStatsOctetsIn": sdlcPortStatsOctetsIn,
       "sdlcPortStatsOctetsOut": sdlcPortStatsOctetsOut,
       "sdlcPortStatsProtocolErrs": sdlcPortStatsProtocolErrs,
       "sdlcPortStatsActivityTOs": sdlcPortStatsActivityTOs,
       "sdlcPortStatsRNRLIMITs": sdlcPortStatsRNRLIMITs,
       "sdlcPortStatsRetriesExps": sdlcPortStatsRetriesExps,
       "sdlcPortStatsRetransmitsIn": sdlcPortStatsRetransmitsIn,
       "sdlcPortStatsRetransmitsOut": sdlcPortStatsRetransmitsOut,
       "sdlcLSGroup": sdlcLSGroup,
       "sdlcLSAdminTable": sdlcLSAdminTable,
       "sdlcLSAdminEntry": sdlcLSAdminEntry,
       "sdlcLSAddress": sdlcLSAddress,
       "sdlcLSAdminName": sdlcLSAdminName,
       "sdlcLSAdminState": sdlcLSAdminState,
       "sdlcLSAdminISTATUS": sdlcLSAdminISTATUS,
       "sdlcLSAdminMAXDATASend": sdlcLSAdminMAXDATASend,
       "sdlcLSAdminMAXDATARcv": sdlcLSAdminMAXDATARcv,
       "sdlcLSAdminREPLYTO": sdlcLSAdminREPLYTO,
       "sdlcLSAdminMAXIN": sdlcLSAdminMAXIN,
       "sdlcLSAdminMAXOUT": sdlcLSAdminMAXOUT,
       "sdlcLSAdminMODULO": sdlcLSAdminMODULO,
       "sdlcLSAdminRETRIESm": sdlcLSAdminRETRIESm,
       "sdlcLSAdminRETRIESt": sdlcLSAdminRETRIESt,
       "sdlcLSAdminRETRIESn": sdlcLSAdminRETRIESn,
       "sdlcLSAdminRNRLIMIT": sdlcLSAdminRNRLIMIT,
       "sdlcLSAdminDATMODE": sdlcLSAdminDATMODE,
       "sdlcLSAdminGPoll": sdlcLSAdminGPoll,
       "sdlcLSAdminSimRim": sdlcLSAdminSimRim,
       "sdlcLSAdminXmitRcvCap": sdlcLSAdminXmitRcvCap,
       "sdlcLSAdminRowStatus": sdlcLSAdminRowStatus,
       "sdlcLSOperTable": sdlcLSOperTable,
       "sdlcLSOperEntry": sdlcLSOperEntry,
       "sdlcLSOperName": sdlcLSOperName,
       "sdlcLSOperRole": sdlcLSOperRole,
       "sdlcLSOperState": sdlcLSOperState,
       "sdlcLSOperMAXDATASend": sdlcLSOperMAXDATASend,
       "sdlcLSOperREPLYTO": sdlcLSOperREPLYTO,
       "sdlcLSOperMAXIN": sdlcLSOperMAXIN,
       "sdlcLSOperMAXOUT": sdlcLSOperMAXOUT,
       "sdlcLSOperMODULO": sdlcLSOperMODULO,
       "sdlcLSOperRETRIESm": sdlcLSOperRETRIESm,
       "sdlcLSOperRETRIESt": sdlcLSOperRETRIESt,
       "sdlcLSOperRETRIESn": sdlcLSOperRETRIESn,
       "sdlcLSOperRNRLIMIT": sdlcLSOperRNRLIMIT,
       "sdlcLSOperDATMODE": sdlcLSOperDATMODE,
       "sdlcLSOperLastModifyTime": sdlcLSOperLastModifyTime,
       "sdlcLSOperLastFailTime": sdlcLSOperLastFailTime,
       "sdlcLSOperLastFailCause": sdlcLSOperLastFailCause,
       "sdlcLSOperLastFailCtrlIn": sdlcLSOperLastFailCtrlIn,
       "sdlcLSOperLastFailCtrlOut": sdlcLSOperLastFailCtrlOut,
       "sdlcLSOperLastFailFRMRInfo": sdlcLSOperLastFailFRMRInfo,
       "sdlcLSOperLastFailREPLYTOs": sdlcLSOperLastFailREPLYTOs,
       "sdlcLSOperEcho": sdlcLSOperEcho,
       "sdlcLSOperGPoll": sdlcLSOperGPoll,
       "sdlcLSOperSimRim": sdlcLSOperSimRim,
       "sdlcLSOperXmitRcvCap": sdlcLSOperXmitRcvCap,
       "sdlcLSStatsTable": sdlcLSStatsTable,
       "sdlcLSStatsEntry": sdlcLSStatsEntry,
       "sdlcLSStatsBLUsIn": sdlcLSStatsBLUsIn,
       "sdlcLSStatsBLUsOut": sdlcLSStatsBLUsOut,
       "sdlcLSStatsOctetsIn": sdlcLSStatsOctetsIn,
       "sdlcLSStatsOctetsOut": sdlcLSStatsOctetsOut,
       "sdlcLSStatsPollsIn": sdlcLSStatsPollsIn,
       "sdlcLSStatsPollsOut": sdlcLSStatsPollsOut,
       "sdlcLSStatsPollRspsOut": sdlcLSStatsPollRspsOut,
       "sdlcLSStatsPollRspsIn": sdlcLSStatsPollRspsIn,
       "sdlcLSStatsLocalBusies": sdlcLSStatsLocalBusies,
       "sdlcLSStatsRemoteBusies": sdlcLSStatsRemoteBusies,
       "sdlcLSStatsIFramesIn": sdlcLSStatsIFramesIn,
       "sdlcLSStatsIFramesOut": sdlcLSStatsIFramesOut,
       "sdlcLSStatsUIFramesIn": sdlcLSStatsUIFramesIn,
       "sdlcLSStatsUIFramesOut": sdlcLSStatsUIFramesOut,
       "sdlcLSStatsXIDsIn": sdlcLSStatsXIDsIn,
       "sdlcLSStatsXIDsOut": sdlcLSStatsXIDsOut,
       "sdlcLSStatsTESTsIn": sdlcLSStatsTESTsIn,
       "sdlcLSStatsTESTsOut": sdlcLSStatsTESTsOut,
       "sdlcLSStatsREJsIn": sdlcLSStatsREJsIn,
       "sdlcLSStatsREJsOut": sdlcLSStatsREJsOut,
       "sdlcLSStatsFRMRsIn": sdlcLSStatsFRMRsIn,
       "sdlcLSStatsFRMRsOut": sdlcLSStatsFRMRsOut,
       "sdlcLSStatsSIMsIn": sdlcLSStatsSIMsIn,
       "sdlcLSStatsSIMsOut": sdlcLSStatsSIMsOut,
       "sdlcLSStatsRIMsIn": sdlcLSStatsRIMsIn,
       "sdlcLSStatsRIMsOut": sdlcLSStatsRIMsOut,
       "sdlcLSStatsDISCIn": sdlcLSStatsDISCIn,
       "sdlcLSStatsDISCOut": sdlcLSStatsDISCOut,
       "sdlcLSStatsUAIn": sdlcLSStatsUAIn,
       "sdlcLSStatsUAOut": sdlcLSStatsUAOut,
       "sdlcLSStatsDMIn": sdlcLSStatsDMIn,
       "sdlcLSStatsDMOut": sdlcLSStatsDMOut,
       "sdlcLSStatsSNRMIn": sdlcLSStatsSNRMIn,
       "sdlcLSStatsSNRMOut": sdlcLSStatsSNRMOut,
       "sdlcLSStatsProtocolErrs": sdlcLSStatsProtocolErrs,
       "sdlcLSStatsActivityTOs": sdlcLSStatsActivityTOs,
       "sdlcLSStatsRNRLIMITs": sdlcLSStatsRNRLIMITs,
       "sdlcLSStatsRetriesExps": sdlcLSStatsRetriesExps,
       "sdlcLSStatsRetransmitsIn": sdlcLSStatsRetransmitsIn,
       "sdlcLSStatsRetransmitsOut": sdlcLSStatsRetransmitsOut,
       "sdlcTraps": sdlcTraps,
       "sdlcPortStatusChange": sdlcPortStatusChange,
       "sdlcLSStatusChange": sdlcLSStatusChange,
       "sdlcConformance": sdlcConformance,
       "sdlcCompliances": sdlcCompliances,
       "sdlcCoreCompliance": sdlcCoreCompliance,
       "sdlcPrimaryCompliance": sdlcPrimaryCompliance,
       "sdlcPrimaryMultipointCompliance": sdlcPrimaryMultipointCompliance,
       "sdlcGroups": sdlcGroups,
       "sdlcCoreGroups": sdlcCoreGroups,
       "sdlcCorePortAdminGroup": sdlcCorePortAdminGroup,
       "sdlcCorePortOperGroup": sdlcCorePortOperGroup,
       "sdlcCorePortStatsGroup": sdlcCorePortStatsGroup,
       "sdlcCoreLSAdminGroup": sdlcCoreLSAdminGroup,
       "sdlcCoreLSOperGroup": sdlcCoreLSOperGroup,
       "sdlcCoreLSStatsGroup": sdlcCoreLSStatsGroup,
       "sdlcPrimaryGroups": sdlcPrimaryGroups,
       "sdlcPrimaryGroup": sdlcPrimaryGroup,
       "sdlcPrimaryMultipointGroup": sdlcPrimaryMultipointGroup}
)
