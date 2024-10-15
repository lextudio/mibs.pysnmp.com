# SNMP MIB module (OA-SL-STATISTICS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OA-SL-STATISTICS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:33:32 2024
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

oaSlStatistics = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 9)
)
oaSlStatistics.setRevisions(
        ("2007-03-18 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Nbase_ObjectIdentity = ObjectIdentity
nbase = _Nbase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629)
)
_NbSwitchG1_ObjectIdentity = ObjectIdentity
nbSwitchG1 = _NbSwitchG1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1)
)
_NbSwitchG1Il_ObjectIdentity = ObjectIdentity
nbSwitchG1Il = _NbSwitchG1Il_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50)
)
_NbPortParams_ObjectIdentity = ObjectIdentity
nbPortParams = _NbPortParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10)
)


class _OaSlStatGenSupport_Type(Integer32):
    """Custom type oaSlStatGenSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("supported", 2))
    )


_OaSlStatGenSupport_Type.__name__ = "Integer32"
_OaSlStatGenSupport_Object = MibScalar
oaSlStatGenSupport = _OaSlStatGenSupport_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 9, 1),
    _OaSlStatGenSupport_Type()
)
oaSlStatGenSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSlStatGenSupport.setStatus("current")
_OaSlStatTable_Object = MibTable
oaSlStatTable = _OaSlStatTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 9, 2)
)
if mibBuilder.loadTexts:
    oaSlStatTable.setStatus("current")
_OaSlStatEntry_Object = MibTableRow
oaSlStatEntry = _OaSlStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 9, 2, 1)
)
oaSlStatEntry.setIndexNames(
    (0, "OA-SL-STATISTICS-MIB", "oaSlStatPortIndex"),
    (0, "OA-SL-STATISTICS-MIB", "oaSlStatServiceLevel"),
)
if mibBuilder.loadTexts:
    oaSlStatEntry.setStatus("current")


class _OaSlStatPortIndex_Type(Integer32):
    """Custom type oaSlStatPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_OaSlStatPortIndex_Type.__name__ = "Integer32"
_OaSlStatPortIndex_Object = MibTableColumn
oaSlStatPortIndex = _OaSlStatPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 9, 2, 1, 1),
    _OaSlStatPortIndex_Type()
)
oaSlStatPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSlStatPortIndex.setStatus("current")


class _OaSlStatServiceLevel_Type(Integer32):
    """Custom type oaSlStatServiceLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_OaSlStatServiceLevel_Type.__name__ = "Integer32"
_OaSlStatServiceLevel_Object = MibTableColumn
oaSlStatServiceLevel = _OaSlStatServiceLevel_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 9, 2, 1, 2),
    _OaSlStatServiceLevel_Type()
)
oaSlStatServiceLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSlStatServiceLevel.setStatus("current")
_OaSlStatAggrOctets_Type = Counter64
_OaSlStatAggrOctets_Object = MibTableColumn
oaSlStatAggrOctets = _OaSlStatAggrOctets_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 9, 2, 1, 3),
    _OaSlStatAggrOctets_Type()
)
oaSlStatAggrOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSlStatAggrOctets.setStatus("current")
_OaSlStatConformance_ObjectIdentity = ObjectIdentity
oaSlStatConformance = _OaSlStatConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 9, 101)
)
_OaSlStatMIBCompliances_ObjectIdentity = ObjectIdentity
oaSlStatMIBCompliances = _OaSlStatMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 9, 101, 1)
)
_OaSlStatMIBGroups_ObjectIdentity = ObjectIdentity
oaSlStatMIBGroups = _OaSlStatMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 9, 101, 2)
)

# Managed Objects groups

oaSlStatMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 9, 101, 2, 1)
)
oaSlStatMandatoryGroup.setObjects(
      *(("OA-SL-STATISTICS-MIB", "oaSlStatGenSupport"),
        ("OA-SL-STATISTICS-MIB", "oaSlStatPortIndex"),
        ("OA-SL-STATISTICS-MIB", "oaSlStatServiceLevel"),
        ("OA-SL-STATISTICS-MIB", "oaSlStatAggrOctets"))
)
if mibBuilder.loadTexts:
    oaSlStatMandatoryGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

oaSlStatMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 9, 101, 1, 1)
)
if mibBuilder.loadTexts:
    oaSlStatMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OA-SL-STATISTICS-MIB",
    **{"nbase": nbase,
       "nbSwitchG1": nbSwitchG1,
       "nbSwitchG1Il": nbSwitchG1Il,
       "nbPortParams": nbPortParams,
       "oaSlStatistics": oaSlStatistics,
       "oaSlStatGenSupport": oaSlStatGenSupport,
       "oaSlStatTable": oaSlStatTable,
       "oaSlStatEntry": oaSlStatEntry,
       "oaSlStatPortIndex": oaSlStatPortIndex,
       "oaSlStatServiceLevel": oaSlStatServiceLevel,
       "oaSlStatAggrOctets": oaSlStatAggrOctets,
       "oaSlStatConformance": oaSlStatConformance,
       "oaSlStatMIBCompliances": oaSlStatMIBCompliances,
       "oaSlStatMIBCompliance": oaSlStatMIBCompliance,
       "oaSlStatMIBGroups": oaSlStatMIBGroups,
       "oaSlStatMandatoryGroup": oaSlStatMandatoryGroup}
)
