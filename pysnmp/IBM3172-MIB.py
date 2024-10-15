# SNMP MIB module (IBM3172-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IBM3172-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:07:45 2024
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

ibm3172MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 1, 8)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ibm_ObjectIdentity = ObjectIdentity
ibm = _Ibm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2)
)
_IbmProd_ObjectIdentity = ObjectIdentity
ibmProd = _IbmProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6)
)
_Ibm3172_ObjectIdentity = ObjectIdentity
ibm3172 = _Ibm3172_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 1)
)
_Ibm3172SystemTable_Object = MibTable
ibm3172SystemTable = _Ibm3172SystemTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 1, 1)
)
if mibBuilder.loadTexts:
    ibm3172SystemTable.setStatus("current")
_Ibm3172SystemTableEntry_Object = MibTableRow
ibm3172SystemTableEntry = _Ibm3172SystemTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 1, 1, 1)
)
ibm3172SystemTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ibm3172SystemTableEntry.setStatus("current")


class _Ibm3172Descr_Type(DisplayString):
    """Custom type ibm3172Descr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 253),
    )


_Ibm3172Descr_Type.__name__ = "DisplayString"
_Ibm3172Descr_Object = MibTableColumn
ibm3172Descr = _Ibm3172Descr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 1, 1, 1, 1),
    _Ibm3172Descr_Type()
)
ibm3172Descr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm3172Descr.setStatus("current")


class _Ibm3172Contact_Type(DisplayString):
    """Custom type ibm3172Contact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Ibm3172Contact_Type.__name__ = "DisplayString"
_Ibm3172Contact_Object = MibTableColumn
ibm3172Contact = _Ibm3172Contact_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 1, 1, 1, 2),
    _Ibm3172Contact_Type()
)
ibm3172Contact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm3172Contact.setStatus("current")


class _Ibm3172Location_Type(DisplayString):
    """Custom type ibm3172Location based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Ibm3172Location_Type.__name__ = "DisplayString"
_Ibm3172Location_Object = MibTableColumn
ibm3172Location = _Ibm3172Location_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 1, 1, 1, 3),
    _Ibm3172Location_Type()
)
ibm3172Location.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm3172Location.setStatus("current")
_Ibm3172ifNumber_Type = Integer32
_Ibm3172ifNumber_Object = MibTableColumn
ibm3172ifNumber = _Ibm3172ifNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 1, 1, 1, 4),
    _Ibm3172ifNumber_Type()
)
ibm3172ifNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm3172ifNumber.setStatus("current")
_Ibm3172ifTrapTable_Object = MibTable
ibm3172ifTrapTable = _Ibm3172ifTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 1, 2)
)
if mibBuilder.loadTexts:
    ibm3172ifTrapTable.setStatus("current")
_Ibm3172ifTrapTableEntry_Object = MibTableRow
ibm3172ifTrapTableEntry = _Ibm3172ifTrapTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 1, 2, 1)
)
ibm3172ifTrapTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ibm3172ifTrapTableEntry.setStatus("current")


class _Ibm3172ifTrapEnable_Type(Integer32):
    """Custom type ibm3172ifTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_Ibm3172ifTrapEnable_Type.__name__ = "Integer32"
_Ibm3172ifTrapEnable_Object = MibTableColumn
ibm3172ifTrapEnable = _Ibm3172ifTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 1, 2, 1, 1),
    _Ibm3172ifTrapEnable_Type()
)
ibm3172ifTrapEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm3172ifTrapEnable.setStatus("current")
_Ibm3172ifChanCountersTable_Object = MibTable
ibm3172ifChanCountersTable = _Ibm3172ifChanCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 1, 3)
)
if mibBuilder.loadTexts:
    ibm3172ifChanCountersTable.setStatus("current")
_Ibm3172ifChanCountersTableEntry_Object = MibTableRow
ibm3172ifChanCountersTableEntry = _Ibm3172ifChanCountersTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 1, 3, 1)
)
ibm3172ifChanCountersTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ibm3172ifChanCountersTableEntry.setStatus("current")
_Ibm3172ifInChanOctets_Type = Counter32
_Ibm3172ifInChanOctets_Object = MibTableColumn
ibm3172ifInChanOctets = _Ibm3172ifInChanOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 1, 3, 1, 1),
    _Ibm3172ifInChanOctets_Type()
)
ibm3172ifInChanOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm3172ifInChanOctets.setStatus("current")
_Ibm3172ifOutChanOctets_Type = Counter32
_Ibm3172ifOutChanOctets_Object = MibTableColumn
ibm3172ifOutChanOctets = _Ibm3172ifOutChanOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 1, 3, 1, 2),
    _Ibm3172ifOutChanOctets_Type()
)
ibm3172ifOutChanOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm3172ifOutChanOctets.setStatus("current")
_Ibm3172ifInChanBlocks_Type = Counter32
_Ibm3172ifInChanBlocks_Object = MibTableColumn
ibm3172ifInChanBlocks = _Ibm3172ifInChanBlocks_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 1, 3, 1, 3),
    _Ibm3172ifInChanBlocks_Type()
)
ibm3172ifInChanBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm3172ifInChanBlocks.setStatus("current")
_Ibm3172ifOutChanBlocks_Type = Counter32
_Ibm3172ifOutChanBlocks_Object = MibTableColumn
ibm3172ifOutChanBlocks = _Ibm3172ifOutChanBlocks_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 1, 3, 1, 4),
    _Ibm3172ifOutChanBlocks_Type()
)
ibm3172ifOutChanBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm3172ifOutChanBlocks.setStatus("current")
_Ibm3172ifLANCountersTable_Object = MibTable
ibm3172ifLANCountersTable = _Ibm3172ifLANCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 1, 4)
)
if mibBuilder.loadTexts:
    ibm3172ifLANCountersTable.setStatus("current")
_Ibm3172ifLANCountersTableEntry_Object = MibTableRow
ibm3172ifLANCountersTableEntry = _Ibm3172ifLANCountersTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 1, 4, 1)
)
ibm3172ifLANCountersTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ibm3172ifLANCountersTableEntry.setStatus("current")
_Ibm3172ifInLANOctets_Type = Counter32
_Ibm3172ifInLANOctets_Object = MibTableColumn
ibm3172ifInLANOctets = _Ibm3172ifInLANOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 1, 4, 1, 1),
    _Ibm3172ifInLANOctets_Type()
)
ibm3172ifInLANOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm3172ifInLANOctets.setStatus("current")
_Ibm3172ifOutLANOctets_Type = Counter32
_Ibm3172ifOutLANOctets_Object = MibTableColumn
ibm3172ifOutLANOctets = _Ibm3172ifOutLANOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 1, 4, 1, 2),
    _Ibm3172ifOutLANOctets_Type()
)
ibm3172ifOutLANOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm3172ifOutLANOctets.setStatus("current")
_Ibm3172ifInLANFrames_Type = Counter32
_Ibm3172ifInLANFrames_Object = MibTableColumn
ibm3172ifInLANFrames = _Ibm3172ifInLANFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 1, 4, 1, 3),
    _Ibm3172ifInLANFrames_Type()
)
ibm3172ifInLANFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm3172ifInLANFrames.setStatus("current")
_Ibm3172ifOutLANFrames_Type = Counter32
_Ibm3172ifOutLANFrames_Object = MibTableColumn
ibm3172ifOutLANFrames = _Ibm3172ifOutLANFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 1, 4, 1, 4),
    _Ibm3172ifOutLANFrames_Type()
)
ibm3172ifOutLANFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm3172ifOutLANFrames.setStatus("current")
_Ibm3172ifInLANErrors_Type = Counter32
_Ibm3172ifInLANErrors_Object = MibTableColumn
ibm3172ifInLANErrors = _Ibm3172ifInLANErrors_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 1, 4, 1, 5),
    _Ibm3172ifInLANErrors_Type()
)
ibm3172ifInLANErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm3172ifInLANErrors.setStatus("current")
_Ibm3172ifOutLANErrors_Type = Counter32
_Ibm3172ifOutLANErrors_Object = MibTableColumn
ibm3172ifOutLANErrors = _Ibm3172ifOutLANErrors_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 1, 4, 1, 6),
    _Ibm3172ifOutLANErrors_Type()
)
ibm3172ifOutLANErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm3172ifOutLANErrors.setStatus("current")
_Ibm3172ifInLANDiscards_Type = Counter32
_Ibm3172ifInLANDiscards_Object = MibTableColumn
ibm3172ifInLANDiscards = _Ibm3172ifInLANDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 1, 4, 1, 7),
    _Ibm3172ifInLANDiscards_Type()
)
ibm3172ifInLANDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm3172ifInLANDiscards.setStatus("current")
_Ibm3172ifOutLANDiscards_Type = Counter32
_Ibm3172ifOutLANDiscards_Object = MibTableColumn
ibm3172ifOutLANDiscards = _Ibm3172ifOutLANDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 1, 4, 1, 8),
    _Ibm3172ifOutLANDiscards_Type()
)
ibm3172ifOutLANDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm3172ifOutLANDiscards.setStatus("current")
_Ibm3172ifBlkCountersTable_Object = MibTable
ibm3172ifBlkCountersTable = _Ibm3172ifBlkCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 1, 5)
)
if mibBuilder.loadTexts:
    ibm3172ifBlkCountersTable.setStatus("current")
_Ibm3172ifBlkCountersTableEntry_Object = MibTableRow
ibm3172ifBlkCountersTableEntry = _Ibm3172ifBlkCountersTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 1, 5, 1)
)
ibm3172ifBlkCountersTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ibm3172ifBlkCountersTableEntry.setStatus("current")
_Ibm3172ifBlkRcvOctets_Type = Counter32
_Ibm3172ifBlkRcvOctets_Object = MibTableColumn
ibm3172ifBlkRcvOctets = _Ibm3172ifBlkRcvOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 1, 5, 1, 1),
    _Ibm3172ifBlkRcvOctets_Type()
)
ibm3172ifBlkRcvOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm3172ifBlkRcvOctets.setStatus("current")
_Ibm3172ifBlkXmitOctets_Type = Counter32
_Ibm3172ifBlkXmitOctets_Object = MibTableColumn
ibm3172ifBlkXmitOctets = _Ibm3172ifBlkXmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 1, 5, 1, 2),
    _Ibm3172ifBlkXmitOctets_Type()
)
ibm3172ifBlkXmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm3172ifBlkXmitOctets.setStatus("current")
_Ibm3172ifBlkRcvFrames_Type = Counter32
_Ibm3172ifBlkRcvFrames_Object = MibTableColumn
ibm3172ifBlkRcvFrames = _Ibm3172ifBlkRcvFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 1, 5, 1, 3),
    _Ibm3172ifBlkRcvFrames_Type()
)
ibm3172ifBlkRcvFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm3172ifBlkRcvFrames.setStatus("current")
_Ibm3172ifBlkXmitBlocks_Type = Counter32
_Ibm3172ifBlkXmitBlocks_Object = MibTableColumn
ibm3172ifBlkXmitBlocks = _Ibm3172ifBlkXmitBlocks_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 1, 5, 1, 4),
    _Ibm3172ifBlkXmitBlocks_Type()
)
ibm3172ifBlkXmitBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm3172ifBlkXmitBlocks.setStatus("current")
_Ibm3172ifInBlkErrors_Type = Counter32
_Ibm3172ifInBlkErrors_Object = MibTableColumn
ibm3172ifInBlkErrors = _Ibm3172ifInBlkErrors_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 1, 5, 1, 5),
    _Ibm3172ifInBlkErrors_Type()
)
ibm3172ifInBlkErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm3172ifInBlkErrors.setStatus("current")
_Ibm3172ifInBlkDiscards_Type = Counter32
_Ibm3172ifInBlkDiscards_Object = MibTableColumn
ibm3172ifInBlkDiscards = _Ibm3172ifInBlkDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 1, 5, 1, 6),
    _Ibm3172ifInBlkDiscards_Type()
)
ibm3172ifInBlkDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm3172ifInBlkDiscards.setStatus("current")
_Ibm3172ifDblkCountersTable_Object = MibTable
ibm3172ifDblkCountersTable = _Ibm3172ifDblkCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 1, 6)
)
if mibBuilder.loadTexts:
    ibm3172ifDblkCountersTable.setStatus("current")
_Ibm3172ifDblkCountersTableEntry_Object = MibTableRow
ibm3172ifDblkCountersTableEntry = _Ibm3172ifDblkCountersTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 1, 6, 1)
)
ibm3172ifDblkCountersTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ibm3172ifDblkCountersTableEntry.setStatus("current")
_Ibm3172ifDblkRcvOctets_Type = Counter32
_Ibm3172ifDblkRcvOctets_Object = MibTableColumn
ibm3172ifDblkRcvOctets = _Ibm3172ifDblkRcvOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 1, 6, 1, 1),
    _Ibm3172ifDblkRcvOctets_Type()
)
ibm3172ifDblkRcvOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm3172ifDblkRcvOctets.setStatus("current")
_Ibm3172ifDblkXmitOctets_Type = Counter32
_Ibm3172ifDblkXmitOctets_Object = MibTableColumn
ibm3172ifDblkXmitOctets = _Ibm3172ifDblkXmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 1, 6, 1, 2),
    _Ibm3172ifDblkXmitOctets_Type()
)
ibm3172ifDblkXmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm3172ifDblkXmitOctets.setStatus("current")
_Ibm3172ifDblkRcvBlocks_Type = Counter32
_Ibm3172ifDblkRcvBlocks_Object = MibTableColumn
ibm3172ifDblkRcvBlocks = _Ibm3172ifDblkRcvBlocks_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 1, 6, 1, 3),
    _Ibm3172ifDblkRcvBlocks_Type()
)
ibm3172ifDblkRcvBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm3172ifDblkRcvBlocks.setStatus("current")
_Ibm3172ifDblkXmitFrames_Type = Counter32
_Ibm3172ifDblkXmitFrames_Object = MibTableColumn
ibm3172ifDblkXmitFrames = _Ibm3172ifDblkXmitFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 1, 6, 1, 4),
    _Ibm3172ifDblkXmitFrames_Type()
)
ibm3172ifDblkXmitFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm3172ifDblkXmitFrames.setStatus("current")
_Ibm3172ifOutDblkErrors_Type = Counter32
_Ibm3172ifOutDblkErrors_Object = MibTableColumn
ibm3172ifOutDblkErrors = _Ibm3172ifOutDblkErrors_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 1, 6, 1, 5),
    _Ibm3172ifOutDblkErrors_Type()
)
ibm3172ifOutDblkErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm3172ifOutDblkErrors.setStatus("current")
_Ibm3172ifOutDblkDiscards_Type = Counter32
_Ibm3172ifOutDblkDiscards_Object = MibTableColumn
ibm3172ifOutDblkDiscards = _Ibm3172ifOutDblkDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 1, 6, 1, 6),
    _Ibm3172ifOutDblkDiscards_Type()
)
ibm3172ifOutDblkDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm3172ifOutDblkDiscards.setStatus("current")
_Ibm3172ifDeviceTable_Object = MibTable
ibm3172ifDeviceTable = _Ibm3172ifDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 1, 7)
)
if mibBuilder.loadTexts:
    ibm3172ifDeviceTable.setStatus("current")
_Ibm3172ifDeviceTableEntry_Object = MibTableRow
ibm3172ifDeviceTableEntry = _Ibm3172ifDeviceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 1, 7, 1)
)
ibm3172ifDeviceTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ibm3172ifDeviceTableEntry.setStatus("current")
_Ibm3172ifDeviceNumber_Type = Integer32
_Ibm3172ifDeviceNumber_Object = MibTableColumn
ibm3172ifDeviceNumber = _Ibm3172ifDeviceNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 1, 7, 1, 1),
    _Ibm3172ifDeviceNumber_Type()
)
ibm3172ifDeviceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm3172ifDeviceNumber.setStatus("current")
_Ibm3172MIBConformance_ObjectIdentity = ObjectIdentity
ibm3172MIBConformance = _Ibm3172MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 1, 8, 2)
)
_Ibm3172MIBCompliances_ObjectIdentity = ObjectIdentity
ibm3172MIBCompliances = _Ibm3172MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 1, 8, 2, 1)
)
_Ibm3172MIBGroups_ObjectIdentity = ObjectIdentity
ibm3172MIBGroups = _Ibm3172MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 1, 8, 2, 2)
)

# Managed Objects groups

ibm3172Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 1, 8, 2, 2, 1)
)
ibm3172Group.setObjects(
      *(("IBM3172-MIB", "ibm3172Descr"),
        ("IBM3172-MIB", "ibm3172Contact"),
        ("IBM3172-MIB", "ibm3172Location"),
        ("IBM3172-MIB", "ibm3172ifNumber"),
        ("IBM3172-MIB", "ibm3172ifTrapEnable"),
        ("IBM3172-MIB", "ibm3172ifInChanOctets"),
        ("IBM3172-MIB", "ibm3172ifOutChanOctets"),
        ("IBM3172-MIB", "ibm3172ifInChanBlocks"),
        ("IBM3172-MIB", "ibm3172ifOutChanBlocks"),
        ("IBM3172-MIB", "ibm3172ifInLANOctets"),
        ("IBM3172-MIB", "ibm3172ifOutLANOctets"),
        ("IBM3172-MIB", "ibm3172ifInLANFrames"),
        ("IBM3172-MIB", "ibm3172ifOutLANFrames"),
        ("IBM3172-MIB", "ibm3172ifInLANErrors"),
        ("IBM3172-MIB", "ibm3172ifOutLANErrors"),
        ("IBM3172-MIB", "ibm3172ifInLANDiscards"),
        ("IBM3172-MIB", "ibm3172ifOutLANDiscards"),
        ("IBM3172-MIB", "ibm3172ifBlkRcvOctets"),
        ("IBM3172-MIB", "ibm3172ifBlkXmitOctets"),
        ("IBM3172-MIB", "ibm3172ifBlkRcvFrames"),
        ("IBM3172-MIB", "ibm3172ifBlkXmitBlocks"),
        ("IBM3172-MIB", "ibm3172ifInBlkErrors"),
        ("IBM3172-MIB", "ibm3172ifInBlkDiscards"),
        ("IBM3172-MIB", "ibm3172ifDblkRcvOctets"),
        ("IBM3172-MIB", "ibm3172ifDblkXmitOctets"),
        ("IBM3172-MIB", "ibm3172ifDblkRcvBlocks"),
        ("IBM3172-MIB", "ibm3172ifDblkXmitFrames"),
        ("IBM3172-MIB", "ibm3172ifOutDblkErrors"),
        ("IBM3172-MIB", "ibm3172ifOutDblkDiscards"),
        ("IBM3172-MIB", "ibm3172ifDeviceNumber"))
)
if mibBuilder.loadTexts:
    ibm3172Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ibm3172MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2, 6, 1, 8, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ibm3172MIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IBM3172-MIB",
    **{"ibm": ibm,
       "ibmProd": ibmProd,
       "ibm3172": ibm3172,
       "ibm3172SystemTable": ibm3172SystemTable,
       "ibm3172SystemTableEntry": ibm3172SystemTableEntry,
       "ibm3172Descr": ibm3172Descr,
       "ibm3172Contact": ibm3172Contact,
       "ibm3172Location": ibm3172Location,
       "ibm3172ifNumber": ibm3172ifNumber,
       "ibm3172ifTrapTable": ibm3172ifTrapTable,
       "ibm3172ifTrapTableEntry": ibm3172ifTrapTableEntry,
       "ibm3172ifTrapEnable": ibm3172ifTrapEnable,
       "ibm3172ifChanCountersTable": ibm3172ifChanCountersTable,
       "ibm3172ifChanCountersTableEntry": ibm3172ifChanCountersTableEntry,
       "ibm3172ifInChanOctets": ibm3172ifInChanOctets,
       "ibm3172ifOutChanOctets": ibm3172ifOutChanOctets,
       "ibm3172ifInChanBlocks": ibm3172ifInChanBlocks,
       "ibm3172ifOutChanBlocks": ibm3172ifOutChanBlocks,
       "ibm3172ifLANCountersTable": ibm3172ifLANCountersTable,
       "ibm3172ifLANCountersTableEntry": ibm3172ifLANCountersTableEntry,
       "ibm3172ifInLANOctets": ibm3172ifInLANOctets,
       "ibm3172ifOutLANOctets": ibm3172ifOutLANOctets,
       "ibm3172ifInLANFrames": ibm3172ifInLANFrames,
       "ibm3172ifOutLANFrames": ibm3172ifOutLANFrames,
       "ibm3172ifInLANErrors": ibm3172ifInLANErrors,
       "ibm3172ifOutLANErrors": ibm3172ifOutLANErrors,
       "ibm3172ifInLANDiscards": ibm3172ifInLANDiscards,
       "ibm3172ifOutLANDiscards": ibm3172ifOutLANDiscards,
       "ibm3172ifBlkCountersTable": ibm3172ifBlkCountersTable,
       "ibm3172ifBlkCountersTableEntry": ibm3172ifBlkCountersTableEntry,
       "ibm3172ifBlkRcvOctets": ibm3172ifBlkRcvOctets,
       "ibm3172ifBlkXmitOctets": ibm3172ifBlkXmitOctets,
       "ibm3172ifBlkRcvFrames": ibm3172ifBlkRcvFrames,
       "ibm3172ifBlkXmitBlocks": ibm3172ifBlkXmitBlocks,
       "ibm3172ifInBlkErrors": ibm3172ifInBlkErrors,
       "ibm3172ifInBlkDiscards": ibm3172ifInBlkDiscards,
       "ibm3172ifDblkCountersTable": ibm3172ifDblkCountersTable,
       "ibm3172ifDblkCountersTableEntry": ibm3172ifDblkCountersTableEntry,
       "ibm3172ifDblkRcvOctets": ibm3172ifDblkRcvOctets,
       "ibm3172ifDblkXmitOctets": ibm3172ifDblkXmitOctets,
       "ibm3172ifDblkRcvBlocks": ibm3172ifDblkRcvBlocks,
       "ibm3172ifDblkXmitFrames": ibm3172ifDblkXmitFrames,
       "ibm3172ifOutDblkErrors": ibm3172ifOutDblkErrors,
       "ibm3172ifOutDblkDiscards": ibm3172ifOutDblkDiscards,
       "ibm3172ifDeviceTable": ibm3172ifDeviceTable,
       "ibm3172ifDeviceTableEntry": ibm3172ifDeviceTableEntry,
       "ibm3172ifDeviceNumber": ibm3172ifDeviceNumber,
       "ibm3172MIB": ibm3172MIB,
       "ibm3172MIBConformance": ibm3172MIBConformance,
       "ibm3172MIBCompliances": ibm3172MIBCompliances,
       "ibm3172MIBCompliance": ibm3172MIBCompliance,
       "ibm3172MIBGroups": ibm3172MIBGroups,
       "ibm3172Group": ibm3172Group}
)
