# SNMP MIB module (CISCO-P2P-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-P2P-IF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:06:36 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

ciscoP2PIfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 668)
)
ciscoP2PIfMIB.setRevisions(
        ("2008-08-12 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Cp2pIfCrcMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crc16", 1),
          ("crc32", 2))
    )



class Cp2pIfScramblingMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoP2PIfMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoP2PIfMIBNotifs = _CiscoP2PIfMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 668, 0)
)
_CiscoP2PIfMIBObjects_ObjectIdentity = ObjectIdentity
ciscoP2PIfMIBObjects = _CiscoP2PIfMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 668, 1)
)
_Cp2pIfGeneralObjects_ObjectIdentity = ObjectIdentity
cp2pIfGeneralObjects = _Cp2pIfGeneralObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 668, 1, 1)
)
_Cp2pIfCfgTable_Object = MibTable
cp2pIfCfgTable = _Cp2pIfCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 668, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cp2pIfCfgTable.setStatus("current")
_Cp2pIfCfgEntry_Object = MibTableRow
cp2pIfCfgEntry = _Cp2pIfCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 668, 1, 1, 1, 1)
)
cp2pIfCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cp2pIfCfgEntry.setStatus("current")


class _Cp2pIfCfgCrcMode_Type(Cp2pIfCrcMode):
    """Custom type cp2pIfCfgCrcMode based on Cp2pIfCrcMode"""


_Cp2pIfCfgCrcMode_Object = MibTableColumn
cp2pIfCfgCrcMode = _Cp2pIfCfgCrcMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 668, 1, 1, 1, 1, 1),
    _Cp2pIfCfgCrcMode_Type()
)
cp2pIfCfgCrcMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cp2pIfCfgCrcMode.setStatus("current")


class _Cp2pIfCfgScramblingMode_Type(Cp2pIfScramblingMode):
    """Custom type cp2pIfCfgScramblingMode based on Cp2pIfScramblingMode"""


_Cp2pIfCfgScramblingMode_Object = MibTableColumn
cp2pIfCfgScramblingMode = _Cp2pIfCfgScramblingMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 668, 1, 1, 1, 1, 2),
    _Cp2pIfCfgScramblingMode_Type()
)
cp2pIfCfgScramblingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cp2pIfCfgScramblingMode.setStatus("current")


class _Cp2pIfCfgTransmitDelay_Type(Unsigned32):
    """Custom type cp2pIfCfgTransmitDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 18000),
    )


_Cp2pIfCfgTransmitDelay_Type.__name__ = "Unsigned32"
_Cp2pIfCfgTransmitDelay_Object = MibTableColumn
cp2pIfCfgTransmitDelay = _Cp2pIfCfgTransmitDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 668, 1, 1, 1, 1, 3),
    _Cp2pIfCfgTransmitDelay_Type()
)
cp2pIfCfgTransmitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cp2pIfCfgTransmitDelay.setStatus("current")
if mibBuilder.loadTexts:
    cp2pIfCfgTransmitDelay.setUnits("microseconds")
_Cp2pIfStatsTable_Object = MibTable
cp2pIfStatsTable = _Cp2pIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 668, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cp2pIfStatsTable.setStatus("current")
_Cp2pIfStatsEntry_Object = MibTableRow
cp2pIfStatsEntry = _Cp2pIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 668, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cp2pIfStatsEntry.setStatus("current")
_Cp2pIfStatsInCrcErrors_Type = Counter32
_Cp2pIfStatsInCrcErrors_Object = MibTableColumn
cp2pIfStatsInCrcErrors = _Cp2pIfStatsInCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 668, 1, 1, 2, 1, 1),
    _Cp2pIfStatsInCrcErrors_Type()
)
cp2pIfStatsInCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cp2pIfStatsInCrcErrors.setStatus("current")
_CiscoP2PIfMIBConformance_ObjectIdentity = ObjectIdentity
ciscoP2PIfMIBConformance = _CiscoP2PIfMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 668, 3)
)
_CiscoP2PIfMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoP2PIfMIBCompliances = _CiscoP2PIfMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 668, 3, 1)
)
_CiscoP2PIfMIBGroups_ObjectIdentity = ObjectIdentity
ciscoP2PIfMIBGroups = _CiscoP2PIfMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 668, 3, 2)
)
cp2pIfCfgEntry.registerAugmentions(
    ("CISCO-P2P-IF-MIB",
     "cp2pIfStatsEntry")
)
cp2pIfStatsEntry.setIndexNames(*cp2pIfCfgEntry.getIndexNames())

# Managed Objects groups

ciscoP2PIfMIBGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 668, 3, 2, 1)
)
ciscoP2PIfMIBGeneralGroup.setObjects(
      *(("CISCO-P2P-IF-MIB", "cp2pIfCfgCrcMode"),
        ("CISCO-P2P-IF-MIB", "cp2pIfCfgScramblingMode"),
        ("CISCO-P2P-IF-MIB", "cp2pIfCfgTransmitDelay"),
        ("CISCO-P2P-IF-MIB", "cp2pIfStatsInCrcErrors"))
)
if mibBuilder.loadTexts:
    ciscoP2PIfMIBGeneralGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoP2PIfMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 668, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoP2PIfMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-P2P-IF-MIB",
    **{"Cp2pIfCrcMode": Cp2pIfCrcMode,
       "Cp2pIfScramblingMode": Cp2pIfScramblingMode,
       "ciscoP2PIfMIB": ciscoP2PIfMIB,
       "ciscoP2PIfMIBNotifs": ciscoP2PIfMIBNotifs,
       "ciscoP2PIfMIBObjects": ciscoP2PIfMIBObjects,
       "cp2pIfGeneralObjects": cp2pIfGeneralObjects,
       "cp2pIfCfgTable": cp2pIfCfgTable,
       "cp2pIfCfgEntry": cp2pIfCfgEntry,
       "cp2pIfCfgCrcMode": cp2pIfCfgCrcMode,
       "cp2pIfCfgScramblingMode": cp2pIfCfgScramblingMode,
       "cp2pIfCfgTransmitDelay": cp2pIfCfgTransmitDelay,
       "cp2pIfStatsTable": cp2pIfStatsTable,
       "cp2pIfStatsEntry": cp2pIfStatsEntry,
       "cp2pIfStatsInCrcErrors": cp2pIfStatsInCrcErrors,
       "ciscoP2PIfMIBConformance": ciscoP2PIfMIBConformance,
       "ciscoP2PIfMIBCompliances": ciscoP2PIfMIBCompliances,
       "ciscoP2PIfMIBCompliance": ciscoP2PIfMIBCompliance,
       "ciscoP2PIfMIBGroups": ciscoP2PIfMIBGroups,
       "ciscoP2PIfMIBGeneralGroup": ciscoP2PIfMIBGeneralGroup}
)
