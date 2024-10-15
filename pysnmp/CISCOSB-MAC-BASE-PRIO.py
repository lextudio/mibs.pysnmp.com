# SNMP MIB module (CISCOSB-MAC-BASE-PRIO) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCOSB-MAC-BASE-PRIO
# Produced by pysmi-1.5.4 at Mon Oct 14 21:14:33 2024
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

(switch001,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "switch001")

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
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

rlMacBasePrio = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 101)
)
rlMacBasePrio.setRevisions(
        ("2011-05-30 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlMacBasePrioMibVersion_Type = Integer32
_RlMacBasePrioMibVersion_Object = MibScalar
rlMacBasePrioMibVersion = _RlMacBasePrioMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 101, 1),
    _RlMacBasePrioMibVersion_Type()
)
rlMacBasePrioMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlMacBasePrioMibVersion.setStatus("current")


class _RlMacBasePrioSupport_Type(OctetString):
    """Custom type rlMacBasePrioSupport based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_RlMacBasePrioSupport_Type.__name__ = "OctetString"
_RlMacBasePrioSupport_Object = MibScalar
rlMacBasePrioSupport = _RlMacBasePrioSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 101, 2),
    _RlMacBasePrioSupport_Type()
)
rlMacBasePrioSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlMacBasePrioSupport.setStatus("current")


class _RlMacBasePrioForceL3CosEnable_Type(Integer32):
    """Custom type rlMacBasePrioForceL3CosEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RlMacBasePrioForceL3CosEnable_Type.__name__ = "Integer32"
_RlMacBasePrioForceL3CosEnable_Object = MibScalar
rlMacBasePrioForceL3CosEnable = _RlMacBasePrioForceL3CosEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 101, 3),
    _RlMacBasePrioForceL3CosEnable_Type()
)
rlMacBasePrioForceL3CosEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMacBasePrioForceL3CosEnable.setStatus("current")
_RlMacBasePrioForceL3CosTable_Object = MibTable
rlMacBasePrioForceL3CosTable = _RlMacBasePrioForceL3CosTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 101, 4)
)
if mibBuilder.loadTexts:
    rlMacBasePrioForceL3CosTable.setStatus("current")
_RlMacBasePrioForceL3CosEntry_Object = MibTableRow
rlMacBasePrioForceL3CosEntry = _RlMacBasePrioForceL3CosEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 101, 4, 1)
)
rlMacBasePrioForceL3CosEntry.setIndexNames(
    (0, "CISCOSB-MAC-BASE-PRIO", "rlMacBasePrioForceL3CosAddress"),
    (0, "CISCOSB-MAC-BASE-PRIO", "rlMacBasePrioForceL3CosMask"),
)
if mibBuilder.loadTexts:
    rlMacBasePrioForceL3CosEntry.setStatus("current")
_RlMacBasePrioForceL3CosAddress_Type = MacAddress
_RlMacBasePrioForceL3CosAddress_Object = MibTableColumn
rlMacBasePrioForceL3CosAddress = _RlMacBasePrioForceL3CosAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 101, 4, 1, 1),
    _RlMacBasePrioForceL3CosAddress_Type()
)
rlMacBasePrioForceL3CosAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMacBasePrioForceL3CosAddress.setStatus("current")
_RlMacBasePrioForceL3CosMask_Type = MacAddress
_RlMacBasePrioForceL3CosMask_Object = MibTableColumn
rlMacBasePrioForceL3CosMask = _RlMacBasePrioForceL3CosMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 101, 4, 1, 2),
    _RlMacBasePrioForceL3CosMask_Type()
)
rlMacBasePrioForceL3CosMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMacBasePrioForceL3CosMask.setStatus("current")
_RlMacBasePrioForceL3CosRowStatus_Type = RowStatus
_RlMacBasePrioForceL3CosRowStatus_Object = MibTableColumn
rlMacBasePrioForceL3CosRowStatus = _RlMacBasePrioForceL3CosRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 101, 4, 1, 3),
    _RlMacBasePrioForceL3CosRowStatus_Type()
)
rlMacBasePrioForceL3CosRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMacBasePrioForceL3CosRowStatus.setStatus("current")
_RlMacBasePrioForceL3CosParamsTable_Object = MibTable
rlMacBasePrioForceL3CosParamsTable = _RlMacBasePrioForceL3CosParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 101, 5)
)
if mibBuilder.loadTexts:
    rlMacBasePrioForceL3CosParamsTable.setStatus("current")
_RlMacBasePrioForceL3CosParamsEntry_Object = MibTableRow
rlMacBasePrioForceL3CosParamsEntry = _RlMacBasePrioForceL3CosParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 101, 5, 1)
)
rlMacBasePrioForceL3CosParamsEntry.setIndexNames(
    (0, "CISCOSB-MAC-BASE-PRIO", "rlMacBasePrioForceL3CosParamsEntryIndex"),
)
if mibBuilder.loadTexts:
    rlMacBasePrioForceL3CosParamsEntry.setStatus("current")
_RlMacBasePrioForceL3CosParamsEntryIndex_Type = Integer32
_RlMacBasePrioForceL3CosParamsEntryIndex_Object = MibTableColumn
rlMacBasePrioForceL3CosParamsEntryIndex = _RlMacBasePrioForceL3CosParamsEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 101, 5, 1, 1),
    _RlMacBasePrioForceL3CosParamsEntryIndex_Type()
)
rlMacBasePrioForceL3CosParamsEntryIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMacBasePrioForceL3CosParamsEntryIndex.setStatus("current")
_RlMacBasePrioForceL3CosParamsEntryTC_Type = Integer32
_RlMacBasePrioForceL3CosParamsEntryTC_Object = MibTableColumn
rlMacBasePrioForceL3CosParamsEntryTC = _RlMacBasePrioForceL3CosParamsEntryTC_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 101, 5, 1, 2),
    _RlMacBasePrioForceL3CosParamsEntryTC_Type()
)
rlMacBasePrioForceL3CosParamsEntryTC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMacBasePrioForceL3CosParamsEntryTC.setStatus("current")
_RlMacBasePrioForceL3CosParamsEntryUP_Type = Integer32
_RlMacBasePrioForceL3CosParamsEntryUP_Object = MibTableColumn
rlMacBasePrioForceL3CosParamsEntryUP = _RlMacBasePrioForceL3CosParamsEntryUP_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 101, 5, 1, 3),
    _RlMacBasePrioForceL3CosParamsEntryUP_Type()
)
rlMacBasePrioForceL3CosParamsEntryUP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMacBasePrioForceL3CosParamsEntryUP.setStatus("current")
_RlMacBasePrioForceL3CosParamsEntryDSCP_Type = Integer32
_RlMacBasePrioForceL3CosParamsEntryDSCP_Object = MibTableColumn
rlMacBasePrioForceL3CosParamsEntryDSCP = _RlMacBasePrioForceL3CosParamsEntryDSCP_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 101, 5, 1, 4),
    _RlMacBasePrioForceL3CosParamsEntryDSCP_Type()
)
rlMacBasePrioForceL3CosParamsEntryDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMacBasePrioForceL3CosParamsEntryDSCP.setStatus("current")


class _RlMacBasePrioSADATCEnable_Type(Integer32):
    """Custom type rlMacBasePrioSADATCEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RlMacBasePrioSADATCEnable_Type.__name__ = "Integer32"
_RlMacBasePrioSADATCEnable_Object = MibScalar
rlMacBasePrioSADATCEnable = _RlMacBasePrioSADATCEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 101, 6),
    _RlMacBasePrioSADATCEnable_Type()
)
rlMacBasePrioSADATCEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMacBasePrioSADATCEnable.setStatus("current")
_RlMacBasePrioSADATCTable_Object = MibTable
rlMacBasePrioSADATCTable = _RlMacBasePrioSADATCTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 101, 7)
)
if mibBuilder.loadTexts:
    rlMacBasePrioSADATCTable.setStatus("current")
_RlMacBasePrioSADATCEntry_Object = MibTableRow
rlMacBasePrioSADATCEntry = _RlMacBasePrioSADATCEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 101, 7, 1)
)
rlMacBasePrioSADATCEntry.setIndexNames(
    (0, "CISCOSB-MAC-BASE-PRIO", "rlMacBasePrioSADATCAddress"),
    (0, "CISCOSB-MAC-BASE-PRIO", "rlMacBasePrioSADATCMask"),
)
if mibBuilder.loadTexts:
    rlMacBasePrioSADATCEntry.setStatus("current")
_RlMacBasePrioSADATCAddress_Type = MacAddress
_RlMacBasePrioSADATCAddress_Object = MibTableColumn
rlMacBasePrioSADATCAddress = _RlMacBasePrioSADATCAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 101, 7, 1, 1),
    _RlMacBasePrioSADATCAddress_Type()
)
rlMacBasePrioSADATCAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMacBasePrioSADATCAddress.setStatus("current")
_RlMacBasePrioSADATCMask_Type = MacAddress
_RlMacBasePrioSADATCMask_Object = MibTableColumn
rlMacBasePrioSADATCMask = _RlMacBasePrioSADATCMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 101, 7, 1, 2),
    _RlMacBasePrioSADATCMask_Type()
)
rlMacBasePrioSADATCMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMacBasePrioSADATCMask.setStatus("current")
_RlMacBasePrioSADATCPrio_Type = Integer32
_RlMacBasePrioSADATCPrio_Object = MibTableColumn
rlMacBasePrioSADATCPrio = _RlMacBasePrioSADATCPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 101, 7, 1, 3),
    _RlMacBasePrioSADATCPrio_Type()
)
rlMacBasePrioSADATCPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMacBasePrioSADATCPrio.setStatus("current")
_RlMacBasePrioSADATCRowStatus_Type = RowStatus
_RlMacBasePrioSADATCRowStatus_Object = MibTableColumn
rlMacBasePrioSADATCRowStatus = _RlMacBasePrioSADATCRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 101, 7, 1, 4),
    _RlMacBasePrioSADATCRowStatus_Type()
)
rlMacBasePrioSADATCRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMacBasePrioSADATCRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-MAC-BASE-PRIO",
    **{"rlMacBasePrio": rlMacBasePrio,
       "rlMacBasePrioMibVersion": rlMacBasePrioMibVersion,
       "rlMacBasePrioSupport": rlMacBasePrioSupport,
       "rlMacBasePrioForceL3CosEnable": rlMacBasePrioForceL3CosEnable,
       "rlMacBasePrioForceL3CosTable": rlMacBasePrioForceL3CosTable,
       "rlMacBasePrioForceL3CosEntry": rlMacBasePrioForceL3CosEntry,
       "rlMacBasePrioForceL3CosAddress": rlMacBasePrioForceL3CosAddress,
       "rlMacBasePrioForceL3CosMask": rlMacBasePrioForceL3CosMask,
       "rlMacBasePrioForceL3CosRowStatus": rlMacBasePrioForceL3CosRowStatus,
       "rlMacBasePrioForceL3CosParamsTable": rlMacBasePrioForceL3CosParamsTable,
       "rlMacBasePrioForceL3CosParamsEntry": rlMacBasePrioForceL3CosParamsEntry,
       "rlMacBasePrioForceL3CosParamsEntryIndex": rlMacBasePrioForceL3CosParamsEntryIndex,
       "rlMacBasePrioForceL3CosParamsEntryTC": rlMacBasePrioForceL3CosParamsEntryTC,
       "rlMacBasePrioForceL3CosParamsEntryUP": rlMacBasePrioForceL3CosParamsEntryUP,
       "rlMacBasePrioForceL3CosParamsEntryDSCP": rlMacBasePrioForceL3CosParamsEntryDSCP,
       "rlMacBasePrioSADATCEnable": rlMacBasePrioSADATCEnable,
       "rlMacBasePrioSADATCTable": rlMacBasePrioSADATCTable,
       "rlMacBasePrioSADATCEntry": rlMacBasePrioSADATCEntry,
       "rlMacBasePrioSADATCAddress": rlMacBasePrioSADATCAddress,
       "rlMacBasePrioSADATCMask": rlMacBasePrioSADATCMask,
       "rlMacBasePrioSADATCPrio": rlMacBasePrioSADATCPrio,
       "rlMacBasePrioSADATCRowStatus": rlMacBasePrioSADATCRowStatus}
)
