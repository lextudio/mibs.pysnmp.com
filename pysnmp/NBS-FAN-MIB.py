# SNMP MIB module (NBS-FAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NBS-FAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:48 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(NbsTcPartIndex,
 NbsTcStatusSimple,
 nbs) = mibBuilder.importSymbols(
    "NBS-MIB",
    "NbsTcPartIndex",
    "NbsTcStatusSimple",
    "nbs")

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


# MODULE-IDENTITY

nbsFanMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 226)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NbsFanFanGrp_ObjectIdentity = ObjectIdentity
nbsFanFanGrp = _NbsFanFanGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 226, 1)
)
if mibBuilder.loadTexts:
    nbsFanFanGrp.setStatus("current")
_NbsFanFanTable_Object = MibTable
nbsFanFanTable = _NbsFanFanTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 226, 1, 1)
)
if mibBuilder.loadTexts:
    nbsFanFanTable.setStatus("current")
_NbsFanFanEntry_Object = MibTableRow
nbsFanFanEntry = _NbsFanFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 226, 1, 1, 1)
)
nbsFanFanEntry.setIndexNames(
    (0, "NBS-FAN-MIB", "nbsFanFanParentIfIndex"),
    (0, "NBS-FAN-MIB", "nbsFanFanParentPartIndex"),
    (0, "NBS-FAN-MIB", "nbsFanFanIndex"),
)
if mibBuilder.loadTexts:
    nbsFanFanEntry.setStatus("current")
_NbsFanFanParentIfIndex_Type = InterfaceIndex
_NbsFanFanParentIfIndex_Object = MibTableColumn
nbsFanFanParentIfIndex = _NbsFanFanParentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 226, 1, 1, 1, 1),
    _NbsFanFanParentIfIndex_Type()
)
nbsFanFanParentIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsFanFanParentIfIndex.setStatus("current")
_NbsFanFanParentPartIndex_Type = NbsTcPartIndex
_NbsFanFanParentPartIndex_Object = MibTableColumn
nbsFanFanParentPartIndex = _NbsFanFanParentPartIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 226, 1, 1, 1, 2),
    _NbsFanFanParentPartIndex_Type()
)
nbsFanFanParentPartIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsFanFanParentPartIndex.setStatus("current")
_NbsFanFanIndex_Type = Integer32
_NbsFanFanIndex_Object = MibTableColumn
nbsFanFanIndex = _NbsFanFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 226, 1, 1, 1, 3),
    _NbsFanFanIndex_Type()
)
nbsFanFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsFanFanIndex.setStatus("current")


class _NbsFanFanDescription_Type(DisplayString):
    """Custom type nbsFanFanDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_NbsFanFanDescription_Type.__name__ = "DisplayString"
_NbsFanFanDescription_Object = MibTableColumn
nbsFanFanDescription = _NbsFanFanDescription_Object(
    (1, 3, 6, 1, 4, 1, 629, 226, 1, 1, 1, 10),
    _NbsFanFanDescription_Type()
)
nbsFanFanDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsFanFanDescription.setStatus("current")
_NbsFanFanStatus_Type = NbsTcStatusSimple
_NbsFanFanStatus_Object = MibTableColumn
nbsFanFanStatus = _NbsFanFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 226, 1, 1, 1, 30),
    _NbsFanFanStatus_Type()
)
nbsFanFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsFanFanStatus.setStatus("current")


class _NbsFanFanSpeed_Type(Integer32):
    """Custom type nbsFanFanSpeed based on Integer32"""
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
        *(("high", 5),
          ("low", 3),
          ("medium", 4),
          ("notSupported", 1),
          ("off", 2))
    )


_NbsFanFanSpeed_Type.__name__ = "Integer32"
_NbsFanFanSpeed_Object = MibTableColumn
nbsFanFanSpeed = _NbsFanFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 629, 226, 1, 1, 1, 40),
    _NbsFanFanSpeed_Type()
)
nbsFanFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsFanFanSpeed.setStatus("current")
_NbsFanFanTableSize_Type = Integer32
_NbsFanFanTableSize_Object = MibScalar
nbsFanFanTableSize = _NbsFanFanTableSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 226, 1, 2),
    _NbsFanFanTableSize_Type()
)
nbsFanFanTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsFanFanTableSize.setStatus("current")
_NbsFanEventsGrp_ObjectIdentity = ObjectIdentity
nbsFanEventsGrp = _NbsFanEventsGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 226, 100)
)
if mibBuilder.loadTexts:
    nbsFanEventsGrp.setStatus("current")
_NbsFanEvents_ObjectIdentity = ObjectIdentity
nbsFanEvents = _NbsFanEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 226, 100, 0)
)
if mibBuilder.loadTexts:
    nbsFanEvents.setStatus("current")

# Managed Objects groups


# Notification objects

nbsFanTrapFanStatusBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 226, 100, 0, 30)
)
nbsFanTrapFanStatusBad.setObjects(
      *(("NBS-FAN-MIB", "nbsFanFanParentIfIndex"),
        ("NBS-FAN-MIB", "nbsFanFanParentPartIndex"),
        ("NBS-FAN-MIB", "nbsFanFanIndex"),
        ("NBS-FAN-MIB", "nbsFanFanDescription"),
        ("NBS-FAN-MIB", "nbsFanFanStatus"))
)
if mibBuilder.loadTexts:
    nbsFanTrapFanStatusBad.setStatus(
        "current"
    )

nbsFanTrapFanStatusOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 226, 100, 0, 31)
)
nbsFanTrapFanStatusOk.setObjects(
      *(("NBS-FAN-MIB", "nbsFanFanParentIfIndex"),
        ("NBS-FAN-MIB", "nbsFanFanParentPartIndex"),
        ("NBS-FAN-MIB", "nbsFanFanIndex"),
        ("NBS-FAN-MIB", "nbsFanFanDescription"),
        ("NBS-FAN-MIB", "nbsFanFanStatus"))
)
if mibBuilder.loadTexts:
    nbsFanTrapFanStatusOk.setStatus(
        "current"
    )

nbsFanTrapFanSpeedChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 226, 100, 0, 40)
)
nbsFanTrapFanSpeedChanged.setObjects(
      *(("NBS-FAN-MIB", "nbsFanFanParentIfIndex"),
        ("NBS-FAN-MIB", "nbsFanFanParentPartIndex"),
        ("NBS-FAN-MIB", "nbsFanFanIndex"),
        ("NBS-FAN-MIB", "nbsFanFanDescription"),
        ("NBS-FAN-MIB", "nbsFanFanSpeed"))
)
if mibBuilder.loadTexts:
    nbsFanTrapFanSpeedChanged.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NBS-FAN-MIB",
    **{"nbsFanMib": nbsFanMib,
       "nbsFanFanGrp": nbsFanFanGrp,
       "nbsFanFanTable": nbsFanFanTable,
       "nbsFanFanEntry": nbsFanFanEntry,
       "nbsFanFanParentIfIndex": nbsFanFanParentIfIndex,
       "nbsFanFanParentPartIndex": nbsFanFanParentPartIndex,
       "nbsFanFanIndex": nbsFanFanIndex,
       "nbsFanFanDescription": nbsFanFanDescription,
       "nbsFanFanStatus": nbsFanFanStatus,
       "nbsFanFanSpeed": nbsFanFanSpeed,
       "nbsFanFanTableSize": nbsFanFanTableSize,
       "nbsFanEventsGrp": nbsFanEventsGrp,
       "nbsFanEvents": nbsFanEvents,
       "nbsFanTrapFanStatusBad": nbsFanTrapFanStatusBad,
       "nbsFanTrapFanStatusOk": nbsFanTrapFanStatusOk,
       "nbsFanTrapFanSpeedChanged": nbsFanTrapFanSpeedChanged}
)
