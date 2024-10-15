# SNMP MIB module (CISCO-ITP-GACT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ITP-GACT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:03:20 2024
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

(cgspInstNetwork,) = mibBuilder.importSymbols(
    "CISCO-ITP-GSP-MIB",
    "cgspInstNetwork")

(CItpTcGlobalTitleSelectorName,
 CItpTcGtaLongAddr,
 CItpTcInstanceNumber,
 CItpTcLinksetId,
 CItpTcPointCode,
 CItpTcServiceIndicator) = mibBuilder.importSymbols(
    "CISCO-ITP-TC-MIB",
    "CItpTcGlobalTitleSelectorName",
    "CItpTcGtaLongAddr",
    "CItpTcInstanceNumber",
    "CItpTcLinksetId",
    "CItpTcPointCode",
    "CItpTcServiceIndicator")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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

ciscoGactMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 333)
)
ciscoGactMIB.setRevisions(
        ("2003-10-01 00:00",
         "2003-03-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CgactMIBNotifs_ObjectIdentity = ObjectIdentity
cgactMIBNotifs = _CgactMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 333, 0)
)
_CgactMIBObjects_ObjectIdentity = ObjectIdentity
cgactMIBObjects = _CgactMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 333, 1)
)
_CgactMtp3_ObjectIdentity = ObjectIdentity
cgactMtp3 = _CgactMtp3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 333, 1, 1)
)
_CgactMtp3Table_Object = MibTable
cgactMtp3Table = _CgactMtp3Table_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 333, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cgactMtp3Table.setStatus("current")
_CgactMtp3TableEntry_Object = MibTableRow
cgactMtp3TableEntry = _CgactMtp3TableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 333, 1, 1, 1, 1)
)
cgactMtp3TableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-GACT-MIB", "cgactMtp3TableId"),
    (0, "CISCO-ITP-GACT-MIB", "cgactMtp3LinksetName"),
    (0, "CISCO-ITP-GACT-MIB", "cgactMtp3Dpc"),
    (0, "CISCO-ITP-GACT-MIB", "cgactMtp3Opc"),
    (0, "CISCO-ITP-GACT-MIB", "cgactMtp3SI"),
)
if mibBuilder.loadTexts:
    cgactMtp3TableEntry.setStatus("current")


class _CgactMtp3TableId_Type(Integer32):
    """Custom type cgactMtp3TableId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("passed", 1),
          ("unroutable", 3),
          ("violation", 2))
    )


_CgactMtp3TableId_Type.__name__ = "Integer32"
_CgactMtp3TableId_Object = MibTableColumn
cgactMtp3TableId = _CgactMtp3TableId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 333, 1, 1, 1, 1, 1),
    _CgactMtp3TableId_Type()
)
cgactMtp3TableId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgactMtp3TableId.setStatus("current")
_CgactMtp3LinksetName_Type = CItpTcLinksetId
_CgactMtp3LinksetName_Object = MibTableColumn
cgactMtp3LinksetName = _CgactMtp3LinksetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 333, 1, 1, 1, 1, 2),
    _CgactMtp3LinksetName_Type()
)
cgactMtp3LinksetName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgactMtp3LinksetName.setStatus("current")
_CgactMtp3Dpc_Type = CItpTcPointCode
_CgactMtp3Dpc_Object = MibTableColumn
cgactMtp3Dpc = _CgactMtp3Dpc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 333, 1, 1, 1, 1, 3),
    _CgactMtp3Dpc_Type()
)
cgactMtp3Dpc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgactMtp3Dpc.setStatus("current")
_CgactMtp3Opc_Type = CItpTcPointCode
_CgactMtp3Opc_Object = MibTableColumn
cgactMtp3Opc = _CgactMtp3Opc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 333, 1, 1, 1, 1, 4),
    _CgactMtp3Opc_Type()
)
cgactMtp3Opc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgactMtp3Opc.setStatus("current")
_CgactMtp3SI_Type = CItpTcServiceIndicator
_CgactMtp3SI_Object = MibTableColumn
cgactMtp3SI = _CgactMtp3SI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 333, 1, 1, 1, 1, 5),
    _CgactMtp3SI_Type()
)
cgactMtp3SI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgactMtp3SI.setStatus("current")
_CgactMtp3InPackets_Type = Counter32
_CgactMtp3InPackets_Object = MibTableColumn
cgactMtp3InPackets = _CgactMtp3InPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 333, 1, 1, 1, 1, 6),
    _CgactMtp3InPackets_Type()
)
cgactMtp3InPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgactMtp3InPackets.setStatus("current")
if mibBuilder.loadTexts:
    cgactMtp3InPackets.setUnits("packets")
_CgactMtp3OutPackets_Type = Counter32
_CgactMtp3OutPackets_Object = MibTableColumn
cgactMtp3OutPackets = _CgactMtp3OutPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 333, 1, 1, 1, 1, 7),
    _CgactMtp3OutPackets_Type()
)
cgactMtp3OutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgactMtp3OutPackets.setStatus("current")
if mibBuilder.loadTexts:
    cgactMtp3OutPackets.setUnits("packets")
_CgactMtp3InOctets_Type = Counter32
_CgactMtp3InOctets_Object = MibTableColumn
cgactMtp3InOctets = _CgactMtp3InOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 333, 1, 1, 1, 1, 8),
    _CgactMtp3InOctets_Type()
)
cgactMtp3InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgactMtp3InOctets.setStatus("current")
if mibBuilder.loadTexts:
    cgactMtp3InOctets.setUnits("octets")
_CgactMtp3OutOctets_Type = Counter32
_CgactMtp3OutOctets_Object = MibTableColumn
cgactMtp3OutOctets = _CgactMtp3OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 333, 1, 1, 1, 1, 9),
    _CgactMtp3OutOctets_Type()
)
cgactMtp3OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgactMtp3OutOctets.setStatus("current")
if mibBuilder.loadTexts:
    cgactMtp3OutOctets.setUnits("octets")
_CgactGtt_ObjectIdentity = ObjectIdentity
cgactGtt = _CgactGtt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 333, 1, 2)
)
_CgactGttTable_Object = MibTable
cgactGttTable = _CgactGttTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 333, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cgactGttTable.setStatus("deprecated")
_CgactGttTableEntry_Object = MibTableRow
cgactGttTableEntry = _CgactGttTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 333, 1, 2, 1, 1)
)
cgactGttTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-GACT-MIB", "cgactGttLinksetName"),
    (0, "CISCO-ITP-GACT-MIB", "cgactGttSelectorName"),
    (0, "CISCO-ITP-GACT-MIB", "cgactGttGta"),
    (0, "CISCO-ITP-GACT-MIB", "cgactGttTranslatedPc"),
)
if mibBuilder.loadTexts:
    cgactGttTableEntry.setStatus("deprecated")
_CgactGttLinksetName_Type = CItpTcLinksetId
_CgactGttLinksetName_Object = MibTableColumn
cgactGttLinksetName = _CgactGttLinksetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 333, 1, 2, 1, 1, 1),
    _CgactGttLinksetName_Type()
)
cgactGttLinksetName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgactGttLinksetName.setStatus("deprecated")
_CgactGttSelectorName_Type = CItpTcGlobalTitleSelectorName
_CgactGttSelectorName_Object = MibTableColumn
cgactGttSelectorName = _CgactGttSelectorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 333, 1, 2, 1, 1, 2),
    _CgactGttSelectorName_Type()
)
cgactGttSelectorName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgactGttSelectorName.setStatus("deprecated")
_CgactGttGta_Type = CItpTcGtaLongAddr
_CgactGttGta_Object = MibTableColumn
cgactGttGta = _CgactGttGta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 333, 1, 2, 1, 1, 3),
    _CgactGttGta_Type()
)
cgactGttGta.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgactGttGta.setStatus("deprecated")
_CgactGttTranslatedPc_Type = CItpTcPointCode
_CgactGttTranslatedPc_Object = MibTableColumn
cgactGttTranslatedPc = _CgactGttTranslatedPc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 333, 1, 2, 1, 1, 4),
    _CgactGttTranslatedPc_Type()
)
cgactGttTranslatedPc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgactGttTranslatedPc.setStatus("deprecated")
_CgactGttPackets_Type = Counter32
_CgactGttPackets_Object = MibTableColumn
cgactGttPackets = _CgactGttPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 333, 1, 2, 1, 1, 5),
    _CgactGttPackets_Type()
)
cgactGttPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgactGttPackets.setStatus("deprecated")
if mibBuilder.loadTexts:
    cgactGttPackets.setUnits("packets")
_CgactGttOctets_Type = Counter32
_CgactGttOctets_Object = MibTableColumn
cgactGttOctets = _CgactGttOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 333, 1, 2, 1, 1, 6),
    _CgactGttOctets_Type()
)
cgactGttOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgactGttOctets.setStatus("deprecated")
if mibBuilder.loadTexts:
    cgactGttOctets.setUnits("octets")
_CgactGtt2Table_Object = MibTable
cgactGtt2Table = _CgactGtt2Table_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 333, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cgactGtt2Table.setStatus("current")
_CgactGtt2TableEntry_Object = MibTableRow
cgactGtt2TableEntry = _CgactGtt2TableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 333, 1, 2, 2, 1)
)
cgactGtt2TableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-GACT-MIB", "cgactGtt2LinksetName"),
    (0, "CISCO-ITP-GACT-MIB", "cgactGtt2SelectorName"),
    (0, "CISCO-ITP-GACT-MIB", "cgactGtt2Gta"),
    (0, "CISCO-ITP-GACT-MIB", "cgactGtt2TranslatedInstNumber"),
    (0, "CISCO-ITP-GACT-MIB", "cgactGtt2TranslatedPc"),
)
if mibBuilder.loadTexts:
    cgactGtt2TableEntry.setStatus("current")
_CgactGtt2LinksetName_Type = CItpTcLinksetId
_CgactGtt2LinksetName_Object = MibTableColumn
cgactGtt2LinksetName = _CgactGtt2LinksetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 333, 1, 2, 2, 1, 1),
    _CgactGtt2LinksetName_Type()
)
cgactGtt2LinksetName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgactGtt2LinksetName.setStatus("current")
_CgactGtt2SelectorName_Type = CItpTcGlobalTitleSelectorName
_CgactGtt2SelectorName_Object = MibTableColumn
cgactGtt2SelectorName = _CgactGtt2SelectorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 333, 1, 2, 2, 1, 2),
    _CgactGtt2SelectorName_Type()
)
cgactGtt2SelectorName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgactGtt2SelectorName.setStatus("current")
_CgactGtt2Gta_Type = CItpTcGtaLongAddr
_CgactGtt2Gta_Object = MibTableColumn
cgactGtt2Gta = _CgactGtt2Gta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 333, 1, 2, 2, 1, 3),
    _CgactGtt2Gta_Type()
)
cgactGtt2Gta.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgactGtt2Gta.setStatus("current")
_CgactGtt2TranslatedInstNumber_Type = CItpTcInstanceNumber
_CgactGtt2TranslatedInstNumber_Object = MibTableColumn
cgactGtt2TranslatedInstNumber = _CgactGtt2TranslatedInstNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 333, 1, 2, 2, 1, 4),
    _CgactGtt2TranslatedInstNumber_Type()
)
cgactGtt2TranslatedInstNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgactGtt2TranslatedInstNumber.setStatus("current")
_CgactGtt2TranslatedPc_Type = CItpTcPointCode
_CgactGtt2TranslatedPc_Object = MibTableColumn
cgactGtt2TranslatedPc = _CgactGtt2TranslatedPc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 333, 1, 2, 2, 1, 5),
    _CgactGtt2TranslatedPc_Type()
)
cgactGtt2TranslatedPc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgactGtt2TranslatedPc.setStatus("current")
_CgactGtt2Packets_Type = Counter32
_CgactGtt2Packets_Object = MibTableColumn
cgactGtt2Packets = _CgactGtt2Packets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 333, 1, 2, 2, 1, 6),
    _CgactGtt2Packets_Type()
)
cgactGtt2Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgactGtt2Packets.setStatus("current")
if mibBuilder.loadTexts:
    cgactGtt2Packets.setUnits("packets")
_CgactGtt2Octets_Type = Counter32
_CgactGtt2Octets_Object = MibTableColumn
cgactGtt2Octets = _CgactGtt2Octets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 333, 1, 2, 2, 1, 7),
    _CgactGtt2Octets_Type()
)
cgactGtt2Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgactGtt2Octets.setStatus("current")
if mibBuilder.loadTexts:
    cgactGtt2Octets.setUnits("octets")
_CgactMIBConform_ObjectIdentity = ObjectIdentity
cgactMIBConform = _CgactMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 333, 2)
)
_CiscoGactMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoGactMIBCompliances = _CiscoGactMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 333, 2, 1)
)
_CiscoGactMIBGroups_ObjectIdentity = ObjectIdentity
ciscoGactMIBGroups = _CiscoGactMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 333, 2, 2)
)

# Managed Objects groups

ciscoGactMtp3Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 333, 2, 2, 1)
)
ciscoGactMtp3Group.setObjects(
      *(("CISCO-ITP-GACT-MIB", "cgactMtp3InPackets"),
        ("CISCO-ITP-GACT-MIB", "cgactMtp3OutPackets"),
        ("CISCO-ITP-GACT-MIB", "cgactMtp3InOctets"),
        ("CISCO-ITP-GACT-MIB", "cgactMtp3OutOctets"))
)
if mibBuilder.loadTexts:
    ciscoGactMtp3Group.setStatus("current")

ciscoGactGttGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 333, 2, 2, 2)
)
ciscoGactGttGroup.setObjects(
      *(("CISCO-ITP-GACT-MIB", "cgactGttPackets"),
        ("CISCO-ITP-GACT-MIB", "cgactGttOctets"))
)
if mibBuilder.loadTexts:
    ciscoGactGttGroup.setStatus("deprecated")

ciscoGactGttGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 333, 2, 2, 3)
)
ciscoGactGttGroupRev1.setObjects(
      *(("CISCO-ITP-GACT-MIB", "cgactGtt2Packets"),
        ("CISCO-ITP-GACT-MIB", "cgactGtt2Octets"))
)
if mibBuilder.loadTexts:
    ciscoGactGttGroupRev1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoGactMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 333, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoGactMIBCompliance.setStatus(
        "deprecated"
    )

ciscoGactMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 333, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoGactMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ITP-GACT-MIB",
    **{"ciscoGactMIB": ciscoGactMIB,
       "cgactMIBNotifs": cgactMIBNotifs,
       "cgactMIBObjects": cgactMIBObjects,
       "cgactMtp3": cgactMtp3,
       "cgactMtp3Table": cgactMtp3Table,
       "cgactMtp3TableEntry": cgactMtp3TableEntry,
       "cgactMtp3TableId": cgactMtp3TableId,
       "cgactMtp3LinksetName": cgactMtp3LinksetName,
       "cgactMtp3Dpc": cgactMtp3Dpc,
       "cgactMtp3Opc": cgactMtp3Opc,
       "cgactMtp3SI": cgactMtp3SI,
       "cgactMtp3InPackets": cgactMtp3InPackets,
       "cgactMtp3OutPackets": cgactMtp3OutPackets,
       "cgactMtp3InOctets": cgactMtp3InOctets,
       "cgactMtp3OutOctets": cgactMtp3OutOctets,
       "cgactGtt": cgactGtt,
       "cgactGttTable": cgactGttTable,
       "cgactGttTableEntry": cgactGttTableEntry,
       "cgactGttLinksetName": cgactGttLinksetName,
       "cgactGttSelectorName": cgactGttSelectorName,
       "cgactGttGta": cgactGttGta,
       "cgactGttTranslatedPc": cgactGttTranslatedPc,
       "cgactGttPackets": cgactGttPackets,
       "cgactGttOctets": cgactGttOctets,
       "cgactGtt2Table": cgactGtt2Table,
       "cgactGtt2TableEntry": cgactGtt2TableEntry,
       "cgactGtt2LinksetName": cgactGtt2LinksetName,
       "cgactGtt2SelectorName": cgactGtt2SelectorName,
       "cgactGtt2Gta": cgactGtt2Gta,
       "cgactGtt2TranslatedInstNumber": cgactGtt2TranslatedInstNumber,
       "cgactGtt2TranslatedPc": cgactGtt2TranslatedPc,
       "cgactGtt2Packets": cgactGtt2Packets,
       "cgactGtt2Octets": cgactGtt2Octets,
       "cgactMIBConform": cgactMIBConform,
       "ciscoGactMIBCompliances": ciscoGactMIBCompliances,
       "ciscoGactMIBCompliance": ciscoGactMIBCompliance,
       "ciscoGactMIBComplianceRev1": ciscoGactMIBComplianceRev1,
       "ciscoGactMIBGroups": ciscoGactMIBGroups,
       "ciscoGactMtp3Group": ciscoGactMtp3Group,
       "ciscoGactGttGroup": ciscoGactGttGroup,
       "ciscoGactGttGroupRev1": ciscoGactGttGroupRev1}
)
