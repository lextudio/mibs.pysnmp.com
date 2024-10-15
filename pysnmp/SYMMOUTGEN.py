# SNMP MIB module (SYMMOUTGEN) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SYMMOUTGEN
# Produced by pysmi-1.5.4 at Mon Oct 14 22:59:55 2024
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(ifIndex,
 ifNumber) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex",
    "ifNumber")

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

(symmPhysicalSignal,) = mibBuilder.importSymbols(
    "SYMM-COMMON-SMI",
    "symmPhysicalSignal")


# MODULE-IDENTITY

symmOutGen = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 6)
)
symmOutGen.setRevisions(
        ("2011-07-18 11:21",)
)


# Types definitions



class GENERALOUTGENTYPE(Integer32):
    """Custom type GENERALOUTGENTYPE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ais", 3),
          ("on", 2),
          ("squelch", 1))
    )




# TEXTUAL-CONVENTIONS



class DateAndTime(OctetString, TextualConvention):
    status = "current"
    displayHint = "2d-1d-1d,1d:1d:1d.1d,1a1d:1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(11, 11),
    )



class TLatAndLon(OctetString, TextualConvention):
    status = "current"
    displayHint = "1a1d:1d:1d.1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )



class TAntHeight(OctetString, TextualConvention):
    status = "current"
    displayHint = "1a2d.1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



class TLocalTimeOffset(OctetString, TextualConvention):
    status = "current"
    displayHint = "1a1d:1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )



class TSsm(Integer32, TextualConvention):
    status = "current"
    displayHint = "x"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_OutGenStatus_ObjectIdentity = ObjectIdentity
outGenStatus = _OutGenStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 6, 1)
)
_OutGenConfig_ObjectIdentity = ObjectIdentity
outGenConfig = _OutGenConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 6, 2)
)
_OutGenConfigTable_Object = MibTable
outGenConfigTable = _OutGenConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 6, 2, 1)
)
if mibBuilder.loadTexts:
    outGenConfigTable.setStatus("current")
_OutGenConfigEntry_Object = MibTableRow
outGenConfigEntry = _OutGenConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 6, 2, 1, 1)
)
outGenConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SYMMOUTGEN", "outGenConfigIndex"),
)
if mibBuilder.loadTexts:
    outGenConfigEntry.setStatus("current")


class _OutGenConfigIndex_Type(Integer32):
    """Custom type outGenConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_OutGenConfigIndex_Type.__name__ = "Integer32"
_OutGenConfigIndex_Object = MibTableColumn
outGenConfigIndex = _OutGenConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 6, 2, 1, 1, 1),
    _OutGenConfigIndex_Type()
)
outGenConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    outGenConfigIndex.setStatus("current")
_OutGenConfigWarmup_Type = GENERALOUTGENTYPE
_OutGenConfigWarmup_Object = MibTableColumn
outGenConfigWarmup = _OutGenConfigWarmup_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 6, 2, 1, 1, 2),
    _OutGenConfigWarmup_Type()
)
outGenConfigWarmup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outGenConfigWarmup.setStatus("current")
_OutGenConfigFreerun_Type = GENERALOUTGENTYPE
_OutGenConfigFreerun_Object = MibTableColumn
outGenConfigFreerun = _OutGenConfigFreerun_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 6, 2, 1, 1, 3),
    _OutGenConfigFreerun_Type()
)
outGenConfigFreerun.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outGenConfigFreerun.setStatus("current")
_OutGenConfigHoldover_Type = GENERALOUTGENTYPE
_OutGenConfigHoldover_Object = MibTableColumn
outGenConfigHoldover = _OutGenConfigHoldover_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 6, 2, 1, 1, 4),
    _OutGenConfigHoldover_Type()
)
outGenConfigHoldover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outGenConfigHoldover.setStatus("current")
_OutGenConfigFasttrack_Type = GENERALOUTGENTYPE
_OutGenConfigFasttrack_Object = MibTableColumn
outGenConfigFasttrack = _OutGenConfigFasttrack_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 6, 2, 1, 1, 5),
    _OutGenConfigFasttrack_Type()
)
outGenConfigFasttrack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outGenConfigFasttrack.setStatus("current")
_OutGenConformance_ObjectIdentity = ObjectIdentity
outGenConformance = _OutGenConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 6, 3)
)
if mibBuilder.loadTexts:
    outGenConformance.setStatus("current")
_OutGenCompliances_ObjectIdentity = ObjectIdentity
outGenCompliances = _OutGenCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 6, 3, 1)
)
_OutGenUocGroups_ObjectIdentity = ObjectIdentity
outGenUocGroups = _OutGenUocGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 6, 3, 2)
)

# Managed Objects groups

outGenGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 6, 3, 2, 1)
)
outGenGroup.setObjects(
      *(("SYMMOUTGEN", "outGenConfigWarmup"),
        ("SYMMOUTGEN", "outGenConfigFreerun"),
        ("SYMMOUTGEN", "outGenConfigHoldover"),
        ("SYMMOUTGEN", "outGenConfigFasttrack"))
)
if mibBuilder.loadTexts:
    outGenGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

outGenBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 6, 3, 1, 1)
)
if mibBuilder.loadTexts:
    outGenBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYMMOUTGEN",
    **{"GENERALOUTGENTYPE": GENERALOUTGENTYPE,
       "DateAndTime": DateAndTime,
       "TLatAndLon": TLatAndLon,
       "TAntHeight": TAntHeight,
       "TLocalTimeOffset": TLocalTimeOffset,
       "TSsm": TSsm,
       "symmOutGen": symmOutGen,
       "outGenStatus": outGenStatus,
       "outGenConfig": outGenConfig,
       "outGenConfigTable": outGenConfigTable,
       "outGenConfigEntry": outGenConfigEntry,
       "outGenConfigIndex": outGenConfigIndex,
       "outGenConfigWarmup": outGenConfigWarmup,
       "outGenConfigFreerun": outGenConfigFreerun,
       "outGenConfigHoldover": outGenConfigHoldover,
       "outGenConfigFasttrack": outGenConfigFasttrack,
       "outGenConformance": outGenConformance,
       "outGenCompliances": outGenCompliances,
       "outGenBasicCompliance": outGenBasicCompliance,
       "outGenUocGroups": outGenUocGroups,
       "outGenGroup": outGenGroup}
)
