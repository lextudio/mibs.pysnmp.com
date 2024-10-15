# SNMP MIB module (NATV2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NATV2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:41 2024
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

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

natv2MIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 234)
)
natv2MIB.setRevisions(
        ("2015-10-02 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ProtocolNumber(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class Natv2SubscriberIndex(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class Natv2SubscriberIndexOrZero(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )



class Natv2InstanceIndex(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class Natv2PoolIndex(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class Natv2PoolIndexOrZero(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )



# MIB Managed Objects in the order of their OIDs

_Natv2MIBNotifications_ObjectIdentity = ObjectIdentity
natv2MIBNotifications = _Natv2MIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 234, 0)
)
_Natv2MIBDeviceObjects_ObjectIdentity = ObjectIdentity
natv2MIBDeviceObjects = _Natv2MIBDeviceObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 234, 1)
)
_Natv2SubscriberTable_Object = MibTable
natv2SubscriberTable = _Natv2SubscriberTable_Object(
    (1, 3, 6, 1, 2, 1, 234, 1, 1)
)
if mibBuilder.loadTexts:
    natv2SubscriberTable.setStatus("current")
_Natv2SubscriberEntry_Object = MibTableRow
natv2SubscriberEntry = _Natv2SubscriberEntry_Object(
    (1, 3, 6, 1, 2, 1, 234, 1, 1, 1)
)
natv2SubscriberEntry.setIndexNames(
    (0, "NATV2-MIB", "natv2SubscriberIndex"),
)
if mibBuilder.loadTexts:
    natv2SubscriberEntry.setStatus("current")
_Natv2SubscriberIndex_Type = Natv2SubscriberIndex
_Natv2SubscriberIndex_Object = MibTableColumn
natv2SubscriberIndex = _Natv2SubscriberIndex_Object(
    (1, 3, 6, 1, 2, 1, 234, 1, 1, 1, 1),
    _Natv2SubscriberIndex_Type()
)
natv2SubscriberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natv2SubscriberIndex.setStatus("current")


class _Natv2SubscriberInternalRealm_Type(SnmpAdminString):
    """Custom type natv2SubscriberInternalRealm based on SnmpAdminString"""
    defaultValue = OctetString("internal")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Natv2SubscriberInternalRealm_Type.__name__ = "SnmpAdminString"
_Natv2SubscriberInternalRealm_Object = MibTableColumn
natv2SubscriberInternalRealm = _Natv2SubscriberInternalRealm_Object(
    (1, 3, 6, 1, 2, 1, 234, 1, 1, 1, 2),
    _Natv2SubscriberInternalRealm_Type()
)
natv2SubscriberInternalRealm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2SubscriberInternalRealm.setStatus("current")
_Natv2SubscriberInternalPrefixType_Type = InetAddressType
_Natv2SubscriberInternalPrefixType_Object = MibTableColumn
natv2SubscriberInternalPrefixType = _Natv2SubscriberInternalPrefixType_Object(
    (1, 3, 6, 1, 2, 1, 234, 1, 1, 1, 3),
    _Natv2SubscriberInternalPrefixType_Type()
)
natv2SubscriberInternalPrefixType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2SubscriberInternalPrefixType.setStatus("current")
_Natv2SubscriberInternalPrefix_Type = InetAddress
_Natv2SubscriberInternalPrefix_Object = MibTableColumn
natv2SubscriberInternalPrefix = _Natv2SubscriberInternalPrefix_Object(
    (1, 3, 6, 1, 2, 1, 234, 1, 1, 1, 4),
    _Natv2SubscriberInternalPrefix_Type()
)
natv2SubscriberInternalPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2SubscriberInternalPrefix.setStatus("current")
_Natv2SubscriberInternalPrefixLength_Type = InetAddressPrefixLength
_Natv2SubscriberInternalPrefixLength_Object = MibTableColumn
natv2SubscriberInternalPrefixLength = _Natv2SubscriberInternalPrefixLength_Object(
    (1, 3, 6, 1, 2, 1, 234, 1, 1, 1, 5),
    _Natv2SubscriberInternalPrefixLength_Type()
)
natv2SubscriberInternalPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2SubscriberInternalPrefixLength.setStatus("current")
_Natv2SubscriberAddressMapEntries_Type = Unsigned32
_Natv2SubscriberAddressMapEntries_Object = MibTableColumn
natv2SubscriberAddressMapEntries = _Natv2SubscriberAddressMapEntries_Object(
    (1, 3, 6, 1, 2, 1, 234, 1, 1, 1, 6),
    _Natv2SubscriberAddressMapEntries_Type()
)
natv2SubscriberAddressMapEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2SubscriberAddressMapEntries.setStatus("current")
_Natv2SubscriberPortMapEntries_Type = Unsigned32
_Natv2SubscriberPortMapEntries_Object = MibTableColumn
natv2SubscriberPortMapEntries = _Natv2SubscriberPortMapEntries_Object(
    (1, 3, 6, 1, 2, 1, 234, 1, 1, 1, 7),
    _Natv2SubscriberPortMapEntries_Type()
)
natv2SubscriberPortMapEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2SubscriberPortMapEntries.setStatus("current")
_Natv2SubscriberTranslations_Type = Counter64
_Natv2SubscriberTranslations_Object = MibTableColumn
natv2SubscriberTranslations = _Natv2SubscriberTranslations_Object(
    (1, 3, 6, 1, 2, 1, 234, 1, 1, 1, 8),
    _Natv2SubscriberTranslations_Type()
)
natv2SubscriberTranslations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2SubscriberTranslations.setStatus("current")
_Natv2SubscriberAddressMapCreations_Type = Counter64
_Natv2SubscriberAddressMapCreations_Object = MibTableColumn
natv2SubscriberAddressMapCreations = _Natv2SubscriberAddressMapCreations_Object(
    (1, 3, 6, 1, 2, 1, 234, 1, 1, 1, 9),
    _Natv2SubscriberAddressMapCreations_Type()
)
natv2SubscriberAddressMapCreations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2SubscriberAddressMapCreations.setStatus("current")
_Natv2SubscriberPortMapCreations_Type = Counter64
_Natv2SubscriberPortMapCreations_Object = MibTableColumn
natv2SubscriberPortMapCreations = _Natv2SubscriberPortMapCreations_Object(
    (1, 3, 6, 1, 2, 1, 234, 1, 1, 1, 10),
    _Natv2SubscriberPortMapCreations_Type()
)
natv2SubscriberPortMapCreations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2SubscriberPortMapCreations.setStatus("current")
_Natv2SubscriberAddressMapFailureDrops_Type = Counter64
_Natv2SubscriberAddressMapFailureDrops_Object = MibTableColumn
natv2SubscriberAddressMapFailureDrops = _Natv2SubscriberAddressMapFailureDrops_Object(
    (1, 3, 6, 1, 2, 1, 234, 1, 1, 1, 11),
    _Natv2SubscriberAddressMapFailureDrops_Type()
)
natv2SubscriberAddressMapFailureDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2SubscriberAddressMapFailureDrops.setStatus("current")
_Natv2SubscriberPortMapFailureDrops_Type = Counter64
_Natv2SubscriberPortMapFailureDrops_Object = MibTableColumn
natv2SubscriberPortMapFailureDrops = _Natv2SubscriberPortMapFailureDrops_Object(
    (1, 3, 6, 1, 2, 1, 234, 1, 1, 1, 12),
    _Natv2SubscriberPortMapFailureDrops_Type()
)
natv2SubscriberPortMapFailureDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2SubscriberPortMapFailureDrops.setStatus("current")
_Natv2SubscriberDiscontinuityTime_Type = TimeStamp
_Natv2SubscriberDiscontinuityTime_Object = MibTableColumn
natv2SubscriberDiscontinuityTime = _Natv2SubscriberDiscontinuityTime_Object(
    (1, 3, 6, 1, 2, 1, 234, 1, 1, 1, 14),
    _Natv2SubscriberDiscontinuityTime_Type()
)
natv2SubscriberDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2SubscriberDiscontinuityTime.setStatus("current")


class _Natv2SubscriberLimitPortMapEntries_Type(Unsigned32):
    """Custom type natv2SubscriberLimitPortMapEntries based on Unsigned32"""
    defaultValue = 0


_Natv2SubscriberLimitPortMapEntries_Object = MibTableColumn
natv2SubscriberLimitPortMapEntries = _Natv2SubscriberLimitPortMapEntries_Object(
    (1, 3, 6, 1, 2, 1, 234, 1, 1, 1, 15),
    _Natv2SubscriberLimitPortMapEntries_Type()
)
natv2SubscriberLimitPortMapEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natv2SubscriberLimitPortMapEntries.setStatus("current")


class _Natv2SubscriberThresholdPortMapEntriesHigh_Type(Integer32):
    """Custom type natv2SubscriberThresholdPortMapEntriesHigh based on Integer32"""
    defaultValue = -1


_Natv2SubscriberThresholdPortMapEntriesHigh_Object = MibTableColumn
natv2SubscriberThresholdPortMapEntriesHigh = _Natv2SubscriberThresholdPortMapEntriesHigh_Object(
    (1, 3, 6, 1, 2, 1, 234, 1, 1, 1, 16),
    _Natv2SubscriberThresholdPortMapEntriesHigh_Type()
)
natv2SubscriberThresholdPortMapEntriesHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natv2SubscriberThresholdPortMapEntriesHigh.setStatus("current")


class _Natv2SubscriberNotificationInterval_Type(Unsigned32):
    """Custom type natv2SubscriberNotificationInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_Natv2SubscriberNotificationInterval_Type.__name__ = "Unsigned32"
_Natv2SubscriberNotificationInterval_Object = MibTableColumn
natv2SubscriberNotificationInterval = _Natv2SubscriberNotificationInterval_Object(
    (1, 3, 6, 1, 2, 1, 234, 1, 1, 1, 17),
    _Natv2SubscriberNotificationInterval_Type()
)
natv2SubscriberNotificationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natv2SubscriberNotificationInterval.setStatus("current")
if mibBuilder.loadTexts:
    natv2SubscriberNotificationInterval.setUnits("Seconds")
_Natv2MIBInstanceObjects_ObjectIdentity = ObjectIdentity
natv2MIBInstanceObjects = _Natv2MIBInstanceObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 234, 2)
)
_Natv2InstanceTable_Object = MibTable
natv2InstanceTable = _Natv2InstanceTable_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 1)
)
if mibBuilder.loadTexts:
    natv2InstanceTable.setStatus("current")
_Natv2InstanceEntry_Object = MibTableRow
natv2InstanceEntry = _Natv2InstanceEntry_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 1, 1)
)
natv2InstanceEntry.setIndexNames(
    (0, "NATV2-MIB", "natv2InstanceIndex"),
)
if mibBuilder.loadTexts:
    natv2InstanceEntry.setStatus("current")
_Natv2InstanceIndex_Type = Natv2InstanceIndex
_Natv2InstanceIndex_Object = MibTableColumn
natv2InstanceIndex = _Natv2InstanceIndex_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 1, 1, 1),
    _Natv2InstanceIndex_Type()
)
natv2InstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natv2InstanceIndex.setStatus("current")


class _Natv2InstanceAlias_Type(DisplayString):
    """Custom type natv2InstanceAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Natv2InstanceAlias_Type.__name__ = "DisplayString"
_Natv2InstanceAlias_Object = MibTableColumn
natv2InstanceAlias = _Natv2InstanceAlias_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 1, 1, 2),
    _Natv2InstanceAlias_Type()
)
natv2InstanceAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2InstanceAlias.setStatus("current")


class _Natv2InstancePortMappingBehavior_Type(Integer32):
    """Custom type natv2InstancePortMappingBehavior based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("addressAndPortDependent", 2),
          ("addressDependent", 1),
          ("endpointIndependent", 0))
    )


_Natv2InstancePortMappingBehavior_Type.__name__ = "Integer32"
_Natv2InstancePortMappingBehavior_Object = MibTableColumn
natv2InstancePortMappingBehavior = _Natv2InstancePortMappingBehavior_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 1, 1, 3),
    _Natv2InstancePortMappingBehavior_Type()
)
natv2InstancePortMappingBehavior.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2InstancePortMappingBehavior.setStatus("current")


class _Natv2InstanceFilteringBehavior_Type(Integer32):
    """Custom type natv2InstanceFilteringBehavior based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("addressAndPortDependent", 2),
          ("addressDependent", 1),
          ("endpointIndependent", 0))
    )


_Natv2InstanceFilteringBehavior_Type.__name__ = "Integer32"
_Natv2InstanceFilteringBehavior_Object = MibTableColumn
natv2InstanceFilteringBehavior = _Natv2InstanceFilteringBehavior_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 1, 1, 4),
    _Natv2InstanceFilteringBehavior_Type()
)
natv2InstanceFilteringBehavior.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2InstanceFilteringBehavior.setStatus("current")


class _Natv2InstancePoolingBehavior_Type(Integer32):
    """Custom type natv2InstancePoolingBehavior based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("arbitrary", 0),
          ("paired", 1))
    )


_Natv2InstancePoolingBehavior_Type.__name__ = "Integer32"
_Natv2InstancePoolingBehavior_Object = MibTableColumn
natv2InstancePoolingBehavior = _Natv2InstancePoolingBehavior_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 1, 1, 5),
    _Natv2InstancePoolingBehavior_Type()
)
natv2InstancePoolingBehavior.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2InstancePoolingBehavior.setStatus("current")


class _Natv2InstanceFragmentBehavior_Type(Integer32):
    """Custom type natv2InstanceFragmentBehavior based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fragmentInOrder", 1),
          ("fragmentNone", 0),
          ("fragmentOutOfOrder", 2))
    )


_Natv2InstanceFragmentBehavior_Type.__name__ = "Integer32"
_Natv2InstanceFragmentBehavior_Object = MibTableColumn
natv2InstanceFragmentBehavior = _Natv2InstanceFragmentBehavior_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 1, 1, 6),
    _Natv2InstanceFragmentBehavior_Type()
)
natv2InstanceFragmentBehavior.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2InstanceFragmentBehavior.setStatus("current")
_Natv2InstanceAddressMapEntries_Type = Unsigned32
_Natv2InstanceAddressMapEntries_Object = MibTableColumn
natv2InstanceAddressMapEntries = _Natv2InstanceAddressMapEntries_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 1, 1, 7),
    _Natv2InstanceAddressMapEntries_Type()
)
natv2InstanceAddressMapEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2InstanceAddressMapEntries.setStatus("current")
_Natv2InstancePortMapEntries_Type = Unsigned32
_Natv2InstancePortMapEntries_Object = MibTableColumn
natv2InstancePortMapEntries = _Natv2InstancePortMapEntries_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 1, 1, 8),
    _Natv2InstancePortMapEntries_Type()
)
natv2InstancePortMapEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2InstancePortMapEntries.setStatus("current")
_Natv2InstanceTranslations_Type = Counter64
_Natv2InstanceTranslations_Object = MibTableColumn
natv2InstanceTranslations = _Natv2InstanceTranslations_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 1, 1, 9),
    _Natv2InstanceTranslations_Type()
)
natv2InstanceTranslations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2InstanceTranslations.setStatus("current")
_Natv2InstanceAddressMapCreations_Type = Counter64
_Natv2InstanceAddressMapCreations_Object = MibTableColumn
natv2InstanceAddressMapCreations = _Natv2InstanceAddressMapCreations_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 1, 1, 10),
    _Natv2InstanceAddressMapCreations_Type()
)
natv2InstanceAddressMapCreations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2InstanceAddressMapCreations.setStatus("current")
_Natv2InstancePortMapCreations_Type = Counter64
_Natv2InstancePortMapCreations_Object = MibTableColumn
natv2InstancePortMapCreations = _Natv2InstancePortMapCreations_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 1, 1, 11),
    _Natv2InstancePortMapCreations_Type()
)
natv2InstancePortMapCreations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2InstancePortMapCreations.setStatus("current")
_Natv2InstanceAddressMapEntryLimitDrops_Type = Counter64
_Natv2InstanceAddressMapEntryLimitDrops_Object = MibTableColumn
natv2InstanceAddressMapEntryLimitDrops = _Natv2InstanceAddressMapEntryLimitDrops_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 1, 1, 12),
    _Natv2InstanceAddressMapEntryLimitDrops_Type()
)
natv2InstanceAddressMapEntryLimitDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2InstanceAddressMapEntryLimitDrops.setStatus("current")
_Natv2InstancePortMapEntryLimitDrops_Type = Counter64
_Natv2InstancePortMapEntryLimitDrops_Object = MibTableColumn
natv2InstancePortMapEntryLimitDrops = _Natv2InstancePortMapEntryLimitDrops_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 1, 1, 13),
    _Natv2InstancePortMapEntryLimitDrops_Type()
)
natv2InstancePortMapEntryLimitDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2InstancePortMapEntryLimitDrops.setStatus("current")
_Natv2InstanceSubscriberActiveLimitDrops_Type = Counter64
_Natv2InstanceSubscriberActiveLimitDrops_Object = MibTableColumn
natv2InstanceSubscriberActiveLimitDrops = _Natv2InstanceSubscriberActiveLimitDrops_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 1, 1, 14),
    _Natv2InstanceSubscriberActiveLimitDrops_Type()
)
natv2InstanceSubscriberActiveLimitDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2InstanceSubscriberActiveLimitDrops.setStatus("current")
_Natv2InstanceAddressMapFailureDrops_Type = Counter64
_Natv2InstanceAddressMapFailureDrops_Object = MibTableColumn
natv2InstanceAddressMapFailureDrops = _Natv2InstanceAddressMapFailureDrops_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 1, 1, 15),
    _Natv2InstanceAddressMapFailureDrops_Type()
)
natv2InstanceAddressMapFailureDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2InstanceAddressMapFailureDrops.setStatus("current")
_Natv2InstancePortMapFailureDrops_Type = Counter64
_Natv2InstancePortMapFailureDrops_Object = MibTableColumn
natv2InstancePortMapFailureDrops = _Natv2InstancePortMapFailureDrops_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 1, 1, 16),
    _Natv2InstancePortMapFailureDrops_Type()
)
natv2InstancePortMapFailureDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2InstancePortMapFailureDrops.setStatus("current")
_Natv2InstanceFragmentDrops_Type = Counter64
_Natv2InstanceFragmentDrops_Object = MibTableColumn
natv2InstanceFragmentDrops = _Natv2InstanceFragmentDrops_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 1, 1, 17),
    _Natv2InstanceFragmentDrops_Type()
)
natv2InstanceFragmentDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2InstanceFragmentDrops.setStatus("current")
_Natv2InstanceOtherResourceFailureDrops_Type = Counter64
_Natv2InstanceOtherResourceFailureDrops_Object = MibTableColumn
natv2InstanceOtherResourceFailureDrops = _Natv2InstanceOtherResourceFailureDrops_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 1, 1, 18),
    _Natv2InstanceOtherResourceFailureDrops_Type()
)
natv2InstanceOtherResourceFailureDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2InstanceOtherResourceFailureDrops.setStatus("current")
_Natv2InstanceDiscontinuityTime_Type = TimeStamp
_Natv2InstanceDiscontinuityTime_Object = MibTableColumn
natv2InstanceDiscontinuityTime = _Natv2InstanceDiscontinuityTime_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 1, 1, 19),
    _Natv2InstanceDiscontinuityTime_Type()
)
natv2InstanceDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2InstanceDiscontinuityTime.setStatus("current")


class _Natv2InstanceThresholdAddressMapEntriesHigh_Type(Integer32):
    """Custom type natv2InstanceThresholdAddressMapEntriesHigh based on Integer32"""
    defaultValue = -1


_Natv2InstanceThresholdAddressMapEntriesHigh_Object = MibTableColumn
natv2InstanceThresholdAddressMapEntriesHigh = _Natv2InstanceThresholdAddressMapEntriesHigh_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 1, 1, 20),
    _Natv2InstanceThresholdAddressMapEntriesHigh_Type()
)
natv2InstanceThresholdAddressMapEntriesHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natv2InstanceThresholdAddressMapEntriesHigh.setStatus("current")


class _Natv2InstanceThresholdPortMapEntriesHigh_Type(Integer32):
    """Custom type natv2InstanceThresholdPortMapEntriesHigh based on Integer32"""
    defaultValue = -1


_Natv2InstanceThresholdPortMapEntriesHigh_Object = MibTableColumn
natv2InstanceThresholdPortMapEntriesHigh = _Natv2InstanceThresholdPortMapEntriesHigh_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 1, 1, 21),
    _Natv2InstanceThresholdPortMapEntriesHigh_Type()
)
natv2InstanceThresholdPortMapEntriesHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natv2InstanceThresholdPortMapEntriesHigh.setStatus("current")


class _Natv2InstanceNotificationInterval_Type(Unsigned32):
    """Custom type natv2InstanceNotificationInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_Natv2InstanceNotificationInterval_Type.__name__ = "Unsigned32"
_Natv2InstanceNotificationInterval_Object = MibTableColumn
natv2InstanceNotificationInterval = _Natv2InstanceNotificationInterval_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 1, 1, 22),
    _Natv2InstanceNotificationInterval_Type()
)
natv2InstanceNotificationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natv2InstanceNotificationInterval.setStatus("current")
if mibBuilder.loadTexts:
    natv2InstanceNotificationInterval.setUnits("Seconds")


class _Natv2InstanceLimitAddressMapEntries_Type(Unsigned32):
    """Custom type natv2InstanceLimitAddressMapEntries based on Unsigned32"""
    defaultValue = 0


_Natv2InstanceLimitAddressMapEntries_Object = MibTableColumn
natv2InstanceLimitAddressMapEntries = _Natv2InstanceLimitAddressMapEntries_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 1, 1, 23),
    _Natv2InstanceLimitAddressMapEntries_Type()
)
natv2InstanceLimitAddressMapEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natv2InstanceLimitAddressMapEntries.setStatus("current")


class _Natv2InstanceLimitPortMapEntries_Type(Unsigned32):
    """Custom type natv2InstanceLimitPortMapEntries based on Unsigned32"""
    defaultValue = 0


_Natv2InstanceLimitPortMapEntries_Object = MibTableColumn
natv2InstanceLimitPortMapEntries = _Natv2InstanceLimitPortMapEntries_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 1, 1, 24),
    _Natv2InstanceLimitPortMapEntries_Type()
)
natv2InstanceLimitPortMapEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natv2InstanceLimitPortMapEntries.setStatus("current")


class _Natv2InstanceLimitPendingFragments_Type(Unsigned32):
    """Custom type natv2InstanceLimitPendingFragments based on Unsigned32"""
    defaultValue = 0


_Natv2InstanceLimitPendingFragments_Object = MibTableColumn
natv2InstanceLimitPendingFragments = _Natv2InstanceLimitPendingFragments_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 1, 1, 25),
    _Natv2InstanceLimitPendingFragments_Type()
)
natv2InstanceLimitPendingFragments.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natv2InstanceLimitPendingFragments.setStatus("current")


class _Natv2InstanceLimitSubscriberActives_Type(Unsigned32):
    """Custom type natv2InstanceLimitSubscriberActives based on Unsigned32"""
    defaultValue = 0


_Natv2InstanceLimitSubscriberActives_Object = MibTableColumn
natv2InstanceLimitSubscriberActives = _Natv2InstanceLimitSubscriberActives_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 1, 1, 26),
    _Natv2InstanceLimitSubscriberActives_Type()
)
natv2InstanceLimitSubscriberActives.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natv2InstanceLimitSubscriberActives.setStatus("current")
_Natv2ProtocolTable_Object = MibTable
natv2ProtocolTable = _Natv2ProtocolTable_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 2)
)
if mibBuilder.loadTexts:
    natv2ProtocolTable.setStatus("current")
_Natv2ProtocolEntry_Object = MibTableRow
natv2ProtocolEntry = _Natv2ProtocolEntry_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 2, 1)
)
natv2ProtocolEntry.setIndexNames(
    (0, "NATV2-MIB", "natv2ProtocolInstanceIndex"),
    (0, "NATV2-MIB", "natv2ProtocolNumber"),
)
if mibBuilder.loadTexts:
    natv2ProtocolEntry.setStatus("current")
_Natv2ProtocolInstanceIndex_Type = Natv2InstanceIndex
_Natv2ProtocolInstanceIndex_Object = MibTableColumn
natv2ProtocolInstanceIndex = _Natv2ProtocolInstanceIndex_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 2, 1, 1),
    _Natv2ProtocolInstanceIndex_Type()
)
natv2ProtocolInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natv2ProtocolInstanceIndex.setStatus("current")
_Natv2ProtocolNumber_Type = ProtocolNumber
_Natv2ProtocolNumber_Object = MibTableColumn
natv2ProtocolNumber = _Natv2ProtocolNumber_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 2, 1, 2),
    _Natv2ProtocolNumber_Type()
)
natv2ProtocolNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natv2ProtocolNumber.setStatus("current")
_Natv2ProtocolPortMapEntries_Type = Unsigned32
_Natv2ProtocolPortMapEntries_Object = MibTableColumn
natv2ProtocolPortMapEntries = _Natv2ProtocolPortMapEntries_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 2, 1, 3),
    _Natv2ProtocolPortMapEntries_Type()
)
natv2ProtocolPortMapEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2ProtocolPortMapEntries.setStatus("current")
_Natv2ProtocolTranslations_Type = Counter64
_Natv2ProtocolTranslations_Object = MibTableColumn
natv2ProtocolTranslations = _Natv2ProtocolTranslations_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 2, 1, 4),
    _Natv2ProtocolTranslations_Type()
)
natv2ProtocolTranslations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2ProtocolTranslations.setStatus("current")
_Natv2ProtocolPortMapCreations_Type = Counter64
_Natv2ProtocolPortMapCreations_Object = MibTableColumn
natv2ProtocolPortMapCreations = _Natv2ProtocolPortMapCreations_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 2, 1, 5),
    _Natv2ProtocolPortMapCreations_Type()
)
natv2ProtocolPortMapCreations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2ProtocolPortMapCreations.setStatus("current")
_Natv2ProtocolPortMapFailureDrops_Type = Counter64
_Natv2ProtocolPortMapFailureDrops_Object = MibTableColumn
natv2ProtocolPortMapFailureDrops = _Natv2ProtocolPortMapFailureDrops_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 2, 1, 6),
    _Natv2ProtocolPortMapFailureDrops_Type()
)
natv2ProtocolPortMapFailureDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2ProtocolPortMapFailureDrops.setStatus("current")
_Natv2PoolTable_Object = MibTable
natv2PoolTable = _Natv2PoolTable_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 3)
)
if mibBuilder.loadTexts:
    natv2PoolTable.setStatus("current")
_Natv2PoolEntry_Object = MibTableRow
natv2PoolEntry = _Natv2PoolEntry_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 3, 1)
)
natv2PoolEntry.setIndexNames(
    (0, "NATV2-MIB", "natv2PoolInstanceIndex"),
    (0, "NATV2-MIB", "natv2PoolIndex"),
)
if mibBuilder.loadTexts:
    natv2PoolEntry.setStatus("current")
_Natv2PoolInstanceIndex_Type = Natv2InstanceIndex
_Natv2PoolInstanceIndex_Object = MibTableColumn
natv2PoolInstanceIndex = _Natv2PoolInstanceIndex_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 3, 1, 1),
    _Natv2PoolInstanceIndex_Type()
)
natv2PoolInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natv2PoolInstanceIndex.setStatus("current")
_Natv2PoolIndex_Type = Natv2PoolIndex
_Natv2PoolIndex_Object = MibTableColumn
natv2PoolIndex = _Natv2PoolIndex_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 3, 1, 2),
    _Natv2PoolIndex_Type()
)
natv2PoolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natv2PoolIndex.setStatus("current")


class _Natv2PoolRealm_Type(SnmpAdminString):
    """Custom type natv2PoolRealm based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Natv2PoolRealm_Type.__name__ = "SnmpAdminString"
_Natv2PoolRealm_Object = MibTableColumn
natv2PoolRealm = _Natv2PoolRealm_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 3, 1, 3),
    _Natv2PoolRealm_Type()
)
natv2PoolRealm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2PoolRealm.setStatus("current")
_Natv2PoolAddressType_Type = InetAddressType
_Natv2PoolAddressType_Object = MibTableColumn
natv2PoolAddressType = _Natv2PoolAddressType_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 3, 1, 4),
    _Natv2PoolAddressType_Type()
)
natv2PoolAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2PoolAddressType.setStatus("current")
_Natv2PoolMinimumPort_Type = InetPortNumber
_Natv2PoolMinimumPort_Object = MibTableColumn
natv2PoolMinimumPort = _Natv2PoolMinimumPort_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 3, 1, 5),
    _Natv2PoolMinimumPort_Type()
)
natv2PoolMinimumPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2PoolMinimumPort.setStatus("current")
_Natv2PoolMaximumPort_Type = InetPortNumber
_Natv2PoolMaximumPort_Object = MibTableColumn
natv2PoolMaximumPort = _Natv2PoolMaximumPort_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 3, 1, 6),
    _Natv2PoolMaximumPort_Type()
)
natv2PoolMaximumPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2PoolMaximumPort.setStatus("current")
_Natv2PoolAddressMapEntries_Type = Unsigned32
_Natv2PoolAddressMapEntries_Object = MibTableColumn
natv2PoolAddressMapEntries = _Natv2PoolAddressMapEntries_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 3, 1, 7),
    _Natv2PoolAddressMapEntries_Type()
)
natv2PoolAddressMapEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2PoolAddressMapEntries.setStatus("current")
_Natv2PoolPortMapEntries_Type = Unsigned32
_Natv2PoolPortMapEntries_Object = MibTableColumn
natv2PoolPortMapEntries = _Natv2PoolPortMapEntries_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 3, 1, 8),
    _Natv2PoolPortMapEntries_Type()
)
natv2PoolPortMapEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2PoolPortMapEntries.setStatus("current")
_Natv2PoolAddressMapCreations_Type = Counter64
_Natv2PoolAddressMapCreations_Object = MibTableColumn
natv2PoolAddressMapCreations = _Natv2PoolAddressMapCreations_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 3, 1, 9),
    _Natv2PoolAddressMapCreations_Type()
)
natv2PoolAddressMapCreations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2PoolAddressMapCreations.setStatus("current")
_Natv2PoolPortMapCreations_Type = Counter64
_Natv2PoolPortMapCreations_Object = MibTableColumn
natv2PoolPortMapCreations = _Natv2PoolPortMapCreations_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 3, 1, 10),
    _Natv2PoolPortMapCreations_Type()
)
natv2PoolPortMapCreations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2PoolPortMapCreations.setStatus("current")
_Natv2PoolAddressMapFailureDrops_Type = Counter64
_Natv2PoolAddressMapFailureDrops_Object = MibTableColumn
natv2PoolAddressMapFailureDrops = _Natv2PoolAddressMapFailureDrops_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 3, 1, 11),
    _Natv2PoolAddressMapFailureDrops_Type()
)
natv2PoolAddressMapFailureDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2PoolAddressMapFailureDrops.setStatus("current")
_Natv2PoolPortMapFailureDrops_Type = Counter64
_Natv2PoolPortMapFailureDrops_Object = MibTableColumn
natv2PoolPortMapFailureDrops = _Natv2PoolPortMapFailureDrops_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 3, 1, 12),
    _Natv2PoolPortMapFailureDrops_Type()
)
natv2PoolPortMapFailureDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2PoolPortMapFailureDrops.setStatus("current")
_Natv2PoolDiscontinuityTime_Type = TimeStamp
_Natv2PoolDiscontinuityTime_Object = MibTableColumn
natv2PoolDiscontinuityTime = _Natv2PoolDiscontinuityTime_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 3, 1, 13),
    _Natv2PoolDiscontinuityTime_Type()
)
natv2PoolDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2PoolDiscontinuityTime.setStatus("current")


class _Natv2PoolThresholdUsageLow_Type(Integer32):
    """Custom type natv2PoolThresholdUsageLow based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 100),
    )


_Natv2PoolThresholdUsageLow_Type.__name__ = "Integer32"
_Natv2PoolThresholdUsageLow_Object = MibTableColumn
natv2PoolThresholdUsageLow = _Natv2PoolThresholdUsageLow_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 3, 1, 14),
    _Natv2PoolThresholdUsageLow_Type()
)
natv2PoolThresholdUsageLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natv2PoolThresholdUsageLow.setStatus("current")
if mibBuilder.loadTexts:
    natv2PoolThresholdUsageLow.setUnits("Percent")


class _Natv2PoolThresholdUsageHigh_Type(Integer32):
    """Custom type natv2PoolThresholdUsageHigh based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 100),
    )


_Natv2PoolThresholdUsageHigh_Type.__name__ = "Integer32"
_Natv2PoolThresholdUsageHigh_Object = MibTableColumn
natv2PoolThresholdUsageHigh = _Natv2PoolThresholdUsageHigh_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 3, 1, 15),
    _Natv2PoolThresholdUsageHigh_Type()
)
natv2PoolThresholdUsageHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natv2PoolThresholdUsageHigh.setStatus("current")
if mibBuilder.loadTexts:
    natv2PoolThresholdUsageHigh.setUnits("Percent")
_Natv2PoolNotifiedPortMapEntries_Type = Unsigned32
_Natv2PoolNotifiedPortMapEntries_Object = MibTableColumn
natv2PoolNotifiedPortMapEntries = _Natv2PoolNotifiedPortMapEntries_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 3, 1, 16),
    _Natv2PoolNotifiedPortMapEntries_Type()
)
natv2PoolNotifiedPortMapEntries.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    natv2PoolNotifiedPortMapEntries.setStatus("current")
_Natv2PoolNotifiedPortMapProtocol_Type = ProtocolNumber
_Natv2PoolNotifiedPortMapProtocol_Object = MibTableColumn
natv2PoolNotifiedPortMapProtocol = _Natv2PoolNotifiedPortMapProtocol_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 3, 1, 17),
    _Natv2PoolNotifiedPortMapProtocol_Type()
)
natv2PoolNotifiedPortMapProtocol.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    natv2PoolNotifiedPortMapProtocol.setStatus("current")


class _Natv2PoolNotificationInterval_Type(Unsigned32):
    """Custom type natv2PoolNotificationInterval based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_Natv2PoolNotificationInterval_Type.__name__ = "Unsigned32"
_Natv2PoolNotificationInterval_Object = MibTableColumn
natv2PoolNotificationInterval = _Natv2PoolNotificationInterval_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 3, 1, 18),
    _Natv2PoolNotificationInterval_Type()
)
natv2PoolNotificationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natv2PoolNotificationInterval.setStatus("current")
if mibBuilder.loadTexts:
    natv2PoolNotificationInterval.setUnits("Seconds")
_Natv2PoolRangeTable_Object = MibTable
natv2PoolRangeTable = _Natv2PoolRangeTable_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 4)
)
if mibBuilder.loadTexts:
    natv2PoolRangeTable.setStatus("current")
_Natv2PoolRangeEntry_Object = MibTableRow
natv2PoolRangeEntry = _Natv2PoolRangeEntry_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 4, 1)
)
natv2PoolRangeEntry.setIndexNames(
    (0, "NATV2-MIB", "natv2PoolRangeInstanceIndex"),
    (0, "NATV2-MIB", "natv2PoolRangePoolIndex"),
    (0, "NATV2-MIB", "natv2PoolRangeRowIndex"),
)
if mibBuilder.loadTexts:
    natv2PoolRangeEntry.setStatus("current")
_Natv2PoolRangeInstanceIndex_Type = Natv2InstanceIndex
_Natv2PoolRangeInstanceIndex_Object = MibTableColumn
natv2PoolRangeInstanceIndex = _Natv2PoolRangeInstanceIndex_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 4, 1, 1),
    _Natv2PoolRangeInstanceIndex_Type()
)
natv2PoolRangeInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natv2PoolRangeInstanceIndex.setStatus("current")
_Natv2PoolRangePoolIndex_Type = Natv2PoolIndex
_Natv2PoolRangePoolIndex_Object = MibTableColumn
natv2PoolRangePoolIndex = _Natv2PoolRangePoolIndex_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 4, 1, 2),
    _Natv2PoolRangePoolIndex_Type()
)
natv2PoolRangePoolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natv2PoolRangePoolIndex.setStatus("current")
_Natv2PoolRangeRowIndex_Type = Unsigned32
_Natv2PoolRangeRowIndex_Object = MibTableColumn
natv2PoolRangeRowIndex = _Natv2PoolRangeRowIndex_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 4, 1, 3),
    _Natv2PoolRangeRowIndex_Type()
)
natv2PoolRangeRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natv2PoolRangeRowIndex.setStatus("current")
_Natv2PoolRangeBegin_Type = InetAddress
_Natv2PoolRangeBegin_Object = MibTableColumn
natv2PoolRangeBegin = _Natv2PoolRangeBegin_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 4, 1, 4),
    _Natv2PoolRangeBegin_Type()
)
natv2PoolRangeBegin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2PoolRangeBegin.setStatus("current")
_Natv2PoolRangeEnd_Type = InetAddress
_Natv2PoolRangeEnd_Object = MibTableColumn
natv2PoolRangeEnd = _Natv2PoolRangeEnd_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 4, 1, 5),
    _Natv2PoolRangeEnd_Type()
)
natv2PoolRangeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2PoolRangeEnd.setStatus("current")
_Natv2AddressMapTable_Object = MibTable
natv2AddressMapTable = _Natv2AddressMapTable_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 5)
)
if mibBuilder.loadTexts:
    natv2AddressMapTable.setStatus("current")
_Natv2AddressMapEntry_Object = MibTableRow
natv2AddressMapEntry = _Natv2AddressMapEntry_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 5, 1)
)
natv2AddressMapEntry.setIndexNames(
    (0, "NATV2-MIB", "natv2AddressMapInstanceIndex"),
    (0, "NATV2-MIB", "natv2AddressMapInternalRealm"),
    (0, "NATV2-MIB", "natv2AddressMapInternalAddressType"),
    (0, "NATV2-MIB", "natv2AddressMapInternalAddress"),
    (0, "NATV2-MIB", "natv2AddressMapRowIndex"),
)
if mibBuilder.loadTexts:
    natv2AddressMapEntry.setStatus("current")
_Natv2AddressMapInstanceIndex_Type = Natv2InstanceIndex
_Natv2AddressMapInstanceIndex_Object = MibTableColumn
natv2AddressMapInstanceIndex = _Natv2AddressMapInstanceIndex_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 5, 1, 1),
    _Natv2AddressMapInstanceIndex_Type()
)
natv2AddressMapInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natv2AddressMapInstanceIndex.setStatus("current")


class _Natv2AddressMapInternalRealm_Type(SnmpAdminString):
    """Custom type natv2AddressMapInternalRealm based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Natv2AddressMapInternalRealm_Type.__name__ = "SnmpAdminString"
_Natv2AddressMapInternalRealm_Object = MibTableColumn
natv2AddressMapInternalRealm = _Natv2AddressMapInternalRealm_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 5, 1, 2),
    _Natv2AddressMapInternalRealm_Type()
)
natv2AddressMapInternalRealm.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natv2AddressMapInternalRealm.setStatus("current")
_Natv2AddressMapInternalAddressType_Type = InetAddressType
_Natv2AddressMapInternalAddressType_Object = MibTableColumn
natv2AddressMapInternalAddressType = _Natv2AddressMapInternalAddressType_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 5, 1, 3),
    _Natv2AddressMapInternalAddressType_Type()
)
natv2AddressMapInternalAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natv2AddressMapInternalAddressType.setStatus("current")


class _Natv2AddressMapInternalAddress_Type(InetAddress):
    """Custom type natv2AddressMapInternalAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Natv2AddressMapInternalAddress_Type.__name__ = "InetAddress"
_Natv2AddressMapInternalAddress_Object = MibTableColumn
natv2AddressMapInternalAddress = _Natv2AddressMapInternalAddress_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 5, 1, 4),
    _Natv2AddressMapInternalAddress_Type()
)
natv2AddressMapInternalAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natv2AddressMapInternalAddress.setStatus("current")
_Natv2AddressMapRowIndex_Type = Unsigned32
_Natv2AddressMapRowIndex_Object = MibTableColumn
natv2AddressMapRowIndex = _Natv2AddressMapRowIndex_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 5, 1, 5),
    _Natv2AddressMapRowIndex_Type()
)
natv2AddressMapRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natv2AddressMapRowIndex.setStatus("current")
_Natv2AddressMapInternalMappedAddressType_Type = InetAddressType
_Natv2AddressMapInternalMappedAddressType_Object = MibTableColumn
natv2AddressMapInternalMappedAddressType = _Natv2AddressMapInternalMappedAddressType_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 5, 1, 6),
    _Natv2AddressMapInternalMappedAddressType_Type()
)
natv2AddressMapInternalMappedAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2AddressMapInternalMappedAddressType.setStatus("current")
_Natv2AddressMapInternalMappedAddress_Type = InetAddress
_Natv2AddressMapInternalMappedAddress_Object = MibTableColumn
natv2AddressMapInternalMappedAddress = _Natv2AddressMapInternalMappedAddress_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 5, 1, 7),
    _Natv2AddressMapInternalMappedAddress_Type()
)
natv2AddressMapInternalMappedAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2AddressMapInternalMappedAddress.setStatus("current")


class _Natv2AddressMapExternalRealm_Type(SnmpAdminString):
    """Custom type natv2AddressMapExternalRealm based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Natv2AddressMapExternalRealm_Type.__name__ = "SnmpAdminString"
_Natv2AddressMapExternalRealm_Object = MibTableColumn
natv2AddressMapExternalRealm = _Natv2AddressMapExternalRealm_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 5, 1, 8),
    _Natv2AddressMapExternalRealm_Type()
)
natv2AddressMapExternalRealm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2AddressMapExternalRealm.setStatus("current")
_Natv2AddressMapExternalAddressType_Type = InetAddressType
_Natv2AddressMapExternalAddressType_Object = MibTableColumn
natv2AddressMapExternalAddressType = _Natv2AddressMapExternalAddressType_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 5, 1, 9),
    _Natv2AddressMapExternalAddressType_Type()
)
natv2AddressMapExternalAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2AddressMapExternalAddressType.setStatus("current")
_Natv2AddressMapExternalAddress_Type = InetAddress
_Natv2AddressMapExternalAddress_Object = MibTableColumn
natv2AddressMapExternalAddress = _Natv2AddressMapExternalAddress_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 5, 1, 10),
    _Natv2AddressMapExternalAddress_Type()
)
natv2AddressMapExternalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2AddressMapExternalAddress.setStatus("current")
_Natv2AddressMapExternalPoolIndex_Type = Natv2PoolIndexOrZero
_Natv2AddressMapExternalPoolIndex_Object = MibTableColumn
natv2AddressMapExternalPoolIndex = _Natv2AddressMapExternalPoolIndex_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 5, 1, 11),
    _Natv2AddressMapExternalPoolIndex_Type()
)
natv2AddressMapExternalPoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2AddressMapExternalPoolIndex.setStatus("current")
_Natv2AddressMapSubscriberIndex_Type = Natv2SubscriberIndexOrZero
_Natv2AddressMapSubscriberIndex_Object = MibTableColumn
natv2AddressMapSubscriberIndex = _Natv2AddressMapSubscriberIndex_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 5, 1, 12),
    _Natv2AddressMapSubscriberIndex_Type()
)
natv2AddressMapSubscriberIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2AddressMapSubscriberIndex.setStatus("current")
_Natv2PortMapTable_Object = MibTable
natv2PortMapTable = _Natv2PortMapTable_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 6)
)
if mibBuilder.loadTexts:
    natv2PortMapTable.setStatus("current")
_Natv2PortMapEntry_Object = MibTableRow
natv2PortMapEntry = _Natv2PortMapEntry_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 6, 1)
)
natv2PortMapEntry.setIndexNames(
    (0, "NATV2-MIB", "natv2PortMapInstanceIndex"),
    (0, "NATV2-MIB", "natv2PortMapProtocol"),
    (0, "NATV2-MIB", "natv2PortMapExternalRealm"),
    (0, "NATV2-MIB", "natv2PortMapExternalAddressType"),
    (0, "NATV2-MIB", "natv2PortMapExternalAddress"),
    (0, "NATV2-MIB", "natv2PortMapExternalPort"),
)
if mibBuilder.loadTexts:
    natv2PortMapEntry.setStatus("current")
_Natv2PortMapInstanceIndex_Type = Natv2InstanceIndex
_Natv2PortMapInstanceIndex_Object = MibTableColumn
natv2PortMapInstanceIndex = _Natv2PortMapInstanceIndex_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 6, 1, 1),
    _Natv2PortMapInstanceIndex_Type()
)
natv2PortMapInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natv2PortMapInstanceIndex.setStatus("current")
_Natv2PortMapProtocol_Type = ProtocolNumber
_Natv2PortMapProtocol_Object = MibTableColumn
natv2PortMapProtocol = _Natv2PortMapProtocol_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 6, 1, 2),
    _Natv2PortMapProtocol_Type()
)
natv2PortMapProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natv2PortMapProtocol.setStatus("current")


class _Natv2PortMapExternalRealm_Type(SnmpAdminString):
    """Custom type natv2PortMapExternalRealm based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Natv2PortMapExternalRealm_Type.__name__ = "SnmpAdminString"
_Natv2PortMapExternalRealm_Object = MibTableColumn
natv2PortMapExternalRealm = _Natv2PortMapExternalRealm_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 6, 1, 3),
    _Natv2PortMapExternalRealm_Type()
)
natv2PortMapExternalRealm.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natv2PortMapExternalRealm.setStatus("current")
_Natv2PortMapExternalAddressType_Type = InetAddressType
_Natv2PortMapExternalAddressType_Object = MibTableColumn
natv2PortMapExternalAddressType = _Natv2PortMapExternalAddressType_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 6, 1, 4),
    _Natv2PortMapExternalAddressType_Type()
)
natv2PortMapExternalAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natv2PortMapExternalAddressType.setStatus("current")


class _Natv2PortMapExternalAddress_Type(InetAddress):
    """Custom type natv2PortMapExternalAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Natv2PortMapExternalAddress_Type.__name__ = "InetAddress"
_Natv2PortMapExternalAddress_Object = MibTableColumn
natv2PortMapExternalAddress = _Natv2PortMapExternalAddress_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 6, 1, 5),
    _Natv2PortMapExternalAddress_Type()
)
natv2PortMapExternalAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natv2PortMapExternalAddress.setStatus("current")
_Natv2PortMapExternalPort_Type = InetPortNumber
_Natv2PortMapExternalPort_Object = MibTableColumn
natv2PortMapExternalPort = _Natv2PortMapExternalPort_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 6, 1, 6),
    _Natv2PortMapExternalPort_Type()
)
natv2PortMapExternalPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natv2PortMapExternalPort.setStatus("current")


class _Natv2PortMapInternalRealm_Type(SnmpAdminString):
    """Custom type natv2PortMapInternalRealm based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Natv2PortMapInternalRealm_Type.__name__ = "SnmpAdminString"
_Natv2PortMapInternalRealm_Object = MibTableColumn
natv2PortMapInternalRealm = _Natv2PortMapInternalRealm_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 6, 1, 7),
    _Natv2PortMapInternalRealm_Type()
)
natv2PortMapInternalRealm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2PortMapInternalRealm.setStatus("current")
_Natv2PortMapInternalAddressType_Type = InetAddressType
_Natv2PortMapInternalAddressType_Object = MibTableColumn
natv2PortMapInternalAddressType = _Natv2PortMapInternalAddressType_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 6, 1, 8),
    _Natv2PortMapInternalAddressType_Type()
)
natv2PortMapInternalAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2PortMapInternalAddressType.setStatus("current")
_Natv2PortMapInternalAddress_Type = InetAddress
_Natv2PortMapInternalAddress_Object = MibTableColumn
natv2PortMapInternalAddress = _Natv2PortMapInternalAddress_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 6, 1, 9),
    _Natv2PortMapInternalAddress_Type()
)
natv2PortMapInternalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2PortMapInternalAddress.setStatus("current")
_Natv2PortMapInternalMappedAddressType_Type = InetAddressType
_Natv2PortMapInternalMappedAddressType_Object = MibTableColumn
natv2PortMapInternalMappedAddressType = _Natv2PortMapInternalMappedAddressType_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 6, 1, 10),
    _Natv2PortMapInternalMappedAddressType_Type()
)
natv2PortMapInternalMappedAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2PortMapInternalMappedAddressType.setStatus("current")
_Natv2PortMapInternalMappedAddress_Type = InetAddress
_Natv2PortMapInternalMappedAddress_Object = MibTableColumn
natv2PortMapInternalMappedAddress = _Natv2PortMapInternalMappedAddress_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 6, 1, 11),
    _Natv2PortMapInternalMappedAddress_Type()
)
natv2PortMapInternalMappedAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2PortMapInternalMappedAddress.setStatus("current")
_Natv2PortMapInternalPort_Type = InetPortNumber
_Natv2PortMapInternalPort_Object = MibTableColumn
natv2PortMapInternalPort = _Natv2PortMapInternalPort_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 6, 1, 12),
    _Natv2PortMapInternalPort_Type()
)
natv2PortMapInternalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2PortMapInternalPort.setStatus("current")
_Natv2PortMapExternalPoolIndex_Type = Natv2PoolIndexOrZero
_Natv2PortMapExternalPoolIndex_Object = MibTableColumn
natv2PortMapExternalPoolIndex = _Natv2PortMapExternalPoolIndex_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 6, 1, 13),
    _Natv2PortMapExternalPoolIndex_Type()
)
natv2PortMapExternalPoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2PortMapExternalPoolIndex.setStatus("current")
_Natv2PortMapSubscriberIndex_Type = Natv2SubscriberIndexOrZero
_Natv2PortMapSubscriberIndex_Object = MibTableColumn
natv2PortMapSubscriberIndex = _Natv2PortMapSubscriberIndex_Object(
    (1, 3, 6, 1, 2, 1, 234, 2, 6, 1, 14),
    _Natv2PortMapSubscriberIndex_Type()
)
natv2PortMapSubscriberIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natv2PortMapSubscriberIndex.setStatus("current")
_Natv2MIBConformance_ObjectIdentity = ObjectIdentity
natv2MIBConformance = _Natv2MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 234, 3)
)
_Natv2MIBCompliances_ObjectIdentity = ObjectIdentity
natv2MIBCompliances = _Natv2MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 234, 3, 1)
)
_Natv2MIBGroups_ObjectIdentity = ObjectIdentity
natv2MIBGroups = _Natv2MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 234, 3, 2)
)

# Managed Objects groups

natv2BasicInstanceLevelGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 234, 3, 2, 2)
)
natv2BasicInstanceLevelGroup.setObjects(
      *(("NATV2-MIB", "natv2InstanceAlias"),
        ("NATV2-MIB", "natv2InstancePortMappingBehavior"),
        ("NATV2-MIB", "natv2InstanceFilteringBehavior"),
        ("NATV2-MIB", "natv2InstanceFragmentBehavior"),
        ("NATV2-MIB", "natv2InstanceAddressMapEntries"),
        ("NATV2-MIB", "natv2InstancePortMapEntries"),
        ("NATV2-MIB", "natv2InstanceTranslations"),
        ("NATV2-MIB", "natv2InstanceAddressMapCreations"),
        ("NATV2-MIB", "natv2InstanceAddressMapEntryLimitDrops"),
        ("NATV2-MIB", "natv2InstanceAddressMapFailureDrops"),
        ("NATV2-MIB", "natv2InstancePortMapCreations"),
        ("NATV2-MIB", "natv2InstancePortMapEntryLimitDrops"),
        ("NATV2-MIB", "natv2InstancePortMapFailureDrops"),
        ("NATV2-MIB", "natv2InstanceFragmentDrops"),
        ("NATV2-MIB", "natv2InstanceOtherResourceFailureDrops"),
        ("NATV2-MIB", "natv2InstanceDiscontinuityTime"),
        ("NATV2-MIB", "natv2InstanceThresholdAddressMapEntriesHigh"),
        ("NATV2-MIB", "natv2InstanceThresholdPortMapEntriesHigh"),
        ("NATV2-MIB", "natv2InstanceNotificationInterval"),
        ("NATV2-MIB", "natv2InstanceLimitAddressMapEntries"),
        ("NATV2-MIB", "natv2InstanceLimitPortMapEntries"),
        ("NATV2-MIB", "natv2InstanceLimitPendingFragments"),
        ("NATV2-MIB", "natv2ProtocolPortMapEntries"),
        ("NATV2-MIB", "natv2ProtocolTranslations"),
        ("NATV2-MIB", "natv2ProtocolPortMapCreations"),
        ("NATV2-MIB", "natv2ProtocolPortMapFailureDrops"),
        ("NATV2-MIB", "natv2AddressMapExternalRealm"),
        ("NATV2-MIB", "natv2AddressMapExternalAddressType"),
        ("NATV2-MIB", "natv2AddressMapExternalAddress"),
        ("NATV2-MIB", "natv2PortMapInternalRealm"),
        ("NATV2-MIB", "natv2PortMapInternalAddressType"),
        ("NATV2-MIB", "natv2PortMapInternalAddress"),
        ("NATV2-MIB", "natv2PortMapInternalPort"))
)
if mibBuilder.loadTexts:
    natv2BasicInstanceLevelGroup.setStatus("current")

natv2PooledInstanceLevelGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 234, 3, 2, 4)
)
natv2PooledInstanceLevelGroup.setObjects(
      *(("NATV2-MIB", "natv2InstancePoolingBehavior"),
        ("NATV2-MIB", "natv2PoolRealm"),
        ("NATV2-MIB", "natv2PoolAddressType"),
        ("NATV2-MIB", "natv2PoolMinimumPort"),
        ("NATV2-MIB", "natv2PoolMaximumPort"),
        ("NATV2-MIB", "natv2PoolAddressMapEntries"),
        ("NATV2-MIB", "natv2PoolPortMapEntries"),
        ("NATV2-MIB", "natv2PoolAddressMapCreations"),
        ("NATV2-MIB", "natv2PoolPortMapCreations"),
        ("NATV2-MIB", "natv2PoolAddressMapFailureDrops"),
        ("NATV2-MIB", "natv2PoolPortMapFailureDrops"),
        ("NATV2-MIB", "natv2PoolDiscontinuityTime"),
        ("NATV2-MIB", "natv2PoolThresholdUsageLow"),
        ("NATV2-MIB", "natv2PoolThresholdUsageHigh"),
        ("NATV2-MIB", "natv2PoolNotifiedPortMapEntries"),
        ("NATV2-MIB", "natv2PoolNotifiedPortMapProtocol"),
        ("NATV2-MIB", "natv2PoolNotificationInterval"),
        ("NATV2-MIB", "natv2PoolRangeBegin"),
        ("NATV2-MIB", "natv2PoolRangeEnd"),
        ("NATV2-MIB", "natv2AddressMapExternalPoolIndex"),
        ("NATV2-MIB", "natv2PortMapExternalPoolIndex"))
)
if mibBuilder.loadTexts:
    natv2PooledInstanceLevelGroup.setStatus("current")

natv2CGNDeviceLevelGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 234, 3, 2, 6)
)
natv2CGNDeviceLevelGroup.setObjects(
      *(("NATV2-MIB", "natv2SubscriberInternalRealm"),
        ("NATV2-MIB", "natv2SubscriberInternalPrefixType"),
        ("NATV2-MIB", "natv2SubscriberInternalPrefix"),
        ("NATV2-MIB", "natv2SubscriberInternalPrefixLength"),
        ("NATV2-MIB", "natv2SubscriberAddressMapEntries"),
        ("NATV2-MIB", "natv2SubscriberPortMapEntries"),
        ("NATV2-MIB", "natv2SubscriberTranslations"),
        ("NATV2-MIB", "natv2SubscriberAddressMapCreations"),
        ("NATV2-MIB", "natv2SubscriberPortMapCreations"),
        ("NATV2-MIB", "natv2SubscriberAddressMapFailureDrops"),
        ("NATV2-MIB", "natv2SubscriberPortMapFailureDrops"),
        ("NATV2-MIB", "natv2SubscriberDiscontinuityTime"),
        ("NATV2-MIB", "natv2SubscriberLimitPortMapEntries"),
        ("NATV2-MIB", "natv2SubscriberThresholdPortMapEntriesHigh"),
        ("NATV2-MIB", "natv2SubscriberNotificationInterval"))
)
if mibBuilder.loadTexts:
    natv2CGNDeviceLevelGroup.setStatus("current")

natv2CGNInstanceLevelGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 234, 3, 2, 7)
)
natv2CGNInstanceLevelGroup.setObjects(
      *(("NATV2-MIB", "natv2InstanceSubscriberActiveLimitDrops"),
        ("NATV2-MIB", "natv2InstanceLimitSubscriberActives"),
        ("NATV2-MIB", "natv2AddressMapInternalMappedAddressType"),
        ("NATV2-MIB", "natv2AddressMapInternalMappedAddress"),
        ("NATV2-MIB", "natv2AddressMapSubscriberIndex"),
        ("NATV2-MIB", "natv2PortMapInternalMappedAddressType"),
        ("NATV2-MIB", "natv2PortMapInternalMappedAddress"),
        ("NATV2-MIB", "natv2PortMapSubscriberIndex"))
)
if mibBuilder.loadTexts:
    natv2CGNInstanceLevelGroup.setStatus("current")


# Notification objects

natv2NotificationPoolUsageLow = NotificationType(
    (1, 3, 6, 1, 2, 1, 234, 0, 1)
)
natv2NotificationPoolUsageLow.setObjects(
      *(("NATV2-MIB", "natv2PoolNotifiedPortMapEntries"),
        ("NATV2-MIB", "natv2PoolNotifiedPortMapProtocol"))
)
if mibBuilder.loadTexts:
    natv2NotificationPoolUsageLow.setStatus(
        "current"
    )

natv2NotificationPoolUsageHigh = NotificationType(
    (1, 3, 6, 1, 2, 1, 234, 0, 2)
)
natv2NotificationPoolUsageHigh.setObjects(
      *(("NATV2-MIB", "natv2PoolNotifiedPortMapEntries"),
        ("NATV2-MIB", "natv2PoolNotifiedPortMapProtocol"))
)
if mibBuilder.loadTexts:
    natv2NotificationPoolUsageHigh.setStatus(
        "current"
    )

natv2NotificationInstanceAddressMapEntriesHigh = NotificationType(
    (1, 3, 6, 1, 2, 1, 234, 0, 3)
)
natv2NotificationInstanceAddressMapEntriesHigh.setObjects(
      *(("NATV2-MIB", "natv2InstanceAddressMapEntries"),
        ("NATV2-MIB", "natv2InstanceAddressMapCreations"))
)
if mibBuilder.loadTexts:
    natv2NotificationInstanceAddressMapEntriesHigh.setStatus(
        "current"
    )

natv2NotificationInstancePortMapEntriesHigh = NotificationType(
    (1, 3, 6, 1, 2, 1, 234, 0, 4)
)
natv2NotificationInstancePortMapEntriesHigh.setObjects(
      *(("NATV2-MIB", "natv2InstancePortMapEntries"),
        ("NATV2-MIB", "natv2InstancePortMapCreations"))
)
if mibBuilder.loadTexts:
    natv2NotificationInstancePortMapEntriesHigh.setStatus(
        "current"
    )

natv2NotificationSubscriberPortMappingEntriesHigh = NotificationType(
    (1, 3, 6, 1, 2, 1, 234, 0, 5)
)
natv2NotificationSubscriberPortMappingEntriesHigh.setObjects(
      *(("NATV2-MIB", "natv2SubscriberPortMapEntries"),
        ("NATV2-MIB", "natv2SubscriberPortMapCreations"))
)
if mibBuilder.loadTexts:
    natv2NotificationSubscriberPortMappingEntriesHigh.setStatus(
        "current"
    )


# Notifications groups

natv2BasicNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 234, 3, 2, 1)
)
natv2BasicNotificationGroup.setObjects(
      *(("NATV2-MIB", "natv2NotificationInstanceAddressMapEntriesHigh"),
        ("NATV2-MIB", "natv2NotificationInstancePortMapEntriesHigh"))
)
if mibBuilder.loadTexts:
    natv2BasicNotificationGroup.setStatus(
        "current"
    )

natv2PooledNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 234, 3, 2, 3)
)
natv2PooledNotificationGroup.setObjects(
      *(("NATV2-MIB", "natv2NotificationPoolUsageLow"),
        ("NATV2-MIB", "natv2NotificationPoolUsageHigh"))
)
if mibBuilder.loadTexts:
    natv2PooledNotificationGroup.setStatus(
        "current"
    )

natv2CGNNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 234, 3, 2, 5)
)
natv2CGNNotificationGroup.setObjects(
    ("NATV2-MIB", "natv2NotificationSubscriberPortMappingEntriesHigh")
)
if mibBuilder.loadTexts:
    natv2CGNNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

natv2MIBBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 234, 3, 1, 1)
)
if mibBuilder.loadTexts:
    natv2MIBBasicCompliance.setStatus(
        "current"
    )

natv2MIBPooledNATCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 234, 3, 1, 2)
)
if mibBuilder.loadTexts:
    natv2MIBPooledNATCompliance.setStatus(
        "current"
    )

natv2MIBCGNCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 234, 3, 1, 3)
)
if mibBuilder.loadTexts:
    natv2MIBCGNCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NATV2-MIB",
    **{"ProtocolNumber": ProtocolNumber,
       "Natv2SubscriberIndex": Natv2SubscriberIndex,
       "Natv2SubscriberIndexOrZero": Natv2SubscriberIndexOrZero,
       "Natv2InstanceIndex": Natv2InstanceIndex,
       "Natv2PoolIndex": Natv2PoolIndex,
       "Natv2PoolIndexOrZero": Natv2PoolIndexOrZero,
       "natv2MIB": natv2MIB,
       "natv2MIBNotifications": natv2MIBNotifications,
       "natv2NotificationPoolUsageLow": natv2NotificationPoolUsageLow,
       "natv2NotificationPoolUsageHigh": natv2NotificationPoolUsageHigh,
       "natv2NotificationInstanceAddressMapEntriesHigh": natv2NotificationInstanceAddressMapEntriesHigh,
       "natv2NotificationInstancePortMapEntriesHigh": natv2NotificationInstancePortMapEntriesHigh,
       "natv2NotificationSubscriberPortMappingEntriesHigh": natv2NotificationSubscriberPortMappingEntriesHigh,
       "natv2MIBDeviceObjects": natv2MIBDeviceObjects,
       "natv2SubscriberTable": natv2SubscriberTable,
       "natv2SubscriberEntry": natv2SubscriberEntry,
       "natv2SubscriberIndex": natv2SubscriberIndex,
       "natv2SubscriberInternalRealm": natv2SubscriberInternalRealm,
       "natv2SubscriberInternalPrefixType": natv2SubscriberInternalPrefixType,
       "natv2SubscriberInternalPrefix": natv2SubscriberInternalPrefix,
       "natv2SubscriberInternalPrefixLength": natv2SubscriberInternalPrefixLength,
       "natv2SubscriberAddressMapEntries": natv2SubscriberAddressMapEntries,
       "natv2SubscriberPortMapEntries": natv2SubscriberPortMapEntries,
       "natv2SubscriberTranslations": natv2SubscriberTranslations,
       "natv2SubscriberAddressMapCreations": natv2SubscriberAddressMapCreations,
       "natv2SubscriberPortMapCreations": natv2SubscriberPortMapCreations,
       "natv2SubscriberAddressMapFailureDrops": natv2SubscriberAddressMapFailureDrops,
       "natv2SubscriberPortMapFailureDrops": natv2SubscriberPortMapFailureDrops,
       "natv2SubscriberDiscontinuityTime": natv2SubscriberDiscontinuityTime,
       "natv2SubscriberLimitPortMapEntries": natv2SubscriberLimitPortMapEntries,
       "natv2SubscriberThresholdPortMapEntriesHigh": natv2SubscriberThresholdPortMapEntriesHigh,
       "natv2SubscriberNotificationInterval": natv2SubscriberNotificationInterval,
       "natv2MIBInstanceObjects": natv2MIBInstanceObjects,
       "natv2InstanceTable": natv2InstanceTable,
       "natv2InstanceEntry": natv2InstanceEntry,
       "natv2InstanceIndex": natv2InstanceIndex,
       "natv2InstanceAlias": natv2InstanceAlias,
       "natv2InstancePortMappingBehavior": natv2InstancePortMappingBehavior,
       "natv2InstanceFilteringBehavior": natv2InstanceFilteringBehavior,
       "natv2InstancePoolingBehavior": natv2InstancePoolingBehavior,
       "natv2InstanceFragmentBehavior": natv2InstanceFragmentBehavior,
       "natv2InstanceAddressMapEntries": natv2InstanceAddressMapEntries,
       "natv2InstancePortMapEntries": natv2InstancePortMapEntries,
       "natv2InstanceTranslations": natv2InstanceTranslations,
       "natv2InstanceAddressMapCreations": natv2InstanceAddressMapCreations,
       "natv2InstancePortMapCreations": natv2InstancePortMapCreations,
       "natv2InstanceAddressMapEntryLimitDrops": natv2InstanceAddressMapEntryLimitDrops,
       "natv2InstancePortMapEntryLimitDrops": natv2InstancePortMapEntryLimitDrops,
       "natv2InstanceSubscriberActiveLimitDrops": natv2InstanceSubscriberActiveLimitDrops,
       "natv2InstanceAddressMapFailureDrops": natv2InstanceAddressMapFailureDrops,
       "natv2InstancePortMapFailureDrops": natv2InstancePortMapFailureDrops,
       "natv2InstanceFragmentDrops": natv2InstanceFragmentDrops,
       "natv2InstanceOtherResourceFailureDrops": natv2InstanceOtherResourceFailureDrops,
       "natv2InstanceDiscontinuityTime": natv2InstanceDiscontinuityTime,
       "natv2InstanceThresholdAddressMapEntriesHigh": natv2InstanceThresholdAddressMapEntriesHigh,
       "natv2InstanceThresholdPortMapEntriesHigh": natv2InstanceThresholdPortMapEntriesHigh,
       "natv2InstanceNotificationInterval": natv2InstanceNotificationInterval,
       "natv2InstanceLimitAddressMapEntries": natv2InstanceLimitAddressMapEntries,
       "natv2InstanceLimitPortMapEntries": natv2InstanceLimitPortMapEntries,
       "natv2InstanceLimitPendingFragments": natv2InstanceLimitPendingFragments,
       "natv2InstanceLimitSubscriberActives": natv2InstanceLimitSubscriberActives,
       "natv2ProtocolTable": natv2ProtocolTable,
       "natv2ProtocolEntry": natv2ProtocolEntry,
       "natv2ProtocolInstanceIndex": natv2ProtocolInstanceIndex,
       "natv2ProtocolNumber": natv2ProtocolNumber,
       "natv2ProtocolPortMapEntries": natv2ProtocolPortMapEntries,
       "natv2ProtocolTranslations": natv2ProtocolTranslations,
       "natv2ProtocolPortMapCreations": natv2ProtocolPortMapCreations,
       "natv2ProtocolPortMapFailureDrops": natv2ProtocolPortMapFailureDrops,
       "natv2PoolTable": natv2PoolTable,
       "natv2PoolEntry": natv2PoolEntry,
       "natv2PoolInstanceIndex": natv2PoolInstanceIndex,
       "natv2PoolIndex": natv2PoolIndex,
       "natv2PoolRealm": natv2PoolRealm,
       "natv2PoolAddressType": natv2PoolAddressType,
       "natv2PoolMinimumPort": natv2PoolMinimumPort,
       "natv2PoolMaximumPort": natv2PoolMaximumPort,
       "natv2PoolAddressMapEntries": natv2PoolAddressMapEntries,
       "natv2PoolPortMapEntries": natv2PoolPortMapEntries,
       "natv2PoolAddressMapCreations": natv2PoolAddressMapCreations,
       "natv2PoolPortMapCreations": natv2PoolPortMapCreations,
       "natv2PoolAddressMapFailureDrops": natv2PoolAddressMapFailureDrops,
       "natv2PoolPortMapFailureDrops": natv2PoolPortMapFailureDrops,
       "natv2PoolDiscontinuityTime": natv2PoolDiscontinuityTime,
       "natv2PoolThresholdUsageLow": natv2PoolThresholdUsageLow,
       "natv2PoolThresholdUsageHigh": natv2PoolThresholdUsageHigh,
       "natv2PoolNotifiedPortMapEntries": natv2PoolNotifiedPortMapEntries,
       "natv2PoolNotifiedPortMapProtocol": natv2PoolNotifiedPortMapProtocol,
       "natv2PoolNotificationInterval": natv2PoolNotificationInterval,
       "natv2PoolRangeTable": natv2PoolRangeTable,
       "natv2PoolRangeEntry": natv2PoolRangeEntry,
       "natv2PoolRangeInstanceIndex": natv2PoolRangeInstanceIndex,
       "natv2PoolRangePoolIndex": natv2PoolRangePoolIndex,
       "natv2PoolRangeRowIndex": natv2PoolRangeRowIndex,
       "natv2PoolRangeBegin": natv2PoolRangeBegin,
       "natv2PoolRangeEnd": natv2PoolRangeEnd,
       "natv2AddressMapTable": natv2AddressMapTable,
       "natv2AddressMapEntry": natv2AddressMapEntry,
       "natv2AddressMapInstanceIndex": natv2AddressMapInstanceIndex,
       "natv2AddressMapInternalRealm": natv2AddressMapInternalRealm,
       "natv2AddressMapInternalAddressType": natv2AddressMapInternalAddressType,
       "natv2AddressMapInternalAddress": natv2AddressMapInternalAddress,
       "natv2AddressMapRowIndex": natv2AddressMapRowIndex,
       "natv2AddressMapInternalMappedAddressType": natv2AddressMapInternalMappedAddressType,
       "natv2AddressMapInternalMappedAddress": natv2AddressMapInternalMappedAddress,
       "natv2AddressMapExternalRealm": natv2AddressMapExternalRealm,
       "natv2AddressMapExternalAddressType": natv2AddressMapExternalAddressType,
       "natv2AddressMapExternalAddress": natv2AddressMapExternalAddress,
       "natv2AddressMapExternalPoolIndex": natv2AddressMapExternalPoolIndex,
       "natv2AddressMapSubscriberIndex": natv2AddressMapSubscriberIndex,
       "natv2PortMapTable": natv2PortMapTable,
       "natv2PortMapEntry": natv2PortMapEntry,
       "natv2PortMapInstanceIndex": natv2PortMapInstanceIndex,
       "natv2PortMapProtocol": natv2PortMapProtocol,
       "natv2PortMapExternalRealm": natv2PortMapExternalRealm,
       "natv2PortMapExternalAddressType": natv2PortMapExternalAddressType,
       "natv2PortMapExternalAddress": natv2PortMapExternalAddress,
       "natv2PortMapExternalPort": natv2PortMapExternalPort,
       "natv2PortMapInternalRealm": natv2PortMapInternalRealm,
       "natv2PortMapInternalAddressType": natv2PortMapInternalAddressType,
       "natv2PortMapInternalAddress": natv2PortMapInternalAddress,
       "natv2PortMapInternalMappedAddressType": natv2PortMapInternalMappedAddressType,
       "natv2PortMapInternalMappedAddress": natv2PortMapInternalMappedAddress,
       "natv2PortMapInternalPort": natv2PortMapInternalPort,
       "natv2PortMapExternalPoolIndex": natv2PortMapExternalPoolIndex,
       "natv2PortMapSubscriberIndex": natv2PortMapSubscriberIndex,
       "natv2MIBConformance": natv2MIBConformance,
       "natv2MIBCompliances": natv2MIBCompliances,
       "natv2MIBBasicCompliance": natv2MIBBasicCompliance,
       "natv2MIBPooledNATCompliance": natv2MIBPooledNATCompliance,
       "natv2MIBCGNCompliance": natv2MIBCGNCompliance,
       "natv2MIBGroups": natv2MIBGroups,
       "natv2BasicNotificationGroup": natv2BasicNotificationGroup,
       "natv2BasicInstanceLevelGroup": natv2BasicInstanceLevelGroup,
       "natv2PooledNotificationGroup": natv2PooledNotificationGroup,
       "natv2PooledInstanceLevelGroup": natv2PooledInstanceLevelGroup,
       "natv2CGNNotificationGroup": natv2CGNNotificationGroup,
       "natv2CGNDeviceLevelGroup": natv2CGNDeviceLevelGroup,
       "natv2CGNInstanceLevelGroup": natv2CGNInstanceLevelGroup}
)
