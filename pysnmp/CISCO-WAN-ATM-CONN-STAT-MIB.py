# SNMP MIB module (CISCO-WAN-ATM-CONN-STAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WAN-ATM-CONN-STAT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:48 2024
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

(cwaChanVci,
 cwaChanVpi) = mibBuilder.importSymbols(
    "CISCO-WAN-ATM-CONN-MIB",
    "cwaChanVci",
    "cwaChanVpi")

(ciscoWan,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "ciscoWan")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoWanAtmConnStatMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 2)
)
ciscoWanAtmConnStatMIB.setRevisions(
        ("2005-08-25 00:00",
         "2004-09-10 00:00",
         "2003-04-18 00:00",
         "2003-04-01 00:00",
         "2002-10-21 00:00",
         "2002-07-09 00:00",
         "2002-07-02 00:00",
         "2001-05-02 00:00",
         "1998-12-04 14:45")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoWanAtmConnStatMIBObjects_ObjectIdentity = ObjectIdentity
ciscoWanAtmConnStatMIBObjects = _CiscoWanAtmConnStatMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1)
)
_Cwacs_ObjectIdentity = ObjectIdentity
cwacs = _Cwacs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1)
)
_CwacsTable_Object = MibTable
cwacsTable = _CwacsTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cwacsTable.setStatus("current")
_CwacsEntry_Object = MibTableRow
cwacsEntry = _CwacsEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1)
)
cwacsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WAN-ATM-CONN-MIB", "cwaChanVpi"),
    (0, "CISCO-WAN-ATM-CONN-MIB", "cwaChanVci"),
)
if mibBuilder.loadTexts:
    cwacsEntry.setStatus("current")
_CwacsIngRcvCLP0_Type = Counter32
_CwacsIngRcvCLP0_Object = MibTableColumn
cwacsIngRcvCLP0 = _CwacsIngRcvCLP0_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 1),
    _CwacsIngRcvCLP0_Type()
)
cwacsIngRcvCLP0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsIngRcvCLP0.setStatus("current")
if mibBuilder.loadTexts:
    cwacsIngRcvCLP0.setUnits("cells")
_CwacsIngRcvCLP1_Type = Counter32
_CwacsIngRcvCLP1_Object = MibTableColumn
cwacsIngRcvCLP1 = _CwacsIngRcvCLP1_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 2),
    _CwacsIngRcvCLP1_Type()
)
cwacsIngRcvCLP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsIngRcvCLP1.setStatus("current")
if mibBuilder.loadTexts:
    cwacsIngRcvCLP1.setUnits("cells")
_CwacsIngXmtCLP0_Type = Counter32
_CwacsIngXmtCLP0_Object = MibTableColumn
cwacsIngXmtCLP0 = _CwacsIngXmtCLP0_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 3),
    _CwacsIngXmtCLP0_Type()
)
cwacsIngXmtCLP0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsIngXmtCLP0.setStatus("current")
if mibBuilder.loadTexts:
    cwacsIngXmtCLP0.setUnits("cells")
_CwacsIngXmtCLP1_Type = Counter32
_CwacsIngXmtCLP1_Object = MibTableColumn
cwacsIngXmtCLP1 = _CwacsIngXmtCLP1_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 4),
    _CwacsIngXmtCLP1_Type()
)
cwacsIngXmtCLP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsIngXmtCLP1.setStatus("current")
if mibBuilder.loadTexts:
    cwacsIngXmtCLP1.setUnits("cells")
_CwacsIngCLP0CoSDiscard_Type = Counter32
_CwacsIngCLP0CoSDiscard_Object = MibTableColumn
cwacsIngCLP0CoSDiscard = _CwacsIngCLP0CoSDiscard_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 5),
    _CwacsIngCLP0CoSDiscard_Type()
)
cwacsIngCLP0CoSDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsIngCLP0CoSDiscard.setStatus("current")
if mibBuilder.loadTexts:
    cwacsIngCLP0CoSDiscard.setUnits("cells")
_CwacsIngCLP1CoSDiscard_Type = Counter32
_CwacsIngCLP1CoSDiscard_Object = MibTableColumn
cwacsIngCLP1CoSDiscard = _CwacsIngCLP1CoSDiscard_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 6),
    _CwacsIngCLP1CoSDiscard_Type()
)
cwacsIngCLP1CoSDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsIngCLP1CoSDiscard.setStatus("current")
if mibBuilder.loadTexts:
    cwacsIngCLP1CoSDiscard.setUnits("cells")
_CwacsIngCLP0UpcDiscard_Type = Counter32
_CwacsIngCLP0UpcDiscard_Object = MibTableColumn
cwacsIngCLP0UpcDiscard = _CwacsIngCLP0UpcDiscard_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 7),
    _CwacsIngCLP0UpcDiscard_Type()
)
cwacsIngCLP0UpcDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsIngCLP0UpcDiscard.setStatus("current")
if mibBuilder.loadTexts:
    cwacsIngCLP0UpcDiscard.setUnits("cells")
_CwacsIngCLP1UpcDiscard_Type = Counter32
_CwacsIngCLP1UpcDiscard_Object = MibTableColumn
cwacsIngCLP1UpcDiscard = _CwacsIngCLP1UpcDiscard_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 8),
    _CwacsIngCLP1UpcDiscard_Type()
)
cwacsIngCLP1UpcDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsIngCLP1UpcDiscard.setStatus("current")
if mibBuilder.loadTexts:
    cwacsIngCLP1UpcDiscard.setUnits("cells")
_CwacsIngCLP0UpcTagged_Type = Counter32
_CwacsIngCLP0UpcTagged_Object = MibTableColumn
cwacsIngCLP0UpcTagged = _CwacsIngCLP0UpcTagged_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 9),
    _CwacsIngCLP0UpcTagged_Type()
)
cwacsIngCLP0UpcTagged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsIngCLP0UpcTagged.setStatus("current")
if mibBuilder.loadTexts:
    cwacsIngCLP0UpcTagged.setUnits("cells")
_CwacsIngRcvEFCI0_Type = Counter32
_CwacsIngRcvEFCI0_Object = MibTableColumn
cwacsIngRcvEFCI0 = _CwacsIngRcvEFCI0_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 10),
    _CwacsIngRcvEFCI0_Type()
)
cwacsIngRcvEFCI0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsIngRcvEFCI0.setStatus("current")
if mibBuilder.loadTexts:
    cwacsIngRcvEFCI0.setUnits("cells")
_CwacsIngRcvEFCI1_Type = Counter32
_CwacsIngRcvEFCI1_Object = MibTableColumn
cwacsIngRcvEFCI1 = _CwacsIngRcvEFCI1_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 11),
    _CwacsIngRcvEFCI1_Type()
)
cwacsIngRcvEFCI1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsIngRcvEFCI1.setStatus("current")
if mibBuilder.loadTexts:
    cwacsIngRcvEFCI1.setUnits("cells")
_CwacsIngEFCI0Discard_Type = Counter32
_CwacsIngEFCI0Discard_Object = MibTableColumn
cwacsIngEFCI0Discard = _CwacsIngEFCI0Discard_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 12),
    _CwacsIngEFCI0Discard_Type()
)
cwacsIngEFCI0Discard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsIngEFCI0Discard.setStatus("current")
if mibBuilder.loadTexts:
    cwacsIngEFCI0Discard.setUnits("cells")
_CwacsIngEFCI1Discard_Type = Counter32
_CwacsIngEFCI1Discard_Object = MibTableColumn
cwacsIngEFCI1Discard = _CwacsIngEFCI1Discard_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 13),
    _CwacsIngEFCI1Discard_Type()
)
cwacsIngEFCI1Discard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsIngEFCI1Discard.setStatus("current")
if mibBuilder.loadTexts:
    cwacsIngEFCI1Discard.setUnits("cells")
_CwacsIngRcvOAM_Type = Counter32
_CwacsIngRcvOAM_Object = MibTableColumn
cwacsIngRcvOAM = _CwacsIngRcvOAM_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 14),
    _CwacsIngRcvOAM_Type()
)
cwacsIngRcvOAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsIngRcvOAM.setStatus("current")
if mibBuilder.loadTexts:
    cwacsIngRcvOAM.setUnits("cells")
_CwacsIngOAMDiscard_Type = Counter32
_CwacsIngOAMDiscard_Object = MibTableColumn
cwacsIngOAMDiscard = _CwacsIngOAMDiscard_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 15),
    _CwacsIngOAMDiscard_Type()
)
cwacsIngOAMDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsIngOAMDiscard.setStatus("current")
if mibBuilder.loadTexts:
    cwacsIngOAMDiscard.setUnits("cells")
_CwacsIngRcvRM_Type = Counter32
_CwacsIngRcvRM_Object = MibTableColumn
cwacsIngRcvRM = _CwacsIngRcvRM_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 16),
    _CwacsIngRcvRM_Type()
)
cwacsIngRcvRM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsIngRcvRM.setStatus("current")
if mibBuilder.loadTexts:
    cwacsIngRcvRM.setUnits("cells")
_CwacsIngRMDiscard_Type = Counter32
_CwacsIngRMDiscard_Object = MibTableColumn
cwacsIngRMDiscard = _CwacsIngRMDiscard_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 17),
    _CwacsIngRMDiscard_Type()
)
cwacsIngRMDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsIngRMDiscard.setStatus("current")
if mibBuilder.loadTexts:
    cwacsIngRMDiscard.setUnits("cells")
_CwacsIngXmtFRm_Type = Counter32
_CwacsIngXmtFRm_Object = MibTableColumn
cwacsIngXmtFRm = _CwacsIngXmtFRm_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 18),
    _CwacsIngXmtFRm_Type()
)
cwacsIngXmtFRm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsIngXmtFRm.setStatus("current")
if mibBuilder.loadTexts:
    cwacsIngXmtFRm.setUnits("cells")
_CwacsIngXmtBRmFsRm_Type = Counter32
_CwacsIngXmtBRmFsRm_Object = MibTableColumn
cwacsIngXmtBRmFsRm = _CwacsIngXmtBRmFsRm_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 19),
    _CwacsIngXmtBRmFsRm_Type()
)
cwacsIngXmtBRmFsRm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsIngXmtBRmFsRm.setStatus("current")
if mibBuilder.loadTexts:
    cwacsIngXmtBRmFsRm.setUnits("cells")
_CwacsIngRcvEOF1_Type = Counter32
_CwacsIngRcvEOF1_Object = MibTableColumn
cwacsIngRcvEOF1 = _CwacsIngRcvEOF1_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 20),
    _CwacsIngRcvEOF1_Type()
)
cwacsIngRcvEOF1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsIngRcvEOF1.setStatus("current")
if mibBuilder.loadTexts:
    cwacsIngRcvEOF1.setUnits("cells")
_CwacsIngEOF1Discard_Type = Counter32
_CwacsIngEOF1Discard_Object = MibTableColumn
cwacsIngEOF1Discard = _CwacsIngEOF1Discard_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 21),
    _CwacsIngEOF1Discard_Type()
)
cwacsIngEOF1Discard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsIngEOF1Discard.setStatus("current")
if mibBuilder.loadTexts:
    cwacsIngEOF1Discard.setUnits("cells")
_CwacsIngACR_Type = Gauge32
_CwacsIngACR_Object = MibTableColumn
cwacsIngACR = _CwacsIngACR_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 22),
    _CwacsIngACR_Type()
)
cwacsIngACR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsIngACR.setStatus("current")
if mibBuilder.loadTexts:
    cwacsIngACR.setUnits("cells/second")
_CwacsIngVCQueueDepth_Type = Gauge32
_CwacsIngVCQueueDepth_Object = MibTableColumn
cwacsIngVCQueueDepth = _CwacsIngVCQueueDepth_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 23),
    _CwacsIngVCQueueDepth_Type()
)
cwacsIngVCQueueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsIngVCQueueDepth.setStatus("current")
if mibBuilder.loadTexts:
    cwacsIngVCQueueDepth.setUnits("cells")
_CwacsEgrRcvCLP0_Type = Counter32
_CwacsEgrRcvCLP0_Object = MibTableColumn
cwacsEgrRcvCLP0 = _CwacsEgrRcvCLP0_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 24),
    _CwacsEgrRcvCLP0_Type()
)
cwacsEgrRcvCLP0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsEgrRcvCLP0.setStatus("current")
if mibBuilder.loadTexts:
    cwacsEgrRcvCLP0.setUnits("cells")
_CwacsEgrRcvCLP1_Type = Counter32
_CwacsEgrRcvCLP1_Object = MibTableColumn
cwacsEgrRcvCLP1 = _CwacsEgrRcvCLP1_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 25),
    _CwacsEgrRcvCLP1_Type()
)
cwacsEgrRcvCLP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsEgrRcvCLP1.setStatus("current")
if mibBuilder.loadTexts:
    cwacsEgrRcvCLP1.setUnits("cells")
_CwacsEgrXmtCLP0_Type = Counter32
_CwacsEgrXmtCLP0_Object = MibTableColumn
cwacsEgrXmtCLP0 = _CwacsEgrXmtCLP0_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 26),
    _CwacsEgrXmtCLP0_Type()
)
cwacsEgrXmtCLP0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsEgrXmtCLP0.setStatus("current")
if mibBuilder.loadTexts:
    cwacsEgrXmtCLP0.setUnits("cells")
_CwacsEgrXmtCLP1_Type = Counter32
_CwacsEgrXmtCLP1_Object = MibTableColumn
cwacsEgrXmtCLP1 = _CwacsEgrXmtCLP1_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 27),
    _CwacsEgrXmtCLP1_Type()
)
cwacsEgrXmtCLP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsEgrXmtCLP1.setStatus("current")
if mibBuilder.loadTexts:
    cwacsEgrXmtCLP1.setUnits("cells")
_CwacsEgrCLP0CoSDiscard_Type = Counter32
_CwacsEgrCLP0CoSDiscard_Object = MibTableColumn
cwacsEgrCLP0CoSDiscard = _CwacsEgrCLP0CoSDiscard_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 28),
    _CwacsEgrCLP0CoSDiscard_Type()
)
cwacsEgrCLP0CoSDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsEgrCLP0CoSDiscard.setStatus("current")
if mibBuilder.loadTexts:
    cwacsEgrCLP0CoSDiscard.setUnits("cells")
_CwacsEgrCLP1CoSDiscard_Type = Counter32
_CwacsEgrCLP1CoSDiscard_Object = MibTableColumn
cwacsEgrCLP1CoSDiscard = _CwacsEgrCLP1CoSDiscard_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 29),
    _CwacsEgrCLP1CoSDiscard_Type()
)
cwacsEgrCLP1CoSDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsEgrCLP1CoSDiscard.setStatus("current")
if mibBuilder.loadTexts:
    cwacsEgrCLP1CoSDiscard.setUnits("cells")
_CwacsEgrRcvEFCI0_Type = Counter32
_CwacsEgrRcvEFCI0_Object = MibTableColumn
cwacsEgrRcvEFCI0 = _CwacsEgrRcvEFCI0_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 30),
    _CwacsEgrRcvEFCI0_Type()
)
cwacsEgrRcvEFCI0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsEgrRcvEFCI0.setStatus("current")
if mibBuilder.loadTexts:
    cwacsEgrRcvEFCI0.setUnits("cells")
_CwacsEgrRcvEFCI1_Type = Counter32
_CwacsEgrRcvEFCI1_Object = MibTableColumn
cwacsEgrRcvEFCI1 = _CwacsEgrRcvEFCI1_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 31),
    _CwacsEgrRcvEFCI1_Type()
)
cwacsEgrRcvEFCI1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsEgrRcvEFCI1.setStatus("current")
if mibBuilder.loadTexts:
    cwacsEgrRcvEFCI1.setUnits("cells")
_CwacsEgrEFCI0Discard_Type = Counter32
_CwacsEgrEFCI0Discard_Object = MibTableColumn
cwacsEgrEFCI0Discard = _CwacsEgrEFCI0Discard_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 32),
    _CwacsEgrEFCI0Discard_Type()
)
cwacsEgrEFCI0Discard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsEgrEFCI0Discard.setStatus("current")
if mibBuilder.loadTexts:
    cwacsEgrEFCI0Discard.setUnits("cells")
_CwacsEgrEFCI1Discard_Type = Counter32
_CwacsEgrEFCI1Discard_Object = MibTableColumn
cwacsEgrEFCI1Discard = _CwacsEgrEFCI1Discard_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 33),
    _CwacsEgrEFCI1Discard_Type()
)
cwacsEgrEFCI1Discard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsEgrEFCI1Discard.setStatus("current")
if mibBuilder.loadTexts:
    cwacsEgrEFCI1Discard.setUnits("cells")
_CwacsEgrRcvOAM_Type = Counter32
_CwacsEgrRcvOAM_Object = MibTableColumn
cwacsEgrRcvOAM = _CwacsEgrRcvOAM_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 34),
    _CwacsEgrRcvOAM_Type()
)
cwacsEgrRcvOAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsEgrRcvOAM.setStatus("current")
if mibBuilder.loadTexts:
    cwacsEgrRcvOAM.setUnits("cells")
_CwacsEgrOAMDiscard_Type = Counter32
_CwacsEgrOAMDiscard_Object = MibTableColumn
cwacsEgrOAMDiscard = _CwacsEgrOAMDiscard_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 35),
    _CwacsEgrOAMDiscard_Type()
)
cwacsEgrOAMDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsEgrOAMDiscard.setStatus("current")
if mibBuilder.loadTexts:
    cwacsEgrOAMDiscard.setUnits("cells")
_CwacsEgrRcvRM_Type = Counter32
_CwacsEgrRcvRM_Object = MibTableColumn
cwacsEgrRcvRM = _CwacsEgrRcvRM_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 36),
    _CwacsEgrRcvRM_Type()
)
cwacsEgrRcvRM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsEgrRcvRM.setStatus("current")
if mibBuilder.loadTexts:
    cwacsEgrRcvRM.setUnits("cells")
_CwacsEgrRMDiscard_Type = Counter32
_CwacsEgrRMDiscard_Object = MibTableColumn
cwacsEgrRMDiscard = _CwacsEgrRMDiscard_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 37),
    _CwacsEgrRMDiscard_Type()
)
cwacsEgrRMDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsEgrRMDiscard.setStatus("current")
if mibBuilder.loadTexts:
    cwacsEgrRMDiscard.setUnits("cells")
_CwacsEgrXmtFRm_Type = Counter32
_CwacsEgrXmtFRm_Object = MibTableColumn
cwacsEgrXmtFRm = _CwacsEgrXmtFRm_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 38),
    _CwacsEgrXmtFRm_Type()
)
cwacsEgrXmtFRm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsEgrXmtFRm.setStatus("current")
if mibBuilder.loadTexts:
    cwacsEgrXmtFRm.setUnits("cells")
_CwacsEgrXmtBRmFsRm_Type = Counter32
_CwacsEgrXmtBRmFsRm_Object = MibTableColumn
cwacsEgrXmtBRmFsRm = _CwacsEgrXmtBRmFsRm_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 39),
    _CwacsEgrXmtBRmFsRm_Type()
)
cwacsEgrXmtBRmFsRm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsEgrXmtBRmFsRm.setStatus("current")
if mibBuilder.loadTexts:
    cwacsEgrXmtBRmFsRm.setUnits("cells")
_CwacsEgrRcvEOF1_Type = Counter32
_CwacsEgrRcvEOF1_Object = MibTableColumn
cwacsEgrRcvEOF1 = _CwacsEgrRcvEOF1_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 40),
    _CwacsEgrRcvEOF1_Type()
)
cwacsEgrRcvEOF1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsEgrRcvEOF1.setStatus("current")
if mibBuilder.loadTexts:
    cwacsEgrRcvEOF1.setUnits("cells")
_CwacsEgrEOF1Discard_Type = Counter32
_CwacsEgrEOF1Discard_Object = MibTableColumn
cwacsEgrEOF1Discard = _CwacsEgrEOF1Discard_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 41),
    _CwacsEgrEOF1Discard_Type()
)
cwacsEgrEOF1Discard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsEgrEOF1Discard.setStatus("current")
if mibBuilder.loadTexts:
    cwacsEgrEOF1Discard.setUnits("cells")
_CwacsEgrACR_Type = Gauge32
_CwacsEgrACR_Object = MibTableColumn
cwacsEgrACR = _CwacsEgrACR_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 42),
    _CwacsEgrACR_Type()
)
cwacsEgrACR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsEgrACR.setStatus("current")
if mibBuilder.loadTexts:
    cwacsEgrACR.setUnits("cells/second")
_CwacsEgrVCQueueDepth_Type = Gauge32
_CwacsEgrVCQueueDepth_Object = MibTableColumn
cwacsEgrVCQueueDepth = _CwacsEgrVCQueueDepth_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 43),
    _CwacsEgrVCQueueDepth_Type()
)
cwacsEgrVCQueueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsEgrVCQueueDepth.setStatus("current")
if mibBuilder.loadTexts:
    cwacsEgrVCQueueDepth.setUnits("cells")


class _CwacsStatsClear_Type(TruthValue):
    """Custom type cwacsStatsClear based on TruthValue"""


_CwacsStatsClear_Object = MibTableColumn
cwacsStatsClear = _CwacsStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 44),
    _CwacsStatsClear_Type()
)
cwacsStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwacsStatsClear.setStatus("current")
_CwacsHighIngRcvCLP0_Type = Counter32
_CwacsHighIngRcvCLP0_Object = MibTableColumn
cwacsHighIngRcvCLP0 = _CwacsHighIngRcvCLP0_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 45),
    _CwacsHighIngRcvCLP0_Type()
)
cwacsHighIngRcvCLP0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsHighIngRcvCLP0.setStatus("current")
if mibBuilder.loadTexts:
    cwacsHighIngRcvCLP0.setUnits("cells")
_CwacsHighIngRcvCLP1_Type = Counter32
_CwacsHighIngRcvCLP1_Object = MibTableColumn
cwacsHighIngRcvCLP1 = _CwacsHighIngRcvCLP1_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 46),
    _CwacsHighIngRcvCLP1_Type()
)
cwacsHighIngRcvCLP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsHighIngRcvCLP1.setStatus("current")
if mibBuilder.loadTexts:
    cwacsHighIngRcvCLP1.setUnits("cells")
_CwacsHighIngXmtCLP0_Type = Counter32
_CwacsHighIngXmtCLP0_Object = MibTableColumn
cwacsHighIngXmtCLP0 = _CwacsHighIngXmtCLP0_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 47),
    _CwacsHighIngXmtCLP0_Type()
)
cwacsHighIngXmtCLP0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsHighIngXmtCLP0.setStatus("current")
if mibBuilder.loadTexts:
    cwacsHighIngXmtCLP0.setUnits("cells")
_CwacsHighIngXmtCLP1_Type = Counter32
_CwacsHighIngXmtCLP1_Object = MibTableColumn
cwacsHighIngXmtCLP1 = _CwacsHighIngXmtCLP1_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 48),
    _CwacsHighIngXmtCLP1_Type()
)
cwacsHighIngXmtCLP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsHighIngXmtCLP1.setStatus("current")
if mibBuilder.loadTexts:
    cwacsHighIngXmtCLP1.setUnits("cells")
_CwacsHighIngCLP0CoSDiscard_Type = Counter32
_CwacsHighIngCLP0CoSDiscard_Object = MibTableColumn
cwacsHighIngCLP0CoSDiscard = _CwacsHighIngCLP0CoSDiscard_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 49),
    _CwacsHighIngCLP0CoSDiscard_Type()
)
cwacsHighIngCLP0CoSDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsHighIngCLP0CoSDiscard.setStatus("current")
if mibBuilder.loadTexts:
    cwacsHighIngCLP0CoSDiscard.setUnits("cells")
_CwacsHighIngCLP1CoSDiscard_Type = Counter32
_CwacsHighIngCLP1CoSDiscard_Object = MibTableColumn
cwacsHighIngCLP1CoSDiscard = _CwacsHighIngCLP1CoSDiscard_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 50),
    _CwacsHighIngCLP1CoSDiscard_Type()
)
cwacsHighIngCLP1CoSDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsHighIngCLP1CoSDiscard.setStatus("current")
if mibBuilder.loadTexts:
    cwacsHighIngCLP1CoSDiscard.setUnits("cells")
_CwacsHighIngCLP0UpcDiscard_Type = Counter32
_CwacsHighIngCLP0UpcDiscard_Object = MibTableColumn
cwacsHighIngCLP0UpcDiscard = _CwacsHighIngCLP0UpcDiscard_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 51),
    _CwacsHighIngCLP0UpcDiscard_Type()
)
cwacsHighIngCLP0UpcDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsHighIngCLP0UpcDiscard.setStatus("current")
if mibBuilder.loadTexts:
    cwacsHighIngCLP0UpcDiscard.setUnits("cells")
_CwacsHighIngCLP1UpcDiscard_Type = Counter32
_CwacsHighIngCLP1UpcDiscard_Object = MibTableColumn
cwacsHighIngCLP1UpcDiscard = _CwacsHighIngCLP1UpcDiscard_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 52),
    _CwacsHighIngCLP1UpcDiscard_Type()
)
cwacsHighIngCLP1UpcDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsHighIngCLP1UpcDiscard.setStatus("current")
if mibBuilder.loadTexts:
    cwacsHighIngCLP1UpcDiscard.setUnits("cells")
_CwacsHighIngCLP0UpcTagged_Type = Counter32
_CwacsHighIngCLP0UpcTagged_Object = MibTableColumn
cwacsHighIngCLP0UpcTagged = _CwacsHighIngCLP0UpcTagged_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 53),
    _CwacsHighIngCLP0UpcTagged_Type()
)
cwacsHighIngCLP0UpcTagged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsHighIngCLP0UpcTagged.setStatus("current")
if mibBuilder.loadTexts:
    cwacsHighIngCLP0UpcTagged.setUnits("cells")
_CwacsHighIngRcvEFCI0_Type = Counter32
_CwacsHighIngRcvEFCI0_Object = MibTableColumn
cwacsHighIngRcvEFCI0 = _CwacsHighIngRcvEFCI0_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 54),
    _CwacsHighIngRcvEFCI0_Type()
)
cwacsHighIngRcvEFCI0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsHighIngRcvEFCI0.setStatus("current")
if mibBuilder.loadTexts:
    cwacsHighIngRcvEFCI0.setUnits("cells")
_CwacsHighIngRcvEFCI1_Type = Counter32
_CwacsHighIngRcvEFCI1_Object = MibTableColumn
cwacsHighIngRcvEFCI1 = _CwacsHighIngRcvEFCI1_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 55),
    _CwacsHighIngRcvEFCI1_Type()
)
cwacsHighIngRcvEFCI1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsHighIngRcvEFCI1.setStatus("current")
if mibBuilder.loadTexts:
    cwacsHighIngRcvEFCI1.setUnits("cells")
_CwacsHighIngEFCI0Discard_Type = Counter32
_CwacsHighIngEFCI0Discard_Object = MibTableColumn
cwacsHighIngEFCI0Discard = _CwacsHighIngEFCI0Discard_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 56),
    _CwacsHighIngEFCI0Discard_Type()
)
cwacsHighIngEFCI0Discard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsHighIngEFCI0Discard.setStatus("current")
if mibBuilder.loadTexts:
    cwacsHighIngEFCI0Discard.setUnits("cells")
_CwacsHighIngEFCI1Discard_Type = Counter32
_CwacsHighIngEFCI1Discard_Object = MibTableColumn
cwacsHighIngEFCI1Discard = _CwacsHighIngEFCI1Discard_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 57),
    _CwacsHighIngEFCI1Discard_Type()
)
cwacsHighIngEFCI1Discard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsHighIngEFCI1Discard.setStatus("current")
if mibBuilder.loadTexts:
    cwacsHighIngEFCI1Discard.setUnits("cells")
_CwacsHighIngRcvEOF1_Type = Counter32
_CwacsHighIngRcvEOF1_Object = MibTableColumn
cwacsHighIngRcvEOF1 = _CwacsHighIngRcvEOF1_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 58),
    _CwacsHighIngRcvEOF1_Type()
)
cwacsHighIngRcvEOF1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsHighIngRcvEOF1.setStatus("current")
if mibBuilder.loadTexts:
    cwacsHighIngRcvEOF1.setUnits("cells")
_CwacsHighIngEOF1Discard_Type = Counter32
_CwacsHighIngEOF1Discard_Object = MibTableColumn
cwacsHighIngEOF1Discard = _CwacsHighIngEOF1Discard_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 59),
    _CwacsHighIngEOF1Discard_Type()
)
cwacsHighIngEOF1Discard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsHighIngEOF1Discard.setStatus("current")
if mibBuilder.loadTexts:
    cwacsHighIngEOF1Discard.setUnits("cells")
_CwacsHighEgrRcvCLP0_Type = Counter32
_CwacsHighEgrRcvCLP0_Object = MibTableColumn
cwacsHighEgrRcvCLP0 = _CwacsHighEgrRcvCLP0_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 60),
    _CwacsHighEgrRcvCLP0_Type()
)
cwacsHighEgrRcvCLP0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsHighEgrRcvCLP0.setStatus("current")
if mibBuilder.loadTexts:
    cwacsHighEgrRcvCLP0.setUnits("cells")
_CwacsHighEgrRcvCLP1_Type = Counter32
_CwacsHighEgrRcvCLP1_Object = MibTableColumn
cwacsHighEgrRcvCLP1 = _CwacsHighEgrRcvCLP1_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 61),
    _CwacsHighEgrRcvCLP1_Type()
)
cwacsHighEgrRcvCLP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsHighEgrRcvCLP1.setStatus("current")
if mibBuilder.loadTexts:
    cwacsHighEgrRcvCLP1.setUnits("cells")
_CwacsHighEgrXmtCLP0_Type = Counter32
_CwacsHighEgrXmtCLP0_Object = MibTableColumn
cwacsHighEgrXmtCLP0 = _CwacsHighEgrXmtCLP0_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 62),
    _CwacsHighEgrXmtCLP0_Type()
)
cwacsHighEgrXmtCLP0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsHighEgrXmtCLP0.setStatus("current")
if mibBuilder.loadTexts:
    cwacsHighEgrXmtCLP0.setUnits("cells")
_CwacsHighEgrXmtCLP1_Type = Counter32
_CwacsHighEgrXmtCLP1_Object = MibTableColumn
cwacsHighEgrXmtCLP1 = _CwacsHighEgrXmtCLP1_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 63),
    _CwacsHighEgrXmtCLP1_Type()
)
cwacsHighEgrXmtCLP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsHighEgrXmtCLP1.setStatus("current")
if mibBuilder.loadTexts:
    cwacsHighEgrXmtCLP1.setUnits("cells")
_CwacsHighEgrCLP0CoSDiscard_Type = Counter32
_CwacsHighEgrCLP0CoSDiscard_Object = MibTableColumn
cwacsHighEgrCLP0CoSDiscard = _CwacsHighEgrCLP0CoSDiscard_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 64),
    _CwacsHighEgrCLP0CoSDiscard_Type()
)
cwacsHighEgrCLP0CoSDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsHighEgrCLP0CoSDiscard.setStatus("current")
if mibBuilder.loadTexts:
    cwacsHighEgrCLP0CoSDiscard.setUnits("cells")
_CwacsHighEgrCLP1CoSDiscard_Type = Counter32
_CwacsHighEgrCLP1CoSDiscard_Object = MibTableColumn
cwacsHighEgrCLP1CoSDiscard = _CwacsHighEgrCLP1CoSDiscard_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 65),
    _CwacsHighEgrCLP1CoSDiscard_Type()
)
cwacsHighEgrCLP1CoSDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsHighEgrCLP1CoSDiscard.setStatus("current")
if mibBuilder.loadTexts:
    cwacsHighEgrCLP1CoSDiscard.setUnits("cells")
_CwacsHighEgrRcvEFCI0_Type = Counter32
_CwacsHighEgrRcvEFCI0_Object = MibTableColumn
cwacsHighEgrRcvEFCI0 = _CwacsHighEgrRcvEFCI0_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 66),
    _CwacsHighEgrRcvEFCI0_Type()
)
cwacsHighEgrRcvEFCI0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsHighEgrRcvEFCI0.setStatus("current")
if mibBuilder.loadTexts:
    cwacsHighEgrRcvEFCI0.setUnits("cells")
_CwacsHighEgrRcvEFCI1_Type = Counter32
_CwacsHighEgrRcvEFCI1_Object = MibTableColumn
cwacsHighEgrRcvEFCI1 = _CwacsHighEgrRcvEFCI1_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 67),
    _CwacsHighEgrRcvEFCI1_Type()
)
cwacsHighEgrRcvEFCI1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsHighEgrRcvEFCI1.setStatus("current")
if mibBuilder.loadTexts:
    cwacsHighEgrRcvEFCI1.setUnits("cells")
_CwacsHighEgrEFCI0Discard_Type = Counter32
_CwacsHighEgrEFCI0Discard_Object = MibTableColumn
cwacsHighEgrEFCI0Discard = _CwacsHighEgrEFCI0Discard_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 68),
    _CwacsHighEgrEFCI0Discard_Type()
)
cwacsHighEgrEFCI0Discard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsHighEgrEFCI0Discard.setStatus("current")
if mibBuilder.loadTexts:
    cwacsHighEgrEFCI0Discard.setUnits("cells")
_CwacsHighEgrEFCI1Discard_Type = Counter32
_CwacsHighEgrEFCI1Discard_Object = MibTableColumn
cwacsHighEgrEFCI1Discard = _CwacsHighEgrEFCI1Discard_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 69),
    _CwacsHighEgrEFCI1Discard_Type()
)
cwacsHighEgrEFCI1Discard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsHighEgrEFCI1Discard.setStatus("current")
if mibBuilder.loadTexts:
    cwacsHighEgrEFCI1Discard.setUnits("cells")
_CwacsHighEgrRcvEOF1_Type = Counter32
_CwacsHighEgrRcvEOF1_Object = MibTableColumn
cwacsHighEgrRcvEOF1 = _CwacsHighEgrRcvEOF1_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 70),
    _CwacsHighEgrRcvEOF1_Type()
)
cwacsHighEgrRcvEOF1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsHighEgrRcvEOF1.setStatus("current")
if mibBuilder.loadTexts:
    cwacsHighEgrRcvEOF1.setUnits("cells")
_CwacsHighEgrEOF1Discard_Type = Counter32
_CwacsHighEgrEOF1Discard_Object = MibTableColumn
cwacsHighEgrEOF1Discard = _CwacsHighEgrEOF1Discard_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 1, 1, 71),
    _CwacsHighEgrEOF1Discard_Type()
)
cwacsHighEgrEOF1Discard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsHighEgrEOF1Discard.setStatus("current")
if mibBuilder.loadTexts:
    cwacsHighEgrEOF1Discard.setUnits("cells")
_CwacsXTable_Object = MibTable
cwacsXTable = _CwacsXTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cwacsXTable.setStatus("current")
_CwacsXEntry_Object = MibTableRow
cwacsXEntry = _CwacsXEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cwacsXEntry.setStatus("current")
_CwacsHCIngRcvCLP0_Type = Counter64
_CwacsHCIngRcvCLP0_Object = MibTableColumn
cwacsHCIngRcvCLP0 = _CwacsHCIngRcvCLP0_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 2, 1, 1),
    _CwacsHCIngRcvCLP0_Type()
)
cwacsHCIngRcvCLP0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsHCIngRcvCLP0.setStatus("current")
if mibBuilder.loadTexts:
    cwacsHCIngRcvCLP0.setUnits("cells")
_CwacsHCIngRcvCLP1_Type = Counter64
_CwacsHCIngRcvCLP1_Object = MibTableColumn
cwacsHCIngRcvCLP1 = _CwacsHCIngRcvCLP1_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 2, 1, 2),
    _CwacsHCIngRcvCLP1_Type()
)
cwacsHCIngRcvCLP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsHCIngRcvCLP1.setStatus("current")
if mibBuilder.loadTexts:
    cwacsHCIngRcvCLP1.setUnits("cells")
_CwacsHCIngXmtCLP0_Type = Counter64
_CwacsHCIngXmtCLP0_Object = MibTableColumn
cwacsHCIngXmtCLP0 = _CwacsHCIngXmtCLP0_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 2, 1, 3),
    _CwacsHCIngXmtCLP0_Type()
)
cwacsHCIngXmtCLP0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsHCIngXmtCLP0.setStatus("current")
if mibBuilder.loadTexts:
    cwacsHCIngXmtCLP0.setUnits("cells")
_CwacsHCIngXmtCLP1_Type = Counter64
_CwacsHCIngXmtCLP1_Object = MibTableColumn
cwacsHCIngXmtCLP1 = _CwacsHCIngXmtCLP1_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 2, 1, 4),
    _CwacsHCIngXmtCLP1_Type()
)
cwacsHCIngXmtCLP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsHCIngXmtCLP1.setStatus("current")
if mibBuilder.loadTexts:
    cwacsHCIngXmtCLP1.setUnits("cells")
_CwacsHCIngCLP0CoSDiscard_Type = Counter64
_CwacsHCIngCLP0CoSDiscard_Object = MibTableColumn
cwacsHCIngCLP0CoSDiscard = _CwacsHCIngCLP0CoSDiscard_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 2, 1, 5),
    _CwacsHCIngCLP0CoSDiscard_Type()
)
cwacsHCIngCLP0CoSDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsHCIngCLP0CoSDiscard.setStatus("current")
if mibBuilder.loadTexts:
    cwacsHCIngCLP0CoSDiscard.setUnits("cells")
_CwacsHCIngCLP1CoSDiscard_Type = Counter64
_CwacsHCIngCLP1CoSDiscard_Object = MibTableColumn
cwacsHCIngCLP1CoSDiscard = _CwacsHCIngCLP1CoSDiscard_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 2, 1, 6),
    _CwacsHCIngCLP1CoSDiscard_Type()
)
cwacsHCIngCLP1CoSDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsHCIngCLP1CoSDiscard.setStatus("current")
if mibBuilder.loadTexts:
    cwacsHCIngCLP1CoSDiscard.setUnits("cells")
_CwacsHCIngCLP0UpcDiscard_Type = Counter64
_CwacsHCIngCLP0UpcDiscard_Object = MibTableColumn
cwacsHCIngCLP0UpcDiscard = _CwacsHCIngCLP0UpcDiscard_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 2, 1, 7),
    _CwacsHCIngCLP0UpcDiscard_Type()
)
cwacsHCIngCLP0UpcDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsHCIngCLP0UpcDiscard.setStatus("current")
if mibBuilder.loadTexts:
    cwacsHCIngCLP0UpcDiscard.setUnits("cells")
_CwacsHCIngCLP1UpcDiscard_Type = Counter64
_CwacsHCIngCLP1UpcDiscard_Object = MibTableColumn
cwacsHCIngCLP1UpcDiscard = _CwacsHCIngCLP1UpcDiscard_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 2, 1, 8),
    _CwacsHCIngCLP1UpcDiscard_Type()
)
cwacsHCIngCLP1UpcDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsHCIngCLP1UpcDiscard.setStatus("current")
if mibBuilder.loadTexts:
    cwacsHCIngCLP1UpcDiscard.setUnits("cells")
_CwacsHCIngCLP0UpcTagged_Type = Counter64
_CwacsHCIngCLP0UpcTagged_Object = MibTableColumn
cwacsHCIngCLP0UpcTagged = _CwacsHCIngCLP0UpcTagged_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 2, 1, 9),
    _CwacsHCIngCLP0UpcTagged_Type()
)
cwacsHCIngCLP0UpcTagged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsHCIngCLP0UpcTagged.setStatus("current")
if mibBuilder.loadTexts:
    cwacsHCIngCLP0UpcTagged.setUnits("cells")
_CwacsHCIngRcvEFCI0_Type = Counter64
_CwacsHCIngRcvEFCI0_Object = MibTableColumn
cwacsHCIngRcvEFCI0 = _CwacsHCIngRcvEFCI0_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 2, 1, 10),
    _CwacsHCIngRcvEFCI0_Type()
)
cwacsHCIngRcvEFCI0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsHCIngRcvEFCI0.setStatus("current")
if mibBuilder.loadTexts:
    cwacsHCIngRcvEFCI0.setUnits("cells")
_CwacsHCIngRcvEFCI1_Type = Counter64
_CwacsHCIngRcvEFCI1_Object = MibTableColumn
cwacsHCIngRcvEFCI1 = _CwacsHCIngRcvEFCI1_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 2, 1, 11),
    _CwacsHCIngRcvEFCI1_Type()
)
cwacsHCIngRcvEFCI1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsHCIngRcvEFCI1.setStatus("current")
if mibBuilder.loadTexts:
    cwacsHCIngRcvEFCI1.setUnits("cells")
_CwacsHCIngEFCI0Discard_Type = Counter64
_CwacsHCIngEFCI0Discard_Object = MibTableColumn
cwacsHCIngEFCI0Discard = _CwacsHCIngEFCI0Discard_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 2, 1, 12),
    _CwacsHCIngEFCI0Discard_Type()
)
cwacsHCIngEFCI0Discard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsHCIngEFCI0Discard.setStatus("current")
if mibBuilder.loadTexts:
    cwacsHCIngEFCI0Discard.setUnits("cells")
_CwacsHCIngEFCI1Discard_Type = Counter64
_CwacsHCIngEFCI1Discard_Object = MibTableColumn
cwacsHCIngEFCI1Discard = _CwacsHCIngEFCI1Discard_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 2, 1, 13),
    _CwacsHCIngEFCI1Discard_Type()
)
cwacsHCIngEFCI1Discard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsHCIngEFCI1Discard.setStatus("current")
if mibBuilder.loadTexts:
    cwacsHCIngEFCI1Discard.setUnits("cells")
_CwacsHCIngRcvEOF1_Type = Counter64
_CwacsHCIngRcvEOF1_Object = MibTableColumn
cwacsHCIngRcvEOF1 = _CwacsHCIngRcvEOF1_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 2, 1, 14),
    _CwacsHCIngRcvEOF1_Type()
)
cwacsHCIngRcvEOF1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsHCIngRcvEOF1.setStatus("current")
if mibBuilder.loadTexts:
    cwacsHCIngRcvEOF1.setUnits("cells")
_CwacsHCIngEOF1Discard_Type = Counter64
_CwacsHCIngEOF1Discard_Object = MibTableColumn
cwacsHCIngEOF1Discard = _CwacsHCIngEOF1Discard_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 2, 1, 15),
    _CwacsHCIngEOF1Discard_Type()
)
cwacsHCIngEOF1Discard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsHCIngEOF1Discard.setStatus("current")
if mibBuilder.loadTexts:
    cwacsHCIngEOF1Discard.setUnits("cells")
_CwacsHCEgrRcvCLP0_Type = Counter64
_CwacsHCEgrRcvCLP0_Object = MibTableColumn
cwacsHCEgrRcvCLP0 = _CwacsHCEgrRcvCLP0_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 2, 1, 16),
    _CwacsHCEgrRcvCLP0_Type()
)
cwacsHCEgrRcvCLP0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsHCEgrRcvCLP0.setStatus("current")
if mibBuilder.loadTexts:
    cwacsHCEgrRcvCLP0.setUnits("cells")
_CwacsHCEgrRcvCLP1_Type = Counter64
_CwacsHCEgrRcvCLP1_Object = MibTableColumn
cwacsHCEgrRcvCLP1 = _CwacsHCEgrRcvCLP1_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 2, 1, 17),
    _CwacsHCEgrRcvCLP1_Type()
)
cwacsHCEgrRcvCLP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsHCEgrRcvCLP1.setStatus("current")
if mibBuilder.loadTexts:
    cwacsHCEgrRcvCLP1.setUnits("cells")
_CwacsHCEgrXmtCLP0_Type = Counter64
_CwacsHCEgrXmtCLP0_Object = MibTableColumn
cwacsHCEgrXmtCLP0 = _CwacsHCEgrXmtCLP0_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 2, 1, 18),
    _CwacsHCEgrXmtCLP0_Type()
)
cwacsHCEgrXmtCLP0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsHCEgrXmtCLP0.setStatus("current")
if mibBuilder.loadTexts:
    cwacsHCEgrXmtCLP0.setUnits("cells")
_CwacsHCEgrXmtCLP1_Type = Counter64
_CwacsHCEgrXmtCLP1_Object = MibTableColumn
cwacsHCEgrXmtCLP1 = _CwacsHCEgrXmtCLP1_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 2, 1, 19),
    _CwacsHCEgrXmtCLP1_Type()
)
cwacsHCEgrXmtCLP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsHCEgrXmtCLP1.setStatus("current")
if mibBuilder.loadTexts:
    cwacsHCEgrXmtCLP1.setUnits("cells")
_CwacsHCEgrCLP0CoSDiscard_Type = Counter64
_CwacsHCEgrCLP0CoSDiscard_Object = MibTableColumn
cwacsHCEgrCLP0CoSDiscard = _CwacsHCEgrCLP0CoSDiscard_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 2, 1, 20),
    _CwacsHCEgrCLP0CoSDiscard_Type()
)
cwacsHCEgrCLP0CoSDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsHCEgrCLP0CoSDiscard.setStatus("current")
if mibBuilder.loadTexts:
    cwacsHCEgrCLP0CoSDiscard.setUnits("cells")
_CwacsHCEgrCLP1CoSDiscard_Type = Counter64
_CwacsHCEgrCLP1CoSDiscard_Object = MibTableColumn
cwacsHCEgrCLP1CoSDiscard = _CwacsHCEgrCLP1CoSDiscard_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 2, 1, 21),
    _CwacsHCEgrCLP1CoSDiscard_Type()
)
cwacsHCEgrCLP1CoSDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsHCEgrCLP1CoSDiscard.setStatus("current")
if mibBuilder.loadTexts:
    cwacsHCEgrCLP1CoSDiscard.setUnits("cells")
_CwacsHCEgrRcvEFCI0_Type = Counter64
_CwacsHCEgrRcvEFCI0_Object = MibTableColumn
cwacsHCEgrRcvEFCI0 = _CwacsHCEgrRcvEFCI0_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 2, 1, 22),
    _CwacsHCEgrRcvEFCI0_Type()
)
cwacsHCEgrRcvEFCI0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsHCEgrRcvEFCI0.setStatus("current")
if mibBuilder.loadTexts:
    cwacsHCEgrRcvEFCI0.setUnits("cells")
_CwacsHCEgrRcvEFCI1_Type = Counter64
_CwacsHCEgrRcvEFCI1_Object = MibTableColumn
cwacsHCEgrRcvEFCI1 = _CwacsHCEgrRcvEFCI1_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 2, 1, 23),
    _CwacsHCEgrRcvEFCI1_Type()
)
cwacsHCEgrRcvEFCI1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsHCEgrRcvEFCI1.setStatus("current")
if mibBuilder.loadTexts:
    cwacsHCEgrRcvEFCI1.setUnits("cells")
_CwacsHCEgrEFCI0Discard_Type = Counter64
_CwacsHCEgrEFCI0Discard_Object = MibTableColumn
cwacsHCEgrEFCI0Discard = _CwacsHCEgrEFCI0Discard_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 2, 1, 24),
    _CwacsHCEgrEFCI0Discard_Type()
)
cwacsHCEgrEFCI0Discard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsHCEgrEFCI0Discard.setStatus("current")
if mibBuilder.loadTexts:
    cwacsHCEgrEFCI0Discard.setUnits("cells")
_CwacsHCEgrEFCI1Discard_Type = Counter64
_CwacsHCEgrEFCI1Discard_Object = MibTableColumn
cwacsHCEgrEFCI1Discard = _CwacsHCEgrEFCI1Discard_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 2, 1, 25),
    _CwacsHCEgrEFCI1Discard_Type()
)
cwacsHCEgrEFCI1Discard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsHCEgrEFCI1Discard.setStatus("current")
if mibBuilder.loadTexts:
    cwacsHCEgrEFCI1Discard.setUnits("cells")
_CwacsHCEgrRcvEOF1_Type = Counter64
_CwacsHCEgrRcvEOF1_Object = MibTableColumn
cwacsHCEgrRcvEOF1 = _CwacsHCEgrRcvEOF1_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 2, 1, 26),
    _CwacsHCEgrRcvEOF1_Type()
)
cwacsHCEgrRcvEOF1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsHCEgrRcvEOF1.setStatus("current")
if mibBuilder.loadTexts:
    cwacsHCEgrRcvEOF1.setUnits("cells")
_CwacsHCEgrEOF1Discard_Type = Counter64
_CwacsHCEgrEOF1Discard_Object = MibTableColumn
cwacsHCEgrEOF1Discard = _CwacsHCEgrEOF1Discard_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 2, 1, 27),
    _CwacsHCEgrEOF1Discard_Type()
)
cwacsHCEgrEOF1Discard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsHCEgrEOF1Discard.setStatus("current")
if mibBuilder.loadTexts:
    cwacsHCEgrEOF1Discard.setUnits("cells")
_CwaConnStatsTable_Object = MibTable
cwaConnStatsTable = _CwaConnStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cwaConnStatsTable.setStatus("current")
_CwaConnStatsEntry_Object = MibTableRow
cwaConnStatsEntry = _CwaConnStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 3, 1)
)
cwaConnStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WAN-ATM-CONN-MIB", "cwaChanVpi"),
    (0, "CISCO-WAN-ATM-CONN-MIB", "cwaChanVci"),
)
if mibBuilder.loadTexts:
    cwaConnStatsEntry.setStatus("current")
_CwaConnStatsIngRcv_Type = Counter32
_CwaConnStatsIngRcv_Object = MibTableColumn
cwaConnStatsIngRcv = _CwaConnStatsIngRcv_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 3, 1, 1),
    _CwaConnStatsIngRcv_Type()
)
cwaConnStatsIngRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwaConnStatsIngRcv.setStatus("current")
if mibBuilder.loadTexts:
    cwaConnStatsIngRcv.setUnits("cells")
_CwaConnStatsIngCLP0Discard_Type = Counter32
_CwaConnStatsIngCLP0Discard_Object = MibTableColumn
cwaConnStatsIngCLP0Discard = _CwaConnStatsIngCLP0Discard_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 3, 1, 2),
    _CwaConnStatsIngCLP0Discard_Type()
)
cwaConnStatsIngCLP0Discard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwaConnStatsIngCLP0Discard.setStatus("current")
if mibBuilder.loadTexts:
    cwaConnStatsIngCLP0Discard.setUnits("cells")
_CwaConnStatsIngCLP1Discard_Type = Counter32
_CwaConnStatsIngCLP1Discard_Object = MibTableColumn
cwaConnStatsIngCLP1Discard = _CwaConnStatsIngCLP1Discard_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 3, 1, 3),
    _CwaConnStatsIngCLP1Discard_Type()
)
cwaConnStatsIngCLP1Discard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwaConnStatsIngCLP1Discard.setStatus("current")
if mibBuilder.loadTexts:
    cwaConnStatsIngCLP1Discard.setUnits("cells")
_CwaConnStatsIngTotalDiscard_Type = Counter32
_CwaConnStatsIngTotalDiscard_Object = MibTableColumn
cwaConnStatsIngTotalDiscard = _CwaConnStatsIngTotalDiscard_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 3, 1, 4),
    _CwaConnStatsIngTotalDiscard_Type()
)
cwaConnStatsIngTotalDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwaConnStatsIngTotalDiscard.setStatus("current")
if mibBuilder.loadTexts:
    cwaConnStatsIngTotalDiscard.setUnits("cells")
_CwaConnStatsEgrXmt_Type = Counter32
_CwaConnStatsEgrXmt_Object = MibTableColumn
cwaConnStatsEgrXmt = _CwaConnStatsEgrXmt_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 3, 1, 5),
    _CwaConnStatsEgrXmt_Type()
)
cwaConnStatsEgrXmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwaConnStatsEgrXmt.setStatus("current")
if mibBuilder.loadTexts:
    cwaConnStatsEgrXmt.setUnits("cells")
_CwaConnStatsEgrCLP0Discard_Type = Counter32
_CwaConnStatsEgrCLP0Discard_Object = MibTableColumn
cwaConnStatsEgrCLP0Discard = _CwaConnStatsEgrCLP0Discard_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 3, 1, 6),
    _CwaConnStatsEgrCLP0Discard_Type()
)
cwaConnStatsEgrCLP0Discard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwaConnStatsEgrCLP0Discard.setStatus("current")
if mibBuilder.loadTexts:
    cwaConnStatsEgrCLP0Discard.setUnits("cells")
_CwaConnStatsEgrCLP1Discard_Type = Counter32
_CwaConnStatsEgrCLP1Discard_Object = MibTableColumn
cwaConnStatsEgrCLP1Discard = _CwaConnStatsEgrCLP1Discard_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 3, 1, 7),
    _CwaConnStatsEgrCLP1Discard_Type()
)
cwaConnStatsEgrCLP1Discard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwaConnStatsEgrCLP1Discard.setStatus("current")
if mibBuilder.loadTexts:
    cwaConnStatsEgrCLP1Discard.setUnits("cells")
_CwaConnStatsEgrTotalDiscard_Type = Counter32
_CwaConnStatsEgrTotalDiscard_Object = MibTableColumn
cwaConnStatsEgrTotalDiscard = _CwaConnStatsEgrTotalDiscard_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 3, 1, 8),
    _CwaConnStatsEgrTotalDiscard_Type()
)
cwaConnStatsEgrTotalDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwaConnStatsEgrTotalDiscard.setStatus("current")
if mibBuilder.loadTexts:
    cwaConnStatsEgrTotalDiscard.setUnits("cells")


class _CwaConnStatsClear_Type(TruthValue):
    """Custom type cwaConnStatsClear based on TruthValue"""


_CwaConnStatsClear_Object = MibTableColumn
cwaConnStatsClear = _CwaConnStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 3, 1, 9),
    _CwaConnStatsClear_Type()
)
cwaConnStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwaConnStatsClear.setStatus("current")
_CwacsExtStatsTable_Object = MibTable
cwacsExtStatsTable = _CwacsExtStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cwacsExtStatsTable.setStatus("current")
_CwacsExtStatsEntry_Object = MibTableRow
cwacsExtStatsEntry = _CwacsExtStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cwacsExtStatsEntry.setStatus("current")
_CwacsEgrAal2HecErrors_Type = Counter32
_CwacsEgrAal2HecErrors_Object = MibTableColumn
cwacsEgrAal2HecErrors = _CwacsEgrAal2HecErrors_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 4, 1, 1),
    _CwacsEgrAal2HecErrors_Type()
)
cwacsEgrAal2HecErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsEgrAal2HecErrors.setStatus("current")
if mibBuilder.loadTexts:
    cwacsEgrAal2HecErrors.setUnits("PDUs")
_CwacsEgrAal2InvalidOsfCells_Type = Counter32
_CwacsEgrAal2InvalidOsfCells_Object = MibTableColumn
cwacsEgrAal2InvalidOsfCells = _CwacsEgrAal2InvalidOsfCells_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 4, 1, 2),
    _CwacsEgrAal2InvalidOsfCells_Type()
)
cwacsEgrAal2InvalidOsfCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsEgrAal2InvalidOsfCells.setStatus("current")
if mibBuilder.loadTexts:
    cwacsEgrAal2InvalidOsfCells.setUnits("cells")
_CwacsEgrAal2InvalidParCells_Type = Counter32
_CwacsEgrAal2InvalidParCells_Object = MibTableColumn
cwacsEgrAal2InvalidParCells = _CwacsEgrAal2InvalidParCells_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 4, 1, 3),
    _CwacsEgrAal2InvalidParCells_Type()
)
cwacsEgrAal2InvalidParCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsEgrAal2InvalidParCells.setStatus("current")
if mibBuilder.loadTexts:
    cwacsEgrAal2InvalidParCells.setUnits("cells")
_CwacsAal2CpsSentPkts_Type = Counter32
_CwacsAal2CpsSentPkts_Object = MibTableColumn
cwacsAal2CpsSentPkts = _CwacsAal2CpsSentPkts_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 4, 1, 4),
    _CwacsAal2CpsSentPkts_Type()
)
cwacsAal2CpsSentPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsAal2CpsSentPkts.setStatus("current")
if mibBuilder.loadTexts:
    cwacsAal2CpsSentPkts.setUnits("packets")
_CwacsAal2CpsRcvdPkts_Type = Counter32
_CwacsAal2CpsRcvdPkts_Object = MibTableColumn
cwacsAal2CpsRcvdPkts = _CwacsAal2CpsRcvdPkts_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 4, 1, 5),
    _CwacsAal2CpsRcvdPkts_Type()
)
cwacsAal2CpsRcvdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsAal2CpsRcvdPkts.setStatus("current")
if mibBuilder.loadTexts:
    cwacsAal2CpsRcvdPkts.setUnits("packets")
_CwacsEgrAal2CpsInvalidCidPkts_Type = Counter32
_CwacsEgrAal2CpsInvalidCidPkts_Object = MibTableColumn
cwacsEgrAal2CpsInvalidCidPkts = _CwacsEgrAal2CpsInvalidCidPkts_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 4, 1, 6),
    _CwacsEgrAal2CpsInvalidCidPkts_Type()
)
cwacsEgrAal2CpsInvalidCidPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsEgrAal2CpsInvalidCidPkts.setStatus("current")
if mibBuilder.loadTexts:
    cwacsEgrAal2CpsInvalidCidPkts.setUnits("packets")
_CwacsCacPassedCalls_Type = Counter32
_CwacsCacPassedCalls_Object = MibTableColumn
cwacsCacPassedCalls = _CwacsCacPassedCalls_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 4, 1, 7),
    _CwacsCacPassedCalls_Type()
)
cwacsCacPassedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsCacPassedCalls.setStatus("current")
_CwacsCacRejectedCalls_Type = Counter32
_CwacsCacRejectedCalls_Object = MibTableColumn
cwacsCacRejectedCalls = _CwacsCacRejectedCalls_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 4, 1, 8),
    _CwacsCacRejectedCalls_Type()
)
cwacsCacRejectedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsCacRejectedCalls.setStatus("current")
_CwacsIngXmtOAM_Type = Counter32
_CwacsIngXmtOAM_Object = MibTableColumn
cwacsIngXmtOAM = _CwacsIngXmtOAM_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 4, 1, 9),
    _CwacsIngXmtOAM_Type()
)
cwacsIngXmtOAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsIngXmtOAM.setStatus("current")
if mibBuilder.loadTexts:
    cwacsIngXmtOAM.setUnits("cells")
_CwacsUsedConns_Type = Gauge32
_CwacsUsedConns_Object = MibTableColumn
cwacsUsedConns = _CwacsUsedConns_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 4, 1, 10),
    _CwacsUsedConns_Type()
)
cwacsUsedConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsUsedConns.setStatus("current")
_CwacsUtilizedCR_Type = Gauge32
_CwacsUtilizedCR_Object = MibTableColumn
cwacsUtilizedCR = _CwacsUtilizedCR_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 4, 1, 11),
    _CwacsUtilizedCR_Type()
)
cwacsUtilizedCR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsUtilizedCR.setStatus("current")
if mibBuilder.loadTexts:
    cwacsUtilizedCR.setUnits("cells per second")
_CwacsUsedVadConns_Type = Gauge32
_CwacsUsedVadConns_Object = MibTableColumn
cwacsUsedVadConns = _CwacsUsedVadConns_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 4, 1, 12),
    _CwacsUsedVadConns_Type()
)
cwacsUsedVadConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsUsedVadConns.setStatus("current")
_CwacsTotalCR_Type = Gauge32
_CwacsTotalCR_Object = MibTableColumn
cwacsTotalCR = _CwacsTotalCR_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 4, 1, 13),
    _CwacsTotalCR_Type()
)
cwacsTotalCR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsTotalCR.setStatus("current")
if mibBuilder.loadTexts:
    cwacsTotalCR.setUnits("cells per second")
_CwacsAisSuppressCount_Type = Counter32
_CwacsAisSuppressCount_Object = MibTableColumn
cwacsAisSuppressCount = _CwacsAisSuppressCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 4, 1, 14),
    _CwacsAisSuppressCount_Type()
)
cwacsAisSuppressCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsAisSuppressCount.setStatus("current")
_CwacsBearerPVCTable_Object = MibTable
cwacsBearerPVCTable = _CwacsBearerPVCTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cwacsBearerPVCTable.setStatus("current")
_CwacsBearerPVCEntry_Object = MibTableRow
cwacsBearerPVCEntry = _CwacsBearerPVCEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 5, 1)
)
cwacsBearerPVCEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WAN-ATM-CONN-MIB", "cwaChanVpi"),
    (0, "CISCO-WAN-ATM-CONN-MIB", "cwaChanVci"),
)
if mibBuilder.loadTexts:
    cwacsBearerPVCEntry.setStatus("current")


class _CwacsAvailableBearerPVCBWMin_Type(Gauge32):
    """Custom type cwacsAvailableBearerPVCBWMin based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CwacsAvailableBearerPVCBWMin_Type.__name__ = "Gauge32"
_CwacsAvailableBearerPVCBWMin_Object = MibTableColumn
cwacsAvailableBearerPVCBWMin = _CwacsAvailableBearerPVCBWMin_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 5, 1, 1),
    _CwacsAvailableBearerPVCBWMin_Type()
)
cwacsAvailableBearerPVCBWMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsAvailableBearerPVCBWMin.setStatus("current")
if mibBuilder.loadTexts:
    cwacsAvailableBearerPVCBWMin.setUnits("percentage")


class _CwacsAvailableBearerPVCBWMax_Type(Gauge32):
    """Custom type cwacsAvailableBearerPVCBWMax based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CwacsAvailableBearerPVCBWMax_Type.__name__ = "Gauge32"
_CwacsAvailableBearerPVCBWMax_Object = MibTableColumn
cwacsAvailableBearerPVCBWMax = _CwacsAvailableBearerPVCBWMax_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 5, 1, 2),
    _CwacsAvailableBearerPVCBWMax_Type()
)
cwacsAvailableBearerPVCBWMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsAvailableBearerPVCBWMax.setStatus("current")
if mibBuilder.loadTexts:
    cwacsAvailableBearerPVCBWMax.setUnits("percentage")


class _CwacsAvailableBearerPVCBWAvg_Type(Gauge32):
    """Custom type cwacsAvailableBearerPVCBWAvg based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CwacsAvailableBearerPVCBWAvg_Type.__name__ = "Gauge32"
_CwacsAvailableBearerPVCBWAvg_Object = MibTableColumn
cwacsAvailableBearerPVCBWAvg = _CwacsAvailableBearerPVCBWAvg_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 5, 1, 3),
    _CwacsAvailableBearerPVCBWAvg_Type()
)
cwacsAvailableBearerPVCBWAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsAvailableBearerPVCBWAvg.setStatus("current")
if mibBuilder.loadTexts:
    cwacsAvailableBearerPVCBWAvg.setUnits("percentage")
_CwacsBearerPVCSinceLastReset_Type = Unsigned32
_CwacsBearerPVCSinceLastReset_Object = MibTableColumn
cwacsBearerPVCSinceLastReset = _CwacsBearerPVCSinceLastReset_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 1, 1, 5, 1, 4),
    _CwacsBearerPVCSinceLastReset_Type()
)
cwacsBearerPVCSinceLastReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacsBearerPVCSinceLastReset.setStatus("current")
if mibBuilder.loadTexts:
    cwacsBearerPVCSinceLastReset.setUnits("seconds")
_CiscoWanAtmConnStatMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ciscoWanAtmConnStatMIBNotificationPrefix = _CiscoWanAtmConnStatMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 2)
)
_CiscoWanAtmConnStatMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoWanAtmConnStatMIBNotifications = _CiscoWanAtmConnStatMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 2, 0)
)
_CiscoWanAtmConnStatMIBConformance_ObjectIdentity = ObjectIdentity
ciscoWanAtmConnStatMIBConformance = _CiscoWanAtmConnStatMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 3)
)
_CiscoWanAtmConnStatMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoWanAtmConnStatMIBCompliances = _CiscoWanAtmConnStatMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 3, 1)
)
_CiscoWanAtmConnStatMIBGroups_ObjectIdentity = ObjectIdentity
ciscoWanAtmConnStatMIBGroups = _CiscoWanAtmConnStatMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 3, 2)
)
cwacsEntry.registerAugmentions(
    ("CISCO-WAN-ATM-CONN-STAT-MIB",
     "cwacsXEntry")
)
cwacsXEntry.setIndexNames(*cwacsEntry.getIndexNames())
cwacsEntry.registerAugmentions(
    ("CISCO-WAN-ATM-CONN-STAT-MIB",
     "cwacsExtStatsEntry")
)
cwacsExtStatsEntry.setIndexNames(*cwacsEntry.getIndexNames())

# Managed Objects groups

cwacsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 3, 2, 1)
)
cwacsGroup.setObjects(
      *(("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsIngRcvCLP0"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsIngRcvCLP1"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsIngXmtCLP0"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsIngXmtCLP1"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsIngCLP0CoSDiscard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsIngCLP1CoSDiscard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsIngCLP0UpcDiscard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsIngCLP1UpcDiscard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsIngCLP0UpcTagged"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsIngRcvEFCI0"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsIngRcvEFCI1"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsIngEFCI0Discard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsIngEFCI1Discard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsIngRcvOAM"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsIngOAMDiscard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsIngRcvRM"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsIngRMDiscard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsIngXmtFRm"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsIngXmtBRmFsRm"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsIngRcvEOF1"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsIngEOF1Discard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsIngACR"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsIngVCQueueDepth"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsEgrRcvCLP0"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsEgrRcvCLP1"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsEgrXmtCLP0"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsEgrXmtCLP1"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsEgrCLP0CoSDiscard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsEgrCLP1CoSDiscard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsEgrRcvEFCI0"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsEgrRcvEFCI1"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsEgrEFCI0Discard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsEgrEFCI1Discard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsEgrRcvOAM"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsEgrOAMDiscard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsEgrRcvRM"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsEgrRMDiscard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsEgrXmtFRm"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsEgrXmtBRmFsRm"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsEgrRcvEOF1"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsEgrEOF1Discard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsEgrACR"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsEgrVCQueueDepth"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsStatsClear"))
)
if mibBuilder.loadTexts:
    cwacsGroup.setStatus("deprecated")

cwaConnStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 3, 2, 2)
)
cwaConnStatsGroup.setObjects(
      *(("CISCO-WAN-ATM-CONN-STAT-MIB", "cwaConnStatsIngRcv"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwaConnStatsIngCLP0Discard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwaConnStatsIngCLP1Discard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwaConnStatsIngTotalDiscard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwaConnStatsEgrXmt"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwaConnStatsEgrCLP0Discard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwaConnStatsEgrCLP1Discard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwaConnStatsEgrTotalDiscard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwaConnStatsClear"))
)
if mibBuilder.loadTexts:
    cwaConnStatsGroup.setStatus("current")

cwacsGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 3, 2, 3)
)
cwacsGroup1.setObjects(
      *(("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsIngRcvCLP0"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsIngRcvCLP1"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsIngXmtCLP0"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsIngXmtCLP1"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsIngCLP0CoSDiscard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsIngCLP1CoSDiscard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsIngCLP0UpcDiscard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsIngCLP1UpcDiscard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsIngCLP0UpcTagged"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsIngRcvEFCI0"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsIngRcvEFCI1"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsIngEFCI0Discard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsIngEFCI1Discard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsIngRcvOAM"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsIngOAMDiscard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsIngRcvRM"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsIngRMDiscard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsIngXmtFRm"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsIngXmtBRmFsRm"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsIngRcvEOF1"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsIngEOF1Discard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsIngACR"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsIngVCQueueDepth"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsEgrRcvCLP0"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsEgrRcvCLP1"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsEgrXmtCLP0"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsEgrXmtCLP1"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsEgrCLP0CoSDiscard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsEgrCLP1CoSDiscard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsEgrRcvEFCI0"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsEgrRcvEFCI1"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsEgrEFCI0Discard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsEgrEFCI1Discard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsEgrRcvOAM"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsEgrOAMDiscard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsEgrRcvRM"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsEgrRMDiscard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsEgrXmtFRm"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsEgrXmtBRmFsRm"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsEgrRcvEOF1"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsEgrEOF1Discard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsEgrACR"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsEgrVCQueueDepth"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsStatsClear"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsHighIngRcvCLP0"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsHighIngRcvCLP1"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsHighIngXmtCLP0"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsHighIngXmtCLP1"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsHighIngCLP0CoSDiscard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsHighIngCLP1CoSDiscard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsHighIngCLP0UpcDiscard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsHighIngCLP1UpcDiscard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsHighIngCLP0UpcTagged"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsHighIngRcvEFCI0"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsHighIngRcvEFCI1"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsHighIngEFCI0Discard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsHighIngEFCI1Discard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsHighIngRcvEOF1"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsHighIngEOF1Discard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsHighEgrRcvCLP0"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsHighEgrRcvCLP1"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsHighEgrXmtCLP0"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsHighEgrXmtCLP1"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsHighEgrCLP0CoSDiscard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsHighEgrCLP1CoSDiscard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsHighEgrRcvEFCI0"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsHighEgrRcvEFCI1"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsHighEgrEFCI0Discard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsHighEgrEFCI1Discard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsHighEgrRcvEOF1"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsHighEgrEOF1Discard"))
)
if mibBuilder.loadTexts:
    cwacsGroup1.setStatus("current")

cwacsHCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 3, 2, 4)
)
cwacsHCGroup.setObjects(
      *(("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsHCIngRcvCLP0"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsHCIngRcvCLP1"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsHCIngXmtCLP0"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsHCIngXmtCLP1"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsHCIngCLP0CoSDiscard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsHCIngCLP1CoSDiscard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsHCIngCLP0UpcDiscard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsHCIngCLP1UpcDiscard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsHCIngCLP0UpcTagged"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsHCIngRcvEFCI0"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsHCIngRcvEFCI1"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsHCIngEFCI0Discard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsHCIngEFCI1Discard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsHCIngRcvEOF1"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsHCIngEOF1Discard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsHCEgrRcvCLP0"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsHCEgrRcvCLP1"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsHCEgrXmtCLP0"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsHCEgrXmtCLP1"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsHCEgrCLP0CoSDiscard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsHCEgrCLP1CoSDiscard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsHCEgrRcvEFCI0"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsHCEgrRcvEFCI1"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsHCEgrEFCI0Discard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsHCEgrEFCI1Discard"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsHCEgrRcvEOF1"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsHCEgrEOF1Discard"))
)
if mibBuilder.loadTexts:
    cwacsHCGroup.setStatus("current")

cwacsAal2Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 3, 2, 5)
)
cwacsAal2Group.setObjects(
      *(("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsEgrAal2HecErrors"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsEgrAal2InvalidOsfCells"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsEgrAal2InvalidParCells"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsAal2CpsSentPkts"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsAal2CpsRcvdPkts"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsEgrAal2CpsInvalidCidPkts"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsCacPassedCalls"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsCacRejectedCalls"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsIngXmtOAM"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsUsedConns"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsUtilizedCR"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsUsedVadConns"))
)
if mibBuilder.loadTexts:
    cwacsAal2Group.setStatus("deprecated")

cwacsAal2GroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 3, 2, 6)
)
cwacsAal2GroupRev1.setObjects(
      *(("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsEgrAal2HecErrors"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsEgrAal2InvalidOsfCells"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsEgrAal2InvalidParCells"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsAal2CpsSentPkts"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsAal2CpsRcvdPkts"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsEgrAal2CpsInvalidCidPkts"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsCacPassedCalls"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsCacRejectedCalls"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsIngXmtOAM"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsUsedConns"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsUtilizedCR"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsUsedVadConns"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsTotalCR"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsAisSuppressCount"))
)
if mibBuilder.loadTexts:
    cwacsAal2GroupRev1.setStatus("current")

cwacsBearerPVCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 3, 2, 7)
)
cwacsBearerPVCGroup.setObjects(
      *(("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsAvailableBearerPVCBWMin"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsAvailableBearerPVCBWMax"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsAvailableBearerPVCBWAvg"),
        ("CISCO-WAN-ATM-CONN-STAT-MIB", "cwacsBearerPVCSinceLastReset"))
)
if mibBuilder.loadTexts:
    cwacsBearerPVCGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoWanAtmConnStatMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoWanAtmConnStatMIBCompliance.setStatus(
        "deprecated"
    )

ciscoWanAtmConnStatMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoWanAtmConnStatMIBCompliance2.setStatus(
        "deprecated"
    )

ciscoWanAtmConnStatMIBCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoWanAtmConnStatMIBCompliance3.setStatus(
        "deprecated"
    )

ciscoWanAtmConnStatMIBCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 3, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoWanAtmConnStatMIBCompliance4.setStatus(
        "deprecated"
    )

ciscoWanAtmConnStatMIBCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 3, 1, 5)
)
if mibBuilder.loadTexts:
    ciscoWanAtmConnStatMIBCompliance5.setStatus(
        "deprecated"
    )

ciscoWanAtmConnStatMIBCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 2, 3, 1, 6)
)
if mibBuilder.loadTexts:
    ciscoWanAtmConnStatMIBCompliance6.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WAN-ATM-CONN-STAT-MIB",
    **{"ciscoWanAtmConnStatMIB": ciscoWanAtmConnStatMIB,
       "ciscoWanAtmConnStatMIBObjects": ciscoWanAtmConnStatMIBObjects,
       "cwacs": cwacs,
       "cwacsTable": cwacsTable,
       "cwacsEntry": cwacsEntry,
       "cwacsIngRcvCLP0": cwacsIngRcvCLP0,
       "cwacsIngRcvCLP1": cwacsIngRcvCLP1,
       "cwacsIngXmtCLP0": cwacsIngXmtCLP0,
       "cwacsIngXmtCLP1": cwacsIngXmtCLP1,
       "cwacsIngCLP0CoSDiscard": cwacsIngCLP0CoSDiscard,
       "cwacsIngCLP1CoSDiscard": cwacsIngCLP1CoSDiscard,
       "cwacsIngCLP0UpcDiscard": cwacsIngCLP0UpcDiscard,
       "cwacsIngCLP1UpcDiscard": cwacsIngCLP1UpcDiscard,
       "cwacsIngCLP0UpcTagged": cwacsIngCLP0UpcTagged,
       "cwacsIngRcvEFCI0": cwacsIngRcvEFCI0,
       "cwacsIngRcvEFCI1": cwacsIngRcvEFCI1,
       "cwacsIngEFCI0Discard": cwacsIngEFCI0Discard,
       "cwacsIngEFCI1Discard": cwacsIngEFCI1Discard,
       "cwacsIngRcvOAM": cwacsIngRcvOAM,
       "cwacsIngOAMDiscard": cwacsIngOAMDiscard,
       "cwacsIngRcvRM": cwacsIngRcvRM,
       "cwacsIngRMDiscard": cwacsIngRMDiscard,
       "cwacsIngXmtFRm": cwacsIngXmtFRm,
       "cwacsIngXmtBRmFsRm": cwacsIngXmtBRmFsRm,
       "cwacsIngRcvEOF1": cwacsIngRcvEOF1,
       "cwacsIngEOF1Discard": cwacsIngEOF1Discard,
       "cwacsIngACR": cwacsIngACR,
       "cwacsIngVCQueueDepth": cwacsIngVCQueueDepth,
       "cwacsEgrRcvCLP0": cwacsEgrRcvCLP0,
       "cwacsEgrRcvCLP1": cwacsEgrRcvCLP1,
       "cwacsEgrXmtCLP0": cwacsEgrXmtCLP0,
       "cwacsEgrXmtCLP1": cwacsEgrXmtCLP1,
       "cwacsEgrCLP0CoSDiscard": cwacsEgrCLP0CoSDiscard,
       "cwacsEgrCLP1CoSDiscard": cwacsEgrCLP1CoSDiscard,
       "cwacsEgrRcvEFCI0": cwacsEgrRcvEFCI0,
       "cwacsEgrRcvEFCI1": cwacsEgrRcvEFCI1,
       "cwacsEgrEFCI0Discard": cwacsEgrEFCI0Discard,
       "cwacsEgrEFCI1Discard": cwacsEgrEFCI1Discard,
       "cwacsEgrRcvOAM": cwacsEgrRcvOAM,
       "cwacsEgrOAMDiscard": cwacsEgrOAMDiscard,
       "cwacsEgrRcvRM": cwacsEgrRcvRM,
       "cwacsEgrRMDiscard": cwacsEgrRMDiscard,
       "cwacsEgrXmtFRm": cwacsEgrXmtFRm,
       "cwacsEgrXmtBRmFsRm": cwacsEgrXmtBRmFsRm,
       "cwacsEgrRcvEOF1": cwacsEgrRcvEOF1,
       "cwacsEgrEOF1Discard": cwacsEgrEOF1Discard,
       "cwacsEgrACR": cwacsEgrACR,
       "cwacsEgrVCQueueDepth": cwacsEgrVCQueueDepth,
       "cwacsStatsClear": cwacsStatsClear,
       "cwacsHighIngRcvCLP0": cwacsHighIngRcvCLP0,
       "cwacsHighIngRcvCLP1": cwacsHighIngRcvCLP1,
       "cwacsHighIngXmtCLP0": cwacsHighIngXmtCLP0,
       "cwacsHighIngXmtCLP1": cwacsHighIngXmtCLP1,
       "cwacsHighIngCLP0CoSDiscard": cwacsHighIngCLP0CoSDiscard,
       "cwacsHighIngCLP1CoSDiscard": cwacsHighIngCLP1CoSDiscard,
       "cwacsHighIngCLP0UpcDiscard": cwacsHighIngCLP0UpcDiscard,
       "cwacsHighIngCLP1UpcDiscard": cwacsHighIngCLP1UpcDiscard,
       "cwacsHighIngCLP0UpcTagged": cwacsHighIngCLP0UpcTagged,
       "cwacsHighIngRcvEFCI0": cwacsHighIngRcvEFCI0,
       "cwacsHighIngRcvEFCI1": cwacsHighIngRcvEFCI1,
       "cwacsHighIngEFCI0Discard": cwacsHighIngEFCI0Discard,
       "cwacsHighIngEFCI1Discard": cwacsHighIngEFCI1Discard,
       "cwacsHighIngRcvEOF1": cwacsHighIngRcvEOF1,
       "cwacsHighIngEOF1Discard": cwacsHighIngEOF1Discard,
       "cwacsHighEgrRcvCLP0": cwacsHighEgrRcvCLP0,
       "cwacsHighEgrRcvCLP1": cwacsHighEgrRcvCLP1,
       "cwacsHighEgrXmtCLP0": cwacsHighEgrXmtCLP0,
       "cwacsHighEgrXmtCLP1": cwacsHighEgrXmtCLP1,
       "cwacsHighEgrCLP0CoSDiscard": cwacsHighEgrCLP0CoSDiscard,
       "cwacsHighEgrCLP1CoSDiscard": cwacsHighEgrCLP1CoSDiscard,
       "cwacsHighEgrRcvEFCI0": cwacsHighEgrRcvEFCI0,
       "cwacsHighEgrRcvEFCI1": cwacsHighEgrRcvEFCI1,
       "cwacsHighEgrEFCI0Discard": cwacsHighEgrEFCI0Discard,
       "cwacsHighEgrEFCI1Discard": cwacsHighEgrEFCI1Discard,
       "cwacsHighEgrRcvEOF1": cwacsHighEgrRcvEOF1,
       "cwacsHighEgrEOF1Discard": cwacsHighEgrEOF1Discard,
       "cwacsXTable": cwacsXTable,
       "cwacsXEntry": cwacsXEntry,
       "cwacsHCIngRcvCLP0": cwacsHCIngRcvCLP0,
       "cwacsHCIngRcvCLP1": cwacsHCIngRcvCLP1,
       "cwacsHCIngXmtCLP0": cwacsHCIngXmtCLP0,
       "cwacsHCIngXmtCLP1": cwacsHCIngXmtCLP1,
       "cwacsHCIngCLP0CoSDiscard": cwacsHCIngCLP0CoSDiscard,
       "cwacsHCIngCLP1CoSDiscard": cwacsHCIngCLP1CoSDiscard,
       "cwacsHCIngCLP0UpcDiscard": cwacsHCIngCLP0UpcDiscard,
       "cwacsHCIngCLP1UpcDiscard": cwacsHCIngCLP1UpcDiscard,
       "cwacsHCIngCLP0UpcTagged": cwacsHCIngCLP0UpcTagged,
       "cwacsHCIngRcvEFCI0": cwacsHCIngRcvEFCI0,
       "cwacsHCIngRcvEFCI1": cwacsHCIngRcvEFCI1,
       "cwacsHCIngEFCI0Discard": cwacsHCIngEFCI0Discard,
       "cwacsHCIngEFCI1Discard": cwacsHCIngEFCI1Discard,
       "cwacsHCIngRcvEOF1": cwacsHCIngRcvEOF1,
       "cwacsHCIngEOF1Discard": cwacsHCIngEOF1Discard,
       "cwacsHCEgrRcvCLP0": cwacsHCEgrRcvCLP0,
       "cwacsHCEgrRcvCLP1": cwacsHCEgrRcvCLP1,
       "cwacsHCEgrXmtCLP0": cwacsHCEgrXmtCLP0,
       "cwacsHCEgrXmtCLP1": cwacsHCEgrXmtCLP1,
       "cwacsHCEgrCLP0CoSDiscard": cwacsHCEgrCLP0CoSDiscard,
       "cwacsHCEgrCLP1CoSDiscard": cwacsHCEgrCLP1CoSDiscard,
       "cwacsHCEgrRcvEFCI0": cwacsHCEgrRcvEFCI0,
       "cwacsHCEgrRcvEFCI1": cwacsHCEgrRcvEFCI1,
       "cwacsHCEgrEFCI0Discard": cwacsHCEgrEFCI0Discard,
       "cwacsHCEgrEFCI1Discard": cwacsHCEgrEFCI1Discard,
       "cwacsHCEgrRcvEOF1": cwacsHCEgrRcvEOF1,
       "cwacsHCEgrEOF1Discard": cwacsHCEgrEOF1Discard,
       "cwaConnStatsTable": cwaConnStatsTable,
       "cwaConnStatsEntry": cwaConnStatsEntry,
       "cwaConnStatsIngRcv": cwaConnStatsIngRcv,
       "cwaConnStatsIngCLP0Discard": cwaConnStatsIngCLP0Discard,
       "cwaConnStatsIngCLP1Discard": cwaConnStatsIngCLP1Discard,
       "cwaConnStatsIngTotalDiscard": cwaConnStatsIngTotalDiscard,
       "cwaConnStatsEgrXmt": cwaConnStatsEgrXmt,
       "cwaConnStatsEgrCLP0Discard": cwaConnStatsEgrCLP0Discard,
       "cwaConnStatsEgrCLP1Discard": cwaConnStatsEgrCLP1Discard,
       "cwaConnStatsEgrTotalDiscard": cwaConnStatsEgrTotalDiscard,
       "cwaConnStatsClear": cwaConnStatsClear,
       "cwacsExtStatsTable": cwacsExtStatsTable,
       "cwacsExtStatsEntry": cwacsExtStatsEntry,
       "cwacsEgrAal2HecErrors": cwacsEgrAal2HecErrors,
       "cwacsEgrAal2InvalidOsfCells": cwacsEgrAal2InvalidOsfCells,
       "cwacsEgrAal2InvalidParCells": cwacsEgrAal2InvalidParCells,
       "cwacsAal2CpsSentPkts": cwacsAal2CpsSentPkts,
       "cwacsAal2CpsRcvdPkts": cwacsAal2CpsRcvdPkts,
       "cwacsEgrAal2CpsInvalidCidPkts": cwacsEgrAal2CpsInvalidCidPkts,
       "cwacsCacPassedCalls": cwacsCacPassedCalls,
       "cwacsCacRejectedCalls": cwacsCacRejectedCalls,
       "cwacsIngXmtOAM": cwacsIngXmtOAM,
       "cwacsUsedConns": cwacsUsedConns,
       "cwacsUtilizedCR": cwacsUtilizedCR,
       "cwacsUsedVadConns": cwacsUsedVadConns,
       "cwacsTotalCR": cwacsTotalCR,
       "cwacsAisSuppressCount": cwacsAisSuppressCount,
       "cwacsBearerPVCTable": cwacsBearerPVCTable,
       "cwacsBearerPVCEntry": cwacsBearerPVCEntry,
       "cwacsAvailableBearerPVCBWMin": cwacsAvailableBearerPVCBWMin,
       "cwacsAvailableBearerPVCBWMax": cwacsAvailableBearerPVCBWMax,
       "cwacsAvailableBearerPVCBWAvg": cwacsAvailableBearerPVCBWAvg,
       "cwacsBearerPVCSinceLastReset": cwacsBearerPVCSinceLastReset,
       "ciscoWanAtmConnStatMIBNotificationPrefix": ciscoWanAtmConnStatMIBNotificationPrefix,
       "ciscoWanAtmConnStatMIBNotifications": ciscoWanAtmConnStatMIBNotifications,
       "ciscoWanAtmConnStatMIBConformance": ciscoWanAtmConnStatMIBConformance,
       "ciscoWanAtmConnStatMIBCompliances": ciscoWanAtmConnStatMIBCompliances,
       "ciscoWanAtmConnStatMIBCompliance": ciscoWanAtmConnStatMIBCompliance,
       "ciscoWanAtmConnStatMIBCompliance2": ciscoWanAtmConnStatMIBCompliance2,
       "ciscoWanAtmConnStatMIBCompliance3": ciscoWanAtmConnStatMIBCompliance3,
       "ciscoWanAtmConnStatMIBCompliance4": ciscoWanAtmConnStatMIBCompliance4,
       "ciscoWanAtmConnStatMIBCompliance5": ciscoWanAtmConnStatMIBCompliance5,
       "ciscoWanAtmConnStatMIBCompliance6": ciscoWanAtmConnStatMIBCompliance6,
       "ciscoWanAtmConnStatMIBGroups": ciscoWanAtmConnStatMIBGroups,
       "cwacsGroup": cwacsGroup,
       "cwaConnStatsGroup": cwaConnStatsGroup,
       "cwacsGroup1": cwacsGroup1,
       "cwacsHCGroup": cwacsHCGroup,
       "cwacsAal2Group": cwacsAal2Group,
       "cwacsAal2GroupRev1": cwacsAal2GroupRev1,
       "cwacsBearerPVCGroup": cwacsBearerPVCGroup}
)
