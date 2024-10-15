# SNMP MIB module (FAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:43:41 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hpicfFanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54)
)
hpicfFanMIB.setRevisions(
        ("2008-08-27 10:30",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpicfDcFanIndex(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"


class HpicfDcFanType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("fm", 2),
          ("im", 3),
          ("maxtype", 6),
          ("mm", 1),
          ("ps", 4),
          ("rollup", 5),
          ("unknown", 0))
    )



class HpicfDcFanAirflowDirection(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("portToPower", 1),
          ("powerToPort", 2))
    )



class HpicfDcFanState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("failed", 0),
          ("maxstate", 6),
          ("off", 2),
          ("ok", 5),
          ("overspeed", 4),
          ("removed", 1),
          ("underspeed", 3))
    )



# MIB Managed Objects in the order of their OIDs

_HpicfFanScalars_ObjectIdentity = ObjectIdentity
hpicfFanScalars = _HpicfFanScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54, 1)
)


class _HpicfFanUserPrefAirflowDir_Type(Integer32):
    """Custom type hpicfFanUserPrefAirflowDir based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("portToPower", 1),
          ("powerToPort", 2))
    )


_HpicfFanUserPrefAirflowDir_Type.__name__ = "Integer32"
_HpicfFanUserPrefAirflowDir_Object = MibScalar
hpicfFanUserPrefAirflowDir = _HpicfFanUserPrefAirflowDir_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54, 1, 1),
    _HpicfFanUserPrefAirflowDir_Type()
)
hpicfFanUserPrefAirflowDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfFanUserPrefAirflowDir.setStatus("current")
_HpicfEntityFan_ObjectIdentity = ObjectIdentity
hpicfEntityFan = _HpicfEntityFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54, 2)
)
_HpicfFanTable_Object = MibTable
hpicfFanTable = _HpicfFanTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfFanTable.setStatus("current")
_HpicfFanEntry_Object = MibTableRow
hpicfFanEntry = _HpicfFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54, 2, 1, 1)
)
hpicfFanEntry.setIndexNames(
    (0, "FAN-MIB", "hpicfFanIndex"),
)
if mibBuilder.loadTexts:
    hpicfFanEntry.setStatus("current")
_HpicfFanIndex_Type = HpicfDcFanIndex
_HpicfFanIndex_Object = MibTableColumn
hpicfFanIndex = _HpicfFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54, 2, 1, 1, 1),
    _HpicfFanIndex_Type()
)
hpicfFanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfFanIndex.setStatus("current")
_HpicfFanTray_Type = Integer32
_HpicfFanTray_Object = MibTableColumn
hpicfFanTray = _HpicfFanTray_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54, 2, 1, 1, 2),
    _HpicfFanTray_Type()
)
hpicfFanTray.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfFanTray.setStatus("current")
_HpicfFanType_Type = HpicfDcFanType
_HpicfFanType_Object = MibTableColumn
hpicfFanType = _HpicfFanType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54, 2, 1, 1, 3),
    _HpicfFanType_Type()
)
hpicfFanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfFanType.setStatus("current")
_HpicfFanState_Type = HpicfDcFanState
_HpicfFanState_Object = MibTableColumn
hpicfFanState = _HpicfFanState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54, 2, 1, 1, 4),
    _HpicfFanState_Type()
)
hpicfFanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfFanState.setStatus("current")
_HpicfFanRecovering_Type = Integer32
_HpicfFanRecovering_Object = MibTableColumn
hpicfFanRecovering = _HpicfFanRecovering_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54, 2, 1, 1, 5),
    _HpicfFanRecovering_Type()
)
hpicfFanRecovering.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfFanRecovering.setStatus("current")
_HpicfFanNumFailures_Type = Counter32
_HpicfFanNumFailures_Object = MibTableColumn
hpicfFanNumFailures = _HpicfFanNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54, 2, 1, 1, 6),
    _HpicfFanNumFailures_Type()
)
hpicfFanNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfFanNumFailures.setStatus("current")
_HpicfFanAirflowDirection_Type = HpicfDcFanAirflowDirection
_HpicfFanAirflowDirection_Object = MibTableColumn
hpicfFanAirflowDirection = _HpicfFanAirflowDirection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54, 2, 1, 1, 7),
    _HpicfFanAirflowDirection_Type()
)
hpicfFanAirflowDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfFanAirflowDirection.setStatus("current")
_HpicfFanConformance_ObjectIdentity = ObjectIdentity
hpicfFanConformance = _HpicfFanConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54, 3)
)
_HpicfFanCompliance_ObjectIdentity = ObjectIdentity
hpicfFanCompliance = _HpicfFanCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54, 3, 1)
)
_HpicfFanGroups_ObjectIdentity = ObjectIdentity
hpicfFanGroups = _HpicfFanGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54, 3, 2)
)

# Managed Objects groups

hpicfFanScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54, 3, 2, 1)
)
hpicfFanScalarsGroup.setObjects(
    ("FAN-MIB", "hpicfFanUserPrefAirflowDir")
)
if mibBuilder.loadTexts:
    hpicfFanScalarsGroup.setStatus("current")

hpicfFanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54, 3, 2, 2)
)
hpicfFanGroup.setObjects(
      *(("FAN-MIB", "hpicfFanTray"),
        ("FAN-MIB", "hpicfFanType"),
        ("FAN-MIB", "hpicfFanState"),
        ("FAN-MIB", "hpicfFanRecovering"),
        ("FAN-MIB", "hpicfFanNumFailures"),
        ("FAN-MIB", "hpicfFanAirflowDirection"))
)
if mibBuilder.loadTexts:
    hpicfFanGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfDcFanCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfDcFanCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FAN-MIB",
    **{"HpicfDcFanIndex": HpicfDcFanIndex,
       "HpicfDcFanType": HpicfDcFanType,
       "HpicfDcFanAirflowDirection": HpicfDcFanAirflowDirection,
       "HpicfDcFanState": HpicfDcFanState,
       "hpicfFanMIB": hpicfFanMIB,
       "hpicfFanScalars": hpicfFanScalars,
       "hpicfFanUserPrefAirflowDir": hpicfFanUserPrefAirflowDir,
       "hpicfEntityFan": hpicfEntityFan,
       "hpicfFanTable": hpicfFanTable,
       "hpicfFanEntry": hpicfFanEntry,
       "hpicfFanIndex": hpicfFanIndex,
       "hpicfFanTray": hpicfFanTray,
       "hpicfFanType": hpicfFanType,
       "hpicfFanState": hpicfFanState,
       "hpicfFanRecovering": hpicfFanRecovering,
       "hpicfFanNumFailures": hpicfFanNumFailures,
       "hpicfFanAirflowDirection": hpicfFanAirflowDirection,
       "hpicfFanConformance": hpicfFanConformance,
       "hpicfFanCompliance": hpicfFanCompliance,
       "hpicfDcFanCompliance": hpicfDcFanCompliance,
       "hpicfFanGroups": hpicfFanGroups,
       "hpicfFanScalarsGroup": hpicfFanScalarsGroup,
       "hpicfFanGroup": hpicfFanGroup}
)
