# SNMP MIB module (FOUNDRY-SN-CAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FOUNDRY-SN-CAM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:45:52 2024
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

(platform,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-ROOT-MIB",
    "platform")

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

snCamMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 1)
)
snCamMIB.setRevisions(
        ("2010-06-02 00:00",
         "2007-11-19 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Percent(Gauge32, TextualConvention):
    status = "current"
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



# MIB Managed Objects in the order of their OIDs

_SnCamObjects_ObjectIdentity = ObjectIdentity
snCamObjects = _SnCamObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1)
)


class _SnCamProfile_Type(Integer32):
    """Custom type snCamProfile based on Integer32"""
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
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("ipv4", 2),
          ("ipv4Ipv6", 3),
          ("ipv4Ipv62", 4),
          ("ipv4Vpls", 5),
          ("ipv4Vpn", 6),
          ("ipv6", 7),
          ("l2Metro", 8),
          ("l2Metro2", 9),
          ("mplsL3vpn", 10),
          ("mplsL3vpn2", 11),
          ("mplsVpls", 12),
          ("mplsVpls2", 13),
          ("mplsVpnVpls", 14),
          ("multiService", 15),
          ("multiService2", 16),
          ("multiService3", 17),
          ("multiService4", 18))
    )


_SnCamProfile_Type.__name__ = "Integer32"
_SnCamProfile_Object = MibScalar
snCamProfile = _SnCamProfile_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 1),
    _SnCamProfile_Type()
)
snCamProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCamProfile.setStatus("current")
_SnCamUsage_ObjectIdentity = ObjectIdentity
snCamUsage = _SnCamUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2)
)
_SnCamUsageL3Table_Object = MibTable
snCamUsageL3Table = _SnCamUsageL3Table_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    snCamUsageL3Table.setStatus("current")
_SnCamUsageL3Entry_Object = MibTableRow
snCamUsageL3Entry = _SnCamUsageL3Entry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 1, 1)
)
snCamUsageL3Entry.setIndexNames(
    (0, "FOUNDRY-SN-CAM-MIB", "snCamUsageL3Slot"),
    (0, "FOUNDRY-SN-CAM-MIB", "snCamUsageL3Processor"),
    (0, "FOUNDRY-SN-CAM-MIB", "snCamUsageL3Type"),
    (0, "FOUNDRY-SN-CAM-MIB", "snCamUsageL3Supernet"),
)
if mibBuilder.loadTexts:
    snCamUsageL3Entry.setStatus("current")
_SnCamUsageL3Slot_Type = Unsigned32
_SnCamUsageL3Slot_Object = MibTableColumn
snCamUsageL3Slot = _SnCamUsageL3Slot_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 1, 1, 1),
    _SnCamUsageL3Slot_Type()
)
snCamUsageL3Slot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snCamUsageL3Slot.setStatus("current")


class _SnCamUsageL3Processor_Type(Unsigned32):
    """Custom type snCamUsageL3Processor based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SnCamUsageL3Processor_Type.__name__ = "Unsigned32"
_SnCamUsageL3Processor_Object = MibTableColumn
snCamUsageL3Processor = _SnCamUsageL3Processor_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 1, 1, 2),
    _SnCamUsageL3Processor_Type()
)
snCamUsageL3Processor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snCamUsageL3Processor.setStatus("current")


class _SnCamUsageL3Type_Type(Integer32):
    """Custom type snCamUsageL3Type based on Integer32"""
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
        *(("ipv4", 1),
          ("ipv4vpn", 3),
          ("ipv6", 2),
          ("ipv6vpn", 4))
    )


_SnCamUsageL3Type_Type.__name__ = "Integer32"
_SnCamUsageL3Type_Object = MibTableColumn
snCamUsageL3Type = _SnCamUsageL3Type_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 1, 1, 3),
    _SnCamUsageL3Type_Type()
)
snCamUsageL3Type.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snCamUsageL3Type.setStatus("current")
_SnCamUsageL3Supernet_Type = Unsigned32
_SnCamUsageL3Supernet_Object = MibTableColumn
snCamUsageL3Supernet = _SnCamUsageL3Supernet_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 1, 1, 4),
    _SnCamUsageL3Supernet_Type()
)
snCamUsageL3Supernet.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snCamUsageL3Supernet.setStatus("current")
_SnCamUsageL3Size_Type = Unsigned32
_SnCamUsageL3Size_Object = MibTableColumn
snCamUsageL3Size = _SnCamUsageL3Size_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 1, 1, 5),
    _SnCamUsageL3Size_Type()
)
snCamUsageL3Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCamUsageL3Size.setStatus("current")
if mibBuilder.loadTexts:
    snCamUsageL3Size.setUnits("Entries")
_SnCamUsageL3Free_Type = Gauge32
_SnCamUsageL3Free_Object = MibTableColumn
snCamUsageL3Free = _SnCamUsageL3Free_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 1, 1, 6),
    _SnCamUsageL3Free_Type()
)
snCamUsageL3Free.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCamUsageL3Free.setStatus("current")
if mibBuilder.loadTexts:
    snCamUsageL3Free.setUnits("Entries")
_SnCamUsageL3UsedPercent_Type = Percent
_SnCamUsageL3UsedPercent_Object = MibTableColumn
snCamUsageL3UsedPercent = _SnCamUsageL3UsedPercent_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 1, 1, 7),
    _SnCamUsageL3UsedPercent_Type()
)
snCamUsageL3UsedPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCamUsageL3UsedPercent.setStatus("current")
_SnCamUsageL2Table_Object = MibTable
snCamUsageL2Table = _SnCamUsageL2Table_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    snCamUsageL2Table.setStatus("current")
_SnCamUsageL2Entry_Object = MibTableRow
snCamUsageL2Entry = _SnCamUsageL2Entry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 2, 1)
)
snCamUsageL2Entry.setIndexNames(
    (0, "FOUNDRY-SN-CAM-MIB", "snCamUsageL2Slot"),
    (0, "FOUNDRY-SN-CAM-MIB", "snCamUsageL2Processor"),
    (0, "FOUNDRY-SN-CAM-MIB", "snCamUsageL2Type"),
)
if mibBuilder.loadTexts:
    snCamUsageL2Entry.setStatus("current")
_SnCamUsageL2Slot_Type = Unsigned32
_SnCamUsageL2Slot_Object = MibTableColumn
snCamUsageL2Slot = _SnCamUsageL2Slot_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 2, 1, 1),
    _SnCamUsageL2Slot_Type()
)
snCamUsageL2Slot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snCamUsageL2Slot.setStatus("current")


class _SnCamUsageL2Processor_Type(Unsigned32):
    """Custom type snCamUsageL2Processor based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SnCamUsageL2Processor_Type.__name__ = "Unsigned32"
_SnCamUsageL2Processor_Object = MibTableColumn
snCamUsageL2Processor = _SnCamUsageL2Processor_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 2, 1, 2),
    _SnCamUsageL2Processor_Type()
)
snCamUsageL2Processor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snCamUsageL2Processor.setStatus("current")


class _SnCamUsageL2Type_Type(Integer32):
    """Custom type snCamUsageL2Type based on Integer32"""
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
        *(("flooding", 3),
          ("forwarding", 1),
          ("protocol", 2),
          ("total", 4))
    )


_SnCamUsageL2Type_Type.__name__ = "Integer32"
_SnCamUsageL2Type_Object = MibTableColumn
snCamUsageL2Type = _SnCamUsageL2Type_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 2, 1, 3),
    _SnCamUsageL2Type_Type()
)
snCamUsageL2Type.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snCamUsageL2Type.setStatus("current")
_SnCamUsageL2Size_Type = Unsigned32
_SnCamUsageL2Size_Object = MibTableColumn
snCamUsageL2Size = _SnCamUsageL2Size_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 2, 1, 4),
    _SnCamUsageL2Size_Type()
)
snCamUsageL2Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCamUsageL2Size.setStatus("current")
if mibBuilder.loadTexts:
    snCamUsageL2Size.setUnits("Entries")
_SnCamUsageL2Free_Type = Gauge32
_SnCamUsageL2Free_Object = MibTableColumn
snCamUsageL2Free = _SnCamUsageL2Free_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 2, 1, 5),
    _SnCamUsageL2Free_Type()
)
snCamUsageL2Free.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCamUsageL2Free.setStatus("current")
if mibBuilder.loadTexts:
    snCamUsageL2Free.setUnits("Entries")
_SnCamUsageL2UsedPercent_Type = Percent
_SnCamUsageL2UsedPercent_Object = MibTableColumn
snCamUsageL2UsedPercent = _SnCamUsageL2UsedPercent_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 2, 1, 6),
    _SnCamUsageL2UsedPercent_Type()
)
snCamUsageL2UsedPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCamUsageL2UsedPercent.setStatus("current")
_SnCamUsageSessionTable_Object = MibTable
snCamUsageSessionTable = _SnCamUsageSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    snCamUsageSessionTable.setStatus("current")
_SnCamUsageSessionEntry_Object = MibTableRow
snCamUsageSessionEntry = _SnCamUsageSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 3, 1)
)
snCamUsageSessionEntry.setIndexNames(
    (0, "FOUNDRY-SN-CAM-MIB", "snCamUsageSessionSlot"),
    (0, "FOUNDRY-SN-CAM-MIB", "snCamUsageSessionProcessor"),
    (0, "FOUNDRY-SN-CAM-MIB", "snCamUsageSessionType"),
)
if mibBuilder.loadTexts:
    snCamUsageSessionEntry.setStatus("current")
_SnCamUsageSessionSlot_Type = Unsigned32
_SnCamUsageSessionSlot_Object = MibTableColumn
snCamUsageSessionSlot = _SnCamUsageSessionSlot_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 3, 1, 1),
    _SnCamUsageSessionSlot_Type()
)
snCamUsageSessionSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snCamUsageSessionSlot.setStatus("current")


class _SnCamUsageSessionProcessor_Type(Unsigned32):
    """Custom type snCamUsageSessionProcessor based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SnCamUsageSessionProcessor_Type.__name__ = "Unsigned32"
_SnCamUsageSessionProcessor_Object = MibTableColumn
snCamUsageSessionProcessor = _SnCamUsageSessionProcessor_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 3, 1, 2),
    _SnCamUsageSessionProcessor_Type()
)
snCamUsageSessionProcessor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snCamUsageSessionProcessor.setStatus("current")


class _SnCamUsageSessionType_Type(Integer32):
    """Custom type snCamUsageSessionType based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("internalForwardingLookup", 14),
          ("ipv4Multicast", 1),
          ("ipv4SrcGuardDenial", 12),
          ("ipv4SrcGuardPermit", 13),
          ("ipv4andMacOut", 5),
          ("ipv4andMacReceiveAcl", 2),
          ("ipv4andMacRuleAcl", 3),
          ("ipv4andMacTotal", 4),
          ("ipv6Multicast", 6),
          ("ipv6Out", 10),
          ("ipv6ReceiveAcl", 7),
          ("ipv6RuleAcl", 8),
          ("ipv6Total", 9),
          ("labelOut", 11))
    )


_SnCamUsageSessionType_Type.__name__ = "Integer32"
_SnCamUsageSessionType_Object = MibTableColumn
snCamUsageSessionType = _SnCamUsageSessionType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 3, 1, 3),
    _SnCamUsageSessionType_Type()
)
snCamUsageSessionType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snCamUsageSessionType.setStatus("current")
_SnCamUsageSessionSize_Type = Unsigned32
_SnCamUsageSessionSize_Object = MibTableColumn
snCamUsageSessionSize = _SnCamUsageSessionSize_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 3, 1, 4),
    _SnCamUsageSessionSize_Type()
)
snCamUsageSessionSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCamUsageSessionSize.setStatus("current")
if mibBuilder.loadTexts:
    snCamUsageSessionSize.setUnits("Entries")
_SnCamUsageSessionFree_Type = Gauge32
_SnCamUsageSessionFree_Object = MibTableColumn
snCamUsageSessionFree = _SnCamUsageSessionFree_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 3, 1, 5),
    _SnCamUsageSessionFree_Type()
)
snCamUsageSessionFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCamUsageSessionFree.setStatus("current")
if mibBuilder.loadTexts:
    snCamUsageSessionFree.setUnits("Entries")
_SnCamUsageSessionUsedPercent_Type = Percent
_SnCamUsageSessionUsedPercent_Object = MibTableColumn
snCamUsageSessionUsedPercent = _SnCamUsageSessionUsedPercent_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 3, 1, 6),
    _SnCamUsageSessionUsedPercent_Type()
)
snCamUsageSessionUsedPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCamUsageSessionUsedPercent.setStatus("current")
_SnCamUsageOtherTable_Object = MibTable
snCamUsageOtherTable = _SnCamUsageOtherTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    snCamUsageOtherTable.setStatus("current")
_SnCamUsageOtherEntry_Object = MibTableRow
snCamUsageOtherEntry = _SnCamUsageOtherEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 4, 1)
)
snCamUsageOtherEntry.setIndexNames(
    (0, "FOUNDRY-SN-CAM-MIB", "snCamUsageOtherSlot"),
    (0, "FOUNDRY-SN-CAM-MIB", "snCamUsageOtherProcessor"),
    (0, "FOUNDRY-SN-CAM-MIB", "snCamUsageOtherType"),
)
if mibBuilder.loadTexts:
    snCamUsageOtherEntry.setStatus("current")
_SnCamUsageOtherSlot_Type = Unsigned32
_SnCamUsageOtherSlot_Object = MibTableColumn
snCamUsageOtherSlot = _SnCamUsageOtherSlot_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 4, 1, 1),
    _SnCamUsageOtherSlot_Type()
)
snCamUsageOtherSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snCamUsageOtherSlot.setStatus("current")


class _SnCamUsageOtherProcessor_Type(Unsigned32):
    """Custom type snCamUsageOtherProcessor based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SnCamUsageOtherProcessor_Type.__name__ = "Unsigned32"
_SnCamUsageOtherProcessor_Object = MibTableColumn
snCamUsageOtherProcessor = _SnCamUsageOtherProcessor_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 4, 1, 2),
    _SnCamUsageOtherProcessor_Type()
)
snCamUsageOtherProcessor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snCamUsageOtherProcessor.setStatus("current")


class _SnCamUsageOtherType_Type(Integer32):
    """Custom type snCamUsageOtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gre", 1),
          ("multicastVpls", 2))
    )


_SnCamUsageOtherType_Type.__name__ = "Integer32"
_SnCamUsageOtherType_Object = MibTableColumn
snCamUsageOtherType = _SnCamUsageOtherType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 4, 1, 3),
    _SnCamUsageOtherType_Type()
)
snCamUsageOtherType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snCamUsageOtherType.setStatus("current")
_SnCamUsageOtherSize_Type = Unsigned32
_SnCamUsageOtherSize_Object = MibTableColumn
snCamUsageOtherSize = _SnCamUsageOtherSize_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 4, 1, 4),
    _SnCamUsageOtherSize_Type()
)
snCamUsageOtherSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCamUsageOtherSize.setStatus("current")
if mibBuilder.loadTexts:
    snCamUsageOtherSize.setUnits("Entries")
_SnCamUsageOtherFree_Type = Gauge32
_SnCamUsageOtherFree_Object = MibTableColumn
snCamUsageOtherFree = _SnCamUsageOtherFree_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 4, 1, 5),
    _SnCamUsageOtherFree_Type()
)
snCamUsageOtherFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCamUsageOtherFree.setStatus("current")
if mibBuilder.loadTexts:
    snCamUsageOtherFree.setUnits("Entries")
_SnCamUsageOtherUsedPercent_Type = Percent
_SnCamUsageOtherUsedPercent_Object = MibTableColumn
snCamUsageOtherUsedPercent = _SnCamUsageOtherUsedPercent_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14, 1, 1, 2, 4, 1, 6),
    _SnCamUsageOtherUsedPercent_Type()
)
snCamUsageOtherUsedPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCamUsageOtherUsedPercent.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FOUNDRY-SN-CAM-MIB",
    **{"Percent": Percent,
       "snCamMIB": snCamMIB,
       "snCamObjects": snCamObjects,
       "snCamProfile": snCamProfile,
       "snCamUsage": snCamUsage,
       "snCamUsageL3Table": snCamUsageL3Table,
       "snCamUsageL3Entry": snCamUsageL3Entry,
       "snCamUsageL3Slot": snCamUsageL3Slot,
       "snCamUsageL3Processor": snCamUsageL3Processor,
       "snCamUsageL3Type": snCamUsageL3Type,
       "snCamUsageL3Supernet": snCamUsageL3Supernet,
       "snCamUsageL3Size": snCamUsageL3Size,
       "snCamUsageL3Free": snCamUsageL3Free,
       "snCamUsageL3UsedPercent": snCamUsageL3UsedPercent,
       "snCamUsageL2Table": snCamUsageL2Table,
       "snCamUsageL2Entry": snCamUsageL2Entry,
       "snCamUsageL2Slot": snCamUsageL2Slot,
       "snCamUsageL2Processor": snCamUsageL2Processor,
       "snCamUsageL2Type": snCamUsageL2Type,
       "snCamUsageL2Size": snCamUsageL2Size,
       "snCamUsageL2Free": snCamUsageL2Free,
       "snCamUsageL2UsedPercent": snCamUsageL2UsedPercent,
       "snCamUsageSessionTable": snCamUsageSessionTable,
       "snCamUsageSessionEntry": snCamUsageSessionEntry,
       "snCamUsageSessionSlot": snCamUsageSessionSlot,
       "snCamUsageSessionProcessor": snCamUsageSessionProcessor,
       "snCamUsageSessionType": snCamUsageSessionType,
       "snCamUsageSessionSize": snCamUsageSessionSize,
       "snCamUsageSessionFree": snCamUsageSessionFree,
       "snCamUsageSessionUsedPercent": snCamUsageSessionUsedPercent,
       "snCamUsageOtherTable": snCamUsageOtherTable,
       "snCamUsageOtherEntry": snCamUsageOtherEntry,
       "snCamUsageOtherSlot": snCamUsageOtherSlot,
       "snCamUsageOtherProcessor": snCamUsageOtherProcessor,
       "snCamUsageOtherType": snCamUsageOtherType,
       "snCamUsageOtherSize": snCamUsageOtherSize,
       "snCamUsageOtherFree": snCamUsageOtherFree,
       "snCamUsageOtherUsedPercent": snCamUsageOtherUsedPercent}
)
