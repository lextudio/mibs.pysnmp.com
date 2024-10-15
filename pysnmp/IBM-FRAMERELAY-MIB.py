# SNMP MIB module (IBM-FRAMERELAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IBM-FRAMERELAY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:07:30 2024
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

(frCircuitDlci,
 frCircuitIfIndex) = mibBuilder.importSymbols(
    "RFC1315-MIB",
    "frCircuitDlci",
    "frCircuitIfIndex")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IbmIROCfrcircuit_ObjectIdentity = ObjectIdentity
ibmIROCfrcircuit = _IbmIROCfrcircuit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 5)
)
_IbmframerelayPVCTable_Object = MibTable
ibmframerelayPVCTable = _IbmframerelayPVCTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 5, 1)
)
if mibBuilder.loadTexts:
    ibmframerelayPVCTable.setStatus("mandatory")
_IbmframerelayPVCEntry_Object = MibTableRow
ibmframerelayPVCEntry = _IbmframerelayPVCEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 5, 1, 1)
)
ibmframerelayPVCEntry.setIndexNames(
    (0, "RFC1315-MIB", "frCircuitIfIndex"),
    (0, "RFC1315-MIB", "frCircuitDlci"),
)
if mibBuilder.loadTexts:
    ibmframerelayPVCEntry.setStatus("mandatory")
_IbmframerelayPVCCircName_Type = DisplayString
_IbmframerelayPVCCircName_Object = MibTableColumn
ibmframerelayPVCCircName = _IbmframerelayPVCCircName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 5, 1, 1, 1),
    _IbmframerelayPVCCircName_Type()
)
ibmframerelayPVCCircName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmframerelayPVCCircName.setStatus("mandatory")
_IbmframerelayPVCTimesActive_Type = Counter32
_IbmframerelayPVCTimesActive_Object = MibTableColumn
ibmframerelayPVCTimesActive = _IbmframerelayPVCTimesActive_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 5, 1, 1, 2),
    _IbmframerelayPVCTimesActive_Type()
)
ibmframerelayPVCTimesActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmframerelayPVCTimesActive.setStatus("mandatory")
_IbmframerelayPVCTimesInactive_Type = Counter32
_IbmframerelayPVCTimesInactive_Object = MibTableColumn
ibmframerelayPVCTimesInactive = _IbmframerelayPVCTimesInactive_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 5, 1, 1, 3),
    _IbmframerelayPVCTimesInactive_Type()
)
ibmframerelayPVCTimesInactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmframerelayPVCTimesInactive.setStatus("mandatory")
_IbmframerelayPVCTimesCongested_Type = Counter32
_IbmframerelayPVCTimesCongested_Object = MibTableColumn
ibmframerelayPVCTimesCongested = _IbmframerelayPVCTimesCongested_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 5, 1, 1, 4),
    _IbmframerelayPVCTimesCongested_Type()
)
ibmframerelayPVCTimesCongested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmframerelayPVCTimesCongested.setStatus("mandatory")
_IbmframerelayPVCTxQueued_Type = Gauge32
_IbmframerelayPVCTxQueued_Object = MibTableColumn
ibmframerelayPVCTxQueued = _IbmframerelayPVCTxQueued_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 5, 1, 1, 5),
    _IbmframerelayPVCTxQueued_Type()
)
ibmframerelayPVCTxQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmframerelayPVCTxQueued.setStatus("mandatory")
_IbmframerelayPVCTxDropped_Type = Counter32
_IbmframerelayPVCTxDropped_Object = MibTableColumn
ibmframerelayPVCTxDropped = _IbmframerelayPVCTxDropped_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 5, 1, 1, 6),
    _IbmframerelayPVCTxDropped_Type()
)
ibmframerelayPVCTxDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmframerelayPVCTxDropped.setStatus("mandatory")
_IbmframerelayPVCClearAll_Type = Integer32
_IbmframerelayPVCClearAll_Object = MibTableColumn
ibmframerelayPVCClearAll = _IbmframerelayPVCClearAll_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 5, 1, 1, 7),
    _IbmframerelayPVCClearAll_Type()
)
ibmframerelayPVCClearAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmframerelayPVCClearAll.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IBM-FRAMERELAY-MIB",
    **{"ibmIROCfrcircuit": ibmIROCfrcircuit,
       "ibmframerelayPVCTable": ibmframerelayPVCTable,
       "ibmframerelayPVCEntry": ibmframerelayPVCEntry,
       "ibmframerelayPVCCircName": ibmframerelayPVCCircName,
       "ibmframerelayPVCTimesActive": ibmframerelayPVCTimesActive,
       "ibmframerelayPVCTimesInactive": ibmframerelayPVCTimesInactive,
       "ibmframerelayPVCTimesCongested": ibmframerelayPVCTimesCongested,
       "ibmframerelayPVCTxQueued": ibmframerelayPVCTxQueued,
       "ibmframerelayPVCTxDropped": ibmframerelayPVCTxDropped,
       "ibmframerelayPVCClearAll": ibmframerelayPVCClearAll}
)
