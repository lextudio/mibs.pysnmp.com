# SNMP MIB module (STN-VIMUX-MPLS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/STN-VIMUX-MPLS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:20 2024
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

(stnRouterVimuxMpls,) = mibBuilder.importSymbols(
    "STN-ROUTER-MIB",
    "stnRouterVimuxMpls")


# MODULE-IDENTITY

stnVimuxMpls = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 8, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_StnVimuxMplsObjects_ObjectIdentity = ObjectIdentity
stnVimuxMplsObjects = _StnVimuxMplsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 8, 1, 1)
)
_StnVimuxMplsL2Table_Object = MibTable
stnVimuxMplsL2Table = _StnVimuxMplsL2Table_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 8, 1, 1, 1)
)
if mibBuilder.loadTexts:
    stnVimuxMplsL2Table.setStatus("current")
_StnVimuxMplsL2Entry_Object = MibTableRow
stnVimuxMplsL2Entry = _StnVimuxMplsL2Entry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 8, 1, 1, 1, 1)
)
stnVimuxMplsL2Entry.setIndexNames(
    (0, "STN-VIMUX-MPLS-MIB", "stnVimuxMplsL2IfIndex"),
)
if mibBuilder.loadTexts:
    stnVimuxMplsL2Entry.setStatus("current")
_StnVimuxMplsL2IfIndex_Type = InterfaceIndex
_StnVimuxMplsL2IfIndex_Object = MibTableColumn
stnVimuxMplsL2IfIndex = _StnVimuxMplsL2IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 8, 1, 1, 1, 1, 1),
    _StnVimuxMplsL2IfIndex_Type()
)
stnVimuxMplsL2IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVimuxMplsL2IfIndex.setStatus("current")
_StnVimuxMplsL2ViId_Type = Integer32
_StnVimuxMplsL2ViId_Object = MibTableColumn
stnVimuxMplsL2ViId = _StnVimuxMplsL2ViId_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 8, 1, 1, 1, 1, 2),
    _StnVimuxMplsL2ViId_Type()
)
stnVimuxMplsL2ViId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVimuxMplsL2ViId.setStatus("current")


class _StnVimuxMplsL2Name_Type(DisplayString):
    """Custom type stnVimuxMplsL2Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_StnVimuxMplsL2Name_Type.__name__ = "DisplayString"
_StnVimuxMplsL2Name_Object = MibTableColumn
stnVimuxMplsL2Name = _StnVimuxMplsL2Name_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 8, 1, 1, 1, 1, 3),
    _StnVimuxMplsL2Name_Type()
)
stnVimuxMplsL2Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVimuxMplsL2Name.setStatus("current")


class _StnVimuxMplsL2State_Type(Integer32):
    """Custom type stnVimuxMplsL2State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_StnVimuxMplsL2State_Type.__name__ = "Integer32"
_StnVimuxMplsL2State_Object = MibTableColumn
stnVimuxMplsL2State = _StnVimuxMplsL2State_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 8, 1, 1, 1, 1, 4),
    _StnVimuxMplsL2State_Type()
)
stnVimuxMplsL2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVimuxMplsL2State.setStatus("current")
_StnVimuxMplsL2RegisteredLowerLinks_Type = Gauge32
_StnVimuxMplsL2RegisteredLowerLinks_Object = MibTableColumn
stnVimuxMplsL2RegisteredLowerLinks = _StnVimuxMplsL2RegisteredLowerLinks_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 8, 1, 1, 1, 1, 5),
    _StnVimuxMplsL2RegisteredLowerLinks_Type()
)
stnVimuxMplsL2RegisteredLowerLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVimuxMplsL2RegisteredLowerLinks.setStatus("current")
_StnVimuxMplsL2ActiveLowerLinks_Type = Gauge32
_StnVimuxMplsL2ActiveLowerLinks_Object = MibTableColumn
stnVimuxMplsL2ActiveLowerLinks = _StnVimuxMplsL2ActiveLowerLinks_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 8, 1, 1, 1, 1, 6),
    _StnVimuxMplsL2ActiveLowerLinks_Type()
)
stnVimuxMplsL2ActiveLowerLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVimuxMplsL2ActiveLowerLinks.setStatus("current")
_StnVimuxMplsL2InvalidInLabelPackets_Type = Integer32
_StnVimuxMplsL2InvalidInLabelPackets_Object = MibTableColumn
stnVimuxMplsL2InvalidInLabelPackets = _StnVimuxMplsL2InvalidInLabelPackets_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 8, 1, 1, 1, 1, 7),
    _StnVimuxMplsL2InvalidInLabelPackets_Type()
)
stnVimuxMplsL2InvalidInLabelPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVimuxMplsL2InvalidInLabelPackets.setStatus("current")
_StnVimuxMplsL2InvalidOutLabelPackets_Type = Integer32
_StnVimuxMplsL2InvalidOutLabelPackets_Object = MibTableColumn
stnVimuxMplsL2InvalidOutLabelPackets = _StnVimuxMplsL2InvalidOutLabelPackets_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 8, 1, 1, 1, 1, 8),
    _StnVimuxMplsL2InvalidOutLabelPackets_Type()
)
stnVimuxMplsL2InvalidOutLabelPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVimuxMplsL2InvalidOutLabelPackets.setStatus("current")
_StnVimuxMplsLinkTable_Object = MibTable
stnVimuxMplsLinkTable = _StnVimuxMplsLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 8, 1, 1, 2)
)
if mibBuilder.loadTexts:
    stnVimuxMplsLinkTable.setStatus("current")
_StnVimuxMplsLinkEntry_Object = MibTableRow
stnVimuxMplsLinkEntry = _StnVimuxMplsLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 8, 1, 1, 2, 1)
)
stnVimuxMplsLinkEntry.setIndexNames(
    (0, "STN-VIMUX-MPLS-MIB", "stnVimuxMplsLinkVimuxMplsIfIndex"),
    (0, "STN-VIMUX-MPLS-MIB", "stnVimuxMplsLinkIfIndex"),
)
if mibBuilder.loadTexts:
    stnVimuxMplsLinkEntry.setStatus("current")
_StnVimuxMplsLinkVimuxMplsIfIndex_Type = InterfaceIndex
_StnVimuxMplsLinkVimuxMplsIfIndex_Object = MibTableColumn
stnVimuxMplsLinkVimuxMplsIfIndex = _StnVimuxMplsLinkVimuxMplsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 8, 1, 1, 2, 1, 1),
    _StnVimuxMplsLinkVimuxMplsIfIndex_Type()
)
stnVimuxMplsLinkVimuxMplsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVimuxMplsLinkVimuxMplsIfIndex.setStatus("current")
_StnVimuxMplsLinkIfIndex_Type = InterfaceIndex
_StnVimuxMplsLinkIfIndex_Object = MibTableColumn
stnVimuxMplsLinkIfIndex = _StnVimuxMplsLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 8, 1, 1, 2, 1, 2),
    _StnVimuxMplsLinkIfIndex_Type()
)
stnVimuxMplsLinkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVimuxMplsLinkIfIndex.setStatus("current")
_StnVimuxMplsLinkPhysIfIndex_Type = InterfaceIndex
_StnVimuxMplsLinkPhysIfIndex_Object = MibTableColumn
stnVimuxMplsLinkPhysIfIndex = _StnVimuxMplsLinkPhysIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 8, 1, 1, 2, 1, 3),
    _StnVimuxMplsLinkPhysIfIndex_Type()
)
stnVimuxMplsLinkPhysIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVimuxMplsLinkPhysIfIndex.setStatus("current")
_StnVimuxMplsLinkVpi_Type = Integer32
_StnVimuxMplsLinkVpi_Object = MibTableColumn
stnVimuxMplsLinkVpi = _StnVimuxMplsLinkVpi_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 8, 1, 1, 2, 1, 4),
    _StnVimuxMplsLinkVpi_Type()
)
stnVimuxMplsLinkVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVimuxMplsLinkVpi.setStatus("current")
_StnVimuxMplsLinkVci_Type = Integer32
_StnVimuxMplsLinkVci_Object = MibTableColumn
stnVimuxMplsLinkVci = _StnVimuxMplsLinkVci_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 8, 1, 1, 2, 1, 5),
    _StnVimuxMplsLinkVci_Type()
)
stnVimuxMplsLinkVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVimuxMplsLinkVci.setStatus("current")
_StnVimuxMplsIncomingLabelTable_Object = MibTable
stnVimuxMplsIncomingLabelTable = _StnVimuxMplsIncomingLabelTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 8, 1, 1, 3)
)
if mibBuilder.loadTexts:
    stnVimuxMplsIncomingLabelTable.setStatus("current")
_StnVimuxMplsIncomingLabel_Object = MibTableRow
stnVimuxMplsIncomingLabel = _StnVimuxMplsIncomingLabel_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 8, 1, 1, 3, 1)
)
stnVimuxMplsIncomingLabel.setIndexNames(
    (0, "STN-VIMUX-MPLS-MIB", "stnVimuxMplsIncomingLabelValue"),
)
if mibBuilder.loadTexts:
    stnVimuxMplsIncomingLabel.setStatus("current")
_StnVimuxMplsIncomingLabelIfIndex_Type = InterfaceIndex
_StnVimuxMplsIncomingLabelIfIndex_Object = MibTableColumn
stnVimuxMplsIncomingLabelIfIndex = _StnVimuxMplsIncomingLabelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 8, 1, 1, 3, 1, 1),
    _StnVimuxMplsIncomingLabelIfIndex_Type()
)
stnVimuxMplsIncomingLabelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVimuxMplsIncomingLabelIfIndex.setStatus("current")
_StnVimuxMplsIncomingLabelValue_Type = Integer32
_StnVimuxMplsIncomingLabelValue_Object = MibTableColumn
stnVimuxMplsIncomingLabelValue = _StnVimuxMplsIncomingLabelValue_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 8, 1, 1, 3, 1, 2),
    _StnVimuxMplsIncomingLabelValue_Type()
)
stnVimuxMplsIncomingLabelValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVimuxMplsIncomingLabelValue.setStatus("current")


class _StnVimuxMplsIncomingLabelAction_Type(Integer32):
    """Custom type stnVimuxMplsIncomingLabelAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pop", 1),
          ("replace", 2))
    )


_StnVimuxMplsIncomingLabelAction_Type.__name__ = "Integer32"
_StnVimuxMplsIncomingLabelAction_Object = MibTableColumn
stnVimuxMplsIncomingLabelAction = _StnVimuxMplsIncomingLabelAction_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 8, 1, 1, 3, 1, 3),
    _StnVimuxMplsIncomingLabelAction_Type()
)
stnVimuxMplsIncomingLabelAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVimuxMplsIncomingLabelAction.setStatus("current")
_StnVimuxMplsIncomingLabelToPush1_Type = Integer32
_StnVimuxMplsIncomingLabelToPush1_Object = MibTableColumn
stnVimuxMplsIncomingLabelToPush1 = _StnVimuxMplsIncomingLabelToPush1_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 8, 1, 1, 3, 1, 4),
    _StnVimuxMplsIncomingLabelToPush1_Type()
)
stnVimuxMplsIncomingLabelToPush1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVimuxMplsIncomingLabelToPush1.setStatus("current")
_StnVimuxMplsIncomingLabelToPush2_Type = Integer32
_StnVimuxMplsIncomingLabelToPush2_Object = MibTableColumn
stnVimuxMplsIncomingLabelToPush2 = _StnVimuxMplsIncomingLabelToPush2_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 8, 1, 1, 3, 1, 5),
    _StnVimuxMplsIncomingLabelToPush2_Type()
)
stnVimuxMplsIncomingLabelToPush2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVimuxMplsIncomingLabelToPush2.setStatus("current")
_StnVimuxMplsIncomingLabelToPush3_Type = Integer32
_StnVimuxMplsIncomingLabelToPush3_Object = MibTableColumn
stnVimuxMplsIncomingLabelToPush3 = _StnVimuxMplsIncomingLabelToPush3_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 8, 1, 1, 3, 1, 6),
    _StnVimuxMplsIncomingLabelToPush3_Type()
)
stnVimuxMplsIncomingLabelToPush3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVimuxMplsIncomingLabelToPush3.setStatus("current")
_StnVimuxMplsIncomingLabelToPush4_Type = Integer32
_StnVimuxMplsIncomingLabelToPush4_Object = MibTableColumn
stnVimuxMplsIncomingLabelToPush4 = _StnVimuxMplsIncomingLabelToPush4_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 8, 1, 1, 3, 1, 7),
    _StnVimuxMplsIncomingLabelToPush4_Type()
)
stnVimuxMplsIncomingLabelToPush4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVimuxMplsIncomingLabelToPush4.setStatus("current")
_StnVimuxMplsIncomingLabelNextVimuxMplsIfIndex_Type = InterfaceIndex
_StnVimuxMplsIncomingLabelNextVimuxMplsIfIndex_Object = MibTableColumn
stnVimuxMplsIncomingLabelNextVimuxMplsIfIndex = _StnVimuxMplsIncomingLabelNextVimuxMplsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 8, 1, 1, 3, 1, 8),
    _StnVimuxMplsIncomingLabelNextVimuxMplsIfIndex_Type()
)
stnVimuxMplsIncomingLabelNextVimuxMplsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVimuxMplsIncomingLabelNextVimuxMplsIfIndex.setStatus("current")
_StnVimuxMplsIncomingLabelTtl_Type = Integer32
_StnVimuxMplsIncomingLabelTtl_Object = MibTableColumn
stnVimuxMplsIncomingLabelTtl = _StnVimuxMplsIncomingLabelTtl_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 8, 1, 1, 3, 1, 9),
    _StnVimuxMplsIncomingLabelTtl_Type()
)
stnVimuxMplsIncomingLabelTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVimuxMplsIncomingLabelTtl.setStatus("current")
_StnVimuxMplsIncomingLabelReceivedPackets_Type = Integer32
_StnVimuxMplsIncomingLabelReceivedPackets_Object = MibTableColumn
stnVimuxMplsIncomingLabelReceivedPackets = _StnVimuxMplsIncomingLabelReceivedPackets_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 8, 1, 1, 3, 1, 10),
    _StnVimuxMplsIncomingLabelReceivedPackets_Type()
)
stnVimuxMplsIncomingLabelReceivedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVimuxMplsIncomingLabelReceivedPackets.setStatus("current")
_StnVimuxMplsIncomingLabelDroppedPackets_Type = Integer32
_StnVimuxMplsIncomingLabelDroppedPackets_Object = MibTableColumn
stnVimuxMplsIncomingLabelDroppedPackets = _StnVimuxMplsIncomingLabelDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 8, 1, 1, 3, 1, 11),
    _StnVimuxMplsIncomingLabelDroppedPackets_Type()
)
stnVimuxMplsIncomingLabelDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVimuxMplsIncomingLabelDroppedPackets.setStatus("current")
_StnVimuxMplsOutgoingLabelTable_Object = MibTable
stnVimuxMplsOutgoingLabelTable = _StnVimuxMplsOutgoingLabelTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 8, 1, 1, 4)
)
if mibBuilder.loadTexts:
    stnVimuxMplsOutgoingLabelTable.setStatus("current")
_StnVimuxMplsOutgoingLabel_Object = MibTableRow
stnVimuxMplsOutgoingLabel = _StnVimuxMplsOutgoingLabel_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 8, 1, 1, 4, 1)
)
stnVimuxMplsOutgoingLabel.setIndexNames(
    (0, "STN-VIMUX-MPLS-MIB", "stnVimuxMplsOutgoingLabelValue"),
)
if mibBuilder.loadTexts:
    stnVimuxMplsOutgoingLabel.setStatus("current")
_StnVimuxMplsOutgoingLabelIfIndex_Type = InterfaceIndex
_StnVimuxMplsOutgoingLabelIfIndex_Object = MibTableColumn
stnVimuxMplsOutgoingLabelIfIndex = _StnVimuxMplsOutgoingLabelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 8, 1, 1, 4, 1, 1),
    _StnVimuxMplsOutgoingLabelIfIndex_Type()
)
stnVimuxMplsOutgoingLabelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVimuxMplsOutgoingLabelIfIndex.setStatus("current")
_StnVimuxMplsOutgoingLabelValue_Type = Integer32
_StnVimuxMplsOutgoingLabelValue_Object = MibTableColumn
stnVimuxMplsOutgoingLabelValue = _StnVimuxMplsOutgoingLabelValue_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 8, 1, 1, 4, 1, 2),
    _StnVimuxMplsOutgoingLabelValue_Type()
)
stnVimuxMplsOutgoingLabelValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVimuxMplsOutgoingLabelValue.setStatus("current")
_StnVimuxMplsOutgoingLabelOutgoingIfIndex_Type = InterfaceIndex
_StnVimuxMplsOutgoingLabelOutgoingIfIndex_Object = MibTableColumn
stnVimuxMplsOutgoingLabelOutgoingIfIndex = _StnVimuxMplsOutgoingLabelOutgoingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 8, 1, 1, 4, 1, 3),
    _StnVimuxMplsOutgoingLabelOutgoingIfIndex_Type()
)
stnVimuxMplsOutgoingLabelOutgoingIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVimuxMplsOutgoingLabelOutgoingIfIndex.setStatus("current")
_StnVimuxMplsOutgoingLabelNexthop_Type = IpAddress
_StnVimuxMplsOutgoingLabelNexthop_Object = MibTableColumn
stnVimuxMplsOutgoingLabelNexthop = _StnVimuxMplsOutgoingLabelNexthop_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 8, 1, 1, 4, 1, 4),
    _StnVimuxMplsOutgoingLabelNexthop_Type()
)
stnVimuxMplsOutgoingLabelNexthop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVimuxMplsOutgoingLabelNexthop.setStatus("current")
_StnVimuxMplsOutgoingLabelSentPackets_Type = Integer32
_StnVimuxMplsOutgoingLabelSentPackets_Object = MibTableColumn
stnVimuxMplsOutgoingLabelSentPackets = _StnVimuxMplsOutgoingLabelSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 8, 1, 1, 4, 1, 5),
    _StnVimuxMplsOutgoingLabelSentPackets_Type()
)
stnVimuxMplsOutgoingLabelSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVimuxMplsOutgoingLabelSentPackets.setStatus("current")
_StnVimuxMplsOutgoingLabelDroppedPackets_Type = Integer32
_StnVimuxMplsOutgoingLabelDroppedPackets_Object = MibTableColumn
stnVimuxMplsOutgoingLabelDroppedPackets = _StnVimuxMplsOutgoingLabelDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 8, 1, 1, 4, 1, 6),
    _StnVimuxMplsOutgoingLabelDroppedPackets_Type()
)
stnVimuxMplsOutgoingLabelDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVimuxMplsOutgoingLabelDroppedPackets.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STN-VIMUX-MPLS-MIB",
    **{"stnVimuxMpls": stnVimuxMpls,
       "stnVimuxMplsObjects": stnVimuxMplsObjects,
       "stnVimuxMplsL2Table": stnVimuxMplsL2Table,
       "stnVimuxMplsL2Entry": stnVimuxMplsL2Entry,
       "stnVimuxMplsL2IfIndex": stnVimuxMplsL2IfIndex,
       "stnVimuxMplsL2ViId": stnVimuxMplsL2ViId,
       "stnVimuxMplsL2Name": stnVimuxMplsL2Name,
       "stnVimuxMplsL2State": stnVimuxMplsL2State,
       "stnVimuxMplsL2RegisteredLowerLinks": stnVimuxMplsL2RegisteredLowerLinks,
       "stnVimuxMplsL2ActiveLowerLinks": stnVimuxMplsL2ActiveLowerLinks,
       "stnVimuxMplsL2InvalidInLabelPackets": stnVimuxMplsL2InvalidInLabelPackets,
       "stnVimuxMplsL2InvalidOutLabelPackets": stnVimuxMplsL2InvalidOutLabelPackets,
       "stnVimuxMplsLinkTable": stnVimuxMplsLinkTable,
       "stnVimuxMplsLinkEntry": stnVimuxMplsLinkEntry,
       "stnVimuxMplsLinkVimuxMplsIfIndex": stnVimuxMplsLinkVimuxMplsIfIndex,
       "stnVimuxMplsLinkIfIndex": stnVimuxMplsLinkIfIndex,
       "stnVimuxMplsLinkPhysIfIndex": stnVimuxMplsLinkPhysIfIndex,
       "stnVimuxMplsLinkVpi": stnVimuxMplsLinkVpi,
       "stnVimuxMplsLinkVci": stnVimuxMplsLinkVci,
       "stnVimuxMplsIncomingLabelTable": stnVimuxMplsIncomingLabelTable,
       "stnVimuxMplsIncomingLabel": stnVimuxMplsIncomingLabel,
       "stnVimuxMplsIncomingLabelIfIndex": stnVimuxMplsIncomingLabelIfIndex,
       "stnVimuxMplsIncomingLabelValue": stnVimuxMplsIncomingLabelValue,
       "stnVimuxMplsIncomingLabelAction": stnVimuxMplsIncomingLabelAction,
       "stnVimuxMplsIncomingLabelToPush1": stnVimuxMplsIncomingLabelToPush1,
       "stnVimuxMplsIncomingLabelToPush2": stnVimuxMplsIncomingLabelToPush2,
       "stnVimuxMplsIncomingLabelToPush3": stnVimuxMplsIncomingLabelToPush3,
       "stnVimuxMplsIncomingLabelToPush4": stnVimuxMplsIncomingLabelToPush4,
       "stnVimuxMplsIncomingLabelNextVimuxMplsIfIndex": stnVimuxMplsIncomingLabelNextVimuxMplsIfIndex,
       "stnVimuxMplsIncomingLabelTtl": stnVimuxMplsIncomingLabelTtl,
       "stnVimuxMplsIncomingLabelReceivedPackets": stnVimuxMplsIncomingLabelReceivedPackets,
       "stnVimuxMplsIncomingLabelDroppedPackets": stnVimuxMplsIncomingLabelDroppedPackets,
       "stnVimuxMplsOutgoingLabelTable": stnVimuxMplsOutgoingLabelTable,
       "stnVimuxMplsOutgoingLabel": stnVimuxMplsOutgoingLabel,
       "stnVimuxMplsOutgoingLabelIfIndex": stnVimuxMplsOutgoingLabelIfIndex,
       "stnVimuxMplsOutgoingLabelValue": stnVimuxMplsOutgoingLabelValue,
       "stnVimuxMplsOutgoingLabelOutgoingIfIndex": stnVimuxMplsOutgoingLabelOutgoingIfIndex,
       "stnVimuxMplsOutgoingLabelNexthop": stnVimuxMplsOutgoingLabelNexthop,
       "stnVimuxMplsOutgoingLabelSentPackets": stnVimuxMplsOutgoingLabelSentPackets,
       "stnVimuxMplsOutgoingLabelDroppedPackets": stnVimuxMplsOutgoingLabelDroppedPackets}
)
