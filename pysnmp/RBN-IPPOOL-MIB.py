# SNMP MIB module (RBN-IPPOOL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBN-IPPOOL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:45:12 2024
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

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

(rbnMgmt,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnMgmt")

(RbnPercentage,) = mibBuilder.importSymbols(
    "RBN-TC",
    "RbnPercentage")

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

rbnIpPoolMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15)
)
rbnIpPoolMib.setRevisions(
        ("2010-02-10 00:00",
         "2005-06-17 00:00",
         "2005-03-14 00:00",
         "2004-09-28 00:00",
         "2001-11-07 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RbnInetPoolType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcpv6", 2),
          ("ipv6", 1))
    )



class RbnInetIpPoolThresholdType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absolute", 1),
          ("none", 0),
          ("percentage", 2))
    )



class RbnInetIpPoolThreshold(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"


class RbnInetIpPoolThrshNotify(Integer32, TextualConvention):
    status = "current"
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
        *(("both", 3),
          ("log", 1),
          ("none", 0),
          ("trap", 2))
    )



# MIB Managed Objects in the order of their OIDs

_RbnIpPoolMIBNotifications_ObjectIdentity = ObjectIdentity
rbnIpPoolMIBNotifications = _RbnIpPoolMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 0)
)
_RbnIpPoolMIBObjects_ObjectIdentity = ObjectIdentity
rbnIpPoolMIBObjects = _RbnIpPoolMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1)
)
_RbnIpPoolTable_Object = MibTable
rbnIpPoolTable = _RbnIpPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 1)
)
if mibBuilder.loadTexts:
    rbnIpPoolTable.setStatus("current")
_RbnIpPoolEntry_Object = MibTableRow
rbnIpPoolEntry = _RbnIpPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 1, 1)
)
rbnIpPoolEntry.setIndexNames(
    (0, "RBN-IPPOOL-MIB", "rbnIpPoolInterfaceIdx"),
    (0, "RBN-IPPOOL-MIB", "rbnIpPoolAddr"),
)
if mibBuilder.loadTexts:
    rbnIpPoolEntry.setStatus("current")
_RbnIpPoolInterfaceIdx_Type = Unsigned32
_RbnIpPoolInterfaceIdx_Object = MibTableColumn
rbnIpPoolInterfaceIdx = _RbnIpPoolInterfaceIdx_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 1, 1, 1),
    _RbnIpPoolInterfaceIdx_Type()
)
rbnIpPoolInterfaceIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnIpPoolInterfaceIdx.setStatus("current")
_RbnIpPoolAddr_Type = IpAddress
_RbnIpPoolAddr_Object = MibTableColumn
rbnIpPoolAddr = _RbnIpPoolAddr_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 1, 1, 2),
    _RbnIpPoolAddr_Type()
)
rbnIpPoolAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnIpPoolAddr.setStatus("current")


class _RbnIpPoolInterfaceName_Type(SnmpAdminString):
    """Custom type rbnIpPoolInterfaceName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_RbnIpPoolInterfaceName_Type.__name__ = "SnmpAdminString"
_RbnIpPoolInterfaceName_Object = MibTableColumn
rbnIpPoolInterfaceName = _RbnIpPoolInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 1, 1, 3),
    _RbnIpPoolInterfaceName_Type()
)
rbnIpPoolInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnIpPoolInterfaceName.setStatus("current")
_RbnIpPoolMask_Type = IpAddress
_RbnIpPoolMask_Object = MibTableColumn
rbnIpPoolMask = _RbnIpPoolMask_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 1, 1, 4),
    _RbnIpPoolMask_Type()
)
rbnIpPoolMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnIpPoolMask.setStatus("current")
_RbnIpPoolSize_Type = Unsigned32
_RbnIpPoolSize_Object = MibTableColumn
rbnIpPoolSize = _RbnIpPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 1, 1, 5),
    _RbnIpPoolSize_Type()
)
rbnIpPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnIpPoolSize.setStatus("current")
_RbnIpPoolAvailable_Type = Unsigned32
_RbnIpPoolAvailable_Object = MibTableColumn
rbnIpPoolAvailable = _RbnIpPoolAvailable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 1, 1, 6),
    _RbnIpPoolAvailable_Type()
)
rbnIpPoolAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnIpPoolAvailable.setStatus("current")
_RbnIpPoolUnusable_Type = Unsigned32
_RbnIpPoolUnusable_Object = MibTableColumn
rbnIpPoolUnusable = _RbnIpPoolUnusable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 1, 1, 7),
    _RbnIpPoolUnusable_Type()
)
rbnIpPoolUnusable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnIpPoolUnusable.setStatus("current")
_RbnIpPoolInuse_Type = Unsigned32
_RbnIpPoolInuse_Object = MibTableColumn
rbnIpPoolInuse = _RbnIpPoolInuse_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 1, 1, 8),
    _RbnIpPoolInuse_Type()
)
rbnIpPoolInuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnIpPoolInuse.setStatus("current")


class _RbnIpPoolThreshold_Type(Unsigned32):
    """Custom type rbnIpPoolThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RbnIpPoolThreshold_Type.__name__ = "Unsigned32"
_RbnIpPoolThreshold_Object = MibTableColumn
rbnIpPoolThreshold = _RbnIpPoolThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 1, 1, 9),
    _RbnIpPoolThreshold_Type()
)
rbnIpPoolThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnIpPoolThreshold.setStatus("current")
_RbnIpPoolSendTrap_Type = TruthValue
_RbnIpPoolSendTrap_Object = MibTableColumn
rbnIpPoolSendTrap = _RbnIpPoolSendTrap_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 1, 1, 10),
    _RbnIpPoolSendTrap_Type()
)
rbnIpPoolSendTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnIpPoolSendTrap.setStatus("current")
_RbnIpPoolLogMessage_Type = TruthValue
_RbnIpPoolLogMessage_Object = MibTableColumn
rbnIpPoolLogMessage = _RbnIpPoolLogMessage_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 1, 1, 11),
    _RbnIpPoolLogMessage_Type()
)
rbnIpPoolLogMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnIpPoolLogMessage.setStatus("current")


class _RbnIpPoolName_Type(SnmpAdminString):
    """Custom type rbnIpPoolName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RbnIpPoolName_Type.__name__ = "SnmpAdminString"
_RbnIpPoolName_Object = MibTableColumn
rbnIpPoolName = _RbnIpPoolName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 1, 1, 12),
    _RbnIpPoolName_Type()
)
rbnIpPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnIpPoolName.setStatus("current")


class _RbnIpPoolType_Type(Integer32):
    """Custom type rbnIpPoolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("range", 1),
          ("subnet", 0))
    )


_RbnIpPoolType_Type.__name__ = "Integer32"
_RbnIpPoolType_Object = MibTableColumn
rbnIpPoolType = _RbnIpPoolType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 1, 1, 13),
    _RbnIpPoolType_Type()
)
rbnIpPoolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnIpPoolType.setStatus("current")
_RbnIpPoolEndAddr_Type = IpAddress
_RbnIpPoolEndAddr_Object = MibTableColumn
rbnIpPoolEndAddr = _RbnIpPoolEndAddr_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 1, 1, 14),
    _RbnIpPoolEndAddr_Type()
)
rbnIpPoolEndAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnIpPoolEndAddr.setStatus("current")
_RbnIpPoolSummary_ObjectIdentity = ObjectIdentity
rbnIpPoolSummary = _RbnIpPoolSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 2)
)


class _RbnIpPoolContextName_Type(SnmpAdminString):
    """Custom type rbnIpPoolContextName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_RbnIpPoolContextName_Type.__name__ = "SnmpAdminString"
_RbnIpPoolContextName_Object = MibScalar
rbnIpPoolContextName = _RbnIpPoolContextName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 2, 1),
    _RbnIpPoolContextName_Type()
)
rbnIpPoolContextName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnIpPoolContextName.setStatus("current")
_RbnIpPoolContextAvailable_Type = Unsigned32
_RbnIpPoolContextAvailable_Object = MibScalar
rbnIpPoolContextAvailable = _RbnIpPoolContextAvailable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 2, 2),
    _RbnIpPoolContextAvailable_Type()
)
rbnIpPoolContextAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnIpPoolContextAvailable.setStatus("current")
_RbnIpPoolContextThreshold_Type = Unsigned32
_RbnIpPoolContextThreshold_Object = MibScalar
rbnIpPoolContextThreshold = _RbnIpPoolContextThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 2, 3),
    _RbnIpPoolContextThreshold_Type()
)
rbnIpPoolContextThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnIpPoolContextThreshold.setStatus("current")
_RbnIpPoolContextSendTrap_Type = TruthValue
_RbnIpPoolContextSendTrap_Object = MibScalar
rbnIpPoolContextSendTrap = _RbnIpPoolContextSendTrap_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 2, 4),
    _RbnIpPoolContextSendTrap_Type()
)
rbnIpPoolContextSendTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnIpPoolContextSendTrap.setStatus("current")
_RbnIpPoolContextLogMessage_Type = TruthValue
_RbnIpPoolContextLogMessage_Object = MibScalar
rbnIpPoolContextLogMessage = _RbnIpPoolContextLogMessage_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 2, 5),
    _RbnIpPoolContextLogMessage_Type()
)
rbnIpPoolContextLogMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnIpPoolContextLogMessage.setStatus("current")
_RbnIpPoolContextTotalSize_Type = Unsigned32
_RbnIpPoolContextTotalSize_Object = MibScalar
rbnIpPoolContextTotalSize = _RbnIpPoolContextTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 2, 6),
    _RbnIpPoolContextTotalSize_Type()
)
rbnIpPoolContextTotalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnIpPoolContextTotalSize.setStatus("current")
_RbnIpPoolContextThresholdPercentTable_Object = MibTable
rbnIpPoolContextThresholdPercentTable = _RbnIpPoolContextThresholdPercentTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 2, 7)
)
if mibBuilder.loadTexts:
    rbnIpPoolContextThresholdPercentTable.setStatus("current")
_RbnIpPoolContextThresholdPercentEntry_Object = MibTableRow
rbnIpPoolContextThresholdPercentEntry = _RbnIpPoolContextThresholdPercentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 2, 7, 1)
)
rbnIpPoolContextThresholdPercentEntry.setIndexNames(
    (0, "RBN-IPPOOL-MIB", "rbnIpPoolContextThresholdIndex"),
)
if mibBuilder.loadTexts:
    rbnIpPoolContextThresholdPercentEntry.setStatus("current")
_RbnIpPoolContextThresholdIndex_Type = Unsigned32
_RbnIpPoolContextThresholdIndex_Object = MibTableColumn
rbnIpPoolContextThresholdIndex = _RbnIpPoolContextThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 2, 7, 1, 1),
    _RbnIpPoolContextThresholdIndex_Type()
)
rbnIpPoolContextThresholdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnIpPoolContextThresholdIndex.setStatus("current")
_RbnIpPoolContextThresholdPercentage_Type = RbnPercentage
_RbnIpPoolContextThresholdPercentage_Object = MibTableColumn
rbnIpPoolContextThresholdPercentage = _RbnIpPoolContextThresholdPercentage_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 2, 7, 1, 2),
    _RbnIpPoolContextThresholdPercentage_Type()
)
rbnIpPoolContextThresholdPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnIpPoolContextThresholdPercentage.setStatus("current")
_RbnIpPoolContextThresholdSendTrap_Type = TruthValue
_RbnIpPoolContextThresholdSendTrap_Object = MibTableColumn
rbnIpPoolContextThresholdSendTrap = _RbnIpPoolContextThresholdSendTrap_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 2, 7, 1, 3),
    _RbnIpPoolContextThresholdSendTrap_Type()
)
rbnIpPoolContextThresholdSendTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnIpPoolContextThresholdSendTrap.setStatus("current")
_RbnIpPoolContextThresholdLogMessage_Type = TruthValue
_RbnIpPoolContextThresholdLogMessage_Object = MibTableColumn
rbnIpPoolContextThresholdLogMessage = _RbnIpPoolContextThresholdLogMessage_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 2, 7, 1, 4),
    _RbnIpPoolContextThresholdLogMessage_Type()
)
rbnIpPoolContextThresholdLogMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnIpPoolContextThresholdLogMessage.setStatus("current")
_RbnInetIpPoolTable_Object = MibTable
rbnInetIpPoolTable = _RbnInetIpPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 3)
)
if mibBuilder.loadTexts:
    rbnInetIpPoolTable.setStatus("current")
_RbnInetIpPoolEntry_Object = MibTableRow
rbnInetIpPoolEntry = _RbnInetIpPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 3, 1)
)
rbnInetIpPoolEntry.setIndexNames(
    (0, "RBN-IPPOOL-MIB", "rbnInetIpPoolType"),
    (0, "RBN-IPPOOL-MIB", "rbnInetIpPoolIfIndex"),
    (0, "RBN-IPPOOL-MIB", "rbnInetIpPoolStartPrefixType"),
    (0, "RBN-IPPOOL-MIB", "rbnInetIpPoolStartPrefix"),
    (0, "RBN-IPPOOL-MIB", "rbnInetIpPoolStartPrefixLen"),
)
if mibBuilder.loadTexts:
    rbnInetIpPoolEntry.setStatus("current")
_RbnInetIpPoolType_Type = RbnInetPoolType
_RbnInetIpPoolType_Object = MibTableColumn
rbnInetIpPoolType = _RbnInetIpPoolType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 3, 1, 1),
    _RbnInetIpPoolType_Type()
)
rbnInetIpPoolType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnInetIpPoolType.setStatus("current")
_RbnInetIpPoolIfIndex_Type = InterfaceIndex
_RbnInetIpPoolIfIndex_Object = MibTableColumn
rbnInetIpPoolIfIndex = _RbnInetIpPoolIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 3, 1, 2),
    _RbnInetIpPoolIfIndex_Type()
)
rbnInetIpPoolIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnInetIpPoolIfIndex.setStatus("current")
_RbnInetIpPoolStartPrefixType_Type = InetAddressType
_RbnInetIpPoolStartPrefixType_Object = MibTableColumn
rbnInetIpPoolStartPrefixType = _RbnInetIpPoolStartPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 3, 1, 3),
    _RbnInetIpPoolStartPrefixType_Type()
)
rbnInetIpPoolStartPrefixType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnInetIpPoolStartPrefixType.setStatus("current")
_RbnInetIpPoolStartPrefix_Type = InetAddress
_RbnInetIpPoolStartPrefix_Object = MibTableColumn
rbnInetIpPoolStartPrefix = _RbnInetIpPoolStartPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 3, 1, 4),
    _RbnInetIpPoolStartPrefix_Type()
)
rbnInetIpPoolStartPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnInetIpPoolStartPrefix.setStatus("current")


class _RbnInetIpPoolStartPrefixLen_Type(InetAddressPrefixLength):
    """Custom type rbnInetIpPoolStartPrefixLen based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_RbnInetIpPoolStartPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_RbnInetIpPoolStartPrefixLen_Object = MibTableColumn
rbnInetIpPoolStartPrefixLen = _RbnInetIpPoolStartPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 3, 1, 5),
    _RbnInetIpPoolStartPrefixLen_Type()
)
rbnInetIpPoolStartPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnInetIpPoolStartPrefixLen.setStatus("current")
_RbnInetIpPoolEndPrefixType_Type = InetAddressType
_RbnInetIpPoolEndPrefixType_Object = MibTableColumn
rbnInetIpPoolEndPrefixType = _RbnInetIpPoolEndPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 3, 1, 6),
    _RbnInetIpPoolEndPrefixType_Type()
)
rbnInetIpPoolEndPrefixType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnInetIpPoolEndPrefixType.setStatus("current")
_RbnInetIpPoolEndPrefix_Type = InetAddress
_RbnInetIpPoolEndPrefix_Object = MibTableColumn
rbnInetIpPoolEndPrefix = _RbnInetIpPoolEndPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 3, 1, 7),
    _RbnInetIpPoolEndPrefix_Type()
)
rbnInetIpPoolEndPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnInetIpPoolEndPrefix.setStatus("current")


class _RbnInetIpPoolEndPrefixLen_Type(InetAddressPrefixLength):
    """Custom type rbnInetIpPoolEndPrefixLen based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_RbnInetIpPoolEndPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_RbnInetIpPoolEndPrefixLen_Object = MibTableColumn
rbnInetIpPoolEndPrefixLen = _RbnInetIpPoolEndPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 3, 1, 8),
    _RbnInetIpPoolEndPrefixLen_Type()
)
rbnInetIpPoolEndPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnInetIpPoolEndPrefixLen.setStatus("current")
_RbnInetIpPoolInterfaceName_Type = SnmpAdminString
_RbnInetIpPoolInterfaceName_Object = MibTableColumn
rbnInetIpPoolInterfaceName = _RbnInetIpPoolInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 3, 1, 9),
    _RbnInetIpPoolInterfaceName_Type()
)
rbnInetIpPoolInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnInetIpPoolInterfaceName.setStatus("current")
_RbnInetIpPoolName_Type = SnmpAdminString
_RbnInetIpPoolName_Object = MibTableColumn
rbnInetIpPoolName = _RbnInetIpPoolName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 3, 1, 10),
    _RbnInetIpPoolName_Type()
)
rbnInetIpPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnInetIpPoolName.setStatus("current")
_RbnInetIpPoolSize_Type = Unsigned32
_RbnInetIpPoolSize_Object = MibTableColumn
rbnInetIpPoolSize = _RbnInetIpPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 3, 1, 11),
    _RbnInetIpPoolSize_Type()
)
rbnInetIpPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnInetIpPoolSize.setStatus("current")
_RbnInetIpPoolAvailable_Type = Unsigned32
_RbnInetIpPoolAvailable_Object = MibTableColumn
rbnInetIpPoolAvailable = _RbnInetIpPoolAvailable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 3, 1, 12),
    _RbnInetIpPoolAvailable_Type()
)
rbnInetIpPoolAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnInetIpPoolAvailable.setStatus("current")
_RbnInetIpPoolUnusable_Type = Unsigned32
_RbnInetIpPoolUnusable_Object = MibTableColumn
rbnInetIpPoolUnusable = _RbnInetIpPoolUnusable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 3, 1, 13),
    _RbnInetIpPoolUnusable_Type()
)
rbnInetIpPoolUnusable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnInetIpPoolUnusable.setStatus("current")
_RbnInetIpPoolInuse_Type = Unsigned32
_RbnInetIpPoolInuse_Object = MibTableColumn
rbnInetIpPoolInuse = _RbnInetIpPoolInuse_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 3, 1, 14),
    _RbnInetIpPoolInuse_Type()
)
rbnInetIpPoolInuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnInetIpPoolInuse.setStatus("current")
_RbnInetIpPoolThrshType_Type = RbnInetIpPoolThresholdType
_RbnInetIpPoolThrshType_Object = MibTableColumn
rbnInetIpPoolThrshType = _RbnInetIpPoolThrshType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 3, 1, 15),
    _RbnInetIpPoolThrshType_Type()
)
rbnInetIpPoolThrshType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnInetIpPoolThrshType.setStatus("current")
_RbnInetIpPoolHiFallingThrsh_Type = RbnInetIpPoolThreshold
_RbnInetIpPoolHiFallingThrsh_Object = MibTableColumn
rbnInetIpPoolHiFallingThrsh = _RbnInetIpPoolHiFallingThrsh_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 3, 1, 16),
    _RbnInetIpPoolHiFallingThrsh_Type()
)
rbnInetIpPoolHiFallingThrsh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnInetIpPoolHiFallingThrsh.setStatus("current")
_RbnInetIpPoolHiFallingNotify_Type = RbnInetIpPoolThrshNotify
_RbnInetIpPoolHiFallingNotify_Object = MibTableColumn
rbnInetIpPoolHiFallingNotify = _RbnInetIpPoolHiFallingNotify_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 3, 1, 17),
    _RbnInetIpPoolHiFallingNotify_Type()
)
rbnInetIpPoolHiFallingNotify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnInetIpPoolHiFallingNotify.setStatus("current")
_RbnInetIpPoolLoFallingThrsh_Type = RbnInetIpPoolThreshold
_RbnInetIpPoolLoFallingThrsh_Object = MibTableColumn
rbnInetIpPoolLoFallingThrsh = _RbnInetIpPoolLoFallingThrsh_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 3, 1, 18),
    _RbnInetIpPoolLoFallingThrsh_Type()
)
rbnInetIpPoolLoFallingThrsh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnInetIpPoolLoFallingThrsh.setStatus("current")
_RbnInetIpPoolLoFallingNotify_Type = RbnInetIpPoolThrshNotify
_RbnInetIpPoolLoFallingNotify_Object = MibTableColumn
rbnInetIpPoolLoFallingNotify = _RbnInetIpPoolLoFallingNotify_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 3, 1, 19),
    _RbnInetIpPoolLoFallingNotify_Type()
)
rbnInetIpPoolLoFallingNotify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnInetIpPoolLoFallingNotify.setStatus("current")
_RbnInetIpPoolSummary_ObjectIdentity = ObjectIdentity
rbnInetIpPoolSummary = _RbnInetIpPoolSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 4)
)
_RbnInetIpPoolCtxName_Type = SnmpAdminString
_RbnInetIpPoolCtxName_Object = MibScalar
rbnInetIpPoolCtxName = _RbnInetIpPoolCtxName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 4, 1),
    _RbnInetIpPoolCtxName_Type()
)
rbnInetIpPoolCtxName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnInetIpPoolCtxName.setStatus("current")
_RbnInetIpPoolCtxTable_Object = MibTable
rbnInetIpPoolCtxTable = _RbnInetIpPoolCtxTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 4, 2)
)
if mibBuilder.loadTexts:
    rbnInetIpPoolCtxTable.setStatus("current")
_RbnInetIpPoolCtxEntry_Object = MibTableRow
rbnInetIpPoolCtxEntry = _RbnInetIpPoolCtxEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 4, 2, 1)
)
rbnInetIpPoolCtxEntry.setIndexNames(
    (0, "RBN-IPPOOL-MIB", "rbnInetIpPoolCtxPoolType"),
)
if mibBuilder.loadTexts:
    rbnInetIpPoolCtxEntry.setStatus("current")
_RbnInetIpPoolCtxPoolType_Type = RbnInetPoolType
_RbnInetIpPoolCtxPoolType_Object = MibTableColumn
rbnInetIpPoolCtxPoolType = _RbnInetIpPoolCtxPoolType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 4, 2, 1, 1),
    _RbnInetIpPoolCtxPoolType_Type()
)
rbnInetIpPoolCtxPoolType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnInetIpPoolCtxPoolType.setStatus("current")
_RbnInetIpPoolCtxAvailable_Type = Unsigned32
_RbnInetIpPoolCtxAvailable_Object = MibTableColumn
rbnInetIpPoolCtxAvailable = _RbnInetIpPoolCtxAvailable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 4, 2, 1, 2),
    _RbnInetIpPoolCtxAvailable_Type()
)
rbnInetIpPoolCtxAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnInetIpPoolCtxAvailable.setStatus("current")
_RbnInetIpPoolCtxPoolSize_Type = Unsigned32
_RbnInetIpPoolCtxPoolSize_Object = MibTableColumn
rbnInetIpPoolCtxPoolSize = _RbnInetIpPoolCtxPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 4, 2, 1, 3),
    _RbnInetIpPoolCtxPoolSize_Type()
)
rbnInetIpPoolCtxPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnInetIpPoolCtxPoolSize.setStatus("current")
_RbnInetIpPoolCtxThrshType_Type = RbnInetIpPoolThresholdType
_RbnInetIpPoolCtxThrshType_Object = MibTableColumn
rbnInetIpPoolCtxThrshType = _RbnInetIpPoolCtxThrshType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 4, 2, 1, 4),
    _RbnInetIpPoolCtxThrshType_Type()
)
rbnInetIpPoolCtxThrshType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnInetIpPoolCtxThrshType.setStatus("current")
_RbnInetIpPoolCtxHiFallingThrsh_Type = RbnInetIpPoolThreshold
_RbnInetIpPoolCtxHiFallingThrsh_Object = MibTableColumn
rbnInetIpPoolCtxHiFallingThrsh = _RbnInetIpPoolCtxHiFallingThrsh_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 4, 2, 1, 5),
    _RbnInetIpPoolCtxHiFallingThrsh_Type()
)
rbnInetIpPoolCtxHiFallingThrsh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnInetIpPoolCtxHiFallingThrsh.setStatus("current")
_RbnInetIpPoolCtxHiFallingNotify_Type = RbnInetIpPoolThrshNotify
_RbnInetIpPoolCtxHiFallingNotify_Object = MibTableColumn
rbnInetIpPoolCtxHiFallingNotify = _RbnInetIpPoolCtxHiFallingNotify_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 4, 2, 1, 6),
    _RbnInetIpPoolCtxHiFallingNotify_Type()
)
rbnInetIpPoolCtxHiFallingNotify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnInetIpPoolCtxHiFallingNotify.setStatus("current")
_RbnInetIpPoolCtxLoFallingThrsh_Type = RbnInetIpPoolThreshold
_RbnInetIpPoolCtxLoFallingThrsh_Object = MibTableColumn
rbnInetIpPoolCtxLoFallingThrsh = _RbnInetIpPoolCtxLoFallingThrsh_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 4, 2, 1, 7),
    _RbnInetIpPoolCtxLoFallingThrsh_Type()
)
rbnInetIpPoolCtxLoFallingThrsh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnInetIpPoolCtxLoFallingThrsh.setStatus("current")
_RbnInetIpPoolCtxLoFallingNotify_Type = RbnInetIpPoolThrshNotify
_RbnInetIpPoolCtxLoFallingNotify_Object = MibTableColumn
rbnInetIpPoolCtxLoFallingNotify = _RbnInetIpPoolCtxLoFallingNotify_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 1, 4, 2, 1, 8),
    _RbnInetIpPoolCtxLoFallingNotify_Type()
)
rbnInetIpPoolCtxLoFallingNotify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnInetIpPoolCtxLoFallingNotify.setStatus("current")
_RbnIpPoolMIBConformance_ObjectIdentity = ObjectIdentity
rbnIpPoolMIBConformance = _RbnIpPoolMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 2)
)
_RbnIpPoolCompliances_ObjectIdentity = ObjectIdentity
rbnIpPoolCompliances = _RbnIpPoolCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 2, 1)
)
_RbnIpPoolGroups_ObjectIdentity = ObjectIdentity
rbnIpPoolGroups = _RbnIpPoolGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 2, 2)
)

# Managed Objects groups

rbnIpPoolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 2, 2, 1)
)
rbnIpPoolGroup.setObjects(
      *(("RBN-IPPOOL-MIB", "rbnIpPoolInterfaceName"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolMask"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolSize"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolAvailable"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolUnusable"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolInuse"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolThreshold"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolSendTrap"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolLogMessage"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolContextName"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolContextAvailable"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolContextThreshold"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolContextSendTrap"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolContextLogMessage"))
)
if mibBuilder.loadTexts:
    rbnIpPoolGroup.setStatus("current")

rbnIpPoolNameGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 2, 2, 3)
)
rbnIpPoolNameGroup.setObjects(
    ("RBN-IPPOOL-MIB", "rbnIpPoolName")
)
if mibBuilder.loadTexts:
    rbnIpPoolNameGroup.setStatus("current")

rbnIpPoolGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 2, 2, 4)
)
rbnIpPoolGroupV2.setObjects(
      *(("RBN-IPPOOL-MIB", "rbnIpPoolInterfaceName"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolMask"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolSize"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolAvailable"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolUnusable"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolInuse"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolThreshold"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolSendTrap"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolLogMessage"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolType"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolContextName"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolContextAvailable"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolContextThreshold"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolContextSendTrap"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolContextLogMessage"))
)
if mibBuilder.loadTexts:
    rbnIpPoolGroupV2.setStatus("current")

rbnIpPoolRangeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 2, 2, 5)
)
rbnIpPoolRangeGroup.setObjects(
    ("RBN-IPPOOL-MIB", "rbnIpPoolEndAddr")
)
if mibBuilder.loadTexts:
    rbnIpPoolRangeGroup.setStatus("current")

rbnIpPoolInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 2, 2, 6)
)
rbnIpPoolInterfaceGroup.setObjects(
      *(("RBN-IPPOOL-MIB", "rbnIpPoolInterfaceName"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolMask"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolSize"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolAvailable"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolUnusable"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolInuse"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolThreshold"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolSendTrap"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolLogMessage"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolName"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolType"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolEndAddr"))
)
if mibBuilder.loadTexts:
    rbnIpPoolInterfaceGroup.setStatus("current")

rbnIpPoolContextGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 2, 2, 7)
)
rbnIpPoolContextGroup.setObjects(
      *(("RBN-IPPOOL-MIB", "rbnIpPoolContextName"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolContextAvailable"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolContextThreshold"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolContextSendTrap"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolContextLogMessage"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolContextTotalSize"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolContextThresholdPercentage"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolContextThresholdSendTrap"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolContextThresholdLogMessage"))
)
if mibBuilder.loadTexts:
    rbnIpPoolContextGroup.setStatus("current")

rbnInetIpPoolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 2, 2, 9)
)
rbnInetIpPoolGroup.setObjects(
      *(("RBN-IPPOOL-MIB", "rbnInetIpPoolEndPrefixType"),
        ("RBN-IPPOOL-MIB", "rbnInetIpPoolEndPrefix"),
        ("RBN-IPPOOL-MIB", "rbnInetIpPoolEndPrefixLen"),
        ("RBN-IPPOOL-MIB", "rbnInetIpPoolInterfaceName"),
        ("RBN-IPPOOL-MIB", "rbnInetIpPoolName"),
        ("RBN-IPPOOL-MIB", "rbnInetIpPoolSize"),
        ("RBN-IPPOOL-MIB", "rbnInetIpPoolAvailable"),
        ("RBN-IPPOOL-MIB", "rbnInetIpPoolUnusable"),
        ("RBN-IPPOOL-MIB", "rbnInetIpPoolInuse"),
        ("RBN-IPPOOL-MIB", "rbnInetIpPoolThrshType"),
        ("RBN-IPPOOL-MIB", "rbnInetIpPoolHiFallingThrsh"),
        ("RBN-IPPOOL-MIB", "rbnInetIpPoolHiFallingNotify"),
        ("RBN-IPPOOL-MIB", "rbnInetIpPoolLoFallingThrsh"),
        ("RBN-IPPOOL-MIB", "rbnInetIpPoolLoFallingNotify"),
        ("RBN-IPPOOL-MIB", "rbnInetIpPoolCtxName"),
        ("RBN-IPPOOL-MIB", "rbnInetIpPoolCtxAvailable"),
        ("RBN-IPPOOL-MIB", "rbnInetIpPoolCtxPoolSize"),
        ("RBN-IPPOOL-MIB", "rbnInetIpPoolCtxThrshType"),
        ("RBN-IPPOOL-MIB", "rbnInetIpPoolCtxHiFallingThrsh"),
        ("RBN-IPPOOL-MIB", "rbnInetIpPoolCtxHiFallingNotify"),
        ("RBN-IPPOOL-MIB", "rbnInetIpPoolCtxLoFallingThrsh"),
        ("RBN-IPPOOL-MIB", "rbnInetIpPoolCtxLoFallingNotify"))
)
if mibBuilder.loadTexts:
    rbnInetIpPoolGroup.setStatus("current")


# Notification objects

rbnIpPoolThresholdMet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 0, 1)
)
rbnIpPoolThresholdMet.setObjects(
      *(("RBN-IPPOOL-MIB", "rbnIpPoolContextName"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolInterfaceName"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolMask"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolAvailable"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolThreshold"))
)
if mibBuilder.loadTexts:
    rbnIpPoolThresholdMet.setStatus(
        "current"
    )

rbnIpPoolContextThresholdMet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 0, 2)
)
rbnIpPoolContextThresholdMet.setObjects(
      *(("RBN-IPPOOL-MIB", "rbnIpPoolContextName"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolContextAvailable"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolContextThreshold"))
)
if mibBuilder.loadTexts:
    rbnIpPoolContextThresholdMet.setStatus(
        "current"
    )

rbnIpPoolContextThresholdPercentageMet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 0, 3)
)
rbnIpPoolContextThresholdPercentageMet.setObjects(
      *(("RBN-IPPOOL-MIB", "rbnIpPoolContextName"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolContextTotalSize"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolContextAvailable"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolContextThresholdPercentage"))
)
if mibBuilder.loadTexts:
    rbnIpPoolContextThresholdPercentageMet.setStatus(
        "current"
    )

rbnInetIpPoolHiFallingThrshMet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 0, 4)
)
rbnInetIpPoolHiFallingThrshMet.setObjects(
      *(("RBN-IPPOOL-MIB", "rbnInetIpPoolEndPrefixType"),
        ("RBN-IPPOOL-MIB", "rbnInetIpPoolEndPrefix"),
        ("RBN-IPPOOL-MIB", "rbnInetIpPoolEndPrefixLen"),
        ("RBN-IPPOOL-MIB", "rbnInetIpPoolInterfaceName"),
        ("RBN-IPPOOL-MIB", "rbnInetIpPoolName"),
        ("RBN-IPPOOL-MIB", "rbnInetIpPoolSize"),
        ("RBN-IPPOOL-MIB", "rbnInetIpPoolAvailable"),
        ("RBN-IPPOOL-MIB", "rbnInetIpPoolThrshType"),
        ("RBN-IPPOOL-MIB", "rbnInetIpPoolHiFallingThrsh"))
)
if mibBuilder.loadTexts:
    rbnInetIpPoolHiFallingThrshMet.setStatus(
        "current"
    )

rbnInetIpPoolLoFallingThrshMet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 0, 5)
)
rbnInetIpPoolLoFallingThrshMet.setObjects(
      *(("RBN-IPPOOL-MIB", "rbnInetIpPoolEndPrefixType"),
        ("RBN-IPPOOL-MIB", "rbnInetIpPoolEndPrefix"),
        ("RBN-IPPOOL-MIB", "rbnInetIpPoolEndPrefixLen"),
        ("RBN-IPPOOL-MIB", "rbnInetIpPoolInterfaceName"),
        ("RBN-IPPOOL-MIB", "rbnInetIpPoolName"),
        ("RBN-IPPOOL-MIB", "rbnInetIpPoolSize"),
        ("RBN-IPPOOL-MIB", "rbnInetIpPoolAvailable"),
        ("RBN-IPPOOL-MIB", "rbnInetIpPoolThrshType"),
        ("RBN-IPPOOL-MIB", "rbnInetIpPoolLoFallingThrsh"))
)
if mibBuilder.loadTexts:
    rbnInetIpPoolLoFallingThrshMet.setStatus(
        "current"
    )

rbnInetIpPoolCtxHiFallingThrshMet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 0, 6)
)
rbnInetIpPoolCtxHiFallingThrshMet.setObjects(
      *(("RBN-IPPOOL-MIB", "rbnInetIpPoolCtxName"),
        ("RBN-IPPOOL-MIB", "rbnInetIpPoolCtxPoolSize"),
        ("RBN-IPPOOL-MIB", "rbnInetIpPoolCtxAvailable"),
        ("RBN-IPPOOL-MIB", "rbnInetIpPoolCtxThrshType"),
        ("RBN-IPPOOL-MIB", "rbnInetIpPoolCtxHiFallingThrsh"))
)
if mibBuilder.loadTexts:
    rbnInetIpPoolCtxHiFallingThrshMet.setStatus(
        "current"
    )

rbnInetIpPoolCtxLoFallingThrshMet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 0, 7)
)
rbnInetIpPoolCtxLoFallingThrshMet.setObjects(
      *(("RBN-IPPOOL-MIB", "rbnInetIpPoolCtxName"),
        ("RBN-IPPOOL-MIB", "rbnInetIpPoolCtxPoolSize"),
        ("RBN-IPPOOL-MIB", "rbnInetIpPoolCtxAvailable"),
        ("RBN-IPPOOL-MIB", "rbnInetIpPoolCtxThrshType"),
        ("RBN-IPPOOL-MIB", "rbnInetIpPoolCtxLoFallingThrsh"))
)
if mibBuilder.loadTexts:
    rbnInetIpPoolCtxLoFallingThrshMet.setStatus(
        "current"
    )


# Notifications groups

rbnIpPoolNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 2, 2, 2)
)
rbnIpPoolNotifyGroup.setObjects(
      *(("RBN-IPPOOL-MIB", "rbnIpPoolThresholdMet"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolContextThresholdMet"))
)
if mibBuilder.loadTexts:
    rbnIpPoolNotifyGroup.setStatus(
        "current"
    )

rbnIpPoolNotifyGroupV2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 2, 2, 8)
)
rbnIpPoolNotifyGroupV2.setObjects(
      *(("RBN-IPPOOL-MIB", "rbnIpPoolThresholdMet"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolContextThresholdMet"),
        ("RBN-IPPOOL-MIB", "rbnIpPoolContextThresholdPercentageMet"))
)
if mibBuilder.loadTexts:
    rbnIpPoolNotifyGroupV2.setStatus(
        "current"
    )

rbnInetIpPoolNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 2, 2, 10)
)
rbnInetIpPoolNotifyGroup.setObjects(
      *(("RBN-IPPOOL-MIB", "rbnInetIpPoolHiFallingThrshMet"),
        ("RBN-IPPOOL-MIB", "rbnInetIpPoolLoFallingThrshMet"),
        ("RBN-IPPOOL-MIB", "rbnInetIpPoolCtxHiFallingThrshMet"),
        ("RBN-IPPOOL-MIB", "rbnInetIpPoolCtxLoFallingThrshMet"))
)
if mibBuilder.loadTexts:
    rbnInetIpPoolNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

rbnIpPoolCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rbnIpPoolCompliance.setStatus(
        "current"
    )

rbnIpPoolNameCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 2, 1, 2)
)
if mibBuilder.loadTexts:
    rbnIpPoolNameCompliance.setStatus(
        "current"
    )

rbnIpPoolComplianceV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 2, 1, 3)
)
if mibBuilder.loadTexts:
    rbnIpPoolComplianceV2.setStatus(
        "current"
    )

rbnIpPoolNameComplianceV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 2, 1, 4)
)
if mibBuilder.loadTexts:
    rbnIpPoolNameComplianceV2.setStatus(
        "current"
    )

rbnIpPoolRangeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 2, 1, 5)
)
if mibBuilder.loadTexts:
    rbnIpPoolRangeCompliance.setStatus(
        "current"
    )

rbnIpPoolThresholdPercentCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 2, 1, 6)
)
if mibBuilder.loadTexts:
    rbnIpPoolThresholdPercentCompliance.setStatus(
        "current"
    )

rbnInetIpPoolCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 15, 2, 1, 7)
)
if mibBuilder.loadTexts:
    rbnInetIpPoolCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-IPPOOL-MIB",
    **{"RbnInetPoolType": RbnInetPoolType,
       "RbnInetIpPoolThresholdType": RbnInetIpPoolThresholdType,
       "RbnInetIpPoolThreshold": RbnInetIpPoolThreshold,
       "RbnInetIpPoolThrshNotify": RbnInetIpPoolThrshNotify,
       "rbnIpPoolMib": rbnIpPoolMib,
       "rbnIpPoolMIBNotifications": rbnIpPoolMIBNotifications,
       "rbnIpPoolThresholdMet": rbnIpPoolThresholdMet,
       "rbnIpPoolContextThresholdMet": rbnIpPoolContextThresholdMet,
       "rbnIpPoolContextThresholdPercentageMet": rbnIpPoolContextThresholdPercentageMet,
       "rbnInetIpPoolHiFallingThrshMet": rbnInetIpPoolHiFallingThrshMet,
       "rbnInetIpPoolLoFallingThrshMet": rbnInetIpPoolLoFallingThrshMet,
       "rbnInetIpPoolCtxHiFallingThrshMet": rbnInetIpPoolCtxHiFallingThrshMet,
       "rbnInetIpPoolCtxLoFallingThrshMet": rbnInetIpPoolCtxLoFallingThrshMet,
       "rbnIpPoolMIBObjects": rbnIpPoolMIBObjects,
       "rbnIpPoolTable": rbnIpPoolTable,
       "rbnIpPoolEntry": rbnIpPoolEntry,
       "rbnIpPoolInterfaceIdx": rbnIpPoolInterfaceIdx,
       "rbnIpPoolAddr": rbnIpPoolAddr,
       "rbnIpPoolInterfaceName": rbnIpPoolInterfaceName,
       "rbnIpPoolMask": rbnIpPoolMask,
       "rbnIpPoolSize": rbnIpPoolSize,
       "rbnIpPoolAvailable": rbnIpPoolAvailable,
       "rbnIpPoolUnusable": rbnIpPoolUnusable,
       "rbnIpPoolInuse": rbnIpPoolInuse,
       "rbnIpPoolThreshold": rbnIpPoolThreshold,
       "rbnIpPoolSendTrap": rbnIpPoolSendTrap,
       "rbnIpPoolLogMessage": rbnIpPoolLogMessage,
       "rbnIpPoolName": rbnIpPoolName,
       "rbnIpPoolType": rbnIpPoolType,
       "rbnIpPoolEndAddr": rbnIpPoolEndAddr,
       "rbnIpPoolSummary": rbnIpPoolSummary,
       "rbnIpPoolContextName": rbnIpPoolContextName,
       "rbnIpPoolContextAvailable": rbnIpPoolContextAvailable,
       "rbnIpPoolContextThreshold": rbnIpPoolContextThreshold,
       "rbnIpPoolContextSendTrap": rbnIpPoolContextSendTrap,
       "rbnIpPoolContextLogMessage": rbnIpPoolContextLogMessage,
       "rbnIpPoolContextTotalSize": rbnIpPoolContextTotalSize,
       "rbnIpPoolContextThresholdPercentTable": rbnIpPoolContextThresholdPercentTable,
       "rbnIpPoolContextThresholdPercentEntry": rbnIpPoolContextThresholdPercentEntry,
       "rbnIpPoolContextThresholdIndex": rbnIpPoolContextThresholdIndex,
       "rbnIpPoolContextThresholdPercentage": rbnIpPoolContextThresholdPercentage,
       "rbnIpPoolContextThresholdSendTrap": rbnIpPoolContextThresholdSendTrap,
       "rbnIpPoolContextThresholdLogMessage": rbnIpPoolContextThresholdLogMessage,
       "rbnInetIpPoolTable": rbnInetIpPoolTable,
       "rbnInetIpPoolEntry": rbnInetIpPoolEntry,
       "rbnInetIpPoolType": rbnInetIpPoolType,
       "rbnInetIpPoolIfIndex": rbnInetIpPoolIfIndex,
       "rbnInetIpPoolStartPrefixType": rbnInetIpPoolStartPrefixType,
       "rbnInetIpPoolStartPrefix": rbnInetIpPoolStartPrefix,
       "rbnInetIpPoolStartPrefixLen": rbnInetIpPoolStartPrefixLen,
       "rbnInetIpPoolEndPrefixType": rbnInetIpPoolEndPrefixType,
       "rbnInetIpPoolEndPrefix": rbnInetIpPoolEndPrefix,
       "rbnInetIpPoolEndPrefixLen": rbnInetIpPoolEndPrefixLen,
       "rbnInetIpPoolInterfaceName": rbnInetIpPoolInterfaceName,
       "rbnInetIpPoolName": rbnInetIpPoolName,
       "rbnInetIpPoolSize": rbnInetIpPoolSize,
       "rbnInetIpPoolAvailable": rbnInetIpPoolAvailable,
       "rbnInetIpPoolUnusable": rbnInetIpPoolUnusable,
       "rbnInetIpPoolInuse": rbnInetIpPoolInuse,
       "rbnInetIpPoolThrshType": rbnInetIpPoolThrshType,
       "rbnInetIpPoolHiFallingThrsh": rbnInetIpPoolHiFallingThrsh,
       "rbnInetIpPoolHiFallingNotify": rbnInetIpPoolHiFallingNotify,
       "rbnInetIpPoolLoFallingThrsh": rbnInetIpPoolLoFallingThrsh,
       "rbnInetIpPoolLoFallingNotify": rbnInetIpPoolLoFallingNotify,
       "rbnInetIpPoolSummary": rbnInetIpPoolSummary,
       "rbnInetIpPoolCtxName": rbnInetIpPoolCtxName,
       "rbnInetIpPoolCtxTable": rbnInetIpPoolCtxTable,
       "rbnInetIpPoolCtxEntry": rbnInetIpPoolCtxEntry,
       "rbnInetIpPoolCtxPoolType": rbnInetIpPoolCtxPoolType,
       "rbnInetIpPoolCtxAvailable": rbnInetIpPoolCtxAvailable,
       "rbnInetIpPoolCtxPoolSize": rbnInetIpPoolCtxPoolSize,
       "rbnInetIpPoolCtxThrshType": rbnInetIpPoolCtxThrshType,
       "rbnInetIpPoolCtxHiFallingThrsh": rbnInetIpPoolCtxHiFallingThrsh,
       "rbnInetIpPoolCtxHiFallingNotify": rbnInetIpPoolCtxHiFallingNotify,
       "rbnInetIpPoolCtxLoFallingThrsh": rbnInetIpPoolCtxLoFallingThrsh,
       "rbnInetIpPoolCtxLoFallingNotify": rbnInetIpPoolCtxLoFallingNotify,
       "rbnIpPoolMIBConformance": rbnIpPoolMIBConformance,
       "rbnIpPoolCompliances": rbnIpPoolCompliances,
       "rbnIpPoolCompliance": rbnIpPoolCompliance,
       "rbnIpPoolNameCompliance": rbnIpPoolNameCompliance,
       "rbnIpPoolComplianceV2": rbnIpPoolComplianceV2,
       "rbnIpPoolNameComplianceV2": rbnIpPoolNameComplianceV2,
       "rbnIpPoolRangeCompliance": rbnIpPoolRangeCompliance,
       "rbnIpPoolThresholdPercentCompliance": rbnIpPoolThresholdPercentCompliance,
       "rbnInetIpPoolCompliance": rbnInetIpPoolCompliance,
       "rbnIpPoolGroups": rbnIpPoolGroups,
       "rbnIpPoolGroup": rbnIpPoolGroup,
       "rbnIpPoolNotifyGroup": rbnIpPoolNotifyGroup,
       "rbnIpPoolNameGroup": rbnIpPoolNameGroup,
       "rbnIpPoolGroupV2": rbnIpPoolGroupV2,
       "rbnIpPoolRangeGroup": rbnIpPoolRangeGroup,
       "rbnIpPoolInterfaceGroup": rbnIpPoolInterfaceGroup,
       "rbnIpPoolContextGroup": rbnIpPoolContextGroup,
       "rbnIpPoolNotifyGroupV2": rbnIpPoolNotifyGroupV2,
       "rbnInetIpPoolGroup": rbnInetIpPoolGroup,
       "rbnInetIpPoolNotifyGroup": rbnInetIpPoolNotifyGroup}
)
