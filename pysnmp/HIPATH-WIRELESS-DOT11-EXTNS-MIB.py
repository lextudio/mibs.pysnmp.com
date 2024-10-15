# SNMP MIB module (HIPATH-WIRELESS-DOT11-EXTNS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HIPATH-WIRELESS-DOT11-EXTNS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:29 2024
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

(hiPathWirelessMgmt,
 hiPathWirelessModules) = mibBuilder.importSymbols(
    "HIPATH-WIRELESS-SMI",
    "hiPathWirelessMgmt",
    "hiPathWirelessModules")

(dot11WEPDefaultKeyIndex,) = mibBuilder.importSymbols(
    "IEEE802dot11-MIB",
    "dot11WEPDefaultKeyIndex")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hiPathWirelessDot11ExtnsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 5, 3)
)
hiPathWirelessDot11ExtnsMIB.setRevisions(
        ("2016-02-23 14:46",
         "2015-03-12 15:15",
         "2013-10-16 15:15",
         "2013-04-30 15:15",
         "2011-08-17 18:15",
         "2011-07-20 11:45",
         "2011-05-05 09:58",
         "2011-01-13 11:25",
         "2010-04-08 17:16",
         "2009-01-19 14:15",
         "2008-05-09 16:51",
         "2007-09-28 14:30",
         "2006-10-24 13:05",
         "2005-10-28 01:14")
)


# Types definitions



class WEPKeytype(OctetString):
    """Custom type WEPKeytype based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(14, 14),
        ValueSizeConstraint(38, 38),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dot11ExtnsMib_ObjectIdentity = ObjectIdentity
dot11ExtnsMib = _Dot11ExtnsMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1)
)
_Dot11Extsmt_ObjectIdentity = ObjectIdentity
dot11Extsmt = _Dot11Extsmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1)
)
_Dot11ExtBSSIDTable_Object = MibTable
dot11ExtBSSIDTable = _Dot11ExtBSSIDTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dot11ExtBSSIDTable.setStatus("current")
_Dot11ExtBSSIDEntry_Object = MibTableRow
dot11ExtBSSIDEntry = _Dot11ExtBSSIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 1, 1)
)
dot11ExtBSSIDEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtBSSIndex"),
)
if mibBuilder.loadTexts:
    dot11ExtBSSIDEntry.setStatus("current")


class _Dot11ExtBSSIndex_Type(Integer32):
    """Custom type dot11ExtBSSIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dot11ExtBSSIndex_Type.__name__ = "Integer32"
_Dot11ExtBSSIndex_Object = MibTableColumn
dot11ExtBSSIndex = _Dot11ExtBSSIndex_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 1, 1, 1),
    _Dot11ExtBSSIndex_Type()
)
dot11ExtBSSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ExtBSSIndex.setStatus("current")
_Dot11ExtBSSID_Type = MacAddress
_Dot11ExtBSSID_Object = MibTableColumn
dot11ExtBSSID = _Dot11ExtBSSID_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 1, 1, 2),
    _Dot11ExtBSSID_Type()
)
dot11ExtBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ExtBSSID.setStatus("current")


class _Dot11ExtSSIDID_Type(Integer32):
    """Custom type dot11ExtSSIDID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dot11ExtSSIDID_Type.__name__ = "Integer32"
_Dot11ExtSSIDID_Object = MibTableColumn
dot11ExtSSIDID = _Dot11ExtSSIDID_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 1, 1, 3),
    _Dot11ExtSSIDID_Type()
)
dot11ExtSSIDID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ExtSSIDID.setStatus("current")


class _Dot11ExtSSID_Type(OctetString):
    """Custom type dot11ExtSSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Dot11ExtSSID_Type.__name__ = "OctetString"
_Dot11ExtSSID_Object = MibTableColumn
dot11ExtSSID = _Dot11ExtSSID_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 1, 1, 4),
    _Dot11ExtSSID_Type()
)
dot11ExtSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ExtSSID.setStatus("current")
_Dot11ExtBSSIDWEPKeyIndex_Type = Integer32
_Dot11ExtBSSIDWEPKeyIndex_Object = MibTableColumn
dot11ExtBSSIDWEPKeyIndex = _Dot11ExtBSSIDWEPKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 1, 1, 5),
    _Dot11ExtBSSIDWEPKeyIndex_Type()
)
dot11ExtBSSIDWEPKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ExtBSSIDWEPKeyIndex.setStatus("current")
_Dot11ExtSSIDSuppress_Type = TruthValue
_Dot11ExtSSIDSuppress_Object = MibTableColumn
dot11ExtSSIDSuppress = _Dot11ExtSSIDSuppress_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 1, 1, 6),
    _Dot11ExtSSIDSuppress_Type()
)
dot11ExtSSIDSuppress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ExtSSIDSuppress.setStatus("current")
_Dot11ExtPriorityTrafficHandling_Type = TruthValue
_Dot11ExtPriorityTrafficHandling_Object = MibTableColumn
dot11ExtPriorityTrafficHandling = _Dot11ExtPriorityTrafficHandling_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 1, 1, 7),
    _Dot11ExtPriorityTrafficHandling_Type()
)
dot11ExtPriorityTrafficHandling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ExtPriorityTrafficHandling.setStatus("current")
_Dot11ExtWEPKeyMappingsTable_Object = MibTable
dot11ExtWEPKeyMappingsTable = _Dot11ExtWEPKeyMappingsTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    dot11ExtWEPKeyMappingsTable.setStatus("deprecated")
_Dot11ExtWEPKeyMappingsEntry_Object = MibTableRow
dot11ExtWEPKeyMappingsEntry = _Dot11ExtWEPKeyMappingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 2, 1)
)
dot11ExtWEPKeyMappingsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtBSSIndex"),
    (0, "HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtWEPKeyMappingIndex"),
)
if mibBuilder.loadTexts:
    dot11ExtWEPKeyMappingsEntry.setStatus("current")


class _Dot11ExtWEPKeyMappingIndex_Type(Integer32):
    """Custom type dot11ExtWEPKeyMappingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dot11ExtWEPKeyMappingIndex_Type.__name__ = "Integer32"
_Dot11ExtWEPKeyMappingIndex_Object = MibTableColumn
dot11ExtWEPKeyMappingIndex = _Dot11ExtWEPKeyMappingIndex_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 2, 1, 1),
    _Dot11ExtWEPKeyMappingIndex_Type()
)
dot11ExtWEPKeyMappingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ExtWEPKeyMappingIndex.setStatus("current")
_Dot11ExtWEPKeyMappingAddress_Type = MacAddress
_Dot11ExtWEPKeyMappingAddress_Object = MibTableColumn
dot11ExtWEPKeyMappingAddress = _Dot11ExtWEPKeyMappingAddress_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 2, 1, 2),
    _Dot11ExtWEPKeyMappingAddress_Type()
)
dot11ExtWEPKeyMappingAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot11ExtWEPKeyMappingAddress.setStatus("current")
_Dot11ExtWEPKeyMappingWEPOn_Type = TruthValue
_Dot11ExtWEPKeyMappingWEPOn_Object = MibTableColumn
dot11ExtWEPKeyMappingWEPOn = _Dot11ExtWEPKeyMappingWEPOn_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 2, 1, 3),
    _Dot11ExtWEPKeyMappingWEPOn_Type()
)
dot11ExtWEPKeyMappingWEPOn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot11ExtWEPKeyMappingWEPOn.setStatus("current")
_Dot11ExtWEPKeyMappingValue_Type = WEPKeytype
_Dot11ExtWEPKeyMappingValue_Object = MibTableColumn
dot11ExtWEPKeyMappingValue = _Dot11ExtWEPKeyMappingValue_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 2, 1, 4),
    _Dot11ExtWEPKeyMappingValue_Type()
)
dot11ExtWEPKeyMappingValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot11ExtWEPKeyMappingValue.setStatus("current")
_Dot11ExtWEPKeyMappingStatus_Type = RowStatus
_Dot11ExtWEPKeyMappingStatus_Object = MibTableColumn
dot11ExtWEPKeyMappingStatus = _Dot11ExtWEPKeyMappingStatus_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 2, 1, 5),
    _Dot11ExtWEPKeyMappingStatus_Type()
)
dot11ExtWEPKeyMappingStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot11ExtWEPKeyMappingStatus.setStatus("current")
_Dot11CapabilitiesTable_Object = MibTable
dot11CapabilitiesTable = _Dot11CapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 3)
)
if mibBuilder.loadTexts:
    dot11CapabilitiesTable.setStatus("current")
_Dot11CapabilitiesEntry_Object = MibTableRow
dot11CapabilitiesEntry = _Dot11CapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 3, 1)
)
dot11CapabilitiesEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11CapabilitiesEntry.setStatus("current")


class _Dot11Capabilities_Type(Bits):
    """Custom type dot11Capabilities based on Bits"""
    namedValues = NamedValues(
        *(("dot11a", 2),
          ("dot11b", 0),
          ("dot11c", 5),
          ("dot11g", 1),
          ("dot11j", 3),
          ("dot11n", 4))
    )

_Dot11Capabilities_Type.__name__ = "Bits"
_Dot11Capabilities_Object = MibTableColumn
dot11Capabilities = _Dot11Capabilities_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 3, 1, 1),
    _Dot11Capabilities_Type()
)
dot11Capabilities.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11Capabilities.setStatus("current")
_Dot11bConfigTable_Object = MibTable
dot11bConfigTable = _Dot11bConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 4)
)
if mibBuilder.loadTexts:
    dot11bConfigTable.setStatus("current")
_Dot11bConfigEntry_Object = MibTableRow
dot11bConfigEntry = _Dot11bConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 4, 1)
)
dot11bConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11bConfigEntry.setStatus("current")
_Dot11bEnabled_Type = TruthValue
_Dot11bEnabled_Object = MibTableColumn
dot11bEnabled = _Dot11bEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 4, 1, 1),
    _Dot11bEnabled_Type()
)
dot11bEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11bEnabled.setStatus("current")


class _Dot11BasicB_Type(Integer32):
    """Custom type dot11BasicB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("basic11", 2),
          ("basic11b", 1))
    )


_Dot11BasicB_Type.__name__ = "Integer32"
_Dot11BasicB_Object = MibTableColumn
dot11BasicB = _Dot11BasicB_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 4, 1, 2),
    _Dot11BasicB_Type()
)
dot11BasicB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11BasicB.setStatus("obsolete")
_Dot11gConfigTable_Object = MibTable
dot11gConfigTable = _Dot11gConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 5)
)
if mibBuilder.loadTexts:
    dot11gConfigTable.setStatus("current")
_Dot11gConfigEntry_Object = MibTableRow
dot11gConfigEntry = _Dot11gConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 5, 1)
)
dot11gConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11gConfigEntry.setStatus("current")
_Dot11gEnabled_Type = TruthValue
_Dot11gEnabled_Object = MibTableColumn
dot11gEnabled = _Dot11gEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 5, 1, 1),
    _Dot11gEnabled_Type()
)
dot11gEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11gEnabled.setStatus("current")


class _Dot11gProtectionMode_Type(Integer32):
    """Custom type dot11gProtectionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("always", 3),
          ("auto", 2),
          ("none", 1))
    )


_Dot11gProtectionMode_Type.__name__ = "Integer32"
_Dot11gProtectionMode_Object = MibTableColumn
dot11gProtectionMode = _Dot11gProtectionMode_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 5, 1, 3),
    _Dot11gProtectionMode_Type()
)
dot11gProtectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11gProtectionMode.setStatus("current")


class _Dot11gProtectionType_Type(Integer32):
    """Custom type dot11gProtectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ctsOnly", 1),
          ("rtcCts", 2))
    )


_Dot11gProtectionType_Type.__name__ = "Integer32"
_Dot11gProtectionType_Object = MibTableColumn
dot11gProtectionType = _Dot11gProtectionType_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 5, 1, 4),
    _Dot11gProtectionType_Type()
)
dot11gProtectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11gProtectionType.setStatus("current")


class _Dot11gProtectionRate_Type(Integer32):
    """Custom type dot11gProtectionRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rate11Mbps", 3),
          ("rate1Mbps", 0),
          ("rate2Mbps", 1),
          ("rate5Mbps", 2))
    )


_Dot11gProtectionRate_Type.__name__ = "Integer32"
_Dot11gProtectionRate_Object = MibTableColumn
dot11gProtectionRate = _Dot11gProtectionRate_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 5, 1, 5),
    _Dot11gProtectionRate_Type()
)
dot11gProtectionRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11gProtectionRate.setStatus("current")


class _Dot11gBasicG_Type(Integer32):
    """Custom type dot11gBasicG based on Integer32"""
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
        *(("basic11", 2),
          ("basic11b", 3),
          ("default", 1),
          ("ofdm", 4))
    )


_Dot11gBasicG_Type.__name__ = "Integer32"
_Dot11gBasicG_Object = MibTableColumn
dot11gBasicG = _Dot11gBasicG_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 5, 1, 6),
    _Dot11gBasicG_Type()
)
dot11gBasicG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11gBasicG.setStatus("obsolete")


class _Dot11gProtectionModeSelected_Type(Integer32):
    """Custom type dot11gProtectionModeSelected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 2),
          ("off", 0),
          ("on", 1))
    )


_Dot11gProtectionModeSelected_Type.__name__ = "Integer32"
_Dot11gProtectionModeSelected_Object = MibTableColumn
dot11gProtectionModeSelected = _Dot11gProtectionModeSelected_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 5, 1, 7),
    _Dot11gProtectionModeSelected_Type()
)
dot11gProtectionModeSelected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11gProtectionModeSelected.setStatus("current")
_Dot11ExtSmtTable_Object = MibTable
dot11ExtSmtTable = _Dot11ExtSmtTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 7)
)
if mibBuilder.loadTexts:
    dot11ExtSmtTable.setStatus("current")
_Dot11ExtSmtEntry_Object = MibTableRow
dot11ExtSmtEntry = _Dot11ExtSmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 7, 1)
)
dot11ExtSmtEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11ExtSmtEntry.setStatus("current")


class _SmtShortPreambleInvoked_Type(Integer32):
    """Custom type smtShortPreambleInvoked based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoSelectPreamble", 3),
          ("longPreamble", 2),
          ("notApplicable", 0),
          ("shortPreamble", 1))
    )


_SmtShortPreambleInvoked_Type.__name__ = "Integer32"
_SmtShortPreambleInvoked_Object = MibTableColumn
smtShortPreambleInvoked = _SmtShortPreambleInvoked_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 7, 1, 1),
    _SmtShortPreambleInvoked_Type()
)
smtShortPreambleInvoked.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtShortPreambleInvoked.setStatus("current")


class _Dot11ExtSmtCurrentChannel_Type(Integer32):
    """Custom type dot11ExtSmtCurrentChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dot11ExtSmtCurrentChannel_Type.__name__ = "Integer32"
_Dot11ExtSmtCurrentChannel_Object = MibTableColumn
dot11ExtSmtCurrentChannel = _Dot11ExtSmtCurrentChannel_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 7, 1, 2),
    _Dot11ExtSmtCurrentChannel_Type()
)
dot11ExtSmtCurrentChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ExtSmtCurrentChannel.setStatus("current")


class _Dot11ExtSmtMaxBasicRate_Type(OctetString):
    """Custom type dot11ExtSmtMaxBasicRate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 126),
    )


_Dot11ExtSmtMaxBasicRate_Type.__name__ = "OctetString"
_Dot11ExtSmtMaxBasicRate_Object = MibTableColumn
dot11ExtSmtMaxBasicRate = _Dot11ExtSmtMaxBasicRate_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 7, 1, 3),
    _Dot11ExtSmtMaxBasicRate_Type()
)
dot11ExtSmtMaxBasicRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ExtSmtMaxBasicRate.setStatus("deprecated")


class _Dot11ExtSmtMinBasicRate_Type(OctetString):
    """Custom type dot11ExtSmtMinBasicRate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 126),
    )


_Dot11ExtSmtMinBasicRate_Type.__name__ = "OctetString"
_Dot11ExtSmtMinBasicRate_Object = MibTableColumn
dot11ExtSmtMinBasicRate = _Dot11ExtSmtMinBasicRate_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 7, 1, 4),
    _Dot11ExtSmtMinBasicRate_Type()
)
dot11ExtSmtMinBasicRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ExtSmtMinBasicRate.setStatus("current")


class _Dot11ExtSmtMaxOperationalRate_Type(OctetString):
    """Custom type dot11ExtSmtMaxOperationalRate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 126),
    )


_Dot11ExtSmtMaxOperationalRate_Type.__name__ = "OctetString"
_Dot11ExtSmtMaxOperationalRate_Object = MibTableColumn
dot11ExtSmtMaxOperationalRate = _Dot11ExtSmtMaxOperationalRate_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 7, 1, 5),
    _Dot11ExtSmtMaxOperationalRate_Type()
)
dot11ExtSmtMaxOperationalRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ExtSmtMaxOperationalRate.setStatus("deprecated")
_Dot11ExtSmtCurChanSelectedByAP_Type = Integer32
_Dot11ExtSmtCurChanSelectedByAP_Object = MibTableColumn
dot11ExtSmtCurChanSelectedByAP = _Dot11ExtSmtCurChanSelectedByAP_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 7, 1, 6),
    _Dot11ExtSmtCurChanSelectedByAP_Type()
)
dot11ExtSmtCurChanSelectedByAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ExtSmtCurChanSelectedByAP.setStatus("current")
_Dot11ExtSmtRFDomain_Type = DisplayString
_Dot11ExtSmtRFDomain_Object = MibTableColumn
dot11ExtSmtRFDomain = _Dot11ExtSmtRFDomain_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 7, 1, 7),
    _Dot11ExtSmtRFDomain_Type()
)
dot11ExtSmtRFDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ExtSmtRFDomain.setStatus("current")
_Dot11ExtSmtAutoTxPowerCtrl_Type = Integer32
_Dot11ExtSmtAutoTxPowerCtrl_Object = MibTableColumn
dot11ExtSmtAutoTxPowerCtrl = _Dot11ExtSmtAutoTxPowerCtrl_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 7, 1, 8),
    _Dot11ExtSmtAutoTxPowerCtrl_Type()
)
dot11ExtSmtAutoTxPowerCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ExtSmtAutoTxPowerCtrl.setStatus("current")
_Dot11ExtSmtCurrentTxPowerLevel_Type = Integer32
_Dot11ExtSmtCurrentTxPowerLevel_Object = MibTableColumn
dot11ExtSmtCurrentTxPowerLevel = _Dot11ExtSmtCurrentTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 7, 1, 9),
    _Dot11ExtSmtCurrentTxPowerLevel_Type()
)
dot11ExtSmtCurrentTxPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ExtSmtCurrentTxPowerLevel.setStatus("current")
_Dot11ExtSmtMaxTxPower_Type = Integer32
_Dot11ExtSmtMaxTxPower_Object = MibTableColumn
dot11ExtSmtMaxTxPower = _Dot11ExtSmtMaxTxPower_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 7, 1, 10),
    _Dot11ExtSmtMaxTxPower_Type()
)
dot11ExtSmtMaxTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ExtSmtMaxTxPower.setStatus("current")
_Dot11ExtSmtMinTxPower_Type = Integer32
_Dot11ExtSmtMinTxPower_Object = MibTableColumn
dot11ExtSmtMinTxPower = _Dot11ExtSmtMinTxPower_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 7, 1, 11),
    _Dot11ExtSmtMinTxPower_Type()
)
dot11ExtSmtMinTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ExtSmtMinTxPower.setStatus("current")
_Dot11ExtSmtAutoTxPowerCtrlAdjust_Type = Integer32
_Dot11ExtSmtAutoTxPowerCtrlAdjust_Object = MibTableColumn
dot11ExtSmtAutoTxPowerCtrlAdjust = _Dot11ExtSmtAutoTxPowerCtrlAdjust_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 7, 1, 12),
    _Dot11ExtSmtAutoTxPowerCtrlAdjust_Type()
)
dot11ExtSmtAutoTxPowerCtrlAdjust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ExtSmtAutoTxPowerCtrlAdjust.setStatus("current")


class _Dot11ExtSmtBGretries_Type(Integer32):
    """Custom type dot11ExtSmtBGretries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Dot11ExtSmtBGretries_Type.__name__ = "Integer32"
_Dot11ExtSmtBGretries_Object = MibTableColumn
dot11ExtSmtBGretries = _Dot11ExtSmtBGretries_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 7, 1, 13),
    _Dot11ExtSmtBGretries_Type()
)
dot11ExtSmtBGretries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ExtSmtBGretries.setStatus("deprecated")


class _Dot11ExtSmtBEretries_Type(Integer32):
    """Custom type dot11ExtSmtBEretries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Dot11ExtSmtBEretries_Type.__name__ = "Integer32"
_Dot11ExtSmtBEretries_Object = MibTableColumn
dot11ExtSmtBEretries = _Dot11ExtSmtBEretries_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 7, 1, 14),
    _Dot11ExtSmtBEretries_Type()
)
dot11ExtSmtBEretries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ExtSmtBEretries.setStatus("deprecated")


class _Dot11ExtSmtVIretries_Type(Integer32):
    """Custom type dot11ExtSmtVIretries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Dot11ExtSmtVIretries_Type.__name__ = "Integer32"
_Dot11ExtSmtVIretries_Object = MibTableColumn
dot11ExtSmtVIretries = _Dot11ExtSmtVIretries_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 7, 1, 15),
    _Dot11ExtSmtVIretries_Type()
)
dot11ExtSmtVIretries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ExtSmtVIretries.setStatus("deprecated")


class _Dot11ExtSmtVOretries_Type(Integer32):
    """Custom type dot11ExtSmtVOretries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Dot11ExtSmtVOretries_Type.__name__ = "Integer32"
_Dot11ExtSmtVOretries_Object = MibTableColumn
dot11ExtSmtVOretries = _Dot11ExtSmtVOretries_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 7, 1, 16),
    _Dot11ExtSmtVOretries_Type()
)
dot11ExtSmtVOretries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ExtSmtVOretries.setStatus("deprecated")


class _Dot11ExtSmtTVOretries_Type(Integer32):
    """Custom type dot11ExtSmtTVOretries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Dot11ExtSmtTVOretries_Type.__name__ = "Integer32"
_Dot11ExtSmtTVOretries_Object = MibTableColumn
dot11ExtSmtTVOretries = _Dot11ExtSmtTVOretries_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 7, 1, 17),
    _Dot11ExtSmtTVOretries_Type()
)
dot11ExtSmtTVOretries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ExtSmtTVOretries.setStatus("deprecated")


class _Dot11ExtSmtDcsMode_Type(Integer32):
    """Custom type dot11ExtSmtDcsMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("monitor", 1),
          ("off", 0))
    )


_Dot11ExtSmtDcsMode_Type.__name__ = "Integer32"
_Dot11ExtSmtDcsMode_Object = MibTableColumn
dot11ExtSmtDcsMode = _Dot11ExtSmtDcsMode_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 7, 1, 18),
    _Dot11ExtSmtDcsMode_Type()
)
dot11ExtSmtDcsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ExtSmtDcsMode.setStatus("current")


class _Dot11ExtSmtDcsNoiseThreshold_Type(Integer32):
    """Custom type dot11ExtSmtDcsNoiseThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-95, -50),
    )


_Dot11ExtSmtDcsNoiseThreshold_Type.__name__ = "Integer32"
_Dot11ExtSmtDcsNoiseThreshold_Object = MibTableColumn
dot11ExtSmtDcsNoiseThreshold = _Dot11ExtSmtDcsNoiseThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 7, 1, 19),
    _Dot11ExtSmtDcsNoiseThreshold_Type()
)
dot11ExtSmtDcsNoiseThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ExtSmtDcsNoiseThreshold.setStatus("current")


class _Dot11ExtSmtDcsChlOccThreshold_Type(Integer32):
    """Custom type dot11ExtSmtDcsChlOccThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100),
    )


_Dot11ExtSmtDcsChlOccThreshold_Type.__name__ = "Integer32"
_Dot11ExtSmtDcsChlOccThreshold_Object = MibTableColumn
dot11ExtSmtDcsChlOccThreshold = _Dot11ExtSmtDcsChlOccThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 7, 1, 20),
    _Dot11ExtSmtDcsChlOccThreshold_Type()
)
dot11ExtSmtDcsChlOccThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ExtSmtDcsChlOccThreshold.setStatus("current")


class _Dot11ExtSmtDcsUpdatePeriod_Type(Integer32):
    """Custom type dot11ExtSmtDcsUpdatePeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Dot11ExtSmtDcsUpdatePeriod_Type.__name__ = "Integer32"
_Dot11ExtSmtDcsUpdatePeriod_Object = MibTableColumn
dot11ExtSmtDcsUpdatePeriod = _Dot11ExtSmtDcsUpdatePeriod_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 7, 1, 21),
    _Dot11ExtSmtDcsUpdatePeriod_Type()
)
dot11ExtSmtDcsUpdatePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ExtSmtDcsUpdatePeriod.setStatus("current")


class _Dot11ExtSmtDcsChannelSelection_Type(Integer32):
    """Custom type dot11ExtSmtDcsChannelSelection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Dot11ExtSmtDcsChannelSelection_Type.__name__ = "Integer32"
_Dot11ExtSmtDcsChannelSelection_Object = MibTableColumn
dot11ExtSmtDcsChannelSelection = _Dot11ExtSmtDcsChannelSelection_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 7, 1, 22),
    _Dot11ExtSmtDcsChannelSelection_Type()
)
dot11ExtSmtDcsChannelSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ExtSmtDcsChannelSelection.setStatus("current")
_Dot11ExtSmtDcsChannelList_Type = DisplayString
_Dot11ExtSmtDcsChannelList_Object = MibTableColumn
dot11ExtSmtDcsChannelList = _Dot11ExtSmtDcsChannelList_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 7, 1, 23),
    _Dot11ExtSmtDcsChannelList_Type()
)
dot11ExtSmtDcsChannelList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ExtSmtDcsChannelList.setStatus("current")
_Dot11ExtSmtRadioAttenuation_Type = Integer32
_Dot11ExtSmtRadioAttenuation_Object = MibTableColumn
dot11ExtSmtRadioAttenuation = _Dot11ExtSmtRadioAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 7, 1, 24),
    _Dot11ExtSmtRadioAttenuation_Type()
)
dot11ExtSmtRadioAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ExtSmtRadioAttenuation.setStatus("current")


class _Dot11ExtSmtProbeSuppression_Type(Integer32):
    """Custom type dot11ExtSmtProbeSuppression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Dot11ExtSmtProbeSuppression_Type.__name__ = "Integer32"
_Dot11ExtSmtProbeSuppression_Object = MibTableColumn
dot11ExtSmtProbeSuppression = _Dot11ExtSmtProbeSuppression_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 7, 1, 25),
    _Dot11ExtSmtProbeSuppression_Type()
)
dot11ExtSmtProbeSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ExtSmtProbeSuppression.setStatus("current")


class _Dot11ExtSmtForceDisassociate_Type(Integer32):
    """Custom type dot11ExtSmtForceDisassociate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Dot11ExtSmtForceDisassociate_Type.__name__ = "Integer32"
_Dot11ExtSmtForceDisassociate_Object = MibTableColumn
dot11ExtSmtForceDisassociate = _Dot11ExtSmtForceDisassociate_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 7, 1, 26),
    _Dot11ExtSmtForceDisassociate_Type()
)
dot11ExtSmtForceDisassociate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ExtSmtForceDisassociate.setStatus("current")
_Dot11ExtSmtRssThreshold_Type = Integer32
_Dot11ExtSmtRssThreshold_Object = MibTableColumn
dot11ExtSmtRssThreshold = _Dot11ExtSmtRssThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 7, 1, 27),
    _Dot11ExtSmtRssThreshold_Type()
)
dot11ExtSmtRssThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ExtSmtRssThreshold.setStatus("current")
_Dot11ExtVlanSmtTable_Object = MibTable
dot11ExtVlanSmtTable = _Dot11ExtVlanSmtTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 8)
)
if mibBuilder.loadTexts:
    dot11ExtVlanSmtTable.setStatus("current")
_Dot11ExtVlanSmtEntry_Object = MibTableRow
dot11ExtVlanSmtEntry = _Dot11ExtVlanSmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 8, 1)
)
dot11ExtVlanSmtEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtBSSIndex"),
)
if mibBuilder.loadTexts:
    dot11ExtVlanSmtEntry.setStatus("current")
_VlanBridgeMode_Type = TruthValue
_VlanBridgeMode_Object = MibTableColumn
vlanBridgeMode = _VlanBridgeMode_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 8, 1, 1),
    _VlanBridgeMode_Type()
)
vlanBridgeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanBridgeMode.setStatus("obsolete")
_VlanTag_Type = Integer32
_VlanTag_Object = MibTableColumn
vlanTag = _VlanTag_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 8, 1, 2),
    _VlanTag_Type()
)
vlanTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTag.setStatus("obsolete")
_Dot11DiversityTable_Object = MibTable
dot11DiversityTable = _Dot11DiversityTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 10)
)
if mibBuilder.loadTexts:
    dot11DiversityTable.setStatus("current")
_Dot11DiversityEntry_Object = MibTableRow
dot11DiversityEntry = _Dot11DiversityEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 10, 1)
)
dot11DiversityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11DiversityEntry.setStatus("current")


class _Dot11DiversityRxDiversity_Type(Integer32):
    """Custom type dot11DiversityRxDiversity based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("best", 1),
          ("left", 2),
          ("notSupport", 0),
          ("right", 3))
    )


_Dot11DiversityRxDiversity_Type.__name__ = "Integer32"
_Dot11DiversityRxDiversity_Object = MibTableColumn
dot11DiversityRxDiversity = _Dot11DiversityRxDiversity_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 10, 1, 1),
    _Dot11DiversityRxDiversity_Type()
)
dot11DiversityRxDiversity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11DiversityRxDiversity.setStatus("current")


class _Dot11DiversityTxDiversity_Type(Integer32):
    """Custom type dot11DiversityTxDiversity based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("best", 1),
          ("left", 2),
          ("notSupport", 0),
          ("right", 3))
    )


_Dot11DiversityTxDiversity_Type.__name__ = "Integer32"
_Dot11DiversityTxDiversity_Object = MibTableColumn
dot11DiversityTxDiversity = _Dot11DiversityTxDiversity_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 10, 1, 2),
    _Dot11DiversityTxDiversity_Type()
)
dot11DiversityTxDiversity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11DiversityTxDiversity.setStatus("current")


class _Dot11AntennaSelection_Type(Integer32):
    """Custom type dot11AntennaSelection based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("left", 1),
          ("leftMiddle", 3),
          ("leftMiddleRight", 7),
          ("leftRight", 5),
          ("middle", 2),
          ("middleRight", 6),
          ("none", 0),
          ("right", 4))
    )


_Dot11AntennaSelection_Type.__name__ = "Integer32"
_Dot11AntennaSelection_Object = MibTableColumn
dot11AntennaSelection = _Dot11AntennaSelection_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 10, 1, 3),
    _Dot11AntennaSelection_Type()
)
dot11AntennaSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11AntennaSelection.setStatus("current")
_Dot11nConfigTable_Object = MibTable
dot11nConfigTable = _Dot11nConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 11)
)
if mibBuilder.loadTexts:
    dot11nConfigTable.setStatus("current")
_Dot11nConfigEntry_Object = MibTableRow
dot11nConfigEntry = _Dot11nConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 11, 1)
)
dot11nConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11nConfigEntry.setStatus("current")
_Dot11nEnabled_Type = TruthValue
_Dot11nEnabled_Object = MibTableColumn
dot11nEnabled = _Dot11nEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 11, 1, 1),
    _Dot11nEnabled_Type()
)
dot11nEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11nEnabled.setStatus("current")


class _Dot11nChlBonding_Type(Integer32):
    """Custom type dot11nChlBonding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("nobond", 0),
          ("up", 1))
    )


_Dot11nChlBonding_Type.__name__ = "Integer32"
_Dot11nChlBonding_Object = MibTableColumn
dot11nChlBonding = _Dot11nChlBonding_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 11, 1, 2),
    _Dot11nChlBonding_Type()
)
dot11nChlBonding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11nChlBonding.setStatus("current")


class _Dot11nChlWidth_Type(Integer32):
    """Custom type dot11nChlWidth based on Integer32"""
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
        *(("auto", 3),
          ("width20Mhz", 1),
          ("width40Mhz", 2),
          ("width80Mhz", 4))
    )


_Dot11nChlWidth_Type.__name__ = "Integer32"
_Dot11nChlWidth_Object = MibTableColumn
dot11nChlWidth = _Dot11nChlWidth_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 11, 1, 3),
    _Dot11nChlWidth_Type()
)
dot11nChlWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11nChlWidth.setStatus("current")


class _Dot11nChlGuardInterval_Type(Integer32):
    """Custom type dot11nChlGuardInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("long", 2),
          ("short", 1))
    )


_Dot11nChlGuardInterval_Type.__name__ = "Integer32"
_Dot11nChlGuardInterval_Object = MibTableColumn
dot11nChlGuardInterval = _Dot11nChlGuardInterval_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 11, 1, 4),
    _Dot11nChlGuardInterval_Type()
)
dot11nChlGuardInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11nChlGuardInterval.setStatus("current")
_Dot11nProtectEnabled_Type = TruthValue
_Dot11nProtectEnabled_Object = MibTableColumn
dot11nProtectEnabled = _Dot11nProtectEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 11, 1, 5),
    _Dot11nProtectEnabled_Type()
)
dot11nProtectEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11nProtectEnabled.setStatus("current")


class _Dot11nProtectType_Type(Integer32):
    """Custom type dot11nProtectType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ctsOnly", 1),
          ("none", 0),
          ("rtsCts", 2))
    )


_Dot11nProtectType_Type.__name__ = "Integer32"
_Dot11nProtectType_Object = MibTableColumn
dot11nProtectType = _Dot11nProtectType_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 11, 1, 6),
    _Dot11nProtectType_Type()
)
dot11nProtectType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11nProtectType.setStatus("current")


class _Dot11nProtectOffset_Type(Integer32):
    """Custom type dot11nProtectOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("protectOffset20Mhz", 1),
          ("protectOffset25Mhz", 2))
    )


_Dot11nProtectOffset_Type.__name__ = "Integer32"
_Dot11nProtectOffset_Object = MibTableColumn
dot11nProtectOffset = _Dot11nProtectOffset_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 11, 1, 7),
    _Dot11nProtectOffset_Type()
)
dot11nProtectOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11nProtectOffset.setStatus("current")


class _Dot11nPtotectBusyThr_Type(Integer32):
    """Custom type dot11nPtotectBusyThr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Dot11nPtotectBusyThr_Type.__name__ = "Integer32"
_Dot11nPtotectBusyThr_Object = MibTableColumn
dot11nPtotectBusyThr = _Dot11nPtotectBusyThr_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 11, 1, 8),
    _Dot11nPtotectBusyThr_Type()
)
dot11nPtotectBusyThr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11nPtotectBusyThr.setStatus("current")
_Dot11nAggrMsduEnabled_Type = TruthValue
_Dot11nAggrMsduEnabled_Object = MibTableColumn
dot11nAggrMsduEnabled = _Dot11nAggrMsduEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 11, 1, 9),
    _Dot11nAggrMsduEnabled_Type()
)
dot11nAggrMsduEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11nAggrMsduEnabled.setStatus("current")


class _Dot11nAggrMsduMaxLen_Type(Integer32):
    """Custom type dot11nAggrMsduMaxLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2290, 4096),
    )


_Dot11nAggrMsduMaxLen_Type.__name__ = "Integer32"
_Dot11nAggrMsduMaxLen_Object = MibTableColumn
dot11nAggrMsduMaxLen = _Dot11nAggrMsduMaxLen_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 11, 1, 10),
    _Dot11nAggrMsduMaxLen_Type()
)
dot11nAggrMsduMaxLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11nAggrMsduMaxLen.setStatus("current")
_Dot11nAggrMpduEnabled_Type = TruthValue
_Dot11nAggrMpduEnabled_Object = MibTableColumn
dot11nAggrMpduEnabled = _Dot11nAggrMpduEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 11, 1, 11),
    _Dot11nAggrMpduEnabled_Type()
)
dot11nAggrMpduEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11nAggrMpduEnabled.setStatus("current")


class _Dot11nAggrMpduMaxLen_Type(Integer32):
    """Custom type dot11nAggrMpduMaxLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_Dot11nAggrMpduMaxLen_Type.__name__ = "Integer32"
_Dot11nAggrMpduMaxLen_Object = MibTableColumn
dot11nAggrMpduMaxLen = _Dot11nAggrMpduMaxLen_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 11, 1, 12),
    _Dot11nAggrMpduMaxLen_Type()
)
dot11nAggrMpduMaxLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11nAggrMpduMaxLen.setStatus("current")


class _Dot11nAggrMsduSubFrames_Type(Integer32):
    """Custom type dot11nAggrMsduSubFrames based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 64),
    )


_Dot11nAggrMsduSubFrames_Type.__name__ = "Integer32"
_Dot11nAggrMsduSubFrames_Object = MibTableColumn
dot11nAggrMsduSubFrames = _Dot11nAggrMsduSubFrames_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 11, 1, 13),
    _Dot11nAggrMsduSubFrames_Type()
)
dot11nAggrMsduSubFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11nAggrMsduSubFrames.setStatus("current")
_Dot11nAddbaSupEnabled_Type = TruthValue
_Dot11nAddbaSupEnabled_Object = MibTableColumn
dot11nAddbaSupEnabled = _Dot11nAddbaSupEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 11, 1, 14),
    _Dot11nAddbaSupEnabled_Type()
)
dot11nAddbaSupEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11nAddbaSupEnabled.setStatus("current")
_Dot11nConfigLDPC_Type = TruthValue
_Dot11nConfigLDPC_Object = MibTableColumn
dot11nConfigLDPC = _Dot11nConfigLDPC_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 11, 1, 15),
    _Dot11nConfigLDPC_Type()
)
dot11nConfigLDPC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11nConfigLDPC.setStatus("current")
_Dot11nConfigSTBC_Type = TruthValue
_Dot11nConfigSTBC_Object = MibTableColumn
dot11nConfigSTBC = _Dot11nConfigSTBC_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 11, 1, 16),
    _Dot11nConfigSTBC_Type()
)
dot11nConfigSTBC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11nConfigSTBC.setStatus("current")
_Dot11nConfigTXBF_Type = TruthValue
_Dot11nConfigTXBF_Object = MibTableColumn
dot11nConfigTXBF = _Dot11nConfigTXBF_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 1, 11, 1, 17),
    _Dot11nConfigTXBF_Type()
)
dot11nConfigTXBF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11nConfigTXBF.setStatus("current")
_Dot11ExtAPObjs_ObjectIdentity = ObjectIdentity
dot11ExtAPObjs = _Dot11ExtAPObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 2)
)
_Dot1XConfigTable_Object = MibTable
dot1XConfigTable = _Dot1XConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    dot1XConfigTable.setStatus("current")
_Dot1XConfigEntry_Object = MibTableRow
dot1XConfigEntry = _Dot1XConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 2, 2, 1)
)
dot1XConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtBSSIndex"),
)
if mibBuilder.loadTexts:
    dot1XConfigEntry.setStatus("current")
_Dot1XEnabled_Type = TruthValue
_Dot1XEnabled_Object = MibTableColumn
dot1XEnabled = _Dot1XEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 2, 2, 1, 1),
    _Dot1XEnabled_Type()
)
dot1XEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1XEnabled.setStatus("current")
_Dot1XDynamicRekeyingInterval_Type = Unsigned32
_Dot1XDynamicRekeyingInterval_Object = MibTableColumn
dot1XDynamicRekeyingInterval = _Dot1XDynamicRekeyingInterval_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 2, 2, 1, 2),
    _Dot1XDynamicRekeyingInterval_Type()
)
dot1XDynamicRekeyingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1XDynamicRekeyingInterval.setStatus("current")
if mibBuilder.loadTexts:
    dot1XDynamicRekeyingInterval.setUnits("seconds")
_Dot1XWPA1Enabled_Type = TruthValue
_Dot1XWPA1Enabled_Object = MibTableColumn
dot1XWPA1Enabled = _Dot1XWPA1Enabled_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 2, 2, 1, 3),
    _Dot1XWPA1Enabled_Type()
)
dot1XWPA1Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1XWPA1Enabled.setStatus("current")
_Dot1XWPAPassphrase_Type = DisplayString
_Dot1XWPAPassphrase_Object = MibTableColumn
dot1XWPAPassphrase = _Dot1XWPAPassphrase_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 2, 2, 1, 4),
    _Dot1XWPAPassphrase_Type()
)
dot1XWPAPassphrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1XWPAPassphrase.setStatus("current")


class _Dot1XWPACipherType_Type(Integer32):
    """Custom type dot1XWPACipherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("tkipOnly", 1))
    )


_Dot1XWPACipherType_Type.__name__ = "Integer32"
_Dot1XWPACipherType_Object = MibTableColumn
dot1XWPACipherType = _Dot1XWPACipherType_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 2, 2, 1, 5),
    _Dot1XWPACipherType_Type()
)
dot1XWPACipherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1XWPACipherType.setStatus("current")
_Dot1XWPA2Enabled_Type = TruthValue
_Dot1XWPA2Enabled_Object = MibTableColumn
dot1XWPA2Enabled = _Dot1XWPA2Enabled_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 2, 2, 1, 6),
    _Dot1XWPA2Enabled_Type()
)
dot1XWPA2Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1XWPA2Enabled.setStatus("current")


class _Dot1XWPA2CipherType_Type(Integer32):
    """Custom type dot1XWPA2CipherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aesOnly", 3),
          ("auto", 2))
    )


_Dot1XWPA2CipherType_Type.__name__ = "Integer32"
_Dot1XWPA2CipherType_Object = MibTableColumn
dot1XWPA2CipherType = _Dot1XWPA2CipherType_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 2, 2, 1, 7),
    _Dot1XWPA2CipherType_Type()
)
dot1XWPA2CipherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1XWPA2CipherType.setStatus("current")


class _Dot1XConfigKeyManagement_Type(Integer32):
    """Custom type dot1XConfigKeyManagement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("opportunisticKeying", 1),
          ("opportunisticKeyingAndPreauth", 3),
          ("preAuthentication", 2))
    )


_Dot1XConfigKeyManagement_Type.__name__ = "Integer32"
_Dot1XConfigKeyManagement_Object = MibTableColumn
dot1XConfigKeyManagement = _Dot1XConfigKeyManagement_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 2, 2, 1, 8),
    _Dot1XConfigKeyManagement_Type()
)
dot1XConfigKeyManagement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1XConfigKeyManagement.setStatus("current")
_Dot11ExtCounters_ObjectIdentity = ObjectIdentity
dot11ExtCounters = _Dot11ExtCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4)
)
_AssocGroupTable_Object = MibTable
assocGroupTable = _AssocGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 1)
)
if mibBuilder.loadTexts:
    assocGroupTable.setStatus("current")
_AssocGroupEntry_Object = MibTableRow
assocGroupEntry = _AssocGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 1, 1)
)
assocGroupEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-DOT11-EXTNS-MIB", "assocAddress"),
)
if mibBuilder.loadTexts:
    assocGroupEntry.setStatus("current")
_AssocAddress_Type = MacAddress
_AssocAddress_Object = MibTableColumn
assocAddress = _AssocAddress_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 1, 1, 1),
    _AssocAddress_Type()
)
assocAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocAddress.setStatus("current")


class _AssocIfIndex_Type(Integer32):
    """Custom type assocIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("mode11A", 1),
          ("mode11AC", 6),
          ("mode11B", 3),
          ("mode11G", 2),
          ("modeN24", 5),
          ("modeN50", 4),
          ("unknown", 0))
    )


_AssocIfIndex_Type.__name__ = "Integer32"
_AssocIfIndex_Object = MibTableColumn
assocIfIndex = _AssocIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 1, 1, 2),
    _AssocIfIndex_Type()
)
assocIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocIfIndex.setStatus("current")
_AssocReceivedRSSI_Type = Integer32
_AssocReceivedRSSI_Object = MibTableColumn
assocReceivedRSSI = _AssocReceivedRSSI_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 1, 1, 3),
    _AssocReceivedRSSI_Type()
)
assocReceivedRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocReceivedRSSI.setStatus("current")
_AssocTransmittedRSSI_Type = Integer32
_AssocTransmittedRSSI_Object = MibTableColumn
assocTransmittedRSSI = _AssocTransmittedRSSI_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 1, 1, 4),
    _AssocTransmittedRSSI_Type()
)
assocTransmittedRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocTransmittedRSSI.setStatus("current")
_AssocReceivedRate_Type = Unsigned32
_AssocReceivedRate_Object = MibTableColumn
assocReceivedRate = _AssocReceivedRate_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 1, 1, 5),
    _AssocReceivedRate_Type()
)
assocReceivedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocReceivedRate.setStatus("current")
_AssocTransmittedRate_Type = Unsigned32
_AssocTransmittedRate_Object = MibTableColumn
assocTransmittedRate = _AssocTransmittedRate_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 1, 1, 6),
    _AssocTransmittedRate_Type()
)
assocTransmittedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocTransmittedRate.setStatus("current")
_AssocReceivedFrameCount_Type = Counter64
_AssocReceivedFrameCount_Object = MibTableColumn
assocReceivedFrameCount = _AssocReceivedFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 1, 1, 7),
    _AssocReceivedFrameCount_Type()
)
assocReceivedFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocReceivedFrameCount.setStatus("current")
_AssocTransmittedFrameCount_Type = Counter64
_AssocTransmittedFrameCount_Object = MibTableColumn
assocTransmittedFrameCount = _AssocTransmittedFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 1, 1, 8),
    _AssocTransmittedFrameCount_Type()
)
assocTransmittedFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocTransmittedFrameCount.setStatus("current")
_AssocReceiveErrors_Type = Counter64
_AssocReceiveErrors_Object = MibTableColumn
assocReceiveErrors = _AssocReceiveErrors_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 1, 1, 9),
    _AssocReceiveErrors_Type()
)
assocReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocReceiveErrors.setStatus("current")
_AssocTransmitErrors_Type = Counter64
_AssocTransmitErrors_Object = MibTableColumn
assocTransmitErrors = _AssocTransmitErrors_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 1, 1, 10),
    _AssocTransmitErrors_Type()
)
assocTransmitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocTransmitErrors.setStatus("current")
_AssocTransmitBytes_Type = Counter64
_AssocTransmitBytes_Object = MibTableColumn
assocTransmitBytes = _AssocTransmitBytes_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 1, 1, 11),
    _AssocTransmitBytes_Type()
)
assocTransmitBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocTransmitBytes.setStatus("current")
_AssocReceiveBytes_Type = Counter64
_AssocReceiveBytes_Object = MibTableColumn
assocReceiveBytes = _AssocReceiveBytes_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 1, 1, 12),
    _AssocReceiveBytes_Type()
)
assocReceiveBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocReceiveBytes.setStatus("current")
_AssocReceivedRSS_Type = Integer32
_AssocReceivedRSS_Object = MibTableColumn
assocReceivedRSS = _AssocReceivedRSS_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 1, 1, 13),
    _AssocReceivedRSS_Type()
)
assocReceivedRSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocReceivedRSS.setStatus("current")
_AssocDLLostRetriesPackets_Type = Integer32
_AssocDLLostRetriesPackets_Object = MibTableColumn
assocDLLostRetriesPackets = _AssocDLLostRetriesPackets_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 1, 1, 14),
    _AssocDLLostRetriesPackets_Type()
)
assocDLLostRetriesPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocDLLostRetriesPackets.setStatus("current")
_AssocDLLostRetriesBytes_Type = Integer32
_AssocDLLostRetriesBytes_Object = MibTableColumn
assocDLLostRetriesBytes = _AssocDLLostRetriesBytes_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 1, 1, 15),
    _AssocDLLostRetriesBytes_Type()
)
assocDLLostRetriesBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocDLLostRetriesBytes.setStatus("current")
_AssocCountersTable_Object = MibTable
assocCountersTable = _AssocCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 2)
)
if mibBuilder.loadTexts:
    assocCountersTable.setStatus("current")
_AssocCountersEntry_Object = MibTableRow
assocCountersEntry = _AssocCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 2, 1)
)
assocCountersEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-DOT11-EXTNS-MIB", "assocAddress"),
)
if mibBuilder.loadTexts:
    assocCountersEntry.setStatus("current")
_AssocAuthenticationCount_Type = Counter64
_AssocAuthenticationCount_Object = MibTableColumn
assocAuthenticationCount = _AssocAuthenticationCount_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 2, 1, 1),
    _AssocAuthenticationCount_Type()
)
assocAuthenticationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocAuthenticationCount.setStatus("current")
_AssocDeauthenticationCount_Type = Counter64
_AssocDeauthenticationCount_Object = MibTableColumn
assocDeauthenticationCount = _AssocDeauthenticationCount_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 2, 1, 2),
    _AssocDeauthenticationCount_Type()
)
assocDeauthenticationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocDeauthenticationCount.setStatus("current")
_AssocAssociationCount_Type = Counter64
_AssocAssociationCount_Object = MibTableColumn
assocAssociationCount = _AssocAssociationCount_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 2, 1, 3),
    _AssocAssociationCount_Type()
)
assocAssociationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocAssociationCount.setStatus("current")
_AssocDeassociationCount_Type = Counter64
_AssocDeassociationCount_Object = MibTableColumn
assocDeassociationCount = _AssocDeassociationCount_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 2, 1, 4),
    _AssocDeassociationCount_Type()
)
assocDeassociationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocDeassociationCount.setStatus("current")
_AssocReassociationCount_Type = Counter64
_AssocReassociationCount_Object = MibTableColumn
assocReassociationCount = _AssocReassociationCount_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 2, 1, 5),
    _AssocReassociationCount_Type()
)
assocReassociationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocReassociationCount.setStatus("current")
_Dot11ExtRadioStatsTable_Object = MibTable
dot11ExtRadioStatsTable = _Dot11ExtRadioStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 3)
)
if mibBuilder.loadTexts:
    dot11ExtRadioStatsTable.setStatus("current")
_Dot11ExtRadioStatsEntry_Object = MibTableRow
dot11ExtRadioStatsEntry = _Dot11ExtRadioStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 3, 1)
)
dot11ExtRadioStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11ExtRadioStatsEntry.setStatus("current")


class _Dot11ExtRadioType_Type(Integer32):
    """Custom type dot11ExtRadioType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("dot11a", 1),
          ("dot11ac", 11),
          ("dot11an", 2),
          ("dot11anStrict", 3),
          ("dot11b", 4),
          ("dot11bg", 6),
          ("dot11bgn", 8),
          ("dot11cStrict", 12),
          ("dot11g", 5),
          ("dot11gn", 7),
          ("dot11gnStrict", 9),
          ("dot11j", 10),
          ("off", 0))
    )


_Dot11ExtRadioType_Type.__name__ = "Integer32"
_Dot11ExtRadioType_Object = MibTableColumn
dot11ExtRadioType = _Dot11ExtRadioType_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 3, 1, 1),
    _Dot11ExtRadioType_Type()
)
dot11ExtRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ExtRadioType.setStatus("current")
_Dot11ExtRadioInUcastPkts_Type = Counter64
_Dot11ExtRadioInUcastPkts_Object = MibTableColumn
dot11ExtRadioInUcastPkts = _Dot11ExtRadioInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 3, 1, 2),
    _Dot11ExtRadioInUcastPkts_Type()
)
dot11ExtRadioInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ExtRadioInUcastPkts.setStatus("current")
_Dot11ExtRadioInMcastPkts_Type = Counter64
_Dot11ExtRadioInMcastPkts_Object = MibTableColumn
dot11ExtRadioInMcastPkts = _Dot11ExtRadioInMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 3, 1, 3),
    _Dot11ExtRadioInMcastPkts_Type()
)
dot11ExtRadioInMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ExtRadioInMcastPkts.setStatus("current")
_Dot11ExtRadioInBcastPkts_Type = Counter64
_Dot11ExtRadioInBcastPkts_Object = MibTableColumn
dot11ExtRadioInBcastPkts = _Dot11ExtRadioInBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 3, 1, 4),
    _Dot11ExtRadioInBcastPkts_Type()
)
dot11ExtRadioInBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ExtRadioInBcastPkts.setStatus("current")
_Dot11ExtRadioInOctets_Type = Counter64
_Dot11ExtRadioInOctets_Object = MibTableColumn
dot11ExtRadioInOctets = _Dot11ExtRadioInOctets_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 3, 1, 5),
    _Dot11ExtRadioInOctets_Type()
)
dot11ExtRadioInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ExtRadioInOctets.setStatus("current")
_Dot11ExtRadioInErrors_Type = Counter64
_Dot11ExtRadioInErrors_Object = MibTableColumn
dot11ExtRadioInErrors = _Dot11ExtRadioInErrors_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 3, 1, 6),
    _Dot11ExtRadioInErrors_Type()
)
dot11ExtRadioInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ExtRadioInErrors.setStatus("current")
_Dot11ExtRadioInDiscardsPkts_Type = Counter64
_Dot11ExtRadioInDiscardsPkts_Object = MibTableColumn
dot11ExtRadioInDiscardsPkts = _Dot11ExtRadioInDiscardsPkts_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 3, 1, 7),
    _Dot11ExtRadioInDiscardsPkts_Type()
)
dot11ExtRadioInDiscardsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ExtRadioInDiscardsPkts.setStatus("current")
_Dot11ExtRadioOutUcastPkts_Type = Counter64
_Dot11ExtRadioOutUcastPkts_Object = MibTableColumn
dot11ExtRadioOutUcastPkts = _Dot11ExtRadioOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 3, 1, 8),
    _Dot11ExtRadioOutUcastPkts_Type()
)
dot11ExtRadioOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ExtRadioOutUcastPkts.setStatus("current")
_Dot11ExtRadioOutMcastPkts_Type = Counter64
_Dot11ExtRadioOutMcastPkts_Object = MibTableColumn
dot11ExtRadioOutMcastPkts = _Dot11ExtRadioOutMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 3, 1, 9),
    _Dot11ExtRadioOutMcastPkts_Type()
)
dot11ExtRadioOutMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ExtRadioOutMcastPkts.setStatus("current")
_Dot11ExtRadioOutBcastPkts_Type = Counter64
_Dot11ExtRadioOutBcastPkts_Object = MibTableColumn
dot11ExtRadioOutBcastPkts = _Dot11ExtRadioOutBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 3, 1, 10),
    _Dot11ExtRadioOutBcastPkts_Type()
)
dot11ExtRadioOutBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ExtRadioOutBcastPkts.setStatus("current")
_Dot11ExtRadioOutOctets_Type = Counter64
_Dot11ExtRadioOutOctets_Object = MibTableColumn
dot11ExtRadioOutOctets = _Dot11ExtRadioOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 3, 1, 11),
    _Dot11ExtRadioOutOctets_Type()
)
dot11ExtRadioOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ExtRadioOutOctets.setStatus("current")
_Dot11ExtRadioOutErrors_Type = Counter64
_Dot11ExtRadioOutErrors_Object = MibTableColumn
dot11ExtRadioOutErrors = _Dot11ExtRadioOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 3, 1, 12),
    _Dot11ExtRadioOutErrors_Type()
)
dot11ExtRadioOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ExtRadioOutErrors.setStatus("current")
_Dot11ExtRadioOutDiscardsPkts_Type = Counter64
_Dot11ExtRadioOutDiscardsPkts_Object = MibTableColumn
dot11ExtRadioOutDiscardsPkts = _Dot11ExtRadioOutDiscardsPkts_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 3, 1, 13),
    _Dot11ExtRadioOutDiscardsPkts_Type()
)
dot11ExtRadioOutDiscardsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ExtRadioOutDiscardsPkts.setStatus("current")
_Dot11ExtRadioWepIcvErrorCount_Type = Counter64
_Dot11ExtRadioWepIcvErrorCount_Object = MibTableColumn
dot11ExtRadioWepIcvErrorCount = _Dot11ExtRadioWepIcvErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 3, 1, 14),
    _Dot11ExtRadioWepIcvErrorCount_Type()
)
dot11ExtRadioWepIcvErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ExtRadioWepIcvErrorCount.setStatus("current")
_Dot11ExtRadioWepExcludedCount_Type = Counter64
_Dot11ExtRadioWepExcludedCount_Object = MibTableColumn
dot11ExtRadioWepExcludedCount = _Dot11ExtRadioWepExcludedCount_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 3, 1, 15),
    _Dot11ExtRadioWepExcludedCount_Type()
)
dot11ExtRadioWepExcludedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ExtRadioWepExcludedCount.setStatus("current")
_Dot11ExtRadioRetryCount_Type = Counter64
_Dot11ExtRadioRetryCount_Object = MibTableColumn
dot11ExtRadioRetryCount = _Dot11ExtRadioRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 3, 1, 16),
    _Dot11ExtRadioRetryCount_Type()
)
dot11ExtRadioRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ExtRadioRetryCount.setStatus("current")
_Dot11ExtRadioMultipleRetryCount_Type = Counter64
_Dot11ExtRadioMultipleRetryCount_Object = MibTableColumn
dot11ExtRadioMultipleRetryCount = _Dot11ExtRadioMultipleRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 3, 1, 17),
    _Dot11ExtRadioMultipleRetryCount_Type()
)
dot11ExtRadioMultipleRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ExtRadioMultipleRetryCount.setStatus("current")
_Dot11ExtRadioRtsSuccessCount_Type = Counter64
_Dot11ExtRadioRtsSuccessCount_Object = MibTableColumn
dot11ExtRadioRtsSuccessCount = _Dot11ExtRadioRtsSuccessCount_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 3, 1, 18),
    _Dot11ExtRadioRtsSuccessCount_Type()
)
dot11ExtRadioRtsSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ExtRadioRtsSuccessCount.setStatus("current")
_Dot11ExtRadioRtsFailCount_Type = Counter64
_Dot11ExtRadioRtsFailCount_Object = MibTableColumn
dot11ExtRadioRtsFailCount = _Dot11ExtRadioRtsFailCount_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 3, 1, 19),
    _Dot11ExtRadioRtsFailCount_Type()
)
dot11ExtRadioRtsFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ExtRadioRtsFailCount.setStatus("current")
_Dot11ExtRadioAckFailCount_Type = Counter64
_Dot11ExtRadioAckFailCount_Object = MibTableColumn
dot11ExtRadioAckFailCount = _Dot11ExtRadioAckFailCount_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 3, 1, 20),
    _Dot11ExtRadioAckFailCount_Type()
)
dot11ExtRadioAckFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ExtRadioAckFailCount.setStatus("current")
_Dot11ExtRadioFrameDupCount_Type = Counter64
_Dot11ExtRadioFrameDupCount_Object = MibTableColumn
dot11ExtRadioFrameDupCount = _Dot11ExtRadioFrameDupCount_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 3, 1, 21),
    _Dot11ExtRadioFrameDupCount_Type()
)
dot11ExtRadioFrameDupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ExtRadioFrameDupCount.setStatus("current")
_Dot11ExtRadioTransFragCount_Type = Counter64
_Dot11ExtRadioTransFragCount_Object = MibTableColumn
dot11ExtRadioTransFragCount = _Dot11ExtRadioTransFragCount_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 3, 1, 22),
    _Dot11ExtRadioTransFragCount_Type()
)
dot11ExtRadioTransFragCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ExtRadioTransFragCount.setStatus("current")
_Dot11ExtRadioMulTransFrameCount_Type = Counter64
_Dot11ExtRadioMulTransFrameCount_Object = MibTableColumn
dot11ExtRadioMulTransFrameCount = _Dot11ExtRadioMulTransFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 3, 1, 23),
    _Dot11ExtRadioMulTransFrameCount_Type()
)
dot11ExtRadioMulTransFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ExtRadioMulTransFrameCount.setStatus("current")
_Dot11ExtRadioFailedCount_Type = Counter64
_Dot11ExtRadioFailedCount_Object = MibTableColumn
dot11ExtRadioFailedCount = _Dot11ExtRadioFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 3, 1, 24),
    _Dot11ExtRadioFailedCount_Type()
)
dot11ExtRadioFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ExtRadioFailedCount.setStatus("current")
_Dot11ExtRadioReceivedFragCount_Type = Counter64
_Dot11ExtRadioReceivedFragCount_Object = MibTableColumn
dot11ExtRadioReceivedFragCount = _Dot11ExtRadioReceivedFragCount_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 3, 1, 25),
    _Dot11ExtRadioReceivedFragCount_Type()
)
dot11ExtRadioReceivedFragCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ExtRadioReceivedFragCount.setStatus("current")
_Dot11ExtRadioMulRecFrameCount_Type = Counter64
_Dot11ExtRadioMulRecFrameCount_Object = MibTableColumn
dot11ExtRadioMulRecFrameCount = _Dot11ExtRadioMulRecFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 3, 1, 26),
    _Dot11ExtRadioMulRecFrameCount_Type()
)
dot11ExtRadioMulRecFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ExtRadioMulRecFrameCount.setStatus("current")
_Dot11ExtRadioFcsErrorCount_Type = Counter64
_Dot11ExtRadioFcsErrorCount_Object = MibTableColumn
dot11ExtRadioFcsErrorCount = _Dot11ExtRadioFcsErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 3, 1, 27),
    _Dot11ExtRadioFcsErrorCount_Type()
)
dot11ExtRadioFcsErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ExtRadioFcsErrorCount.setStatus("current")
_Dot11ExtRadioWepUndecrypCount_Type = Counter64
_Dot11ExtRadioWepUndecrypCount_Object = MibTableColumn
dot11ExtRadioWepUndecrypCount = _Dot11ExtRadioWepUndecrypCount_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 3, 1, 28),
    _Dot11ExtRadioWepUndecrypCount_Type()
)
dot11ExtRadioWepUndecrypCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ExtRadioWepUndecrypCount.setStatus("current")
_Dot11ExtRadioTransFrameCount_Type = Counter64
_Dot11ExtRadioTransFrameCount_Object = MibTableColumn
dot11ExtRadioTransFrameCount = _Dot11ExtRadioTransFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 3, 1, 29),
    _Dot11ExtRadioTransFrameCount_Type()
)
dot11ExtRadioTransFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ExtRadioTransFrameCount.setStatus("current")
_Dot11ExtRadioDeauthCacCount_Type = Counter64
_Dot11ExtRadioDeauthCacCount_Object = MibTableColumn
dot11ExtRadioDeauthCacCount = _Dot11ExtRadioDeauthCacCount_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 3, 1, 30),
    _Dot11ExtRadioDeauthCacCount_Type()
)
dot11ExtRadioDeauthCacCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ExtRadioDeauthCacCount.setStatus("current")


class _Dot11ExtRadioAvgNfCount_Type(Integer32):
    """Custom type dot11ExtRadioAvgNfCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 100),
    )


_Dot11ExtRadioAvgNfCount_Type.__name__ = "Integer32"
_Dot11ExtRadioAvgNfCount_Object = MibTableColumn
dot11ExtRadioAvgNfCount = _Dot11ExtRadioAvgNfCount_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 3, 1, 31),
    _Dot11ExtRadioAvgNfCount_Type()
)
dot11ExtRadioAvgNfCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ExtRadioAvgNfCount.setStatus("current")
if mibBuilder.loadTexts:
    dot11ExtRadioAvgNfCount.setUnits("dBm")


class _Dot11ExtRadioMaxNfCount_Type(Integer32):
    """Custom type dot11ExtRadioMaxNfCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 100),
    )


_Dot11ExtRadioMaxNfCount_Type.__name__ = "Integer32"
_Dot11ExtRadioMaxNfCount_Object = MibTableColumn
dot11ExtRadioMaxNfCount = _Dot11ExtRadioMaxNfCount_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 3, 1, 32),
    _Dot11ExtRadioMaxNfCount_Type()
)
dot11ExtRadioMaxNfCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ExtRadioMaxNfCount.setStatus("current")
if mibBuilder.loadTexts:
    dot11ExtRadioMaxNfCount.setUnits("dBm")


class _Dot11ExtRadioAvgChlOccCount_Type(Integer32):
    """Custom type dot11ExtRadioAvgChlOccCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Dot11ExtRadioAvgChlOccCount_Type.__name__ = "Integer32"
_Dot11ExtRadioAvgChlOccCount_Object = MibTableColumn
dot11ExtRadioAvgChlOccCount = _Dot11ExtRadioAvgChlOccCount_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 3, 1, 33),
    _Dot11ExtRadioAvgChlOccCount_Type()
)
dot11ExtRadioAvgChlOccCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ExtRadioAvgChlOccCount.setStatus("current")


class _Dot11ExtRadioMaxChlOccCount_Type(Integer32):
    """Custom type dot11ExtRadioMaxChlOccCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Dot11ExtRadioMaxChlOccCount_Type.__name__ = "Integer32"
_Dot11ExtRadioMaxChlOccCount_Object = MibTableColumn
dot11ExtRadioMaxChlOccCount = _Dot11ExtRadioMaxChlOccCount_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 3, 1, 34),
    _Dot11ExtRadioMaxChlOccCount_Type()
)
dot11ExtRadioMaxChlOccCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ExtRadioMaxChlOccCount.setStatus("current")


class _Dot11ExtRadioAvgTxOccCount_Type(Integer32):
    """Custom type dot11ExtRadioAvgTxOccCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Dot11ExtRadioAvgTxOccCount_Type.__name__ = "Integer32"
_Dot11ExtRadioAvgTxOccCount_Object = MibTableColumn
dot11ExtRadioAvgTxOccCount = _Dot11ExtRadioAvgTxOccCount_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 3, 1, 35),
    _Dot11ExtRadioAvgTxOccCount_Type()
)
dot11ExtRadioAvgTxOccCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ExtRadioAvgTxOccCount.setStatus("current")


class _Dot11ExtRadioMaxTxOccCount_Type(Integer32):
    """Custom type dot11ExtRadioMaxTxOccCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Dot11ExtRadioMaxTxOccCount_Type.__name__ = "Integer32"
_Dot11ExtRadioMaxTxOccCount_Object = MibTableColumn
dot11ExtRadioMaxTxOccCount = _Dot11ExtRadioMaxTxOccCount_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 3, 1, 36),
    _Dot11ExtRadioMaxTxOccCount_Type()
)
dot11ExtRadioMaxTxOccCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ExtRadioMaxTxOccCount.setStatus("current")


class _Dot11ExtRadioAvgRxOccCount_Type(Integer32):
    """Custom type dot11ExtRadioAvgRxOccCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Dot11ExtRadioAvgRxOccCount_Type.__name__ = "Integer32"
_Dot11ExtRadioAvgRxOccCount_Object = MibTableColumn
dot11ExtRadioAvgRxOccCount = _Dot11ExtRadioAvgRxOccCount_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 3, 1, 37),
    _Dot11ExtRadioAvgRxOccCount_Type()
)
dot11ExtRadioAvgRxOccCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ExtRadioAvgRxOccCount.setStatus("current")


class _Dot11ExtRadioMaxRxOccCount_Type(Integer32):
    """Custom type dot11ExtRadioMaxRxOccCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Dot11ExtRadioMaxRxOccCount_Type.__name__ = "Integer32"
_Dot11ExtRadioMaxRxOccCount_Object = MibTableColumn
dot11ExtRadioMaxRxOccCount = _Dot11ExtRadioMaxRxOccCount_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 3, 1, 38),
    _Dot11ExtRadioMaxRxOccCount_Type()
)
dot11ExtRadioMaxRxOccCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ExtRadioMaxRxOccCount.setStatus("current")
_Dot11ExtRadioAvgBusyChPercentage_Type = Unsigned32
_Dot11ExtRadioAvgBusyChPercentage_Object = MibTableColumn
dot11ExtRadioAvgBusyChPercentage = _Dot11ExtRadioAvgBusyChPercentage_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 3, 1, 39),
    _Dot11ExtRadioAvgBusyChPercentage_Type()
)
dot11ExtRadioAvgBusyChPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ExtRadioAvgBusyChPercentage.setStatus("current")
_Dot11ExtRadioMaxBusyChPercentage_Type = Unsigned32
_Dot11ExtRadioMaxBusyChPercentage_Object = MibTableColumn
dot11ExtRadioMaxBusyChPercentage = _Dot11ExtRadioMaxBusyChPercentage_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 3, 1, 40),
    _Dot11ExtRadioMaxBusyChPercentage_Type()
)
dot11ExtRadioMaxBusyChPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ExtRadioMaxBusyChPercentage.setStatus("current")
_Dot11ExtRadioAvgRxChOccPercentage_Type = Unsigned32
_Dot11ExtRadioAvgRxChOccPercentage_Object = MibTableColumn
dot11ExtRadioAvgRxChOccPercentage = _Dot11ExtRadioAvgRxChOccPercentage_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 3, 1, 41),
    _Dot11ExtRadioAvgRxChOccPercentage_Type()
)
dot11ExtRadioAvgRxChOccPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ExtRadioAvgRxChOccPercentage.setStatus("current")
_Dot11ExtRadioMaxRxChOccPercentage_Type = Unsigned32
_Dot11ExtRadioMaxRxChOccPercentage_Object = MibTableColumn
dot11ExtRadioMaxRxChOccPercentage = _Dot11ExtRadioMaxRxChOccPercentage_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 4, 3, 1, 42),
    _Dot11ExtRadioMaxRxChOccPercentage_Type()
)
dot11ExtRadioMaxRxChOccPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ExtRadioMaxRxChOccPercentage.setStatus("current")
_Dot11ExtConformance_ObjectIdentity = ObjectIdentity
dot11ExtConformance = _Dot11ExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 5)
)
_Dot11EWCGroups_ObjectIdentity = ObjectIdentity
dot11EWCGroups = _Dot11EWCGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 5, 4)
)

# Managed Objects groups

hiPathWirelessDot11ExtGroups = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 5, 2)
)
hiPathWirelessDot11ExtGroups.setObjects(
      *(("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtSSIDID"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtSSID"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtWEPKeyMappingIndex"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtWEPKeyMappingAddress"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtWEPKeyMappingWEPOn"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtWEPKeyMappingValue"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtWEPKeyMappingStatus"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11gEnabled"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11gProtectionMode"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11gProtectionType"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "smtShortPreambleInvoked"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtBSSID"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtBSSIDWEPKeyIndex"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11bEnabled"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11Capabilities"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtBSSIndex"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtSSIDSuppress"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtPriorityTrafficHandling"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11gProtectionRate"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot1XWPA2Enabled"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot1XEnabled"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot1XDynamicRekeyingInterval"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot1XWPA1Enabled"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot1XWPAPassphrase"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot1XWPACipherType"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtSmtMinBasicRate"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtSmtMaxBasicRate"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtSmtMaxOperationalRate"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11DiversityTxDiversity"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11DiversityRxDiversity"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot1XConfigKeyManagement"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtSmtTVOretries"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtSmtCurChanSelectedByAP"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtSmtRFDomain"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtSmtAutoTxPowerCtrl"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtSmtCurrentTxPowerLevel"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtSmtMaxTxPower"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtSmtMinTxPower"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtSmtAutoTxPowerCtrlAdjust"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtSmtBGretries"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtSmtBEretries"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtSmtVIretries"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtSmtVOretries"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11gProtectionModeSelected"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot1XWPA2CipherType"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtSmtCurrentChannel"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtSmtDcsMode"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtSmtDcsNoiseThreshold"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtSmtDcsChlOccThreshold"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtSmtDcsUpdatePeriod"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtSmtDcsChannelSelection"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtSmtDcsChannelList"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11AntennaSelection"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtSmtRadioAttenuation"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtSmtProbeSuppression"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtSmtForceDisassociate"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtSmtRssThreshold"))
)
if mibBuilder.loadTexts:
    hiPathWirelessDot11ExtGroups.setStatus("current")

hiPathWirelessDot11ObsoleteGroups = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 5, 3)
)
hiPathWirelessDot11ObsoleteGroups.setObjects(
      *(("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "vlanBridgeMode"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11gBasicG"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11BasicB"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "vlanTag"))
)
if mibBuilder.loadTexts:
    hiPathWirelessDot11ObsoleteGroups.setStatus("obsolete")

dot11nConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 5, 4, 1)
)
dot11nConfigGroup.setObjects(
      *(("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11nEnabled"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11nChlBonding"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11nChlWidth"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11nChlGuardInterval"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11nProtectEnabled"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11nProtectType"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11nProtectOffset"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11nPtotectBusyThr"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11nAggrMsduEnabled"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11nAggrMsduMaxLen"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11nAggrMpduEnabled"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11nAggrMpduMaxLen"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11nAggrMsduSubFrames"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11nAddbaSupEnabled"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11nConfigLDPC"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11nConfigSTBC"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11nConfigTXBF"))
)
if mibBuilder.loadTexts:
    dot11nConfigGroup.setStatus("current")

assocGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 5, 4, 2)
)
assocGroupGroup.setObjects(
      *(("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "assocAddress"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "assocIfIndex"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "assocReceivedRSSI"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "assocTransmittedRSSI"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "assocReceivedRate"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "assocTransmittedRate"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "assocReceivedFrameCount"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "assocTransmittedFrameCount"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "assocReceiveErrors"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "assocTransmitErrors"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "assocTransmitBytes"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "assocReceiveBytes"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "assocReceivedRSS"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "assocDLLostRetriesPackets"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "assocDLLostRetriesBytes"))
)
if mibBuilder.loadTexts:
    assocGroupGroup.setStatus("current")

assocCountersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 5, 4, 3)
)
assocCountersGroup.setObjects(
      *(("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "assocAuthenticationCount"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "assocDeauthenticationCount"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "assocAssociationCount"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "assocDeassociationCount"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "assocReassociationCount"))
)
if mibBuilder.loadTexts:
    assocCountersGroup.setStatus("current")

dot11ExtRadioStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 5, 4, 4)
)
dot11ExtRadioStatsGroup.setObjects(
      *(("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtRadioType"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtRadioInUcastPkts"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtRadioInMcastPkts"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtRadioInBcastPkts"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtRadioInOctets"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtRadioInErrors"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtRadioInDiscardsPkts"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtRadioOutUcastPkts"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtRadioOutMcastPkts"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtRadioOutBcastPkts"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtRadioOutOctets"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtRadioOutErrors"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtRadioOutDiscardsPkts"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtRadioWepIcvErrorCount"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtRadioWepExcludedCount"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtRadioRetryCount"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtRadioMultipleRetryCount"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtRadioRtsSuccessCount"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtRadioRtsFailCount"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtRadioAckFailCount"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtRadioFrameDupCount"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtRadioTransFragCount"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtRadioMulTransFrameCount"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtRadioFailedCount"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtRadioReceivedFragCount"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtRadioMulRecFrameCount"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtRadioFcsErrorCount"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtRadioWepUndecrypCount"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtRadioTransFrameCount"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtRadioDeauthCacCount"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtRadioAvgNfCount"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtRadioMaxNfCount"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtRadioAvgChlOccCount"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtRadioMaxChlOccCount"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtRadioAvgTxOccCount"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtRadioMaxTxOccCount"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtRadioAvgRxOccCount"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtRadioMaxRxOccCount"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtRadioAvgBusyChPercentage"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtRadioMaxBusyChPercentage"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtRadioAvgRxChOccPercentage"),
        ("HIPATH-WIRELESS-DOT11-EXTNS-MIB", "dot11ExtRadioMaxRxChOccPercentage"))
)
if mibBuilder.loadTexts:
    dot11ExtRadioStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hiPathWirelessDot11ExtModule = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 1, 5, 1)
)
if mibBuilder.loadTexts:
    hiPathWirelessDot11ExtModule.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HIPATH-WIRELESS-DOT11-EXTNS-MIB",
    **{"WEPKeytype": WEPKeytype,
       "dot11ExtnsMib": dot11ExtnsMib,
       "dot11Extsmt": dot11Extsmt,
       "dot11ExtBSSIDTable": dot11ExtBSSIDTable,
       "dot11ExtBSSIDEntry": dot11ExtBSSIDEntry,
       "dot11ExtBSSIndex": dot11ExtBSSIndex,
       "dot11ExtBSSID": dot11ExtBSSID,
       "dot11ExtSSIDID": dot11ExtSSIDID,
       "dot11ExtSSID": dot11ExtSSID,
       "dot11ExtBSSIDWEPKeyIndex": dot11ExtBSSIDWEPKeyIndex,
       "dot11ExtSSIDSuppress": dot11ExtSSIDSuppress,
       "dot11ExtPriorityTrafficHandling": dot11ExtPriorityTrafficHandling,
       "dot11ExtWEPKeyMappingsTable": dot11ExtWEPKeyMappingsTable,
       "dot11ExtWEPKeyMappingsEntry": dot11ExtWEPKeyMappingsEntry,
       "dot11ExtWEPKeyMappingIndex": dot11ExtWEPKeyMappingIndex,
       "dot11ExtWEPKeyMappingAddress": dot11ExtWEPKeyMappingAddress,
       "dot11ExtWEPKeyMappingWEPOn": dot11ExtWEPKeyMappingWEPOn,
       "dot11ExtWEPKeyMappingValue": dot11ExtWEPKeyMappingValue,
       "dot11ExtWEPKeyMappingStatus": dot11ExtWEPKeyMappingStatus,
       "dot11CapabilitiesTable": dot11CapabilitiesTable,
       "dot11CapabilitiesEntry": dot11CapabilitiesEntry,
       "dot11Capabilities": dot11Capabilities,
       "dot11bConfigTable": dot11bConfigTable,
       "dot11bConfigEntry": dot11bConfigEntry,
       "dot11bEnabled": dot11bEnabled,
       "dot11BasicB": dot11BasicB,
       "dot11gConfigTable": dot11gConfigTable,
       "dot11gConfigEntry": dot11gConfigEntry,
       "dot11gEnabled": dot11gEnabled,
       "dot11gProtectionMode": dot11gProtectionMode,
       "dot11gProtectionType": dot11gProtectionType,
       "dot11gProtectionRate": dot11gProtectionRate,
       "dot11gBasicG": dot11gBasicG,
       "dot11gProtectionModeSelected": dot11gProtectionModeSelected,
       "dot11ExtSmtTable": dot11ExtSmtTable,
       "dot11ExtSmtEntry": dot11ExtSmtEntry,
       "smtShortPreambleInvoked": smtShortPreambleInvoked,
       "dot11ExtSmtCurrentChannel": dot11ExtSmtCurrentChannel,
       "dot11ExtSmtMaxBasicRate": dot11ExtSmtMaxBasicRate,
       "dot11ExtSmtMinBasicRate": dot11ExtSmtMinBasicRate,
       "dot11ExtSmtMaxOperationalRate": dot11ExtSmtMaxOperationalRate,
       "dot11ExtSmtCurChanSelectedByAP": dot11ExtSmtCurChanSelectedByAP,
       "dot11ExtSmtRFDomain": dot11ExtSmtRFDomain,
       "dot11ExtSmtAutoTxPowerCtrl": dot11ExtSmtAutoTxPowerCtrl,
       "dot11ExtSmtCurrentTxPowerLevel": dot11ExtSmtCurrentTxPowerLevel,
       "dot11ExtSmtMaxTxPower": dot11ExtSmtMaxTxPower,
       "dot11ExtSmtMinTxPower": dot11ExtSmtMinTxPower,
       "dot11ExtSmtAutoTxPowerCtrlAdjust": dot11ExtSmtAutoTxPowerCtrlAdjust,
       "dot11ExtSmtBGretries": dot11ExtSmtBGretries,
       "dot11ExtSmtBEretries": dot11ExtSmtBEretries,
       "dot11ExtSmtVIretries": dot11ExtSmtVIretries,
       "dot11ExtSmtVOretries": dot11ExtSmtVOretries,
       "dot11ExtSmtTVOretries": dot11ExtSmtTVOretries,
       "dot11ExtSmtDcsMode": dot11ExtSmtDcsMode,
       "dot11ExtSmtDcsNoiseThreshold": dot11ExtSmtDcsNoiseThreshold,
       "dot11ExtSmtDcsChlOccThreshold": dot11ExtSmtDcsChlOccThreshold,
       "dot11ExtSmtDcsUpdatePeriod": dot11ExtSmtDcsUpdatePeriod,
       "dot11ExtSmtDcsChannelSelection": dot11ExtSmtDcsChannelSelection,
       "dot11ExtSmtDcsChannelList": dot11ExtSmtDcsChannelList,
       "dot11ExtSmtRadioAttenuation": dot11ExtSmtRadioAttenuation,
       "dot11ExtSmtProbeSuppression": dot11ExtSmtProbeSuppression,
       "dot11ExtSmtForceDisassociate": dot11ExtSmtForceDisassociate,
       "dot11ExtSmtRssThreshold": dot11ExtSmtRssThreshold,
       "dot11ExtVlanSmtTable": dot11ExtVlanSmtTable,
       "dot11ExtVlanSmtEntry": dot11ExtVlanSmtEntry,
       "vlanBridgeMode": vlanBridgeMode,
       "vlanTag": vlanTag,
       "dot11DiversityTable": dot11DiversityTable,
       "dot11DiversityEntry": dot11DiversityEntry,
       "dot11DiversityRxDiversity": dot11DiversityRxDiversity,
       "dot11DiversityTxDiversity": dot11DiversityTxDiversity,
       "dot11AntennaSelection": dot11AntennaSelection,
       "dot11nConfigTable": dot11nConfigTable,
       "dot11nConfigEntry": dot11nConfigEntry,
       "dot11nEnabled": dot11nEnabled,
       "dot11nChlBonding": dot11nChlBonding,
       "dot11nChlWidth": dot11nChlWidth,
       "dot11nChlGuardInterval": dot11nChlGuardInterval,
       "dot11nProtectEnabled": dot11nProtectEnabled,
       "dot11nProtectType": dot11nProtectType,
       "dot11nProtectOffset": dot11nProtectOffset,
       "dot11nPtotectBusyThr": dot11nPtotectBusyThr,
       "dot11nAggrMsduEnabled": dot11nAggrMsduEnabled,
       "dot11nAggrMsduMaxLen": dot11nAggrMsduMaxLen,
       "dot11nAggrMpduEnabled": dot11nAggrMpduEnabled,
       "dot11nAggrMpduMaxLen": dot11nAggrMpduMaxLen,
       "dot11nAggrMsduSubFrames": dot11nAggrMsduSubFrames,
       "dot11nAddbaSupEnabled": dot11nAddbaSupEnabled,
       "dot11nConfigLDPC": dot11nConfigLDPC,
       "dot11nConfigSTBC": dot11nConfigSTBC,
       "dot11nConfigTXBF": dot11nConfigTXBF,
       "dot11ExtAPObjs": dot11ExtAPObjs,
       "dot1XConfigTable": dot1XConfigTable,
       "dot1XConfigEntry": dot1XConfigEntry,
       "dot1XEnabled": dot1XEnabled,
       "dot1XDynamicRekeyingInterval": dot1XDynamicRekeyingInterval,
       "dot1XWPA1Enabled": dot1XWPA1Enabled,
       "dot1XWPAPassphrase": dot1XWPAPassphrase,
       "dot1XWPACipherType": dot1XWPACipherType,
       "dot1XWPA2Enabled": dot1XWPA2Enabled,
       "dot1XWPA2CipherType": dot1XWPA2CipherType,
       "dot1XConfigKeyManagement": dot1XConfigKeyManagement,
       "dot11ExtCounters": dot11ExtCounters,
       "assocGroupTable": assocGroupTable,
       "assocGroupEntry": assocGroupEntry,
       "assocAddress": assocAddress,
       "assocIfIndex": assocIfIndex,
       "assocReceivedRSSI": assocReceivedRSSI,
       "assocTransmittedRSSI": assocTransmittedRSSI,
       "assocReceivedRate": assocReceivedRate,
       "assocTransmittedRate": assocTransmittedRate,
       "assocReceivedFrameCount": assocReceivedFrameCount,
       "assocTransmittedFrameCount": assocTransmittedFrameCount,
       "assocReceiveErrors": assocReceiveErrors,
       "assocTransmitErrors": assocTransmitErrors,
       "assocTransmitBytes": assocTransmitBytes,
       "assocReceiveBytes": assocReceiveBytes,
       "assocReceivedRSS": assocReceivedRSS,
       "assocDLLostRetriesPackets": assocDLLostRetriesPackets,
       "assocDLLostRetriesBytes": assocDLLostRetriesBytes,
       "assocCountersTable": assocCountersTable,
       "assocCountersEntry": assocCountersEntry,
       "assocAuthenticationCount": assocAuthenticationCount,
       "assocDeauthenticationCount": assocDeauthenticationCount,
       "assocAssociationCount": assocAssociationCount,
       "assocDeassociationCount": assocDeassociationCount,
       "assocReassociationCount": assocReassociationCount,
       "dot11ExtRadioStatsTable": dot11ExtRadioStatsTable,
       "dot11ExtRadioStatsEntry": dot11ExtRadioStatsEntry,
       "dot11ExtRadioType": dot11ExtRadioType,
       "dot11ExtRadioInUcastPkts": dot11ExtRadioInUcastPkts,
       "dot11ExtRadioInMcastPkts": dot11ExtRadioInMcastPkts,
       "dot11ExtRadioInBcastPkts": dot11ExtRadioInBcastPkts,
       "dot11ExtRadioInOctets": dot11ExtRadioInOctets,
       "dot11ExtRadioInErrors": dot11ExtRadioInErrors,
       "dot11ExtRadioInDiscardsPkts": dot11ExtRadioInDiscardsPkts,
       "dot11ExtRadioOutUcastPkts": dot11ExtRadioOutUcastPkts,
       "dot11ExtRadioOutMcastPkts": dot11ExtRadioOutMcastPkts,
       "dot11ExtRadioOutBcastPkts": dot11ExtRadioOutBcastPkts,
       "dot11ExtRadioOutOctets": dot11ExtRadioOutOctets,
       "dot11ExtRadioOutErrors": dot11ExtRadioOutErrors,
       "dot11ExtRadioOutDiscardsPkts": dot11ExtRadioOutDiscardsPkts,
       "dot11ExtRadioWepIcvErrorCount": dot11ExtRadioWepIcvErrorCount,
       "dot11ExtRadioWepExcludedCount": dot11ExtRadioWepExcludedCount,
       "dot11ExtRadioRetryCount": dot11ExtRadioRetryCount,
       "dot11ExtRadioMultipleRetryCount": dot11ExtRadioMultipleRetryCount,
       "dot11ExtRadioRtsSuccessCount": dot11ExtRadioRtsSuccessCount,
       "dot11ExtRadioRtsFailCount": dot11ExtRadioRtsFailCount,
       "dot11ExtRadioAckFailCount": dot11ExtRadioAckFailCount,
       "dot11ExtRadioFrameDupCount": dot11ExtRadioFrameDupCount,
       "dot11ExtRadioTransFragCount": dot11ExtRadioTransFragCount,
       "dot11ExtRadioMulTransFrameCount": dot11ExtRadioMulTransFrameCount,
       "dot11ExtRadioFailedCount": dot11ExtRadioFailedCount,
       "dot11ExtRadioReceivedFragCount": dot11ExtRadioReceivedFragCount,
       "dot11ExtRadioMulRecFrameCount": dot11ExtRadioMulRecFrameCount,
       "dot11ExtRadioFcsErrorCount": dot11ExtRadioFcsErrorCount,
       "dot11ExtRadioWepUndecrypCount": dot11ExtRadioWepUndecrypCount,
       "dot11ExtRadioTransFrameCount": dot11ExtRadioTransFrameCount,
       "dot11ExtRadioDeauthCacCount": dot11ExtRadioDeauthCacCount,
       "dot11ExtRadioAvgNfCount": dot11ExtRadioAvgNfCount,
       "dot11ExtRadioMaxNfCount": dot11ExtRadioMaxNfCount,
       "dot11ExtRadioAvgChlOccCount": dot11ExtRadioAvgChlOccCount,
       "dot11ExtRadioMaxChlOccCount": dot11ExtRadioMaxChlOccCount,
       "dot11ExtRadioAvgTxOccCount": dot11ExtRadioAvgTxOccCount,
       "dot11ExtRadioMaxTxOccCount": dot11ExtRadioMaxTxOccCount,
       "dot11ExtRadioAvgRxOccCount": dot11ExtRadioAvgRxOccCount,
       "dot11ExtRadioMaxRxOccCount": dot11ExtRadioMaxRxOccCount,
       "dot11ExtRadioAvgBusyChPercentage": dot11ExtRadioAvgBusyChPercentage,
       "dot11ExtRadioMaxBusyChPercentage": dot11ExtRadioMaxBusyChPercentage,
       "dot11ExtRadioAvgRxChOccPercentage": dot11ExtRadioAvgRxChOccPercentage,
       "dot11ExtRadioMaxRxChOccPercentage": dot11ExtRadioMaxRxChOccPercentage,
       "dot11ExtConformance": dot11ExtConformance,
       "hiPathWirelessDot11ExtModule": hiPathWirelessDot11ExtModule,
       "hiPathWirelessDot11ExtGroups": hiPathWirelessDot11ExtGroups,
       "hiPathWirelessDot11ObsoleteGroups": hiPathWirelessDot11ObsoleteGroups,
       "dot11EWCGroups": dot11EWCGroups,
       "dot11nConfigGroup": dot11nConfigGroup,
       "assocGroupGroup": assocGroupGroup,
       "assocCountersGroup": assocCountersGroup,
       "dot11ExtRadioStatsGroup": dot11ExtRadioStatsGroup,
       "hiPathWirelessDot11ExtnsMIB": hiPathWirelessDot11ExtnsMIB}
)
