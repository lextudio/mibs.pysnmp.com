# SNMP MIB module (CISCO-ITP-ACT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ITP-ACT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:03:14 2024
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

(CItpTcGlobalTitleSelectorName,
 CItpTcGtaAddr,
 CItpTcLinksetId,
 CItpTcPointCode,
 CItpTcServiceIndicator) = mibBuilder.importSymbols(
    "CISCO-ITP-TC-MIB",
    "CItpTcGlobalTitleSelectorName",
    "CItpTcGtaAddr",
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

ciscoItpActMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 230)
)
ciscoItpActMIB.setRevisions(
        ("2002-12-18 00:00",
         "2001-09-26 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CItpActMIBNotifs_ObjectIdentity = ObjectIdentity
cItpActMIBNotifs = _CItpActMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 230, 0)
)
_CItpActMIBObjects_ObjectIdentity = ObjectIdentity
cItpActMIBObjects = _CItpActMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 230, 1)
)
_CItpActMtp3_ObjectIdentity = ObjectIdentity
cItpActMtp3 = _CItpActMtp3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 230, 1, 1)
)
_CItpActMtp3Table_Object = MibTable
cItpActMtp3Table = _CItpActMtp3Table_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 230, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cItpActMtp3Table.setStatus("deprecated")
_CItpActMtp3TableEntry_Object = MibTableRow
cItpActMtp3TableEntry = _CItpActMtp3TableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 230, 1, 1, 1, 1)
)
cItpActMtp3TableEntry.setIndexNames(
    (0, "CISCO-ITP-ACT-MIB", "cItpActMtp3TableId"),
    (0, "CISCO-ITP-ACT-MIB", "cItpActMtp3LinksetName"),
    (0, "CISCO-ITP-ACT-MIB", "cItpActMtp3Dpc"),
    (0, "CISCO-ITP-ACT-MIB", "cItpActMtp3Opc"),
    (0, "CISCO-ITP-ACT-MIB", "cItpActMtp3SI"),
)
if mibBuilder.loadTexts:
    cItpActMtp3TableEntry.setStatus("deprecated")


class _CItpActMtp3TableId_Type(Integer32):
    """Custom type cItpActMtp3TableId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("passed", 1),
          ("violation", 2))
    )


_CItpActMtp3TableId_Type.__name__ = "Integer32"
_CItpActMtp3TableId_Object = MibTableColumn
cItpActMtp3TableId = _CItpActMtp3TableId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 230, 1, 1, 1, 1, 1),
    _CItpActMtp3TableId_Type()
)
cItpActMtp3TableId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cItpActMtp3TableId.setStatus("deprecated")
_CItpActMtp3LinksetName_Type = CItpTcLinksetId
_CItpActMtp3LinksetName_Object = MibTableColumn
cItpActMtp3LinksetName = _CItpActMtp3LinksetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 230, 1, 1, 1, 1, 2),
    _CItpActMtp3LinksetName_Type()
)
cItpActMtp3LinksetName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cItpActMtp3LinksetName.setStatus("deprecated")
_CItpActMtp3Dpc_Type = CItpTcPointCode
_CItpActMtp3Dpc_Object = MibTableColumn
cItpActMtp3Dpc = _CItpActMtp3Dpc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 230, 1, 1, 1, 1, 3),
    _CItpActMtp3Dpc_Type()
)
cItpActMtp3Dpc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cItpActMtp3Dpc.setStatus("deprecated")
_CItpActMtp3Opc_Type = CItpTcPointCode
_CItpActMtp3Opc_Object = MibTableColumn
cItpActMtp3Opc = _CItpActMtp3Opc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 230, 1, 1, 1, 1, 4),
    _CItpActMtp3Opc_Type()
)
cItpActMtp3Opc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cItpActMtp3Opc.setStatus("deprecated")
_CItpActMtp3SI_Type = CItpTcServiceIndicator
_CItpActMtp3SI_Object = MibTableColumn
cItpActMtp3SI = _CItpActMtp3SI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 230, 1, 1, 1, 1, 5),
    _CItpActMtp3SI_Type()
)
cItpActMtp3SI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cItpActMtp3SI.setStatus("deprecated")
_CItpActMtp3RcvdPackets_Type = Counter32
_CItpActMtp3RcvdPackets_Object = MibTableColumn
cItpActMtp3RcvdPackets = _CItpActMtp3RcvdPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 230, 1, 1, 1, 1, 6),
    _CItpActMtp3RcvdPackets_Type()
)
cItpActMtp3RcvdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpActMtp3RcvdPackets.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpActMtp3RcvdPackets.setUnits("packets")
_CItpActMtp3SentPackets_Type = Counter32
_CItpActMtp3SentPackets_Object = MibTableColumn
cItpActMtp3SentPackets = _CItpActMtp3SentPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 230, 1, 1, 1, 1, 7),
    _CItpActMtp3SentPackets_Type()
)
cItpActMtp3SentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpActMtp3SentPackets.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpActMtp3SentPackets.setUnits("packets")
_CItpActMtp3RcvdBytes_Type = Counter32
_CItpActMtp3RcvdBytes_Object = MibTableColumn
cItpActMtp3RcvdBytes = _CItpActMtp3RcvdBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 230, 1, 1, 1, 1, 8),
    _CItpActMtp3RcvdBytes_Type()
)
cItpActMtp3RcvdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpActMtp3RcvdBytes.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpActMtp3RcvdBytes.setUnits("bytes")
_CItpActMtp3SentBytes_Type = Counter32
_CItpActMtp3SentBytes_Object = MibTableColumn
cItpActMtp3SentBytes = _CItpActMtp3SentBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 230, 1, 1, 1, 1, 9),
    _CItpActMtp3SentBytes_Type()
)
cItpActMtp3SentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpActMtp3SentBytes.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpActMtp3SentBytes.setUnits("bytes")
_CItpActGtt_ObjectIdentity = ObjectIdentity
cItpActGtt = _CItpActGtt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 230, 1, 2)
)
_CItpActGttTable_Object = MibTable
cItpActGttTable = _CItpActGttTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 230, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cItpActGttTable.setStatus("deprecated")
_CItpActGttTableEntry_Object = MibTableRow
cItpActGttTableEntry = _CItpActGttTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 230, 1, 2, 1, 1)
)
cItpActGttTableEntry.setIndexNames(
    (0, "CISCO-ITP-ACT-MIB", "cItpActGttLinksetName"),
    (0, "CISCO-ITP-ACT-MIB", "cItpActGttSelectorName"),
    (0, "CISCO-ITP-ACT-MIB", "cItpActGttGta"),
    (0, "CISCO-ITP-ACT-MIB", "cItpActGttTranslatedPc"),
)
if mibBuilder.loadTexts:
    cItpActGttTableEntry.setStatus("deprecated")
_CItpActGttLinksetName_Type = CItpTcLinksetId
_CItpActGttLinksetName_Object = MibTableColumn
cItpActGttLinksetName = _CItpActGttLinksetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 230, 1, 2, 1, 1, 1),
    _CItpActGttLinksetName_Type()
)
cItpActGttLinksetName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cItpActGttLinksetName.setStatus("deprecated")
_CItpActGttSelectorName_Type = CItpTcGlobalTitleSelectorName
_CItpActGttSelectorName_Object = MibTableColumn
cItpActGttSelectorName = _CItpActGttSelectorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 230, 1, 2, 1, 1, 2),
    _CItpActGttSelectorName_Type()
)
cItpActGttSelectorName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cItpActGttSelectorName.setStatus("deprecated")
_CItpActGttGta_Type = CItpTcGtaAddr
_CItpActGttGta_Object = MibTableColumn
cItpActGttGta = _CItpActGttGta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 230, 1, 2, 1, 1, 3),
    _CItpActGttGta_Type()
)
cItpActGttGta.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cItpActGttGta.setStatus("deprecated")
_CItpActGttTranslatedPc_Type = CItpTcPointCode
_CItpActGttTranslatedPc_Object = MibTableColumn
cItpActGttTranslatedPc = _CItpActGttTranslatedPc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 230, 1, 2, 1, 1, 4),
    _CItpActGttTranslatedPc_Type()
)
cItpActGttTranslatedPc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cItpActGttTranslatedPc.setStatus("deprecated")
_CItpActGttPackets_Type = Counter32
_CItpActGttPackets_Object = MibTableColumn
cItpActGttPackets = _CItpActGttPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 230, 1, 2, 1, 1, 5),
    _CItpActGttPackets_Type()
)
cItpActGttPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpActGttPackets.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpActGttPackets.setUnits("bytes")
_CItpActGttBytes_Type = Counter32
_CItpActGttBytes_Object = MibTableColumn
cItpActGttBytes = _CItpActGttBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 230, 1, 2, 1, 1, 6),
    _CItpActGttBytes_Type()
)
cItpActGttBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpActGttBytes.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpActGttBytes.setUnits("bytes")
_CItpActMIBConformance_ObjectIdentity = ObjectIdentity
cItpActMIBConformance = _CItpActMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 230, 2)
)
_CItpActMIBCompliances_ObjectIdentity = ObjectIdentity
cItpActMIBCompliances = _CItpActMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 230, 2, 1)
)
_CItpActMIBGroups_ObjectIdentity = ObjectIdentity
cItpActMIBGroups = _CItpActMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 230, 2, 2)
)

# Managed Objects groups

cItpActMtp3Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 230, 2, 2, 1)
)
cItpActMtp3Group.setObjects(
      *(("CISCO-ITP-ACT-MIB", "cItpActMtp3RcvdPackets"),
        ("CISCO-ITP-ACT-MIB", "cItpActMtp3SentPackets"),
        ("CISCO-ITP-ACT-MIB", "cItpActMtp3RcvdBytes"),
        ("CISCO-ITP-ACT-MIB", "cItpActMtp3SentBytes"))
)
if mibBuilder.loadTexts:
    cItpActMtp3Group.setStatus("deprecated")

cItpActGttGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 230, 2, 2, 2)
)
cItpActGttGroup.setObjects(
      *(("CISCO-ITP-ACT-MIB", "cItpActGttPackets"),
        ("CISCO-ITP-ACT-MIB", "cItpActGttBytes"))
)
if mibBuilder.loadTexts:
    cItpActGttGroup.setStatus("deprecated")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cItpActMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 230, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cItpActMIBCompliance.setStatus(
        "deprecated"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ITP-ACT-MIB",
    **{"ciscoItpActMIB": ciscoItpActMIB,
       "cItpActMIBNotifs": cItpActMIBNotifs,
       "cItpActMIBObjects": cItpActMIBObjects,
       "cItpActMtp3": cItpActMtp3,
       "cItpActMtp3Table": cItpActMtp3Table,
       "cItpActMtp3TableEntry": cItpActMtp3TableEntry,
       "cItpActMtp3TableId": cItpActMtp3TableId,
       "cItpActMtp3LinksetName": cItpActMtp3LinksetName,
       "cItpActMtp3Dpc": cItpActMtp3Dpc,
       "cItpActMtp3Opc": cItpActMtp3Opc,
       "cItpActMtp3SI": cItpActMtp3SI,
       "cItpActMtp3RcvdPackets": cItpActMtp3RcvdPackets,
       "cItpActMtp3SentPackets": cItpActMtp3SentPackets,
       "cItpActMtp3RcvdBytes": cItpActMtp3RcvdBytes,
       "cItpActMtp3SentBytes": cItpActMtp3SentBytes,
       "cItpActGtt": cItpActGtt,
       "cItpActGttTable": cItpActGttTable,
       "cItpActGttTableEntry": cItpActGttTableEntry,
       "cItpActGttLinksetName": cItpActGttLinksetName,
       "cItpActGttSelectorName": cItpActGttSelectorName,
       "cItpActGttGta": cItpActGttGta,
       "cItpActGttTranslatedPc": cItpActGttTranslatedPc,
       "cItpActGttPackets": cItpActGttPackets,
       "cItpActGttBytes": cItpActGttBytes,
       "cItpActMIBConformance": cItpActMIBConformance,
       "cItpActMIBCompliances": cItpActMIBCompliances,
       "cItpActMIBCompliance": cItpActMIBCompliance,
       "cItpActMIBGroups": cItpActMIBGroups,
       "cItpActMtp3Group": cItpActMtp3Group,
       "cItpActGttGroup": cItpActGttGroup}
)
