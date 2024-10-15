# SNMP MIB module (CISCO-ATM-CONN-INFO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ATM-CONN-INFO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:48 2024
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

ciscoAtmConnInfoMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999)
)
ciscoAtmConnInfoMIB.setRevisions(
        ("2003-06-16 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CaciGeneralConnEPCategory(Integer32, TextualConvention):
    status = "current"
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
        *(("caciP2mpL", 3),
          ("caciP2mpPty", 4),
          ("caciP2mpR", 2),
          ("caciP2p", 1))
    )



class CaciP2pConnCategory(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("caciP2pSpvcD", 3),
          ("caciP2pSpvcR", 5),
          ("caciP2pSpvpD", 4),
          ("caciP2pSpvpR", 6),
          ("caciP2pSvcc", 1),
          ("caciP2pSvpc", 2))
    )



class CaciP2pEndpointCategory(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("caciP2pSpvcDEP", 5),
          ("caciP2pSpvcRNPEP", 2),
          ("caciP2pSpvcRPEP", 1),
          ("caciP2pSpvpDEP", 6),
          ("caciP2pSpvpRNPEP", 4),
          ("caciP2pSpvpRPEP", 3))
    )



class CaciP2pIntEndpointCategory(Integer32, TextualConvention):
    status = "current"
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
        *(("caciP2pSpvcRIntEP", 3),
          ("caciP2pSpvpRIntEP", 4),
          ("caciP2pSvccIntEP", 1),
          ("caciP2pSvpcIntEP", 2))
    )



class CaciP2mpConnCategory(Integer32, TextualConvention):
    status = "current"
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("caciP2mpSpvcAct", 9),
          ("caciP2mpSpvcNP", 8),
          ("caciP2mpSpvcP", 7),
          ("caciP2mpSpvcPaAct", 14),
          ("caciP2mpSpvcPaP", 13),
          ("caciP2mpSpvpAct", 12),
          ("caciP2mpSpvpNP", 11),
          ("caciP2mpSpvpP", 10),
          ("caciP2mpSpvpPaAct", 16),
          ("caciP2mpSpvpPaP", 15),
          ("caciP2mpSvcLeaf", 2),
          ("caciP2mpSvcParty", 3),
          ("caciP2mpSvcRoot", 1),
          ("caciP2mpSvpcLeaf", 5),
          ("caciP2mpSvpcParty", 6),
          ("caciP2mpSvpcRoot", 4))
    )



class CaciATMEndpointCategory(Integer32, TextualConvention):
    status = "current"
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
        *(("caciP2pTotalInt", 2),
          ("caciTotalMaster", 3),
          ("caciTotalSlave", 4),
          ("caciTotalSpvc", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CaciMIBNotifications_ObjectIdentity = ObjectIdentity
caciMIBNotifications = _CaciMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 0)
)
_CaciMIBObjects_ObjectIdentity = ObjectIdentity
caciMIBObjects = _CaciMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1)
)
_CaciAtmConnInfo_ObjectIdentity = ObjectIdentity
caciAtmConnInfo = _CaciAtmConnInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1)
)
_CaciIfInfo_ObjectIdentity = ObjectIdentity
caciIfInfo = _CaciIfInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1)
)
_CaciConnInfoTable_Object = MibTable
caciConnInfoTable = _CaciConnInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    caciConnInfoTable.setStatus("current")
_CaciConnInfoEntry_Object = MibTableRow
caciConnInfoEntry = _CaciConnInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 1)
)
caciConnInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-ATM-CONN-INFO-MIB", "caciGeneralConnEPCategory"),
)
if mibBuilder.loadTexts:
    caciConnInfoEntry.setStatus("current")
_CaciGeneralConnEPCategory_Type = CaciGeneralConnEPCategory
_CaciGeneralConnEPCategory_Object = MibTableColumn
caciGeneralConnEPCategory = _CaciGeneralConnEPCategory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 1, 1),
    _CaciGeneralConnEPCategory_Type()
)
caciGeneralConnEPCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caciGeneralConnEPCategory.setStatus("current")
_CaciNumUsedConns_Type = Gauge32
_CaciNumUsedConns_Object = MibTableColumn
caciNumUsedConns = _CaciNumUsedConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 1, 2),
    _CaciNumUsedConns_Type()
)
caciNumUsedConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caciNumUsedConns.setStatus("current")
_CaciP2pConns_ObjectIdentity = ObjectIdentity
caciP2pConns = _CaciP2pConns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 2)
)
_CaciP2pConnTable_Object = MibTable
caciP2pConnTable = _CaciP2pConnTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    caciP2pConnTable.setStatus("current")
_CaciP2pConnEntry_Object = MibTableRow
caciP2pConnEntry = _CaciP2pConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 2, 1, 1)
)
caciP2pConnEntry.setIndexNames(
    (0, "CISCO-ATM-CONN-INFO-MIB", "caciP2pConnectionCategory"),
)
if mibBuilder.loadTexts:
    caciP2pConnEntry.setStatus("current")
_CaciP2pConnectionCategory_Type = CaciP2pConnCategory
_CaciP2pConnectionCategory_Object = MibTableColumn
caciP2pConnectionCategory = _CaciP2pConnectionCategory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 2, 1, 1, 1),
    _CaciP2pConnectionCategory_Type()
)
caciP2pConnectionCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caciP2pConnectionCategory.setStatus("current")
_CaciP2pTotalConns_Type = Gauge32
_CaciP2pTotalConns_Object = MibTableColumn
caciP2pTotalConns = _CaciP2pTotalConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 2, 1, 1, 2),
    _CaciP2pTotalConns_Type()
)
caciP2pTotalConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caciP2pTotalConns.setStatus("current")
_CaciP2pEndpoints_ObjectIdentity = ObjectIdentity
caciP2pEndpoints = _CaciP2pEndpoints_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 3)
)
_CaciP2pEndpointTable_Object = MibTable
caciP2pEndpointTable = _CaciP2pEndpointTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    caciP2pEndpointTable.setStatus("current")
_CaciP2pEndpointEntry_Object = MibTableRow
caciP2pEndpointEntry = _CaciP2pEndpointEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 3, 1, 1)
)
caciP2pEndpointEntry.setIndexNames(
    (0, "CISCO-ATM-CONN-INFO-MIB", "caciP2pEndptCategory"),
)
if mibBuilder.loadTexts:
    caciP2pEndpointEntry.setStatus("current")
_CaciP2pEndptCategory_Type = CaciP2pEndpointCategory
_CaciP2pEndptCategory_Object = MibTableColumn
caciP2pEndptCategory = _CaciP2pEndptCategory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 3, 1, 1, 1),
    _CaciP2pEndptCategory_Type()
)
caciP2pEndptCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caciP2pEndptCategory.setStatus("current")
_CaciP2pTotalConfEndpoints_Type = Gauge32
_CaciP2pTotalConfEndpoints_Object = MibTableColumn
caciP2pTotalConfEndpoints = _CaciP2pTotalConfEndpoints_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 3, 1, 1, 2),
    _CaciP2pTotalConfEndpoints_Type()
)
caciP2pTotalConfEndpoints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caciP2pTotalConfEndpoints.setStatus("current")
_CaciP2pIntEndpoints_ObjectIdentity = ObjectIdentity
caciP2pIntEndpoints = _CaciP2pIntEndpoints_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 4)
)
_CaciP2pIntEndpointTable_Object = MibTable
caciP2pIntEndpointTable = _CaciP2pIntEndpointTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    caciP2pIntEndpointTable.setStatus("current")
_CaciP2pIntEndpointEntry_Object = MibTableRow
caciP2pIntEndpointEntry = _CaciP2pIntEndpointEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 4, 1, 1)
)
caciP2pIntEndpointEntry.setIndexNames(
    (0, "CISCO-ATM-CONN-INFO-MIB", "caciP2pIntEndptCategory"),
)
if mibBuilder.loadTexts:
    caciP2pIntEndpointEntry.setStatus("current")
_CaciP2pIntEndptCategory_Type = CaciP2pIntEndpointCategory
_CaciP2pIntEndptCategory_Object = MibTableColumn
caciP2pIntEndptCategory = _CaciP2pIntEndptCategory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 4, 1, 1, 1),
    _CaciP2pIntEndptCategory_Type()
)
caciP2pIntEndptCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caciP2pIntEndptCategory.setStatus("current")
_CaciP2pTotalIntEndpoints_Type = Gauge32
_CaciP2pTotalIntEndpoints_Object = MibTableColumn
caciP2pTotalIntEndpoints = _CaciP2pTotalIntEndpoints_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 4, 1, 1, 2),
    _CaciP2pTotalIntEndpoints_Type()
)
caciP2pTotalIntEndpoints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caciP2pTotalIntEndpoints.setStatus("current")
_CaciP2mpConns_ObjectIdentity = ObjectIdentity
caciP2mpConns = _CaciP2mpConns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5)
)
_CaciP2mpConnTable_Object = MibTable
caciP2mpConnTable = _CaciP2mpConnTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    caciP2mpConnTable.setStatus("current")
_CaciP2mpConnEntry_Object = MibTableRow
caciP2mpConnEntry = _CaciP2mpConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 1)
)
caciP2mpConnEntry.setIndexNames(
    (0, "CISCO-ATM-CONN-INFO-MIB", "caciP2mpConnectionCategory"),
)
if mibBuilder.loadTexts:
    caciP2mpConnEntry.setStatus("current")
_CaciP2mpConnectionCategory_Type = CaciP2mpConnCategory
_CaciP2mpConnectionCategory_Object = MibTableColumn
caciP2mpConnectionCategory = _CaciP2mpConnectionCategory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 1, 1),
    _CaciP2mpConnectionCategory_Type()
)
caciP2mpConnectionCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caciP2mpConnectionCategory.setStatus("current")
_CaciP2mpTotalConfConns_Type = Gauge32
_CaciP2mpTotalConfConns_Object = MibTableColumn
caciP2mpTotalConfConns = _CaciP2mpTotalConfConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 1, 2),
    _CaciP2mpTotalConfConns_Type()
)
caciP2mpTotalConfConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caciP2mpTotalConfConns.setStatus("current")
_CaciGeneric_ObjectIdentity = ObjectIdentity
caciGeneric = _CaciGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 6)
)
_CaciP2pTotalConfConns_Type = Unsigned32
_CaciP2pTotalConfConns_Object = MibScalar
caciP2pTotalConfConns = _CaciP2pTotalConfConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 6, 1),
    _CaciP2pTotalConfConns_Type()
)
caciP2pTotalConfConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caciP2pTotalConfConns.setStatus("current")
_CaciP2pMaxPossibleConns_Type = Unsigned32
_CaciP2pMaxPossibleConns_Object = MibScalar
caciP2pMaxPossibleConns = _CaciP2pMaxPossibleConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 6, 2),
    _CaciP2pMaxPossibleConns_Type()
)
caciP2pMaxPossibleConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caciP2pMaxPossibleConns.setStatus("current")
_CaciMaxPossibleEndpoints_Type = Unsigned32
_CaciMaxPossibleEndpoints_Object = MibScalar
caciMaxPossibleEndpoints = _CaciMaxPossibleEndpoints_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 6, 3),
    _CaciMaxPossibleEndpoints_Type()
)
caciMaxPossibleEndpoints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caciMaxPossibleEndpoints.setStatus("current")
_CaciGenericEndpointTable_Object = MibTable
caciGenericEndpointTable = _CaciGenericEndpointTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 6, 4)
)
if mibBuilder.loadTexts:
    caciGenericEndpointTable.setStatus("current")
_CaciGenericEndpointEntry_Object = MibTableRow
caciGenericEndpointEntry = _CaciGenericEndpointEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 6, 4, 1)
)
caciGenericEndpointEntry.setIndexNames(
    (0, "CISCO-ATM-CONN-INFO-MIB", "caciATMEndpointCategory"),
)
if mibBuilder.loadTexts:
    caciGenericEndpointEntry.setStatus("current")
_CaciATMEndpointCategory_Type = CaciATMEndpointCategory
_CaciATMEndpointCategory_Object = MibTableColumn
caciATMEndpointCategory = _CaciATMEndpointCategory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 6, 4, 1, 1),
    _CaciATMEndpointCategory_Type()
)
caciATMEndpointCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caciATMEndpointCategory.setStatus("current")
_CaciTotalEndpoints_Type = Gauge32
_CaciTotalEndpoints_Object = MibTableColumn
caciTotalEndpoints = _CaciTotalEndpoints_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 6, 4, 1, 2),
    _CaciTotalEndpoints_Type()
)
caciTotalEndpoints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caciTotalEndpoints.setStatus("current")
_CiscoAtmConnInfoMIBConformance_ObjectIdentity = ObjectIdentity
ciscoAtmConnInfoMIBConformance = _CiscoAtmConnInfoMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 2)
)
_CiscoAtmConnInfoMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoAtmConnInfoMIBCompliances = _CiscoAtmConnInfoMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 1)
)
_CiscoAtmConnInfoMIBGroups_ObjectIdentity = ObjectIdentity
ciscoAtmConnInfoMIBGroups = _CiscoAtmConnInfoMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2)
)

# Managed Objects groups

ciscoConnInfoConfMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2, 1)
)
ciscoConnInfoConfMIBGroup.setObjects(
    ("CISCO-ATM-CONN-INFO-MIB", "caciNumUsedConns")
)
if mibBuilder.loadTexts:
    ciscoConnInfoConfMIBGroup.setStatus("current")

ciscoP2pConnsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2, 2)
)
ciscoP2pConnsMIBGroup.setObjects(
    ("CISCO-ATM-CONN-INFO-MIB", "caciP2pTotalConns")
)
if mibBuilder.loadTexts:
    ciscoP2pConnsMIBGroup.setStatus("current")

ciscoP2pEndpointsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2, 3)
)
ciscoP2pEndpointsMIBGroup.setObjects(
    ("CISCO-ATM-CONN-INFO-MIB", "caciP2pTotalConfEndpoints")
)
if mibBuilder.loadTexts:
    ciscoP2pEndpointsMIBGroup.setStatus("current")

ciscoP2pIntEndpointsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2, 4)
)
ciscoP2pIntEndpointsMIBGroup.setObjects(
    ("CISCO-ATM-CONN-INFO-MIB", "caciP2pTotalIntEndpoints")
)
if mibBuilder.loadTexts:
    ciscoP2pIntEndpointsMIBGroup.setStatus("current")

ciscoP2mpConnsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2, 5)
)
ciscoP2mpConnsMIBGroup.setObjects(
    ("CISCO-ATM-CONN-INFO-MIB", "caciP2mpTotalConfConns")
)
if mibBuilder.loadTexts:
    ciscoP2mpConnsMIBGroup.setStatus("current")

ciscoTotalConnsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2, 6)
)
ciscoTotalConnsMIBGroup.setObjects(
      *(("CISCO-ATM-CONN-INFO-MIB", "caciP2pTotalConfConns"),
        ("CISCO-ATM-CONN-INFO-MIB", "caciP2pMaxPossibleConns"))
)
if mibBuilder.loadTexts:
    ciscoTotalConnsMIBGroup.setStatus("current")

ciscoTotalEndpointsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2, 7)
)
ciscoTotalEndpointsMIBGroup.setObjects(
      *(("CISCO-ATM-CONN-INFO-MIB", "caciMaxPossibleEndpoints"),
        ("CISCO-ATM-CONN-INFO-MIB", "caciTotalEndpoints"))
)
if mibBuilder.loadTexts:
    ciscoTotalEndpointsMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoAtmConnInfoMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoAtmConnInfoMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ATM-CONN-INFO-MIB",
    **{"CaciGeneralConnEPCategory": CaciGeneralConnEPCategory,
       "CaciP2pConnCategory": CaciP2pConnCategory,
       "CaciP2pEndpointCategory": CaciP2pEndpointCategory,
       "CaciP2pIntEndpointCategory": CaciP2pIntEndpointCategory,
       "CaciP2mpConnCategory": CaciP2mpConnCategory,
       "CaciATMEndpointCategory": CaciATMEndpointCategory,
       "ciscoAtmConnInfoMIB": ciscoAtmConnInfoMIB,
       "caciMIBNotifications": caciMIBNotifications,
       "caciMIBObjects": caciMIBObjects,
       "caciAtmConnInfo": caciAtmConnInfo,
       "caciIfInfo": caciIfInfo,
       "caciConnInfoTable": caciConnInfoTable,
       "caciConnInfoEntry": caciConnInfoEntry,
       "caciGeneralConnEPCategory": caciGeneralConnEPCategory,
       "caciNumUsedConns": caciNumUsedConns,
       "caciP2pConns": caciP2pConns,
       "caciP2pConnTable": caciP2pConnTable,
       "caciP2pConnEntry": caciP2pConnEntry,
       "caciP2pConnectionCategory": caciP2pConnectionCategory,
       "caciP2pTotalConns": caciP2pTotalConns,
       "caciP2pEndpoints": caciP2pEndpoints,
       "caciP2pEndpointTable": caciP2pEndpointTable,
       "caciP2pEndpointEntry": caciP2pEndpointEntry,
       "caciP2pEndptCategory": caciP2pEndptCategory,
       "caciP2pTotalConfEndpoints": caciP2pTotalConfEndpoints,
       "caciP2pIntEndpoints": caciP2pIntEndpoints,
       "caciP2pIntEndpointTable": caciP2pIntEndpointTable,
       "caciP2pIntEndpointEntry": caciP2pIntEndpointEntry,
       "caciP2pIntEndptCategory": caciP2pIntEndptCategory,
       "caciP2pTotalIntEndpoints": caciP2pTotalIntEndpoints,
       "caciP2mpConns": caciP2mpConns,
       "caciP2mpConnTable": caciP2mpConnTable,
       "caciP2mpConnEntry": caciP2mpConnEntry,
       "caciP2mpConnectionCategory": caciP2mpConnectionCategory,
       "caciP2mpTotalConfConns": caciP2mpTotalConfConns,
       "caciGeneric": caciGeneric,
       "caciP2pTotalConfConns": caciP2pTotalConfConns,
       "caciP2pMaxPossibleConns": caciP2pMaxPossibleConns,
       "caciMaxPossibleEndpoints": caciMaxPossibleEndpoints,
       "caciGenericEndpointTable": caciGenericEndpointTable,
       "caciGenericEndpointEntry": caciGenericEndpointEntry,
       "caciATMEndpointCategory": caciATMEndpointCategory,
       "caciTotalEndpoints": caciTotalEndpoints,
       "ciscoAtmConnInfoMIBConformance": ciscoAtmConnInfoMIBConformance,
       "ciscoAtmConnInfoMIBCompliances": ciscoAtmConnInfoMIBCompliances,
       "ciscoAtmConnInfoMIBCompliance": ciscoAtmConnInfoMIBCompliance,
       "ciscoAtmConnInfoMIBGroups": ciscoAtmConnInfoMIBGroups,
       "ciscoConnInfoConfMIBGroup": ciscoConnInfoConfMIBGroup,
       "ciscoP2pConnsMIBGroup": ciscoP2pConnsMIBGroup,
       "ciscoP2pEndpointsMIBGroup": ciscoP2pEndpointsMIBGroup,
       "ciscoP2pIntEndpointsMIBGroup": ciscoP2pIntEndpointsMIBGroup,
       "ciscoP2mpConnsMIBGroup": ciscoP2mpConnsMIBGroup,
       "ciscoTotalConnsMIBGroup": ciscoTotalConnsMIBGroup,
       "ciscoTotalEndpointsMIBGroup": ciscoTotalEndpointsMIBGroup}
)
