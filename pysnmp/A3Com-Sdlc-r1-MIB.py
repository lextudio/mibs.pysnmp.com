# SNMP MIB module (A3COM-SDLC-R1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-SDLC-R1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:29:46 2024
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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_A3com_ObjectIdentity = ObjectIdentity
a3com = _A3com_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43)
)
_BrouterMIB_ObjectIdentity = ObjectIdentity
brouterMIB = _BrouterMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2)
)
_Sdlc_ObjectIdentity = ObjectIdentity
sdlc = _Sdlc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 25)
)
_SdlcPortGroup_ObjectIdentity = ObjectIdentity
sdlcPortGroup = _SdlcPortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 1)
)
_SdlcPortAdminTable_Object = MibTable
sdlcPortAdminTable = _SdlcPortAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 1, 1)
)
if mibBuilder.loadTexts:
    sdlcPortAdminTable.setStatus("mandatory")
_SdlcPortAdminEntry_Object = MibTableRow
sdlcPortAdminEntry = _SdlcPortAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 1, 1, 1)
)
sdlcPortAdminEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    sdlcPortAdminEntry.setStatus("mandatory")


class _SdlcPortAdminName_Type(DisplayString):
    """Custom type sdlcPortAdminName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_SdlcPortAdminName_Type.__name__ = "DisplayString"
_SdlcPortAdminName_Object = MibTableColumn
sdlcPortAdminName = _SdlcPortAdminName_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 1, 1, 1, 1),
    _SdlcPortAdminName_Type()
)
sdlcPortAdminName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPortAdminName.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 1, 1, 1, 2),
    _SdlcPortAdminRole_Type()
)
sdlcPortAdminRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdlcPortAdminRole.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 1, 1, 1, 3),
    _SdlcPortAdminType_Type()
)
sdlcPortAdminType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdlcPortAdminType.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 1, 1, 1, 4),
    _SdlcPortAdminTopology_Type()
)
sdlcPortAdminTopology.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdlcPortAdminTopology.setStatus("mandatory")


class _SdlcPortAdminACTIVTO_Type(TimeTicks):
    """Custom type sdlcPortAdminACTIVTO based on TimeTicks"""
    defaultValue = 0


_SdlcPortAdminACTIVTO_Object = MibTableColumn
sdlcPortAdminACTIVTO = _SdlcPortAdminACTIVTO_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 1, 1, 1, 5),
    _SdlcPortAdminACTIVTO_Type()
)
sdlcPortAdminACTIVTO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdlcPortAdminACTIVTO.setStatus("mandatory")


class _SdlcPortAdminPAUSE_Type(TimeTicks):
    """Custom type sdlcPortAdminPAUSE based on TimeTicks"""
    defaultValue = 200


_SdlcPortAdminPAUSE_Object = MibTableColumn
sdlcPortAdminPAUSE = _SdlcPortAdminPAUSE_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 1, 1, 1, 6),
    _SdlcPortAdminPAUSE_Type()
)
sdlcPortAdminPAUSE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdlcPortAdminPAUSE.setStatus("mandatory")


class _SdlcPortAdminSlowPollTimer_Type(TimeTicks):
    """Custom type sdlcPortAdminSlowPollTimer based on TimeTicks"""
    defaultValue = 2000


_SdlcPortAdminSlowPollTimer_Object = MibTableColumn
sdlcPortAdminSlowPollTimer = _SdlcPortAdminSlowPollTimer_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 1, 1, 1, 7),
    _SdlcPortAdminSlowPollTimer_Type()
)
sdlcPortAdminSlowPollTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdlcPortAdminSlowPollTimer.setStatus("mandatory")
_SdlcPortOperTable_Object = MibTable
sdlcPortOperTable = _SdlcPortOperTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 1, 2)
)
if mibBuilder.loadTexts:
    sdlcPortOperTable.setStatus("mandatory")
_SdlcPortOperEntry_Object = MibTableRow
sdlcPortOperEntry = _SdlcPortOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 1, 2, 1)
)
sdlcPortOperEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    sdlcPortOperEntry.setStatus("mandatory")


class _SdlcPortOperName_Type(DisplayString):
    """Custom type sdlcPortOperName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_SdlcPortOperName_Type.__name__ = "DisplayString"
_SdlcPortOperName_Object = MibTableColumn
sdlcPortOperName = _SdlcPortOperName_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 1, 2, 1, 1),
    _SdlcPortOperName_Type()
)
sdlcPortOperName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPortOperName.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 1, 2, 1, 2),
    _SdlcPortOperRole_Type()
)
sdlcPortOperRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPortOperRole.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 1, 2, 1, 3),
    _SdlcPortOperType_Type()
)
sdlcPortOperType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPortOperType.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 1, 2, 1, 4),
    _SdlcPortOperTopology_Type()
)
sdlcPortOperTopology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPortOperTopology.setStatus("mandatory")
_SdlcPortOperACTIVTO_Type = TimeTicks
_SdlcPortOperACTIVTO_Object = MibTableColumn
sdlcPortOperACTIVTO = _SdlcPortOperACTIVTO_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 1, 2, 1, 5),
    _SdlcPortOperACTIVTO_Type()
)
sdlcPortOperACTIVTO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPortOperACTIVTO.setStatus("mandatory")
_SdlcPortOperPAUSE_Type = TimeTicks
_SdlcPortOperPAUSE_Object = MibTableColumn
sdlcPortOperPAUSE = _SdlcPortOperPAUSE_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 1, 2, 1, 6),
    _SdlcPortOperPAUSE_Type()
)
sdlcPortOperPAUSE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPortOperPAUSE.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 1, 2, 1, 7),
    _SdlcPortOperSlowPollMethod_Type()
)
sdlcPortOperSlowPollMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPortOperSlowPollMethod.setStatus("mandatory")
_SdlcPortOperSlowPollTimer_Type = TimeTicks
_SdlcPortOperSlowPollTimer_Object = MibTableColumn
sdlcPortOperSlowPollTimer = _SdlcPortOperSlowPollTimer_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 1, 2, 1, 8),
    _SdlcPortOperSlowPollTimer_Type()
)
sdlcPortOperSlowPollTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPortOperSlowPollTimer.setStatus("mandatory")
_SdlcPortOperLastFailTime_Type = TimeTicks
_SdlcPortOperLastFailTime_Object = MibTableColumn
sdlcPortOperLastFailTime = _SdlcPortOperLastFailTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 1, 2, 1, 9),
    _SdlcPortOperLastFailTime_Type()
)
sdlcPortOperLastFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPortOperLastFailTime.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 1, 2, 1, 10),
    _SdlcPortOperLastFailCause_Type()
)
sdlcPortOperLastFailCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPortOperLastFailCause.setStatus("mandatory")
_SdlcPortStatsTable_Object = MibTable
sdlcPortStatsTable = _SdlcPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 1, 3)
)
if mibBuilder.loadTexts:
    sdlcPortStatsTable.setStatus("mandatory")
_SdlcPortStatsEntry_Object = MibTableRow
sdlcPortStatsEntry = _SdlcPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 1, 3, 1)
)
sdlcPortStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    sdlcPortStatsEntry.setStatus("mandatory")
_SdlcPortStatsPhysicalFailures_Type = Counter32
_SdlcPortStatsPhysicalFailures_Object = MibTableColumn
sdlcPortStatsPhysicalFailures = _SdlcPortStatsPhysicalFailures_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 1, 3, 1, 1),
    _SdlcPortStatsPhysicalFailures_Type()
)
sdlcPortStatsPhysicalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPortStatsPhysicalFailures.setStatus("mandatory")
_SdlcPortStatsInvalidAddresses_Type = Counter32
_SdlcPortStatsInvalidAddresses_Object = MibTableColumn
sdlcPortStatsInvalidAddresses = _SdlcPortStatsInvalidAddresses_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 1, 3, 1, 2),
    _SdlcPortStatsInvalidAddresses_Type()
)
sdlcPortStatsInvalidAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPortStatsInvalidAddresses.setStatus("mandatory")
_SdlcPortStatsDwarfFrames_Type = Counter32
_SdlcPortStatsDwarfFrames_Object = MibTableColumn
sdlcPortStatsDwarfFrames = _SdlcPortStatsDwarfFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 1, 3, 1, 3),
    _SdlcPortStatsDwarfFrames_Type()
)
sdlcPortStatsDwarfFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcPortStatsDwarfFrames.setStatus("mandatory")
_SdlcLSGroup_ObjectIdentity = ObjectIdentity
sdlcLSGroup = _SdlcLSGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2)
)
_SdlcLSAdminTable_Object = MibTable
sdlcLSAdminTable = _SdlcLSAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 1)
)
if mibBuilder.loadTexts:
    sdlcLSAdminTable.setStatus("mandatory")
_SdlcLSAdminEntry_Object = MibTableRow
sdlcLSAdminEntry = _SdlcLSAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 1, 1)
)
sdlcLSAdminEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-SDLC-R1-MIB", "sdlcLSAddress"),
)
if mibBuilder.loadTexts:
    sdlcLSAdminEntry.setStatus("mandatory")


class _SdlcLSAddress_Type(Integer32):
    """Custom type sdlcLSAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SdlcLSAddress_Type.__name__ = "Integer32"
_SdlcLSAddress_Object = MibTableColumn
sdlcLSAddress = _SdlcLSAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 1, 1, 1),
    _SdlcLSAddress_Type()
)
sdlcLSAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdlcLSAddress.setStatus("mandatory")


class _SdlcLSAdminName_Type(DisplayString):
    """Custom type sdlcLSAdminName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_SdlcLSAdminName_Type.__name__ = "DisplayString"
_SdlcLSAdminName_Object = MibTableColumn
sdlcLSAdminName = _SdlcLSAdminName_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 1, 1, 2),
    _SdlcLSAdminName_Type()
)
sdlcLSAdminName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdlcLSAdminName.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 1, 1, 3),
    _SdlcLSAdminState_Type()
)
sdlcLSAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdlcLSAdminState.setStatus("mandatory")
_SdlcLSAdminMAXDATA_Type = Integer32
_SdlcLSAdminMAXDATA_Object = MibTableColumn
sdlcLSAdminMAXDATA = _SdlcLSAdminMAXDATA_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 1, 1, 4),
    _SdlcLSAdminMAXDATA_Type()
)
sdlcLSAdminMAXDATA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSAdminMAXDATA.setStatus("mandatory")


class _SdlcLSAdminREPLYTO_Type(TimeTicks):
    """Custom type sdlcLSAdminREPLYTO based on TimeTicks"""
    defaultValue = 100


_SdlcLSAdminREPLYTO_Object = MibTableColumn
sdlcLSAdminREPLYTO = _SdlcLSAdminREPLYTO_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 1, 1, 5),
    _SdlcLSAdminREPLYTO_Type()
)
sdlcLSAdminREPLYTO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdlcLSAdminREPLYTO.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 1, 1, 6),
    _SdlcLSAdminMAXIN_Type()
)
sdlcLSAdminMAXIN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSAdminMAXIN.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 1, 1, 7),
    _SdlcLSAdminMAXOUT_Type()
)
sdlcLSAdminMAXOUT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdlcLSAdminMAXOUT.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 1, 1, 8),
    _SdlcLSAdminMODULO_Type()
)
sdlcLSAdminMODULO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSAdminMODULO.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 1, 1, 9),
    _SdlcLSAdminRETRIESm_Type()
)
sdlcLSAdminRETRIESm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSAdminRETRIESm.setStatus("mandatory")


class _SdlcLSAdminRETRIESt_Type(TimeTicks):
    """Custom type sdlcLSAdminRETRIESt based on TimeTicks"""
    defaultValue = 0


_SdlcLSAdminRETRIESt_Object = MibTableColumn
sdlcLSAdminRETRIESt = _SdlcLSAdminRETRIESt_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 1, 1, 10),
    _SdlcLSAdminRETRIESt_Type()
)
sdlcLSAdminRETRIESt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdlcLSAdminRETRIESt.setStatus("mandatory")


class _SdlcLSAdminRETRIESn_Type(Integer32):
    """Custom type sdlcLSAdminRETRIESn based on Integer32"""
    defaultValue = 0


_SdlcLSAdminRETRIESn_Object = MibTableColumn
sdlcLSAdminRETRIESn = _SdlcLSAdminRETRIESn_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 1, 1, 11),
    _SdlcLSAdminRETRIESn_Type()
)
sdlcLSAdminRETRIESn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdlcLSAdminRETRIESn.setStatus("mandatory")


class _SdlcLSAdminRNRLIMIT_Type(TimeTicks):
    """Custom type sdlcLSAdminRNRLIMIT based on TimeTicks"""
    defaultValue = 18000


_SdlcLSAdminRNRLIMIT_Object = MibTableColumn
sdlcLSAdminRNRLIMIT = _SdlcLSAdminRNRLIMIT_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 1, 1, 12),
    _SdlcLSAdminRNRLIMIT_Type()
)
sdlcLSAdminRNRLIMIT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdlcLSAdminRNRLIMIT.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 1, 1, 13),
    _SdlcLSAdminDATMODE_Type()
)
sdlcLSAdminDATMODE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSAdminDATMODE.setStatus("mandatory")


class _SdlcLSAdminGPoll_Type(Integer32):
    """Custom type sdlcLSAdminGPoll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_SdlcLSAdminGPoll_Type.__name__ = "Integer32"
_SdlcLSAdminGPoll_Object = MibTableColumn
sdlcLSAdminGPoll = _SdlcLSAdminGPoll_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 1, 1, 14),
    _SdlcLSAdminGPoll_Type()
)
sdlcLSAdminGPoll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdlcLSAdminGPoll.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 1, 1, 15),
    _SdlcLSAdminSimRim_Type()
)
sdlcLSAdminSimRim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSAdminSimRim.setStatus("mandatory")
_SdlcLSOperTable_Object = MibTable
sdlcLSOperTable = _SdlcLSOperTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 2)
)
if mibBuilder.loadTexts:
    sdlcLSOperTable.setStatus("mandatory")
_SdlcLSOperEntry_Object = MibTableRow
sdlcLSOperEntry = _SdlcLSOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 2, 1)
)
sdlcLSOperEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-SDLC-R1-MIB", "sdlcLSAddress"),
)
if mibBuilder.loadTexts:
    sdlcLSOperEntry.setStatus("mandatory")


class _SdlcLSOperName_Type(DisplayString):
    """Custom type sdlcLSOperName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_SdlcLSOperName_Type.__name__ = "DisplayString"
_SdlcLSOperName_Object = MibTableColumn
sdlcLSOperName = _SdlcLSOperName_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 2, 1, 1),
    _SdlcLSOperName_Type()
)
sdlcLSOperName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSOperName.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 2, 1, 2),
    _SdlcLSOperRole_Type()
)
sdlcLSOperRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSOperRole.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 2, 1, 3),
    _SdlcLSOperState_Type()
)
sdlcLSOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSOperState.setStatus("mandatory")
_SdlcLSOperMAXDATA_Type = Integer32
_SdlcLSOperMAXDATA_Object = MibTableColumn
sdlcLSOperMAXDATA = _SdlcLSOperMAXDATA_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 2, 1, 4),
    _SdlcLSOperMAXDATA_Type()
)
sdlcLSOperMAXDATA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSOperMAXDATA.setStatus("mandatory")
_SdlcLSOperREPLYTO_Type = TimeTicks
_SdlcLSOperREPLYTO_Object = MibTableColumn
sdlcLSOperREPLYTO = _SdlcLSOperREPLYTO_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 2, 1, 5),
    _SdlcLSOperREPLYTO_Type()
)
sdlcLSOperREPLYTO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSOperREPLYTO.setStatus("mandatory")


class _SdlcLSOperMAXIN_Type(Integer32):
    """Custom type sdlcLSOperMAXIN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_SdlcLSOperMAXIN_Type.__name__ = "Integer32"
_SdlcLSOperMAXIN_Object = MibTableColumn
sdlcLSOperMAXIN = _SdlcLSOperMAXIN_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 2, 1, 6),
    _SdlcLSOperMAXIN_Type()
)
sdlcLSOperMAXIN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSOperMAXIN.setStatus("mandatory")


class _SdlcLSOperMAXOUT_Type(Integer32):
    """Custom type sdlcLSOperMAXOUT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_SdlcLSOperMAXOUT_Type.__name__ = "Integer32"
_SdlcLSOperMAXOUT_Object = MibTableColumn
sdlcLSOperMAXOUT = _SdlcLSOperMAXOUT_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 2, 1, 7),
    _SdlcLSOperMAXOUT_Type()
)
sdlcLSOperMAXOUT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSOperMAXOUT.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 2, 1, 8),
    _SdlcLSOperMODULO_Type()
)
sdlcLSOperMODULO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSOperMODULO.setStatus("mandatory")


class _SdlcLSOperRETRIESm_Type(Integer32):
    """Custom type sdlcLSOperRETRIESm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SdlcLSOperRETRIESm_Type.__name__ = "Integer32"
_SdlcLSOperRETRIESm_Object = MibTableColumn
sdlcLSOperRETRIESm = _SdlcLSOperRETRIESm_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 2, 1, 9),
    _SdlcLSOperRETRIESm_Type()
)
sdlcLSOperRETRIESm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSOperRETRIESm.setStatus("mandatory")
_SdlcLSOperRETRIESt_Type = TimeTicks
_SdlcLSOperRETRIESt_Object = MibTableColumn
sdlcLSOperRETRIESt = _SdlcLSOperRETRIESt_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 2, 1, 10),
    _SdlcLSOperRETRIESt_Type()
)
sdlcLSOperRETRIESt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSOperRETRIESt.setStatus("mandatory")


class _SdlcLSOperRETRIESn_Type(Integer32):
    """Custom type sdlcLSOperRETRIESn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SdlcLSOperRETRIESn_Type.__name__ = "Integer32"
_SdlcLSOperRETRIESn_Object = MibTableColumn
sdlcLSOperRETRIESn = _SdlcLSOperRETRIESn_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 2, 1, 11),
    _SdlcLSOperRETRIESn_Type()
)
sdlcLSOperRETRIESn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSOperRETRIESn.setStatus("mandatory")
_SdlcLSOperRNRLIMIT_Type = TimeTicks
_SdlcLSOperRNRLIMIT_Object = MibTableColumn
sdlcLSOperRNRLIMIT = _SdlcLSOperRNRLIMIT_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 2, 1, 12),
    _SdlcLSOperRNRLIMIT_Type()
)
sdlcLSOperRNRLIMIT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSOperRNRLIMIT.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 2, 1, 13),
    _SdlcLSOperDATMODE_Type()
)
sdlcLSOperDATMODE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSOperDATMODE.setStatus("mandatory")
_SdlcLSOperLastFailTime_Type = TimeTicks
_SdlcLSOperLastFailTime_Object = MibTableColumn
sdlcLSOperLastFailTime = _SdlcLSOperLastFailTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 2, 1, 14),
    _SdlcLSOperLastFailTime_Type()
)
sdlcLSOperLastFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSOperLastFailTime.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 2, 1, 15),
    _SdlcLSOperLastFailCause_Type()
)
sdlcLSOperLastFailCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSOperLastFailCause.setStatus("mandatory")


class _SdlcLSOperLastFailCtrlIn_Type(OctetString):
    """Custom type sdlcLSOperLastFailCtrlIn based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2),
    )


_SdlcLSOperLastFailCtrlIn_Type.__name__ = "OctetString"
_SdlcLSOperLastFailCtrlIn_Object = MibTableColumn
sdlcLSOperLastFailCtrlIn = _SdlcLSOperLastFailCtrlIn_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 2, 1, 16),
    _SdlcLSOperLastFailCtrlIn_Type()
)
sdlcLSOperLastFailCtrlIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSOperLastFailCtrlIn.setStatus("mandatory")


class _SdlcLSOperLastFailCtrlOut_Type(OctetString):
    """Custom type sdlcLSOperLastFailCtrlOut based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2),
    )


_SdlcLSOperLastFailCtrlOut_Type.__name__ = "OctetString"
_SdlcLSOperLastFailCtrlOut_Object = MibTableColumn
sdlcLSOperLastFailCtrlOut = _SdlcLSOperLastFailCtrlOut_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 2, 1, 17),
    _SdlcLSOperLastFailCtrlOut_Type()
)
sdlcLSOperLastFailCtrlOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSOperLastFailCtrlOut.setStatus("mandatory")


class _SdlcLSOperLastFailFRMRInfo_Type(OctetString):
    """Custom type sdlcLSOperLastFailFRMRInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_SdlcLSOperLastFailFRMRInfo_Type.__name__ = "OctetString"
_SdlcLSOperLastFailFRMRInfo_Object = MibTableColumn
sdlcLSOperLastFailFRMRInfo = _SdlcLSOperLastFailFRMRInfo_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 2, 1, 18),
    _SdlcLSOperLastFailFRMRInfo_Type()
)
sdlcLSOperLastFailFRMRInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSOperLastFailFRMRInfo.setStatus("mandatory")
_SdlcLSOperLastFailREPLYTOs_Type = Counter32
_SdlcLSOperLastFailREPLYTOs_Object = MibTableColumn
sdlcLSOperLastFailREPLYTOs = _SdlcLSOperLastFailREPLYTOs_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 2, 1, 19),
    _SdlcLSOperLastFailREPLYTOs_Type()
)
sdlcLSOperLastFailREPLYTOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSOperLastFailREPLYTOs.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 2, 1, 20),
    _SdlcLSOperGPoll_Type()
)
sdlcLSOperGPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSOperGPoll.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 2, 1, 21),
    _SdlcLSOperSimRim_Type()
)
sdlcLSOperSimRim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSOperSimRim.setStatus("mandatory")
_SdlcLSStatsTable_Object = MibTable
sdlcLSStatsTable = _SdlcLSStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3)
)
if mibBuilder.loadTexts:
    sdlcLSStatsTable.setStatus("mandatory")
_SdlcLSStatsEntry_Object = MibTableRow
sdlcLSStatsEntry = _SdlcLSStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1)
)
sdlcLSStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-SDLC-R1-MIB", "sdlcLSAddress"),
)
if mibBuilder.loadTexts:
    sdlcLSStatsEntry.setStatus("mandatory")
_SdlcLSStatsBLUsIn_Type = Counter32
_SdlcLSStatsBLUsIn_Object = MibTableColumn
sdlcLSStatsBLUsIn = _SdlcLSStatsBLUsIn_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 1),
    _SdlcLSStatsBLUsIn_Type()
)
sdlcLSStatsBLUsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsBLUsIn.setStatus("mandatory")
_SdlcLSStatsBLUsOut_Type = Counter32
_SdlcLSStatsBLUsOut_Object = MibTableColumn
sdlcLSStatsBLUsOut = _SdlcLSStatsBLUsOut_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 2),
    _SdlcLSStatsBLUsOut_Type()
)
sdlcLSStatsBLUsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsBLUsOut.setStatus("mandatory")
_SdlcLSStatsOctetsIn_Type = Counter32
_SdlcLSStatsOctetsIn_Object = MibTableColumn
sdlcLSStatsOctetsIn = _SdlcLSStatsOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 3),
    _SdlcLSStatsOctetsIn_Type()
)
sdlcLSStatsOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsOctetsIn.setStatus("mandatory")
_SdlcLSStatsOctetsOut_Type = Counter32
_SdlcLSStatsOctetsOut_Object = MibTableColumn
sdlcLSStatsOctetsOut = _SdlcLSStatsOctetsOut_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 4),
    _SdlcLSStatsOctetsOut_Type()
)
sdlcLSStatsOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsOctetsOut.setStatus("mandatory")
_SdlcLSStatsPollsOut_Type = Counter32
_SdlcLSStatsPollsOut_Object = MibTableColumn
sdlcLSStatsPollsOut = _SdlcLSStatsPollsOut_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 5),
    _SdlcLSStatsPollsOut_Type()
)
sdlcLSStatsPollsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsPollsOut.setStatus("mandatory")
_SdlcLSStatsPollRspsOut_Type = Counter32
_SdlcLSStatsPollRspsOut_Object = MibTableColumn
sdlcLSStatsPollRspsOut = _SdlcLSStatsPollRspsOut_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 6),
    _SdlcLSStatsPollRspsOut_Type()
)
sdlcLSStatsPollRspsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsPollRspsOut.setStatus("mandatory")
_SdlcLSStatsLocalBusies_Type = Counter32
_SdlcLSStatsLocalBusies_Object = MibTableColumn
sdlcLSStatsLocalBusies = _SdlcLSStatsLocalBusies_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 7),
    _SdlcLSStatsLocalBusies_Type()
)
sdlcLSStatsLocalBusies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsLocalBusies.setStatus("mandatory")
_SdlcLSStatsRemoteBusies_Type = Counter32
_SdlcLSStatsRemoteBusies_Object = MibTableColumn
sdlcLSStatsRemoteBusies = _SdlcLSStatsRemoteBusies_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 8),
    _SdlcLSStatsRemoteBusies_Type()
)
sdlcLSStatsRemoteBusies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsRemoteBusies.setStatus("mandatory")
_SdlcLSStatsIFramesIn_Type = Counter32
_SdlcLSStatsIFramesIn_Object = MibTableColumn
sdlcLSStatsIFramesIn = _SdlcLSStatsIFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 9),
    _SdlcLSStatsIFramesIn_Type()
)
sdlcLSStatsIFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsIFramesIn.setStatus("mandatory")
_SdlcLSStatsIFramesOut_Type = Counter32
_SdlcLSStatsIFramesOut_Object = MibTableColumn
sdlcLSStatsIFramesOut = _SdlcLSStatsIFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 10),
    _SdlcLSStatsIFramesOut_Type()
)
sdlcLSStatsIFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsIFramesOut.setStatus("mandatory")
_SdlcLSStatsRetransmits_Type = Counter32
_SdlcLSStatsRetransmits_Object = MibTableColumn
sdlcLSStatsRetransmits = _SdlcLSStatsRetransmits_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 11),
    _SdlcLSStatsRetransmits_Type()
)
sdlcLSStatsRetransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsRetransmits.setStatus("mandatory")
_SdlcLSStatsIOctetsIn_Type = Counter32
_SdlcLSStatsIOctetsIn_Object = MibTableColumn
sdlcLSStatsIOctetsIn = _SdlcLSStatsIOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 12),
    _SdlcLSStatsIOctetsIn_Type()
)
sdlcLSStatsIOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsIOctetsIn.setStatus("mandatory")
_SdlcLSStatsIOctetsOut_Type = Counter32
_SdlcLSStatsIOctetsOut_Object = MibTableColumn
sdlcLSStatsIOctetsOut = _SdlcLSStatsIOctetsOut_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 13),
    _SdlcLSStatsIOctetsOut_Type()
)
sdlcLSStatsIOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsIOctetsOut.setStatus("mandatory")
_SdlcLSStatsUIFramesIn_Type = Counter32
_SdlcLSStatsUIFramesIn_Object = MibTableColumn
sdlcLSStatsUIFramesIn = _SdlcLSStatsUIFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 14),
    _SdlcLSStatsUIFramesIn_Type()
)
sdlcLSStatsUIFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsUIFramesIn.setStatus("mandatory")
_SdlcLSStatsUIFramesOut_Type = Counter32
_SdlcLSStatsUIFramesOut_Object = MibTableColumn
sdlcLSStatsUIFramesOut = _SdlcLSStatsUIFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 15),
    _SdlcLSStatsUIFramesOut_Type()
)
sdlcLSStatsUIFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsUIFramesOut.setStatus("mandatory")
_SdlcLSStatsXIDsIn_Type = Counter32
_SdlcLSStatsXIDsIn_Object = MibTableColumn
sdlcLSStatsXIDsIn = _SdlcLSStatsXIDsIn_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 16),
    _SdlcLSStatsXIDsIn_Type()
)
sdlcLSStatsXIDsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsXIDsIn.setStatus("mandatory")
_SdlcLSStatsXIDsOut_Type = Counter32
_SdlcLSStatsXIDsOut_Object = MibTableColumn
sdlcLSStatsXIDsOut = _SdlcLSStatsXIDsOut_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 17),
    _SdlcLSStatsXIDsOut_Type()
)
sdlcLSStatsXIDsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsXIDsOut.setStatus("mandatory")
_SdlcLSStatsTESTsIn_Type = Counter32
_SdlcLSStatsTESTsIn_Object = MibTableColumn
sdlcLSStatsTESTsIn = _SdlcLSStatsTESTsIn_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 18),
    _SdlcLSStatsTESTsIn_Type()
)
sdlcLSStatsTESTsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsTESTsIn.setStatus("mandatory")
_SdlcLSStatsTESTsOut_Type = Counter32
_SdlcLSStatsTESTsOut_Object = MibTableColumn
sdlcLSStatsTESTsOut = _SdlcLSStatsTESTsOut_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 19),
    _SdlcLSStatsTESTsOut_Type()
)
sdlcLSStatsTESTsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsTESTsOut.setStatus("mandatory")
_SdlcLSStatsREJsIn_Type = Counter32
_SdlcLSStatsREJsIn_Object = MibTableColumn
sdlcLSStatsREJsIn = _SdlcLSStatsREJsIn_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 20),
    _SdlcLSStatsREJsIn_Type()
)
sdlcLSStatsREJsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsREJsIn.setStatus("mandatory")
_SdlcLSStatsREJsOut_Type = Counter32
_SdlcLSStatsREJsOut_Object = MibTableColumn
sdlcLSStatsREJsOut = _SdlcLSStatsREJsOut_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 21),
    _SdlcLSStatsREJsOut_Type()
)
sdlcLSStatsREJsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsREJsOut.setStatus("mandatory")
_SdlcLSStatsFRMRsIn_Type = Counter32
_SdlcLSStatsFRMRsIn_Object = MibTableColumn
sdlcLSStatsFRMRsIn = _SdlcLSStatsFRMRsIn_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 22),
    _SdlcLSStatsFRMRsIn_Type()
)
sdlcLSStatsFRMRsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsFRMRsIn.setStatus("mandatory")
_SdlcLSStatsFRMRsOut_Type = Counter32
_SdlcLSStatsFRMRsOut_Object = MibTableColumn
sdlcLSStatsFRMRsOut = _SdlcLSStatsFRMRsOut_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 23),
    _SdlcLSStatsFRMRsOut_Type()
)
sdlcLSStatsFRMRsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsFRMRsOut.setStatus("mandatory")
_SdlcLSStatsSIMsIn_Type = Counter32
_SdlcLSStatsSIMsIn_Object = MibTableColumn
sdlcLSStatsSIMsIn = _SdlcLSStatsSIMsIn_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 24),
    _SdlcLSStatsSIMsIn_Type()
)
sdlcLSStatsSIMsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsSIMsIn.setStatus("mandatory")
_SdlcLSStatsSIMsOut_Type = Counter32
_SdlcLSStatsSIMsOut_Object = MibTableColumn
sdlcLSStatsSIMsOut = _SdlcLSStatsSIMsOut_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 25),
    _SdlcLSStatsSIMsOut_Type()
)
sdlcLSStatsSIMsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsSIMsOut.setStatus("mandatory")
_SdlcLSStatsRIMsIn_Type = Counter32
_SdlcLSStatsRIMsIn_Object = MibTableColumn
sdlcLSStatsRIMsIn = _SdlcLSStatsRIMsIn_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 26),
    _SdlcLSStatsRIMsIn_Type()
)
sdlcLSStatsRIMsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsRIMsIn.setStatus("mandatory")
_SdlcLSStatsRIMsOut_Type = Counter32
_SdlcLSStatsRIMsOut_Object = MibTableColumn
sdlcLSStatsRIMsOut = _SdlcLSStatsRIMsOut_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 27),
    _SdlcLSStatsRIMsOut_Type()
)
sdlcLSStatsRIMsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsRIMsOut.setStatus("mandatory")
_SdlcLSStatsProtocolErrs_Type = Counter32
_SdlcLSStatsProtocolErrs_Object = MibTableColumn
sdlcLSStatsProtocolErrs = _SdlcLSStatsProtocolErrs_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 28),
    _SdlcLSStatsProtocolErrs_Type()
)
sdlcLSStatsProtocolErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsProtocolErrs.setStatus("mandatory")
_SdlcLSStatsActivityTOs_Type = Counter32
_SdlcLSStatsActivityTOs_Object = MibTableColumn
sdlcLSStatsActivityTOs = _SdlcLSStatsActivityTOs_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 29),
    _SdlcLSStatsActivityTOs_Type()
)
sdlcLSStatsActivityTOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsActivityTOs.setStatus("mandatory")
_SdlcLSStatsRNRLIMITs_Type = Counter32
_SdlcLSStatsRNRLIMITs_Object = MibTableColumn
sdlcLSStatsRNRLIMITs = _SdlcLSStatsRNRLIMITs_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 30),
    _SdlcLSStatsRNRLIMITs_Type()
)
sdlcLSStatsRNRLIMITs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsRNRLIMITs.setStatus("mandatory")
_SdlcLSStatsRetriesExps_Type = Counter32
_SdlcLSStatsRetriesExps_Object = MibTableColumn
sdlcLSStatsRetriesExps = _SdlcLSStatsRetriesExps_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 2, 3, 1, 31),
    _SdlcLSStatsRetriesExps_Type()
)
sdlcLSStatsRetriesExps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLSStatsRetriesExps.setStatus("mandatory")
_SdlcMapGroup_ObjectIdentity = ObjectIdentity
sdlcMapGroup = _SdlcMapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 3)
)
_SdlcMapTable_Object = MibTable
sdlcMapTable = _SdlcMapTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 3, 1)
)
if mibBuilder.loadTexts:
    sdlcMapTable.setStatus("mandatory")
_SdlcMapEntry_Object = MibTableRow
sdlcMapEntry = _SdlcMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 3, 1, 1)
)
sdlcMapEntry.setIndexNames(
    (0, "A3COM-SDLC-R1-MIB", "pysmiFakeCol1"),
)
if mibBuilder.loadTexts:
    sdlcMapEntry.setStatus("mandatory")


class _SdlcMapPollAddress_Type(Integer32):
    """Custom type sdlcMapPollAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SdlcMapPollAddress_Type.__name__ = "Integer32"
_SdlcMapPollAddress_Object = MibTableColumn
sdlcMapPollAddress = _SdlcMapPollAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 3, 1, 1, 1),
    _SdlcMapPollAddress_Type()
)
sdlcMapPollAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcMapPollAddress.setStatus("mandatory")
_SdlcMapLocalMacAddress_Type = MacAddress
_SdlcMapLocalMacAddress_Object = MibTableColumn
sdlcMapLocalMacAddress = _SdlcMapLocalMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 3, 1, 1, 2),
    _SdlcMapLocalMacAddress_Type()
)
sdlcMapLocalMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcMapLocalMacAddress.setStatus("mandatory")


class _SdlcMapLocalSap_Type(OctetString):
    """Custom type sdlcMapLocalSap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_SdlcMapLocalSap_Type.__name__ = "OctetString"
_SdlcMapLocalSap_Object = MibTableColumn
sdlcMapLocalSap = _SdlcMapLocalSap_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 3, 1, 1, 3),
    _SdlcMapLocalSap_Type()
)
sdlcMapLocalSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcMapLocalSap.setStatus("mandatory")
_SdlcMapRemoteMacAddress_Type = MacAddress
_SdlcMapRemoteMacAddress_Object = MibTableColumn
sdlcMapRemoteMacAddress = _SdlcMapRemoteMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 3, 1, 1, 4),
    _SdlcMapRemoteMacAddress_Type()
)
sdlcMapRemoteMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcMapRemoteMacAddress.setStatus("mandatory")


class _SdlcMapRemoteSap_Type(OctetString):
    """Custom type sdlcMapRemoteSap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_SdlcMapRemoteSap_Type.__name__ = "OctetString"
_SdlcMapRemoteSap_Object = MibTableColumn
sdlcMapRemoteSap = _SdlcMapRemoteSap_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 3, 1, 1, 5),
    _SdlcMapRemoteSap_Type()
)
sdlcMapRemoteSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcMapRemoteSap.setStatus("mandatory")


class _SdlcMapName_Type(DisplayString):
    """Custom type sdlcMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_SdlcMapName_Type.__name__ = "DisplayString"
_SdlcMapName_Object = MibTableColumn
sdlcMapName = _SdlcMapName_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 3, 1, 1, 6),
    _SdlcMapName_Type()
)
sdlcMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcMapName.setStatus("mandatory")


class _SdlcMapPortState_Type(Integer32):
    """Custom type sdlcMapPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_SdlcMapPortState_Type.__name__ = "Integer32"
_SdlcMapPortState_Object = MibTableColumn
sdlcMapPortState = _SdlcMapPortState_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 3, 1, 1, 7),
    _SdlcMapPortState_Type()
)
sdlcMapPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcMapPortState.setStatus("mandatory")


class _SdlcMapLSState_Type(Integer32):
    """Custom type sdlcMapLSState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_SdlcMapLSState_Type.__name__ = "Integer32"
_SdlcMapLSState_Object = MibTableColumn
sdlcMapLSState = _SdlcMapLSState_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 3, 1, 1, 8),
    _SdlcMapLSState_Type()
)
sdlcMapLSState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcMapLSState.setStatus("mandatory")
_PysmiFakeCol1_Type = Integer32
_PysmiFakeCol1_Object = MibTableColumn
pysmiFakeCol1 = _PysmiFakeCol1_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 3, 1, 1, 4294967295),
    _PysmiFakeCol1_Type()
)
pysmiFakeCol1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol1.setStatus("mandatory")

# Managed Objects groups


# Notification objects

sdlcPortStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 0, 1)
)
sdlcPortStatusChange.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifAdminStatus"),
        ("IF-MIB", "ifOperStatus"),
        ("A3COM-SDLC-R1-MIB", "sdlcPortOperLastFailTime"),
        ("A3COM-SDLC-R1-MIB", "sdlcPortOperLastFailCause"))
)
if mibBuilder.loadTexts:
    sdlcPortStatusChange.setStatus(
        ""
    )

sdlcLSStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 2, 25, 0, 2)
)
sdlcLSStatusChange.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("A3COM-SDLC-R1-MIB", "sdlcLSAddress"),
        ("A3COM-SDLC-R1-MIB", "sdlcLSOperState"),
        ("A3COM-SDLC-R1-MIB", "sdlcLSAdminState"),
        ("A3COM-SDLC-R1-MIB", "sdlcLSOperLastFailTime"),
        ("A3COM-SDLC-R1-MIB", "sdlcLSOperLastFailCause"),
        ("A3COM-SDLC-R1-MIB", "sdlcLSOperLastFailFRMRInfo"),
        ("A3COM-SDLC-R1-MIB", "sdlcLSOperLastFailCtrlIn"),
        ("A3COM-SDLC-R1-MIB", "sdlcLSOperLastFailCtrlOut"),
        ("A3COM-SDLC-R1-MIB", "sdlcLSOperLastFailREPLYTOs"))
)
if mibBuilder.loadTexts:
    sdlcLSStatusChange.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-SDLC-R1-MIB",
    **{"MacAddress": MacAddress,
       "a3com": a3com,
       "brouterMIB": brouterMIB,
       "sdlc": sdlc,
       "sdlcPortStatusChange": sdlcPortStatusChange,
       "sdlcLSStatusChange": sdlcLSStatusChange,
       "sdlcPortGroup": sdlcPortGroup,
       "sdlcPortAdminTable": sdlcPortAdminTable,
       "sdlcPortAdminEntry": sdlcPortAdminEntry,
       "sdlcPortAdminName": sdlcPortAdminName,
       "sdlcPortAdminRole": sdlcPortAdminRole,
       "sdlcPortAdminType": sdlcPortAdminType,
       "sdlcPortAdminTopology": sdlcPortAdminTopology,
       "sdlcPortAdminACTIVTO": sdlcPortAdminACTIVTO,
       "sdlcPortAdminPAUSE": sdlcPortAdminPAUSE,
       "sdlcPortAdminSlowPollTimer": sdlcPortAdminSlowPollTimer,
       "sdlcPortOperTable": sdlcPortOperTable,
       "sdlcPortOperEntry": sdlcPortOperEntry,
       "sdlcPortOperName": sdlcPortOperName,
       "sdlcPortOperRole": sdlcPortOperRole,
       "sdlcPortOperType": sdlcPortOperType,
       "sdlcPortOperTopology": sdlcPortOperTopology,
       "sdlcPortOperACTIVTO": sdlcPortOperACTIVTO,
       "sdlcPortOperPAUSE": sdlcPortOperPAUSE,
       "sdlcPortOperSlowPollMethod": sdlcPortOperSlowPollMethod,
       "sdlcPortOperSlowPollTimer": sdlcPortOperSlowPollTimer,
       "sdlcPortOperLastFailTime": sdlcPortOperLastFailTime,
       "sdlcPortOperLastFailCause": sdlcPortOperLastFailCause,
       "sdlcPortStatsTable": sdlcPortStatsTable,
       "sdlcPortStatsEntry": sdlcPortStatsEntry,
       "sdlcPortStatsPhysicalFailures": sdlcPortStatsPhysicalFailures,
       "sdlcPortStatsInvalidAddresses": sdlcPortStatsInvalidAddresses,
       "sdlcPortStatsDwarfFrames": sdlcPortStatsDwarfFrames,
       "sdlcLSGroup": sdlcLSGroup,
       "sdlcLSAdminTable": sdlcLSAdminTable,
       "sdlcLSAdminEntry": sdlcLSAdminEntry,
       "sdlcLSAddress": sdlcLSAddress,
       "sdlcLSAdminName": sdlcLSAdminName,
       "sdlcLSAdminState": sdlcLSAdminState,
       "sdlcLSAdminMAXDATA": sdlcLSAdminMAXDATA,
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
       "sdlcLSOperTable": sdlcLSOperTable,
       "sdlcLSOperEntry": sdlcLSOperEntry,
       "sdlcLSOperName": sdlcLSOperName,
       "sdlcLSOperRole": sdlcLSOperRole,
       "sdlcLSOperState": sdlcLSOperState,
       "sdlcLSOperMAXDATA": sdlcLSOperMAXDATA,
       "sdlcLSOperREPLYTO": sdlcLSOperREPLYTO,
       "sdlcLSOperMAXIN": sdlcLSOperMAXIN,
       "sdlcLSOperMAXOUT": sdlcLSOperMAXOUT,
       "sdlcLSOperMODULO": sdlcLSOperMODULO,
       "sdlcLSOperRETRIESm": sdlcLSOperRETRIESm,
       "sdlcLSOperRETRIESt": sdlcLSOperRETRIESt,
       "sdlcLSOperRETRIESn": sdlcLSOperRETRIESn,
       "sdlcLSOperRNRLIMIT": sdlcLSOperRNRLIMIT,
       "sdlcLSOperDATMODE": sdlcLSOperDATMODE,
       "sdlcLSOperLastFailTime": sdlcLSOperLastFailTime,
       "sdlcLSOperLastFailCause": sdlcLSOperLastFailCause,
       "sdlcLSOperLastFailCtrlIn": sdlcLSOperLastFailCtrlIn,
       "sdlcLSOperLastFailCtrlOut": sdlcLSOperLastFailCtrlOut,
       "sdlcLSOperLastFailFRMRInfo": sdlcLSOperLastFailFRMRInfo,
       "sdlcLSOperLastFailREPLYTOs": sdlcLSOperLastFailREPLYTOs,
       "sdlcLSOperGPoll": sdlcLSOperGPoll,
       "sdlcLSOperSimRim": sdlcLSOperSimRim,
       "sdlcLSStatsTable": sdlcLSStatsTable,
       "sdlcLSStatsEntry": sdlcLSStatsEntry,
       "sdlcLSStatsBLUsIn": sdlcLSStatsBLUsIn,
       "sdlcLSStatsBLUsOut": sdlcLSStatsBLUsOut,
       "sdlcLSStatsOctetsIn": sdlcLSStatsOctetsIn,
       "sdlcLSStatsOctetsOut": sdlcLSStatsOctetsOut,
       "sdlcLSStatsPollsOut": sdlcLSStatsPollsOut,
       "sdlcLSStatsPollRspsOut": sdlcLSStatsPollRspsOut,
       "sdlcLSStatsLocalBusies": sdlcLSStatsLocalBusies,
       "sdlcLSStatsRemoteBusies": sdlcLSStatsRemoteBusies,
       "sdlcLSStatsIFramesIn": sdlcLSStatsIFramesIn,
       "sdlcLSStatsIFramesOut": sdlcLSStatsIFramesOut,
       "sdlcLSStatsRetransmits": sdlcLSStatsRetransmits,
       "sdlcLSStatsIOctetsIn": sdlcLSStatsIOctetsIn,
       "sdlcLSStatsIOctetsOut": sdlcLSStatsIOctetsOut,
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
       "sdlcLSStatsProtocolErrs": sdlcLSStatsProtocolErrs,
       "sdlcLSStatsActivityTOs": sdlcLSStatsActivityTOs,
       "sdlcLSStatsRNRLIMITs": sdlcLSStatsRNRLIMITs,
       "sdlcLSStatsRetriesExps": sdlcLSStatsRetriesExps,
       "sdlcMapGroup": sdlcMapGroup,
       "sdlcMapTable": sdlcMapTable,
       "sdlcMapEntry": sdlcMapEntry,
       "sdlcMapPollAddress": sdlcMapPollAddress,
       "sdlcMapLocalMacAddress": sdlcMapLocalMacAddress,
       "sdlcMapLocalSap": sdlcMapLocalSap,
       "sdlcMapRemoteMacAddress": sdlcMapRemoteMacAddress,
       "sdlcMapRemoteSap": sdlcMapRemoteSap,
       "sdlcMapName": sdlcMapName,
       "sdlcMapPortState": sdlcMapPortState,
       "sdlcMapLSState": sdlcMapLSState,
       "pysmiFakeCol1": pysmiFakeCol1}
)
