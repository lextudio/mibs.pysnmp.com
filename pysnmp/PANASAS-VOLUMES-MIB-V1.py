# SNMP MIB module (PANASAS-VOLUMES-MIB-V1) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PANASAS-VOLUMES-MIB-V1
# Produced by pysmi-1.5.4 at Mon Oct 14 22:36:39 2024
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

(panFs,) = mibBuilder.importSymbols(
    "PANASAS-PANFS-MIB-V1",
    "panFs")

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

panVol = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 4)
)
panVol.setRevisions(
        ("2011-04-07 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PanVolTable_Object = MibTable
panVolTable = _PanVolTable_Object(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 4, 1)
)
if mibBuilder.loadTexts:
    panVolTable.setStatus("current")
_PanVolEntry_Object = MibTableRow
panVolEntry = _PanVolEntry_Object(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 4, 1, 1)
)
panVolEntry.setIndexNames(
    (0, "PANASAS-VOLUMES-MIB-V1", "panVolPath"),
)
if mibBuilder.loadTexts:
    panVolEntry.setStatus("current")
_PanVolPath_Type = DisplayString
_PanVolPath_Object = MibTableColumn
panVolPath = _PanVolPath_Object(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 4, 1, 1, 1),
    _PanVolPath_Type()
)
panVolPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panVolPath.setStatus("current")
_PanVolBladeSet_Type = DisplayString
_PanVolBladeSet_Object = MibTableColumn
panVolBladeSet = _PanVolBladeSet_Object(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 4, 1, 1, 2),
    _PanVolBladeSet_Type()
)
panVolBladeSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panVolBladeSet.setStatus("current")
_PanVolSoftQuota_Type = Unsigned32
_PanVolSoftQuota_Object = MibTableColumn
panVolSoftQuota = _PanVolSoftQuota_Object(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 4, 1, 1, 3),
    _PanVolSoftQuota_Type()
)
panVolSoftQuota.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panVolSoftQuota.setStatus("current")
_PanVolHardQuota_Type = Unsigned32
_PanVolHardQuota_Object = MibTableColumn
panVolHardQuota = _PanVolHardQuota_Object(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 4, 1, 1, 4),
    _PanVolHardQuota_Type()
)
panVolHardQuota.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panVolHardQuota.setStatus("current")
_PanVolUsed_Type = Unsigned32
_PanVolUsed_Object = MibTableColumn
panVolUsed = _PanVolUsed_Object(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 4, 1, 1, 5),
    _PanVolUsed_Type()
)
panVolUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panVolUsed.setStatus("current")
_PanVolRaid_Type = DisplayString
_PanVolRaid_Object = MibTableColumn
panVolRaid = _PanVolRaid_Object(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 4, 1, 1, 6),
    _PanVolRaid_Type()
)
panVolRaid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panVolRaid.setStatus("current")
_PanVolInfo_Type = DisplayString
_PanVolInfo_Object = MibTableColumn
panVolInfo = _PanVolInfo_Object(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 4, 1, 1, 7),
    _PanVolInfo_Type()
)
panVolInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panVolInfo.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PANASAS-VOLUMES-MIB-V1",
    **{"panVol": panVol,
       "panVolTable": panVolTable,
       "panVolEntry": panVolEntry,
       "panVolPath": panVolPath,
       "panVolBladeSet": panVolBladeSet,
       "panVolSoftQuota": panVolSoftQuota,
       "panVolHardQuota": panVolHardQuota,
       "panVolUsed": panVolUsed,
       "panVolRaid": panVolRaid,
       "panVolInfo": panVolInfo}
)
