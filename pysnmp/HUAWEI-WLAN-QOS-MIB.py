# SNMP MIB module (HUAWEI-WLAN-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-WLAN-QOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:41 2024
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

(hwWlan,) = mibBuilder.importSymbols(
    "HUAWEI-WLAN-MIB",
    "hwWlan")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwWlanQosManagement = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5)
)
hwWlanQosManagement.setRevisions(
        ("2010-10-12 10:00",
         "2010-06-01 10:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwWlanWmmProfileTable_Object = MibTable
hwWlanWmmProfileTable = _HwWlanWmmProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1)
)
if mibBuilder.loadTexts:
    hwWlanWmmProfileTable.setStatus("current")
_HwWlanWmmProfileEntry_Object = MibTableRow
hwWlanWmmProfileEntry = _HwWlanWmmProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1)
)
hwWlanWmmProfileEntry.setIndexNames(
    (0, "HUAWEI-WLAN-QOS-MIB", "hwWlanWmmProfileName"),
)
if mibBuilder.loadTexts:
    hwWlanWmmProfileEntry.setStatus("current")


class _HwWlanWmmProfileName_Type(OctetString):
    """Custom type hwWlanWmmProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwWlanWmmProfileName_Type.__name__ = "OctetString"
_HwWlanWmmProfileName_Object = MibTableColumn
hwWlanWmmProfileName = _HwWlanWmmProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 1),
    _HwWlanWmmProfileName_Type()
)
hwWlanWmmProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwWlanWmmProfileName.setStatus("current")


class _HwWlanWmmSwitch_Type(Integer32):
    """Custom type hwWlanWmmSwitch based on Integer32"""
    defaultValue = 1

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


_HwWlanWmmSwitch_Type.__name__ = "Integer32"
_HwWlanWmmSwitch_Object = MibTableColumn
hwWlanWmmSwitch = _HwWlanWmmSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 2),
    _HwWlanWmmSwitch_Type()
)
hwWlanWmmSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlanWmmSwitch.setStatus("current")


class _HwWlanWmmMandatorySwitch_Type(Integer32):
    """Custom type hwWlanWmmMandatorySwitch based on Integer32"""
    defaultValue = 2

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


_HwWlanWmmMandatorySwitch_Type.__name__ = "Integer32"
_HwWlanWmmMandatorySwitch_Object = MibTableColumn
hwWlanWmmMandatorySwitch = _HwWlanWmmMandatorySwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 3),
    _HwWlanWmmMandatorySwitch_Type()
)
hwWlanWmmMandatorySwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlanWmmMandatorySwitch.setStatus("current")
_HwWlanWmmProfileRowStatus_Type = RowStatus
_HwWlanWmmProfileRowStatus_Object = MibTableColumn
hwWlanWmmProfileRowStatus = _HwWlanWmmProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 4),
    _HwWlanWmmProfileRowStatus_Type()
)
hwWlanWmmProfileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanWmmProfileRowStatus.setStatus("current")


class _HwQAPEDCAVoiceECWmax_Type(Integer32):
    """Custom type hwQAPEDCAVoiceECWmax based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HwQAPEDCAVoiceECWmax_Type.__name__ = "Integer32"
_HwQAPEDCAVoiceECWmax_Object = MibTableColumn
hwQAPEDCAVoiceECWmax = _HwQAPEDCAVoiceECWmax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 5),
    _HwQAPEDCAVoiceECWmax_Type()
)
hwQAPEDCAVoiceECWmax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQAPEDCAVoiceECWmax.setStatus("current")


class _HwQAPEDCAVoiceECWmin_Type(Integer32):
    """Custom type hwQAPEDCAVoiceECWmin based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HwQAPEDCAVoiceECWmin_Type.__name__ = "Integer32"
_HwQAPEDCAVoiceECWmin_Object = MibTableColumn
hwQAPEDCAVoiceECWmin = _HwQAPEDCAVoiceECWmin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 6),
    _HwQAPEDCAVoiceECWmin_Type()
)
hwQAPEDCAVoiceECWmin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQAPEDCAVoiceECWmin.setStatus("current")


class _HwQAPEDCAVoiceAIFSN_Type(Integer32):
    """Custom type hwQAPEDCAVoiceAIFSN based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_HwQAPEDCAVoiceAIFSN_Type.__name__ = "Integer32"
_HwQAPEDCAVoiceAIFSN_Object = MibTableColumn
hwQAPEDCAVoiceAIFSN = _HwQAPEDCAVoiceAIFSN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 7),
    _HwQAPEDCAVoiceAIFSN_Type()
)
hwQAPEDCAVoiceAIFSN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQAPEDCAVoiceAIFSN.setStatus("current")


class _HwQAPEDCAVoiceTXOPLimit_Type(Integer32):
    """Custom type hwQAPEDCAVoiceTXOPLimit based on Integer32"""
    defaultValue = 47

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwQAPEDCAVoiceTXOPLimit_Type.__name__ = "Integer32"
_HwQAPEDCAVoiceTXOPLimit_Object = MibTableColumn
hwQAPEDCAVoiceTXOPLimit = _HwQAPEDCAVoiceTXOPLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 8),
    _HwQAPEDCAVoiceTXOPLimit_Type()
)
hwQAPEDCAVoiceTXOPLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQAPEDCAVoiceTXOPLimit.setStatus("current")


class _HwQAPEDCAVoiceACKPolicy_Type(Integer32):
    """Custom type hwQAPEDCAVoiceACKPolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noack", 2),
          ("normal", 1))
    )


_HwQAPEDCAVoiceACKPolicy_Type.__name__ = "Integer32"
_HwQAPEDCAVoiceACKPolicy_Object = MibTableColumn
hwQAPEDCAVoiceACKPolicy = _HwQAPEDCAVoiceACKPolicy_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 9),
    _HwQAPEDCAVoiceACKPolicy_Type()
)
hwQAPEDCAVoiceACKPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQAPEDCAVoiceACKPolicy.setStatus("current")


class _HwQAPEDCAVideoECWmax_Type(Integer32):
    """Custom type hwQAPEDCAVideoECWmax based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HwQAPEDCAVideoECWmax_Type.__name__ = "Integer32"
_HwQAPEDCAVideoECWmax_Object = MibTableColumn
hwQAPEDCAVideoECWmax = _HwQAPEDCAVideoECWmax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 10),
    _HwQAPEDCAVideoECWmax_Type()
)
hwQAPEDCAVideoECWmax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQAPEDCAVideoECWmax.setStatus("current")


class _HwQAPEDCAVideoECWmin_Type(Integer32):
    """Custom type hwQAPEDCAVideoECWmin based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HwQAPEDCAVideoECWmin_Type.__name__ = "Integer32"
_HwQAPEDCAVideoECWmin_Object = MibTableColumn
hwQAPEDCAVideoECWmin = _HwQAPEDCAVideoECWmin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 11),
    _HwQAPEDCAVideoECWmin_Type()
)
hwQAPEDCAVideoECWmin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQAPEDCAVideoECWmin.setStatus("current")


class _HwQAPEDCAVideoAIFSN_Type(Integer32):
    """Custom type hwQAPEDCAVideoAIFSN based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_HwQAPEDCAVideoAIFSN_Type.__name__ = "Integer32"
_HwQAPEDCAVideoAIFSN_Object = MibTableColumn
hwQAPEDCAVideoAIFSN = _HwQAPEDCAVideoAIFSN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 12),
    _HwQAPEDCAVideoAIFSN_Type()
)
hwQAPEDCAVideoAIFSN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQAPEDCAVideoAIFSN.setStatus("current")


class _HwQAPEDCAVideoTXOPLimit_Type(Integer32):
    """Custom type hwQAPEDCAVideoTXOPLimit based on Integer32"""
    defaultValue = 94

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwQAPEDCAVideoTXOPLimit_Type.__name__ = "Integer32"
_HwQAPEDCAVideoTXOPLimit_Object = MibTableColumn
hwQAPEDCAVideoTXOPLimit = _HwQAPEDCAVideoTXOPLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 13),
    _HwQAPEDCAVideoTXOPLimit_Type()
)
hwQAPEDCAVideoTXOPLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQAPEDCAVideoTXOPLimit.setStatus("current")


class _HwQAPEDCAVideoACKPolicy_Type(Integer32):
    """Custom type hwQAPEDCAVideoACKPolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noack", 2),
          ("normal", 1))
    )


_HwQAPEDCAVideoACKPolicy_Type.__name__ = "Integer32"
_HwQAPEDCAVideoACKPolicy_Object = MibTableColumn
hwQAPEDCAVideoACKPolicy = _HwQAPEDCAVideoACKPolicy_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 14),
    _HwQAPEDCAVideoACKPolicy_Type()
)
hwQAPEDCAVideoACKPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQAPEDCAVideoACKPolicy.setStatus("current")


class _HwQAPEDCABEECWmax_Type(Integer32):
    """Custom type hwQAPEDCABEECWmax based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HwQAPEDCABEECWmax_Type.__name__ = "Integer32"
_HwQAPEDCABEECWmax_Object = MibTableColumn
hwQAPEDCABEECWmax = _HwQAPEDCABEECWmax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 15),
    _HwQAPEDCABEECWmax_Type()
)
hwQAPEDCABEECWmax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQAPEDCABEECWmax.setStatus("current")


class _HwQAPEDCABEECWmin_Type(Integer32):
    """Custom type hwQAPEDCABEECWmin based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HwQAPEDCABEECWmin_Type.__name__ = "Integer32"
_HwQAPEDCABEECWmin_Object = MibTableColumn
hwQAPEDCABEECWmin = _HwQAPEDCABEECWmin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 16),
    _HwQAPEDCABEECWmin_Type()
)
hwQAPEDCABEECWmin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQAPEDCABEECWmin.setStatus("current")


class _HwQAPEDCABEAIFSN_Type(Integer32):
    """Custom type hwQAPEDCABEAIFSN based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_HwQAPEDCABEAIFSN_Type.__name__ = "Integer32"
_HwQAPEDCABEAIFSN_Object = MibTableColumn
hwQAPEDCABEAIFSN = _HwQAPEDCABEAIFSN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 17),
    _HwQAPEDCABEAIFSN_Type()
)
hwQAPEDCABEAIFSN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQAPEDCABEAIFSN.setStatus("current")


class _HwQAPEDCABETXOPLimit_Type(Integer32):
    """Custom type hwQAPEDCABETXOPLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwQAPEDCABETXOPLimit_Type.__name__ = "Integer32"
_HwQAPEDCABETXOPLimit_Object = MibTableColumn
hwQAPEDCABETXOPLimit = _HwQAPEDCABETXOPLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 18),
    _HwQAPEDCABETXOPLimit_Type()
)
hwQAPEDCABETXOPLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQAPEDCABETXOPLimit.setStatus("current")


class _HwQAPEDCABEACKPolicy_Type(Integer32):
    """Custom type hwQAPEDCABEACKPolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noack", 2),
          ("normal", 1))
    )


_HwQAPEDCABEACKPolicy_Type.__name__ = "Integer32"
_HwQAPEDCABEACKPolicy_Object = MibTableColumn
hwQAPEDCABEACKPolicy = _HwQAPEDCABEACKPolicy_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 19),
    _HwQAPEDCABEACKPolicy_Type()
)
hwQAPEDCABEACKPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQAPEDCABEACKPolicy.setStatus("current")


class _HwQAPEDCABKECWmax_Type(Integer32):
    """Custom type hwQAPEDCABKECWmax based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HwQAPEDCABKECWmax_Type.__name__ = "Integer32"
_HwQAPEDCABKECWmax_Object = MibTableColumn
hwQAPEDCABKECWmax = _HwQAPEDCABKECWmax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 20),
    _HwQAPEDCABKECWmax_Type()
)
hwQAPEDCABKECWmax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQAPEDCABKECWmax.setStatus("current")


class _HwQAPEDCABKECWmin_Type(Integer32):
    """Custom type hwQAPEDCABKECWmin based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HwQAPEDCABKECWmin_Type.__name__ = "Integer32"
_HwQAPEDCABKECWmin_Object = MibTableColumn
hwQAPEDCABKECWmin = _HwQAPEDCABKECWmin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 21),
    _HwQAPEDCABKECWmin_Type()
)
hwQAPEDCABKECWmin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQAPEDCABKECWmin.setStatus("current")


class _HwQAPEDCABKAIFSN_Type(Integer32):
    """Custom type hwQAPEDCABKAIFSN based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_HwQAPEDCABKAIFSN_Type.__name__ = "Integer32"
_HwQAPEDCABKAIFSN_Object = MibTableColumn
hwQAPEDCABKAIFSN = _HwQAPEDCABKAIFSN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 22),
    _HwQAPEDCABKAIFSN_Type()
)
hwQAPEDCABKAIFSN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQAPEDCABKAIFSN.setStatus("current")


class _HwQAPEDCABKTXOPLimit_Type(Integer32):
    """Custom type hwQAPEDCABKTXOPLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwQAPEDCABKTXOPLimit_Type.__name__ = "Integer32"
_HwQAPEDCABKTXOPLimit_Object = MibTableColumn
hwQAPEDCABKTXOPLimit = _HwQAPEDCABKTXOPLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 23),
    _HwQAPEDCABKTXOPLimit_Type()
)
hwQAPEDCABKTXOPLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQAPEDCABKTXOPLimit.setStatus("current")


class _HwQAPEDCABKACKPolicy_Type(Integer32):
    """Custom type hwQAPEDCABKACKPolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noack", 2),
          ("normal", 1))
    )


_HwQAPEDCABKACKPolicy_Type.__name__ = "Integer32"
_HwQAPEDCABKACKPolicy_Object = MibTableColumn
hwQAPEDCABKACKPolicy = _HwQAPEDCABKACKPolicy_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 24),
    _HwQAPEDCABKACKPolicy_Type()
)
hwQAPEDCABKACKPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQAPEDCABKACKPolicy.setStatus("current")


class _HwQClientEDCAVoiceECWmax_Type(Integer32):
    """Custom type hwQClientEDCAVoiceECWmax based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HwQClientEDCAVoiceECWmax_Type.__name__ = "Integer32"
_HwQClientEDCAVoiceECWmax_Object = MibTableColumn
hwQClientEDCAVoiceECWmax = _HwQClientEDCAVoiceECWmax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 25),
    _HwQClientEDCAVoiceECWmax_Type()
)
hwQClientEDCAVoiceECWmax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQClientEDCAVoiceECWmax.setStatus("current")


class _HwQClientEDCAVoiceECWmin_Type(Integer32):
    """Custom type hwQClientEDCAVoiceECWmin based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HwQClientEDCAVoiceECWmin_Type.__name__ = "Integer32"
_HwQClientEDCAVoiceECWmin_Object = MibTableColumn
hwQClientEDCAVoiceECWmin = _HwQClientEDCAVoiceECWmin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 26),
    _HwQClientEDCAVoiceECWmin_Type()
)
hwQClientEDCAVoiceECWmin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQClientEDCAVoiceECWmin.setStatus("current")


class _HwQClientEDCAVoiceAIFSN_Type(Integer32):
    """Custom type hwQClientEDCAVoiceAIFSN based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_HwQClientEDCAVoiceAIFSN_Type.__name__ = "Integer32"
_HwQClientEDCAVoiceAIFSN_Object = MibTableColumn
hwQClientEDCAVoiceAIFSN = _HwQClientEDCAVoiceAIFSN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 27),
    _HwQClientEDCAVoiceAIFSN_Type()
)
hwQClientEDCAVoiceAIFSN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQClientEDCAVoiceAIFSN.setStatus("current")


class _HwQClientEDCAVoiceTXOPLimit_Type(Integer32):
    """Custom type hwQClientEDCAVoiceTXOPLimit based on Integer32"""
    defaultValue = 47

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwQClientEDCAVoiceTXOPLimit_Type.__name__ = "Integer32"
_HwQClientEDCAVoiceTXOPLimit_Object = MibTableColumn
hwQClientEDCAVoiceTXOPLimit = _HwQClientEDCAVoiceTXOPLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 28),
    _HwQClientEDCAVoiceTXOPLimit_Type()
)
hwQClientEDCAVoiceTXOPLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQClientEDCAVoiceTXOPLimit.setStatus("current")


class _HwQClientEDCAVideoECWmax_Type(Integer32):
    """Custom type hwQClientEDCAVideoECWmax based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HwQClientEDCAVideoECWmax_Type.__name__ = "Integer32"
_HwQClientEDCAVideoECWmax_Object = MibTableColumn
hwQClientEDCAVideoECWmax = _HwQClientEDCAVideoECWmax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 29),
    _HwQClientEDCAVideoECWmax_Type()
)
hwQClientEDCAVideoECWmax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQClientEDCAVideoECWmax.setStatus("current")


class _HwQClientEDCAVideoECWmin_Type(Integer32):
    """Custom type hwQClientEDCAVideoECWmin based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HwQClientEDCAVideoECWmin_Type.__name__ = "Integer32"
_HwQClientEDCAVideoECWmin_Object = MibTableColumn
hwQClientEDCAVideoECWmin = _HwQClientEDCAVideoECWmin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 30),
    _HwQClientEDCAVideoECWmin_Type()
)
hwQClientEDCAVideoECWmin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQClientEDCAVideoECWmin.setStatus("current")


class _HwQClientEDCAVideoAIFSN_Type(Integer32):
    """Custom type hwQClientEDCAVideoAIFSN based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_HwQClientEDCAVideoAIFSN_Type.__name__ = "Integer32"
_HwQClientEDCAVideoAIFSN_Object = MibTableColumn
hwQClientEDCAVideoAIFSN = _HwQClientEDCAVideoAIFSN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 31),
    _HwQClientEDCAVideoAIFSN_Type()
)
hwQClientEDCAVideoAIFSN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQClientEDCAVideoAIFSN.setStatus("current")


class _HwQClientEDCAVideoTXOPLimit_Type(Integer32):
    """Custom type hwQClientEDCAVideoTXOPLimit based on Integer32"""
    defaultValue = 94

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwQClientEDCAVideoTXOPLimit_Type.__name__ = "Integer32"
_HwQClientEDCAVideoTXOPLimit_Object = MibTableColumn
hwQClientEDCAVideoTXOPLimit = _HwQClientEDCAVideoTXOPLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 32),
    _HwQClientEDCAVideoTXOPLimit_Type()
)
hwQClientEDCAVideoTXOPLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQClientEDCAVideoTXOPLimit.setStatus("current")


class _HwQClientEDCABEECWmax_Type(Integer32):
    """Custom type hwQClientEDCABEECWmax based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HwQClientEDCABEECWmax_Type.__name__ = "Integer32"
_HwQClientEDCABEECWmax_Object = MibTableColumn
hwQClientEDCABEECWmax = _HwQClientEDCABEECWmax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 33),
    _HwQClientEDCABEECWmax_Type()
)
hwQClientEDCABEECWmax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQClientEDCABEECWmax.setStatus("current")


class _HwQClientEDCABEECWmin_Type(Integer32):
    """Custom type hwQClientEDCABEECWmin based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HwQClientEDCABEECWmin_Type.__name__ = "Integer32"
_HwQClientEDCABEECWmin_Object = MibTableColumn
hwQClientEDCABEECWmin = _HwQClientEDCABEECWmin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 34),
    _HwQClientEDCABEECWmin_Type()
)
hwQClientEDCABEECWmin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQClientEDCABEECWmin.setStatus("current")


class _HwQClientEDCABEAIFSN_Type(Integer32):
    """Custom type hwQClientEDCABEAIFSN based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_HwQClientEDCABEAIFSN_Type.__name__ = "Integer32"
_HwQClientEDCABEAIFSN_Object = MibTableColumn
hwQClientEDCABEAIFSN = _HwQClientEDCABEAIFSN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 35),
    _HwQClientEDCABEAIFSN_Type()
)
hwQClientEDCABEAIFSN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQClientEDCABEAIFSN.setStatus("current")


class _HwQClientEDCABETXOPLimit_Type(Integer32):
    """Custom type hwQClientEDCABETXOPLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwQClientEDCABETXOPLimit_Type.__name__ = "Integer32"
_HwQClientEDCABETXOPLimit_Object = MibTableColumn
hwQClientEDCABETXOPLimit = _HwQClientEDCABETXOPLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 36),
    _HwQClientEDCABETXOPLimit_Type()
)
hwQClientEDCABETXOPLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQClientEDCABETXOPLimit.setStatus("current")


class _HwQClientEDCABKECWmax_Type(Integer32):
    """Custom type hwQClientEDCABKECWmax based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HwQClientEDCABKECWmax_Type.__name__ = "Integer32"
_HwQClientEDCABKECWmax_Object = MibTableColumn
hwQClientEDCABKECWmax = _HwQClientEDCABKECWmax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 37),
    _HwQClientEDCABKECWmax_Type()
)
hwQClientEDCABKECWmax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQClientEDCABKECWmax.setStatus("current")


class _HwQClientEDCABKECWmin_Type(Integer32):
    """Custom type hwQClientEDCABKECWmin based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HwQClientEDCABKECWmin_Type.__name__ = "Integer32"
_HwQClientEDCABKECWmin_Object = MibTableColumn
hwQClientEDCABKECWmin = _HwQClientEDCABKECWmin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 38),
    _HwQClientEDCABKECWmin_Type()
)
hwQClientEDCABKECWmin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQClientEDCABKECWmin.setStatus("current")


class _HwQClientEDCABKAIFSN_Type(Integer32):
    """Custom type hwQClientEDCABKAIFSN based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_HwQClientEDCABKAIFSN_Type.__name__ = "Integer32"
_HwQClientEDCABKAIFSN_Object = MibTableColumn
hwQClientEDCABKAIFSN = _HwQClientEDCABKAIFSN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 39),
    _HwQClientEDCABKAIFSN_Type()
)
hwQClientEDCABKAIFSN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQClientEDCABKAIFSN.setStatus("current")


class _HwQClientEDCABKTXOPLimit_Type(Integer32):
    """Custom type hwQClientEDCABKTXOPLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwQClientEDCABKTXOPLimit_Type.__name__ = "Integer32"
_HwQClientEDCABKTXOPLimit_Object = MibTableColumn
hwQClientEDCABKTXOPLimit = _HwQClientEDCABKTXOPLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 40),
    _HwQClientEDCABKTXOPLimit_Type()
)
hwQClientEDCABKTXOPLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQClientEDCABKTXOPLimit.setStatus("current")
_HwWlanTrafficProfileTable_Object = MibTable
hwWlanTrafficProfileTable = _HwWlanTrafficProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2)
)
if mibBuilder.loadTexts:
    hwWlanTrafficProfileTable.setStatus("current")
_HwWlanTrafficProfileEntry_Object = MibTableRow
hwWlanTrafficProfileEntry = _HwWlanTrafficProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1)
)
hwWlanTrafficProfileEntry.setIndexNames(
    (0, "HUAWEI-WLAN-QOS-MIB", "hwWlanTrafficProfileName"),
)
if mibBuilder.loadTexts:
    hwWlanTrafficProfileEntry.setStatus("current")


class _HwWlanTrafficProfileName_Type(OctetString):
    """Custom type hwWlanTrafficProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwWlanTrafficProfileName_Type.__name__ = "OctetString"
_HwWlanTrafficProfileName_Object = MibTableColumn
hwWlanTrafficProfileName = _HwWlanTrafficProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 1),
    _HwWlanTrafficProfileName_Type()
)
hwWlanTrafficProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwWlanTrafficProfileName.setStatus("current")
_HwWlanTrafficProfileRowStatus_Type = RowStatus
_HwWlanTrafficProfileRowStatus_Object = MibTableColumn
hwWlanTrafficProfileRowStatus = _HwWlanTrafficProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 2),
    _HwWlanTrafficProfileRowStatus_Type()
)
hwWlanTrafficProfileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanTrafficProfileRowStatus.setStatus("current")
_HwWlanClientUpLimitRate_Type = Unsigned32
_HwWlanClientUpLimitRate_Object = MibTableColumn
hwWlanClientUpLimitRate = _HwWlanClientUpLimitRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 3),
    _HwWlanClientUpLimitRate_Type()
)
hwWlanClientUpLimitRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlanClientUpLimitRate.setStatus("current")
_HwWlanVAPUpLimitRate_Type = Unsigned32
_HwWlanVAPUpLimitRate_Object = MibTableColumn
hwWlanVAPUpLimitRate = _HwWlanVAPUpLimitRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 4),
    _HwWlanVAPUpLimitRate_Type()
)
hwWlanVAPUpLimitRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlanVAPUpLimitRate.setStatus("current")


class _HwWlan8021pMapMode_Type(Integer32):
    """Custom type hwWlan8021pMapMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("designate", 1),
          ("mapping", 2))
    )


_HwWlan8021pMapMode_Type.__name__ = "Integer32"
_HwWlan8021pMapMode_Object = MibTableColumn
hwWlan8021pMapMode = _HwWlan8021pMapMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 5),
    _HwWlan8021pMapMode_Type()
)
hwWlan8021pMapMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlan8021pMapMode.setStatus("current")


class _HwWlan8021pSpecValue_Type(Integer32):
    """Custom type hwWlan8021pSpecValue based on Integer32"""
    defaultValue = 0


_HwWlan8021pSpecValue_Object = MibTableColumn
hwWlan8021pSpecValue = _HwWlan8021pSpecValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 6),
    _HwWlan8021pSpecValue_Type()
)
hwWlan8021pSpecValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlan8021pSpecValue.setStatus("current")


class _HwWlanUP0Map8021p_Type(Integer32):
    """Custom type hwWlanUP0Map8021p based on Integer32"""
    defaultValue = 0


_HwWlanUP0Map8021p_Object = MibTableColumn
hwWlanUP0Map8021p = _HwWlanUP0Map8021p_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 7),
    _HwWlanUP0Map8021p_Type()
)
hwWlanUP0Map8021p.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlanUP0Map8021p.setStatus("current")


class _HwWlanUP1Map8021p_Type(Integer32):
    """Custom type hwWlanUP1Map8021p based on Integer32"""
    defaultValue = 1


_HwWlanUP1Map8021p_Object = MibTableColumn
hwWlanUP1Map8021p = _HwWlanUP1Map8021p_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 8),
    _HwWlanUP1Map8021p_Type()
)
hwWlanUP1Map8021p.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlanUP1Map8021p.setStatus("current")


class _HwWlanUP2Map8021p_Type(Integer32):
    """Custom type hwWlanUP2Map8021p based on Integer32"""
    defaultValue = 2


_HwWlanUP2Map8021p_Object = MibTableColumn
hwWlanUP2Map8021p = _HwWlanUP2Map8021p_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 9),
    _HwWlanUP2Map8021p_Type()
)
hwWlanUP2Map8021p.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlanUP2Map8021p.setStatus("current")


class _HwWlanUP3Map8021p_Type(Integer32):
    """Custom type hwWlanUP3Map8021p based on Integer32"""
    defaultValue = 3


_HwWlanUP3Map8021p_Object = MibTableColumn
hwWlanUP3Map8021p = _HwWlanUP3Map8021p_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 10),
    _HwWlanUP3Map8021p_Type()
)
hwWlanUP3Map8021p.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlanUP3Map8021p.setStatus("current")


class _HwWlanUP4Map8021p_Type(Integer32):
    """Custom type hwWlanUP4Map8021p based on Integer32"""
    defaultValue = 4


_HwWlanUP4Map8021p_Object = MibTableColumn
hwWlanUP4Map8021p = _HwWlanUP4Map8021p_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 11),
    _HwWlanUP4Map8021p_Type()
)
hwWlanUP4Map8021p.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlanUP4Map8021p.setStatus("current")


class _HwWlanUP5Map8021p_Type(Integer32):
    """Custom type hwWlanUP5Map8021p based on Integer32"""
    defaultValue = 5


_HwWlanUP5Map8021p_Object = MibTableColumn
hwWlanUP5Map8021p = _HwWlanUP5Map8021p_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 12),
    _HwWlanUP5Map8021p_Type()
)
hwWlanUP5Map8021p.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlanUP5Map8021p.setStatus("current")


class _HwWlanUP6Map8021p_Type(Integer32):
    """Custom type hwWlanUP6Map8021p based on Integer32"""
    defaultValue = 6


_HwWlanUP6Map8021p_Object = MibTableColumn
hwWlanUP6Map8021p = _HwWlanUP6Map8021p_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 13),
    _HwWlanUP6Map8021p_Type()
)
hwWlanUP6Map8021p.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlanUP6Map8021p.setStatus("current")


class _HwWlanUP7Map8021p_Type(Integer32):
    """Custom type hwWlanUP7Map8021p based on Integer32"""
    defaultValue = 7


_HwWlanUP7Map8021p_Object = MibTableColumn
hwWlanUP7Map8021p = _HwWlanUP7Map8021p_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 14),
    _HwWlanUP7Map8021p_Type()
)
hwWlanUP7Map8021p.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlanUP7Map8021p.setStatus("current")


class _HwWlan8021p0MapUPValue_Type(Integer32):
    """Custom type hwWlan8021p0MapUPValue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwWlan8021p0MapUPValue_Type.__name__ = "Integer32"
_HwWlan8021p0MapUPValue_Object = MibTableColumn
hwWlan8021p0MapUPValue = _HwWlan8021p0MapUPValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 15),
    _HwWlan8021p0MapUPValue_Type()
)
hwWlan8021p0MapUPValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlan8021p0MapUPValue.setStatus("current")


class _HwWlan8021p1MapUPValue_Type(Integer32):
    """Custom type hwWlan8021p1MapUPValue based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwWlan8021p1MapUPValue_Type.__name__ = "Integer32"
_HwWlan8021p1MapUPValue_Object = MibTableColumn
hwWlan8021p1MapUPValue = _HwWlan8021p1MapUPValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 16),
    _HwWlan8021p1MapUPValue_Type()
)
hwWlan8021p1MapUPValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlan8021p1MapUPValue.setStatus("current")


class _HwWlan8021p2MapUPValue_Type(Integer32):
    """Custom type hwWlan8021p2MapUPValue based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwWlan8021p2MapUPValue_Type.__name__ = "Integer32"
_HwWlan8021p2MapUPValue_Object = MibTableColumn
hwWlan8021p2MapUPValue = _HwWlan8021p2MapUPValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 17),
    _HwWlan8021p2MapUPValue_Type()
)
hwWlan8021p2MapUPValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlan8021p2MapUPValue.setStatus("current")


class _HwWlan8021p3MapUPValue_Type(Integer32):
    """Custom type hwWlan8021p3MapUPValue based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwWlan8021p3MapUPValue_Type.__name__ = "Integer32"
_HwWlan8021p3MapUPValue_Object = MibTableColumn
hwWlan8021p3MapUPValue = _HwWlan8021p3MapUPValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 18),
    _HwWlan8021p3MapUPValue_Type()
)
hwWlan8021p3MapUPValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlan8021p3MapUPValue.setStatus("current")


class _HwWlan8021p4MapUPValue_Type(Integer32):
    """Custom type hwWlan8021p4MapUPValue based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwWlan8021p4MapUPValue_Type.__name__ = "Integer32"
_HwWlan8021p4MapUPValue_Object = MibTableColumn
hwWlan8021p4MapUPValue = _HwWlan8021p4MapUPValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 19),
    _HwWlan8021p4MapUPValue_Type()
)
hwWlan8021p4MapUPValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlan8021p4MapUPValue.setStatus("current")


class _HwWlan8021p5MapUPValue_Type(Integer32):
    """Custom type hwWlan8021p5MapUPValue based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwWlan8021p5MapUPValue_Type.__name__ = "Integer32"
_HwWlan8021p5MapUPValue_Object = MibTableColumn
hwWlan8021p5MapUPValue = _HwWlan8021p5MapUPValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 20),
    _HwWlan8021p5MapUPValue_Type()
)
hwWlan8021p5MapUPValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlan8021p5MapUPValue.setStatus("current")


class _HwWlan8021p6MapUPValue_Type(Integer32):
    """Custom type hwWlan8021p6MapUPValue based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwWlan8021p6MapUPValue_Type.__name__ = "Integer32"
_HwWlan8021p6MapUPValue_Object = MibTableColumn
hwWlan8021p6MapUPValue = _HwWlan8021p6MapUPValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 21),
    _HwWlan8021p6MapUPValue_Type()
)
hwWlan8021p6MapUPValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlan8021p6MapUPValue.setStatus("current")


class _HwWlan8021p7MapUPValue_Type(Integer32):
    """Custom type hwWlan8021p7MapUPValue based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwWlan8021p7MapUPValue_Type.__name__ = "Integer32"
_HwWlan8021p7MapUPValue_Object = MibTableColumn
hwWlan8021p7MapUPValue = _HwWlan8021p7MapUPValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 22),
    _HwWlan8021p7MapUPValue_Type()
)
hwWlan8021p7MapUPValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlan8021p7MapUPValue.setStatus("current")


class _HwWlanUpTunnelPriorityMapMode_Type(Integer32):
    """Custom type hwWlanUpTunnelPriorityMapMode based on Integer32"""
    defaultValue = 6

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
        *(("cos2cos", 3),
          ("cos2dscp", 4),
          ("dscp2cos", 5),
          ("dscp2dscp", 6),
          ("specCOS", 1),
          ("specDSCP", 2))
    )


_HwWlanUpTunnelPriorityMapMode_Type.__name__ = "Integer32"
_HwWlanUpTunnelPriorityMapMode_Object = MibTableColumn
hwWlanUpTunnelPriorityMapMode = _HwWlanUpTunnelPriorityMapMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 23),
    _HwWlanUpTunnelPriorityMapMode_Type()
)
hwWlanUpTunnelPriorityMapMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlanUpTunnelPriorityMapMode.setStatus("current")


class _HwWlanUpTunnelPrioritySpecValue_Type(Integer32):
    """Custom type hwWlanUpTunnelPrioritySpecValue based on Integer32"""
    defaultValue = 0


_HwWlanUpTunnelPrioritySpecValue_Object = MibTableColumn
hwWlanUpTunnelPrioritySpecValue = _HwWlanUpTunnelPrioritySpecValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 24),
    _HwWlanUpTunnelPrioritySpecValue_Type()
)
hwWlanUpTunnelPrioritySpecValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlanUpTunnelPrioritySpecValue.setStatus("current")


class _HwWlanValue0MapUpTunnelPriority_Type(Integer32):
    """Custom type hwWlanValue0MapUpTunnelPriority based on Integer32"""
    defaultValue = 0


_HwWlanValue0MapUpTunnelPriority_Object = MibTableColumn
hwWlanValue0MapUpTunnelPriority = _HwWlanValue0MapUpTunnelPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 25),
    _HwWlanValue0MapUpTunnelPriority_Type()
)
hwWlanValue0MapUpTunnelPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlanValue0MapUpTunnelPriority.setStatus("current")


class _HwWlanValue1MapUpTunnelPriority_Type(Integer32):
    """Custom type hwWlanValue1MapUpTunnelPriority based on Integer32"""
    defaultValue = 1


_HwWlanValue1MapUpTunnelPriority_Object = MibTableColumn
hwWlanValue1MapUpTunnelPriority = _HwWlanValue1MapUpTunnelPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 26),
    _HwWlanValue1MapUpTunnelPriority_Type()
)
hwWlanValue1MapUpTunnelPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlanValue1MapUpTunnelPriority.setStatus("current")


class _HwWlanValue2MapUpTunnelPriority_Type(Integer32):
    """Custom type hwWlanValue2MapUpTunnelPriority based on Integer32"""
    defaultValue = 2


_HwWlanValue2MapUpTunnelPriority_Object = MibTableColumn
hwWlanValue2MapUpTunnelPriority = _HwWlanValue2MapUpTunnelPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 27),
    _HwWlanValue2MapUpTunnelPriority_Type()
)
hwWlanValue2MapUpTunnelPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlanValue2MapUpTunnelPriority.setStatus("current")


class _HwWlanValue3MapUpTunnelPriority_Type(Integer32):
    """Custom type hwWlanValue3MapUpTunnelPriority based on Integer32"""
    defaultValue = 3


_HwWlanValue3MapUpTunnelPriority_Object = MibTableColumn
hwWlanValue3MapUpTunnelPriority = _HwWlanValue3MapUpTunnelPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 28),
    _HwWlanValue3MapUpTunnelPriority_Type()
)
hwWlanValue3MapUpTunnelPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlanValue3MapUpTunnelPriority.setStatus("current")


class _HwWlanValue4MapUpTunnelPriority_Type(Integer32):
    """Custom type hwWlanValue4MapUpTunnelPriority based on Integer32"""
    defaultValue = 4


_HwWlanValue4MapUpTunnelPriority_Object = MibTableColumn
hwWlanValue4MapUpTunnelPriority = _HwWlanValue4MapUpTunnelPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 29),
    _HwWlanValue4MapUpTunnelPriority_Type()
)
hwWlanValue4MapUpTunnelPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlanValue4MapUpTunnelPriority.setStatus("current")


class _HwWlanValue5MapUpTunnelPriority_Type(Integer32):
    """Custom type hwWlanValue5MapUpTunnelPriority based on Integer32"""
    defaultValue = 5


_HwWlanValue5MapUpTunnelPriority_Object = MibTableColumn
hwWlanValue5MapUpTunnelPriority = _HwWlanValue5MapUpTunnelPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 30),
    _HwWlanValue5MapUpTunnelPriority_Type()
)
hwWlanValue5MapUpTunnelPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlanValue5MapUpTunnelPriority.setStatus("current")


class _HwWlanValue6MapUpTunnelPriority_Type(Integer32):
    """Custom type hwWlanValue6MapUpTunnelPriority based on Integer32"""
    defaultValue = 6


_HwWlanValue6MapUpTunnelPriority_Object = MibTableColumn
hwWlanValue6MapUpTunnelPriority = _HwWlanValue6MapUpTunnelPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 31),
    _HwWlanValue6MapUpTunnelPriority_Type()
)
hwWlanValue6MapUpTunnelPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlanValue6MapUpTunnelPriority.setStatus("current")


class _HwWlanValue7MapUpTunnelPriority_Type(Integer32):
    """Custom type hwWlanValue7MapUpTunnelPriority based on Integer32"""
    defaultValue = 7


_HwWlanValue7MapUpTunnelPriority_Object = MibTableColumn
hwWlanValue7MapUpTunnelPriority = _HwWlanValue7MapUpTunnelPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 32),
    _HwWlanValue7MapUpTunnelPriority_Type()
)
hwWlanValue7MapUpTunnelPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlanValue7MapUpTunnelPriority.setStatus("current")


class _HwWlanDownTunnelPriorityMapMode_Type(Integer32):
    """Custom type hwWlanDownTunnelPriorityMapMode based on Integer32"""
    defaultValue = 6

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
        *(("cos2cos", 3),
          ("cos2dscp", 4),
          ("dscp2cos", 5),
          ("dscp2dscp", 6),
          ("specCOS", 1),
          ("specDSCP", 2))
    )


_HwWlanDownTunnelPriorityMapMode_Type.__name__ = "Integer32"
_HwWlanDownTunnelPriorityMapMode_Object = MibTableColumn
hwWlanDownTunnelPriorityMapMode = _HwWlanDownTunnelPriorityMapMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 33),
    _HwWlanDownTunnelPriorityMapMode_Type()
)
hwWlanDownTunnelPriorityMapMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlanDownTunnelPriorityMapMode.setStatus("current")


class _HwWlanDownTunnelPrioritySpecValue_Type(Integer32):
    """Custom type hwWlanDownTunnelPrioritySpecValue based on Integer32"""
    defaultValue = 0


_HwWlanDownTunnelPrioritySpecValue_Object = MibTableColumn
hwWlanDownTunnelPrioritySpecValue = _HwWlanDownTunnelPrioritySpecValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 34),
    _HwWlanDownTunnelPrioritySpecValue_Type()
)
hwWlanDownTunnelPrioritySpecValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlanDownTunnelPrioritySpecValue.setStatus("current")


class _HwWlanValue0MapDownTunnelPriority_Type(Integer32):
    """Custom type hwWlanValue0MapDownTunnelPriority based on Integer32"""
    defaultValue = 0


_HwWlanValue0MapDownTunnelPriority_Object = MibTableColumn
hwWlanValue0MapDownTunnelPriority = _HwWlanValue0MapDownTunnelPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 35),
    _HwWlanValue0MapDownTunnelPriority_Type()
)
hwWlanValue0MapDownTunnelPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlanValue0MapDownTunnelPriority.setStatus("current")


class _HwWlanValue1MapDownTunnelPriority_Type(Integer32):
    """Custom type hwWlanValue1MapDownTunnelPriority based on Integer32"""
    defaultValue = 1


_HwWlanValue1MapDownTunnelPriority_Object = MibTableColumn
hwWlanValue1MapDownTunnelPriority = _HwWlanValue1MapDownTunnelPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 36),
    _HwWlanValue1MapDownTunnelPriority_Type()
)
hwWlanValue1MapDownTunnelPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlanValue1MapDownTunnelPriority.setStatus("current")


class _HwWlanValue2MapDownTunnelPriority_Type(Integer32):
    """Custom type hwWlanValue2MapDownTunnelPriority based on Integer32"""
    defaultValue = 2


_HwWlanValue2MapDownTunnelPriority_Object = MibTableColumn
hwWlanValue2MapDownTunnelPriority = _HwWlanValue2MapDownTunnelPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 37),
    _HwWlanValue2MapDownTunnelPriority_Type()
)
hwWlanValue2MapDownTunnelPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlanValue2MapDownTunnelPriority.setStatus("current")


class _HwWlanValue3MapDownTunnelPriority_Type(Integer32):
    """Custom type hwWlanValue3MapDownTunnelPriority based on Integer32"""
    defaultValue = 7


_HwWlanValue3MapDownTunnelPriority_Object = MibTableColumn
hwWlanValue3MapDownTunnelPriority = _HwWlanValue3MapDownTunnelPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 38),
    _HwWlanValue3MapDownTunnelPriority_Type()
)
hwWlanValue3MapDownTunnelPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlanValue3MapDownTunnelPriority.setStatus("current")


class _HwWlanValue4MapDownTunnelPriority_Type(Integer32):
    """Custom type hwWlanValue4MapDownTunnelPriority based on Integer32"""
    defaultValue = 4


_HwWlanValue4MapDownTunnelPriority_Object = MibTableColumn
hwWlanValue4MapDownTunnelPriority = _HwWlanValue4MapDownTunnelPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 39),
    _HwWlanValue4MapDownTunnelPriority_Type()
)
hwWlanValue4MapDownTunnelPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlanValue4MapDownTunnelPriority.setStatus("current")


class _HwWlanValue5MapDownTunnelPriority_Type(Integer32):
    """Custom type hwWlanValue5MapDownTunnelPriority based on Integer32"""
    defaultValue = 5


_HwWlanValue5MapDownTunnelPriority_Object = MibTableColumn
hwWlanValue5MapDownTunnelPriority = _HwWlanValue5MapDownTunnelPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 40),
    _HwWlanValue5MapDownTunnelPriority_Type()
)
hwWlanValue5MapDownTunnelPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlanValue5MapDownTunnelPriority.setStatus("current")


class _HwWlanValue6MapDownTunnelPriority_Type(Integer32):
    """Custom type hwWlanValue6MapDownTunnelPriority based on Integer32"""
    defaultValue = 6


_HwWlanValue6MapDownTunnelPriority_Object = MibTableColumn
hwWlanValue6MapDownTunnelPriority = _HwWlanValue6MapDownTunnelPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 41),
    _HwWlanValue6MapDownTunnelPriority_Type()
)
hwWlanValue6MapDownTunnelPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlanValue6MapDownTunnelPriority.setStatus("current")


class _HwWlanValue7MapDownTunnelPriority_Type(Integer32):
    """Custom type hwWlanValue7MapDownTunnelPriority based on Integer32"""
    defaultValue = 7


_HwWlanValue7MapDownTunnelPriority_Object = MibTableColumn
hwWlanValue7MapDownTunnelPriority = _HwWlanValue7MapDownTunnelPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 42),
    _HwWlanValue7MapDownTunnelPriority_Type()
)
hwWlanValue7MapDownTunnelPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlanValue7MapDownTunnelPriority.setStatus("current")
_HwWlanClientDownLimitRate_Type = Unsigned32
_HwWlanClientDownLimitRate_Object = MibTableColumn
hwWlanClientDownLimitRate = _HwWlanClientDownLimitRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 43),
    _HwWlanClientDownLimitRate_Type()
)
hwWlanClientDownLimitRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlanClientDownLimitRate.setStatus("current")
_HwWlanVAPDownLimitRate_Type = Unsigned32
_HwWlanVAPDownLimitRate_Object = MibTableColumn
hwWlanVAPDownLimitRate = _HwWlanVAPDownLimitRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 44),
    _HwWlanVAPDownLimitRate_Type()
)
hwWlanVAPDownLimitRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlanVAPDownLimitRate.setStatus("current")


class _HwWlanTos0MapUPValue_Type(Integer32):
    """Custom type hwWlanTos0MapUPValue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwWlanTos0MapUPValue_Type.__name__ = "Integer32"
_HwWlanTos0MapUPValue_Object = MibTableColumn
hwWlanTos0MapUPValue = _HwWlanTos0MapUPValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 45),
    _HwWlanTos0MapUPValue_Type()
)
hwWlanTos0MapUPValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlanTos0MapUPValue.setStatus("current")


class _HwWlanTos1MapUPValue_Type(Integer32):
    """Custom type hwWlanTos1MapUPValue based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwWlanTos1MapUPValue_Type.__name__ = "Integer32"
_HwWlanTos1MapUPValue_Object = MibTableColumn
hwWlanTos1MapUPValue = _HwWlanTos1MapUPValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 46),
    _HwWlanTos1MapUPValue_Type()
)
hwWlanTos1MapUPValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlanTos1MapUPValue.setStatus("current")


class _HwWlanTos2MapUPValue_Type(Integer32):
    """Custom type hwWlanTos2MapUPValue based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwWlanTos2MapUPValue_Type.__name__ = "Integer32"
_HwWlanTos2MapUPValue_Object = MibTableColumn
hwWlanTos2MapUPValue = _HwWlanTos2MapUPValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 47),
    _HwWlanTos2MapUPValue_Type()
)
hwWlanTos2MapUPValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlanTos2MapUPValue.setStatus("current")


class _HwWlanTos3MapUPValue_Type(Integer32):
    """Custom type hwWlanTos3MapUPValue based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwWlanTos3MapUPValue_Type.__name__ = "Integer32"
_HwWlanTos3MapUPValue_Object = MibTableColumn
hwWlanTos3MapUPValue = _HwWlanTos3MapUPValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 48),
    _HwWlanTos3MapUPValue_Type()
)
hwWlanTos3MapUPValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlanTos3MapUPValue.setStatus("current")


class _HwWlanTos4MapUPValue_Type(Integer32):
    """Custom type hwWlanTos4MapUPValue based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwWlanTos4MapUPValue_Type.__name__ = "Integer32"
_HwWlanTos4MapUPValue_Object = MibTableColumn
hwWlanTos4MapUPValue = _HwWlanTos4MapUPValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 49),
    _HwWlanTos4MapUPValue_Type()
)
hwWlanTos4MapUPValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlanTos4MapUPValue.setStatus("current")


class _HwWlanTos5MapUPValue_Type(Integer32):
    """Custom type hwWlanTos5MapUPValue based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwWlanTos5MapUPValue_Type.__name__ = "Integer32"
_HwWlanTos5MapUPValue_Object = MibTableColumn
hwWlanTos5MapUPValue = _HwWlanTos5MapUPValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 50),
    _HwWlanTos5MapUPValue_Type()
)
hwWlanTos5MapUPValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlanTos5MapUPValue.setStatus("current")


class _HwWlanTos6MapUPValue_Type(Integer32):
    """Custom type hwWlanTos6MapUPValue based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwWlanTos6MapUPValue_Type.__name__ = "Integer32"
_HwWlanTos6MapUPValue_Object = MibTableColumn
hwWlanTos6MapUPValue = _HwWlanTos6MapUPValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 51),
    _HwWlanTos6MapUPValue_Type()
)
hwWlanTos6MapUPValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlanTos6MapUPValue.setStatus("current")


class _HwWlanTos7MapUPValue_Type(Integer32):
    """Custom type hwWlanTos7MapUPValue based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwWlanTos7MapUPValue_Type.__name__ = "Integer32"
_HwWlanTos7MapUPValue_Object = MibTableColumn
hwWlanTos7MapUPValue = _HwWlanTos7MapUPValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 52),
    _HwWlanTos7MapUPValue_Type()
)
hwWlanTos7MapUPValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlanTos7MapUPValue.setStatus("current")


class _HwWlanBatchWmmProfileStartNumber_Type(Integer32):
    """Custom type hwWlanBatchWmmProfileStartNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_HwWlanBatchWmmProfileStartNumber_Type.__name__ = "Integer32"
_HwWlanBatchWmmProfileStartNumber_Object = MibScalar
hwWlanBatchWmmProfileStartNumber = _HwWlanBatchWmmProfileStartNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 3),
    _HwWlanBatchWmmProfileStartNumber_Type()
)
hwWlanBatchWmmProfileStartNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanBatchWmmProfileStartNumber.setStatus("current")


class _HwWlanBatchWmmProfileGetNumber_Type(Integer32):
    """Custom type hwWlanBatchWmmProfileGetNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_HwWlanBatchWmmProfileGetNumber_Type.__name__ = "Integer32"
_HwWlanBatchWmmProfileGetNumber_Object = MibScalar
hwWlanBatchWmmProfileGetNumber = _HwWlanBatchWmmProfileGetNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 4),
    _HwWlanBatchWmmProfileGetNumber_Type()
)
hwWlanBatchWmmProfileGetNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanBatchWmmProfileGetNumber.setStatus("current")
_HwWlanBatchWmmProfileReturnNumber_Type = Integer32
_HwWlanBatchWmmProfileReturnNumber_Object = MibScalar
hwWlanBatchWmmProfileReturnNumber = _HwWlanBatchWmmProfileReturnNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 5),
    _HwWlanBatchWmmProfileReturnNumber_Type()
)
hwWlanBatchWmmProfileReturnNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanBatchWmmProfileReturnNumber.setStatus("current")
_HwWlanBatchWmmProfileName_Type = OctetString
_HwWlanBatchWmmProfileName_Object = MibScalar
hwWlanBatchWmmProfileName = _HwWlanBatchWmmProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 6),
    _HwWlanBatchWmmProfileName_Type()
)
hwWlanBatchWmmProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanBatchWmmProfileName.setStatus("current")


class _HwWlanBatchTrafficProfileStartNumber_Type(Integer32):
    """Custom type hwWlanBatchTrafficProfileStartNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_HwWlanBatchTrafficProfileStartNumber_Type.__name__ = "Integer32"
_HwWlanBatchTrafficProfileStartNumber_Object = MibScalar
hwWlanBatchTrafficProfileStartNumber = _HwWlanBatchTrafficProfileStartNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 7),
    _HwWlanBatchTrafficProfileStartNumber_Type()
)
hwWlanBatchTrafficProfileStartNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanBatchTrafficProfileStartNumber.setStatus("current")


class _HwWlanBatchTrafficProfileGetNumber_Type(Integer32):
    """Custom type hwWlanBatchTrafficProfileGetNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_HwWlanBatchTrafficProfileGetNumber_Type.__name__ = "Integer32"
_HwWlanBatchTrafficProfileGetNumber_Object = MibScalar
hwWlanBatchTrafficProfileGetNumber = _HwWlanBatchTrafficProfileGetNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 8),
    _HwWlanBatchTrafficProfileGetNumber_Type()
)
hwWlanBatchTrafficProfileGetNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanBatchTrafficProfileGetNumber.setStatus("current")
_HwWlanBatchTrafficProfileReturnNumber_Type = Integer32
_HwWlanBatchTrafficProfileReturnNumber_Object = MibScalar
hwWlanBatchTrafficProfileReturnNumber = _HwWlanBatchTrafficProfileReturnNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 9),
    _HwWlanBatchTrafficProfileReturnNumber_Type()
)
hwWlanBatchTrafficProfileReturnNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanBatchTrafficProfileReturnNumber.setStatus("current")
_HwWlanBatchTrafficProfileName_Type = OctetString
_HwWlanBatchTrafficProfileName_Object = MibScalar
hwWlanBatchTrafficProfileName = _HwWlanBatchTrafficProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 10),
    _HwWlanBatchTrafficProfileName_Type()
)
hwWlanBatchTrafficProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanBatchTrafficProfileName.setStatus("current")
_HwWlanQosManagementObjects_ObjectIdentity = ObjectIdentity
hwWlanQosManagementObjects = _HwWlanQosManagementObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 11)
)
_HwWlanQosManagementConformance_ObjectIdentity = ObjectIdentity
hwWlanQosManagementConformance = _HwWlanQosManagementConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 12)
)
_HwWlanQosManagementCompliances_ObjectIdentity = ObjectIdentity
hwWlanQosManagementCompliances = _HwWlanQosManagementCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 12, 1)
)
_HwWlanQosManagementObjectGroups_ObjectIdentity = ObjectIdentity
hwWlanQosManagementObjectGroups = _HwWlanQosManagementObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 12, 2)
)

# Managed Objects groups

hwWlanWmmProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 12, 2, 1)
)
hwWlanWmmProfileGroup.setObjects(
      *(("HUAWEI-WLAN-QOS-MIB", "hwWlanWmmSwitch"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlanWmmMandatorySwitch"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlanWmmProfileRowStatus"),
        ("HUAWEI-WLAN-QOS-MIB", "hwQAPEDCAVoiceECWmax"),
        ("HUAWEI-WLAN-QOS-MIB", "hwQAPEDCAVoiceECWmin"),
        ("HUAWEI-WLAN-QOS-MIB", "hwQAPEDCAVoiceAIFSN"),
        ("HUAWEI-WLAN-QOS-MIB", "hwQAPEDCAVoiceTXOPLimit"),
        ("HUAWEI-WLAN-QOS-MIB", "hwQAPEDCAVoiceACKPolicy"),
        ("HUAWEI-WLAN-QOS-MIB", "hwQAPEDCAVideoECWmax"),
        ("HUAWEI-WLAN-QOS-MIB", "hwQAPEDCAVideoECWmin"),
        ("HUAWEI-WLAN-QOS-MIB", "hwQAPEDCAVideoAIFSN"),
        ("HUAWEI-WLAN-QOS-MIB", "hwQAPEDCAVideoTXOPLimit"),
        ("HUAWEI-WLAN-QOS-MIB", "hwQAPEDCAVideoACKPolicy"),
        ("HUAWEI-WLAN-QOS-MIB", "hwQAPEDCABEECWmax"),
        ("HUAWEI-WLAN-QOS-MIB", "hwQAPEDCABEECWmin"),
        ("HUAWEI-WLAN-QOS-MIB", "hwQAPEDCABEAIFSN"),
        ("HUAWEI-WLAN-QOS-MIB", "hwQAPEDCABETXOPLimit"),
        ("HUAWEI-WLAN-QOS-MIB", "hwQAPEDCABEACKPolicy"),
        ("HUAWEI-WLAN-QOS-MIB", "hwQAPEDCABKECWmax"),
        ("HUAWEI-WLAN-QOS-MIB", "hwQAPEDCABKECWmin"),
        ("HUAWEI-WLAN-QOS-MIB", "hwQAPEDCABKAIFSN"),
        ("HUAWEI-WLAN-QOS-MIB", "hwQAPEDCABKTXOPLimit"),
        ("HUAWEI-WLAN-QOS-MIB", "hwQAPEDCABKACKPolicy"),
        ("HUAWEI-WLAN-QOS-MIB", "hwQClientEDCAVoiceECWmax"),
        ("HUAWEI-WLAN-QOS-MIB", "hwQClientEDCAVoiceECWmin"),
        ("HUAWEI-WLAN-QOS-MIB", "hwQClientEDCAVoiceAIFSN"),
        ("HUAWEI-WLAN-QOS-MIB", "hwQClientEDCAVoiceTXOPLimit"),
        ("HUAWEI-WLAN-QOS-MIB", "hwQClientEDCAVideoECWmax"),
        ("HUAWEI-WLAN-QOS-MIB", "hwQClientEDCAVideoECWmin"),
        ("HUAWEI-WLAN-QOS-MIB", "hwQClientEDCAVideoAIFSN"),
        ("HUAWEI-WLAN-QOS-MIB", "hwQClientEDCAVideoTXOPLimit"),
        ("HUAWEI-WLAN-QOS-MIB", "hwQClientEDCABEECWmax"),
        ("HUAWEI-WLAN-QOS-MIB", "hwQClientEDCABEECWmin"),
        ("HUAWEI-WLAN-QOS-MIB", "hwQClientEDCABEAIFSN"),
        ("HUAWEI-WLAN-QOS-MIB", "hwQClientEDCABETXOPLimit"),
        ("HUAWEI-WLAN-QOS-MIB", "hwQClientEDCABKECWmax"),
        ("HUAWEI-WLAN-QOS-MIB", "hwQClientEDCABKECWmin"),
        ("HUAWEI-WLAN-QOS-MIB", "hwQClientEDCABKAIFSN"),
        ("HUAWEI-WLAN-QOS-MIB", "hwQClientEDCABKTXOPLimit"))
)
if mibBuilder.loadTexts:
    hwWlanWmmProfileGroup.setStatus("current")

hwWlanTrafficProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 12, 2, 2)
)
hwWlanTrafficProfileGroup.setObjects(
      *(("HUAWEI-WLAN-QOS-MIB", "hwWlanTrafficProfileRowStatus"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlanClientUpLimitRate"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlanVAPUpLimitRate"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlan8021pMapMode"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlan8021pSpecValue"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlanUP0Map8021p"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlanUP1Map8021p"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlanUP2Map8021p"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlanUP3Map8021p"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlanUP4Map8021p"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlanUP5Map8021p"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlanUP6Map8021p"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlanUP7Map8021p"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlan8021p0MapUPValue"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlan8021p1MapUPValue"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlan8021p2MapUPValue"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlan8021p3MapUPValue"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlan8021p4MapUPValue"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlan8021p5MapUPValue"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlan8021p6MapUPValue"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlan8021p7MapUPValue"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlanUpTunnelPriorityMapMode"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlanUpTunnelPrioritySpecValue"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlanValue0MapUpTunnelPriority"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlanValue1MapUpTunnelPriority"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlanValue2MapUpTunnelPriority"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlanValue3MapUpTunnelPriority"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlanValue4MapUpTunnelPriority"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlanValue5MapUpTunnelPriority"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlanValue6MapUpTunnelPriority"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlanValue7MapUpTunnelPriority"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlanDownTunnelPriorityMapMode"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlanDownTunnelPrioritySpecValue"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlanValue0MapDownTunnelPriority"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlanValue1MapDownTunnelPriority"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlanValue2MapDownTunnelPriority"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlanValue3MapDownTunnelPriority"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlanValue4MapDownTunnelPriority"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlanValue5MapDownTunnelPriority"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlanValue6MapDownTunnelPriority"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlanValue7MapDownTunnelPriority"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlanClientDownLimitRate"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlanVAPDownLimitRate"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlanTos0MapUPValue"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlanTos1MapUPValue"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlanTos2MapUPValue"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlanTos3MapUPValue"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlanTos4MapUPValue"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlanTos5MapUPValue"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlanTos6MapUPValue"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlanTos7MapUPValue"))
)
if mibBuilder.loadTexts:
    hwWlanTrafficProfileGroup.setStatus("current")

hwWlanQosManagementGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 12, 2, 3)
)
hwWlanQosManagementGroup.setObjects(
      *(("HUAWEI-WLAN-QOS-MIB", "hwWlanBatchWmmProfileStartNumber"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlanBatchWmmProfileGetNumber"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlanBatchWmmProfileReturnNumber"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlanBatchWmmProfileName"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlanBatchTrafficProfileStartNumber"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlanBatchTrafficProfileGetNumber"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlanBatchTrafficProfileReturnNumber"),
        ("HUAWEI-WLAN-QOS-MIB", "hwWlanBatchTrafficProfileName"))
)
if mibBuilder.loadTexts:
    hwWlanQosManagementGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwWlanQosManagementCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 12, 1, 1)
)
if mibBuilder.loadTexts:
    hwWlanQosManagementCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-WLAN-QOS-MIB",
    **{"hwWlanQosManagement": hwWlanQosManagement,
       "hwWlanWmmProfileTable": hwWlanWmmProfileTable,
       "hwWlanWmmProfileEntry": hwWlanWmmProfileEntry,
       "hwWlanWmmProfileName": hwWlanWmmProfileName,
       "hwWlanWmmSwitch": hwWlanWmmSwitch,
       "hwWlanWmmMandatorySwitch": hwWlanWmmMandatorySwitch,
       "hwWlanWmmProfileRowStatus": hwWlanWmmProfileRowStatus,
       "hwQAPEDCAVoiceECWmax": hwQAPEDCAVoiceECWmax,
       "hwQAPEDCAVoiceECWmin": hwQAPEDCAVoiceECWmin,
       "hwQAPEDCAVoiceAIFSN": hwQAPEDCAVoiceAIFSN,
       "hwQAPEDCAVoiceTXOPLimit": hwQAPEDCAVoiceTXOPLimit,
       "hwQAPEDCAVoiceACKPolicy": hwQAPEDCAVoiceACKPolicy,
       "hwQAPEDCAVideoECWmax": hwQAPEDCAVideoECWmax,
       "hwQAPEDCAVideoECWmin": hwQAPEDCAVideoECWmin,
       "hwQAPEDCAVideoAIFSN": hwQAPEDCAVideoAIFSN,
       "hwQAPEDCAVideoTXOPLimit": hwQAPEDCAVideoTXOPLimit,
       "hwQAPEDCAVideoACKPolicy": hwQAPEDCAVideoACKPolicy,
       "hwQAPEDCABEECWmax": hwQAPEDCABEECWmax,
       "hwQAPEDCABEECWmin": hwQAPEDCABEECWmin,
       "hwQAPEDCABEAIFSN": hwQAPEDCABEAIFSN,
       "hwQAPEDCABETXOPLimit": hwQAPEDCABETXOPLimit,
       "hwQAPEDCABEACKPolicy": hwQAPEDCABEACKPolicy,
       "hwQAPEDCABKECWmax": hwQAPEDCABKECWmax,
       "hwQAPEDCABKECWmin": hwQAPEDCABKECWmin,
       "hwQAPEDCABKAIFSN": hwQAPEDCABKAIFSN,
       "hwQAPEDCABKTXOPLimit": hwQAPEDCABKTXOPLimit,
       "hwQAPEDCABKACKPolicy": hwQAPEDCABKACKPolicy,
       "hwQClientEDCAVoiceECWmax": hwQClientEDCAVoiceECWmax,
       "hwQClientEDCAVoiceECWmin": hwQClientEDCAVoiceECWmin,
       "hwQClientEDCAVoiceAIFSN": hwQClientEDCAVoiceAIFSN,
       "hwQClientEDCAVoiceTXOPLimit": hwQClientEDCAVoiceTXOPLimit,
       "hwQClientEDCAVideoECWmax": hwQClientEDCAVideoECWmax,
       "hwQClientEDCAVideoECWmin": hwQClientEDCAVideoECWmin,
       "hwQClientEDCAVideoAIFSN": hwQClientEDCAVideoAIFSN,
       "hwQClientEDCAVideoTXOPLimit": hwQClientEDCAVideoTXOPLimit,
       "hwQClientEDCABEECWmax": hwQClientEDCABEECWmax,
       "hwQClientEDCABEECWmin": hwQClientEDCABEECWmin,
       "hwQClientEDCABEAIFSN": hwQClientEDCABEAIFSN,
       "hwQClientEDCABETXOPLimit": hwQClientEDCABETXOPLimit,
       "hwQClientEDCABKECWmax": hwQClientEDCABKECWmax,
       "hwQClientEDCABKECWmin": hwQClientEDCABKECWmin,
       "hwQClientEDCABKAIFSN": hwQClientEDCABKAIFSN,
       "hwQClientEDCABKTXOPLimit": hwQClientEDCABKTXOPLimit,
       "hwWlanTrafficProfileTable": hwWlanTrafficProfileTable,
       "hwWlanTrafficProfileEntry": hwWlanTrafficProfileEntry,
       "hwWlanTrafficProfileName": hwWlanTrafficProfileName,
       "hwWlanTrafficProfileRowStatus": hwWlanTrafficProfileRowStatus,
       "hwWlanClientUpLimitRate": hwWlanClientUpLimitRate,
       "hwWlanVAPUpLimitRate": hwWlanVAPUpLimitRate,
       "hwWlan8021pMapMode": hwWlan8021pMapMode,
       "hwWlan8021pSpecValue": hwWlan8021pSpecValue,
       "hwWlanUP0Map8021p": hwWlanUP0Map8021p,
       "hwWlanUP1Map8021p": hwWlanUP1Map8021p,
       "hwWlanUP2Map8021p": hwWlanUP2Map8021p,
       "hwWlanUP3Map8021p": hwWlanUP3Map8021p,
       "hwWlanUP4Map8021p": hwWlanUP4Map8021p,
       "hwWlanUP5Map8021p": hwWlanUP5Map8021p,
       "hwWlanUP6Map8021p": hwWlanUP6Map8021p,
       "hwWlanUP7Map8021p": hwWlanUP7Map8021p,
       "hwWlan8021p0MapUPValue": hwWlan8021p0MapUPValue,
       "hwWlan8021p1MapUPValue": hwWlan8021p1MapUPValue,
       "hwWlan8021p2MapUPValue": hwWlan8021p2MapUPValue,
       "hwWlan8021p3MapUPValue": hwWlan8021p3MapUPValue,
       "hwWlan8021p4MapUPValue": hwWlan8021p4MapUPValue,
       "hwWlan8021p5MapUPValue": hwWlan8021p5MapUPValue,
       "hwWlan8021p6MapUPValue": hwWlan8021p6MapUPValue,
       "hwWlan8021p7MapUPValue": hwWlan8021p7MapUPValue,
       "hwWlanUpTunnelPriorityMapMode": hwWlanUpTunnelPriorityMapMode,
       "hwWlanUpTunnelPrioritySpecValue": hwWlanUpTunnelPrioritySpecValue,
       "hwWlanValue0MapUpTunnelPriority": hwWlanValue0MapUpTunnelPriority,
       "hwWlanValue1MapUpTunnelPriority": hwWlanValue1MapUpTunnelPriority,
       "hwWlanValue2MapUpTunnelPriority": hwWlanValue2MapUpTunnelPriority,
       "hwWlanValue3MapUpTunnelPriority": hwWlanValue3MapUpTunnelPriority,
       "hwWlanValue4MapUpTunnelPriority": hwWlanValue4MapUpTunnelPriority,
       "hwWlanValue5MapUpTunnelPriority": hwWlanValue5MapUpTunnelPriority,
       "hwWlanValue6MapUpTunnelPriority": hwWlanValue6MapUpTunnelPriority,
       "hwWlanValue7MapUpTunnelPriority": hwWlanValue7MapUpTunnelPriority,
       "hwWlanDownTunnelPriorityMapMode": hwWlanDownTunnelPriorityMapMode,
       "hwWlanDownTunnelPrioritySpecValue": hwWlanDownTunnelPrioritySpecValue,
       "hwWlanValue0MapDownTunnelPriority": hwWlanValue0MapDownTunnelPriority,
       "hwWlanValue1MapDownTunnelPriority": hwWlanValue1MapDownTunnelPriority,
       "hwWlanValue2MapDownTunnelPriority": hwWlanValue2MapDownTunnelPriority,
       "hwWlanValue3MapDownTunnelPriority": hwWlanValue3MapDownTunnelPriority,
       "hwWlanValue4MapDownTunnelPriority": hwWlanValue4MapDownTunnelPriority,
       "hwWlanValue5MapDownTunnelPriority": hwWlanValue5MapDownTunnelPriority,
       "hwWlanValue6MapDownTunnelPriority": hwWlanValue6MapDownTunnelPriority,
       "hwWlanValue7MapDownTunnelPriority": hwWlanValue7MapDownTunnelPriority,
       "hwWlanClientDownLimitRate": hwWlanClientDownLimitRate,
       "hwWlanVAPDownLimitRate": hwWlanVAPDownLimitRate,
       "hwWlanTos0MapUPValue": hwWlanTos0MapUPValue,
       "hwWlanTos1MapUPValue": hwWlanTos1MapUPValue,
       "hwWlanTos2MapUPValue": hwWlanTos2MapUPValue,
       "hwWlanTos3MapUPValue": hwWlanTos3MapUPValue,
       "hwWlanTos4MapUPValue": hwWlanTos4MapUPValue,
       "hwWlanTos5MapUPValue": hwWlanTos5MapUPValue,
       "hwWlanTos6MapUPValue": hwWlanTos6MapUPValue,
       "hwWlanTos7MapUPValue": hwWlanTos7MapUPValue,
       "hwWlanBatchWmmProfileStartNumber": hwWlanBatchWmmProfileStartNumber,
       "hwWlanBatchWmmProfileGetNumber": hwWlanBatchWmmProfileGetNumber,
       "hwWlanBatchWmmProfileReturnNumber": hwWlanBatchWmmProfileReturnNumber,
       "hwWlanBatchWmmProfileName": hwWlanBatchWmmProfileName,
       "hwWlanBatchTrafficProfileStartNumber": hwWlanBatchTrafficProfileStartNumber,
       "hwWlanBatchTrafficProfileGetNumber": hwWlanBatchTrafficProfileGetNumber,
       "hwWlanBatchTrafficProfileReturnNumber": hwWlanBatchTrafficProfileReturnNumber,
       "hwWlanBatchTrafficProfileName": hwWlanBatchTrafficProfileName,
       "hwWlanQosManagementObjects": hwWlanQosManagementObjects,
       "hwWlanQosManagementConformance": hwWlanQosManagementConformance,
       "hwWlanQosManagementCompliances": hwWlanQosManagementCompliances,
       "hwWlanQosManagementCompliance": hwWlanQosManagementCompliance,
       "hwWlanQosManagementObjectGroups": hwWlanQosManagementObjectGroups,
       "hwWlanWmmProfileGroup": hwWlanWmmProfileGroup,
       "hwWlanTrafficProfileGroup": hwWlanTrafficProfileGroup,
       "hwWlanQosManagementGroup": hwWlanQosManagementGroup}
)
