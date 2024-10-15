# SNMP MIB module (RADLAN-SNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADLAN-SNMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:43:25 2024
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
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(rnd,) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rnd")

(snmpTargetAddrExtEntry,) = mibBuilder.importSymbols(
    "SNMP-COMMUNITY-MIB",
    "snmpTargetAddrExtEntry")

(SnmpEngineID,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpEngineID")

(usmUserEntry,) = mibBuilder.importSymbols(
    "SNMP-USER-BASED-SM-MIB",
    "usmUserEntry")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlSNMP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 98)
)
rlSNMP.setRevisions(
        ("2011-02-11 00:00",
         "2010-02-15 00:00",
         "2007-09-10 00:00",
         "2006-06-06 00:00",
         "1904-10-20 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RlSnmpUDPMridAddress(OctetString, TextualConvention):
    status = "current"
    displayHint = "1d.1d.1d.1d/2d/2d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class RlSnmpUDPIpv6MridAddress(OctetString, TextualConvention):
    status = "current"
    displayHint = "0a[2x:2x:2x:2x:2x:2x:2x:2x]0a:2d:2d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )



class RlSnmpUDPIpv6zMridAddress(OctetString, TextualConvention):
    status = "current"
    displayHint = "0a[2x:2x:2x:2x:2x:2x:2x:2x%4d]0a:2d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(24, 24),
    )



# MIB Managed Objects in the order of their OIDs

_RlSNMPv3_ObjectIdentity = ObjectIdentity
rlSNMPv3 = _RlSNMPv3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 98, 1)
)


class _RlTargetParamsTestingLevel_Type(Integer32):
    """Custom type rlTargetParamsTestingLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 1))
    )


_RlTargetParamsTestingLevel_Type.__name__ = "Integer32"
_RlTargetParamsTestingLevel_Object = MibScalar
rlTargetParamsTestingLevel = _RlTargetParamsTestingLevel_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 1, 1),
    _RlTargetParamsTestingLevel_Type()
)
rlTargetParamsTestingLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTargetParamsTestingLevel.setStatus("current")


class _RlNotifyFilterTestingLevel_Type(Integer32):
    """Custom type rlNotifyFilterTestingLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 1))
    )


_RlNotifyFilterTestingLevel_Type.__name__ = "Integer32"
_RlNotifyFilterTestingLevel_Object = MibScalar
rlNotifyFilterTestingLevel = _RlNotifyFilterTestingLevel_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 1, 2),
    _RlNotifyFilterTestingLevel_Type()
)
rlNotifyFilterTestingLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlNotifyFilterTestingLevel.setStatus("current")


class _RlSnmpEngineID_Type(SnmpEngineID):
    """Custom type rlSnmpEngineID based on SnmpEngineID"""
    defaultHexValue = "0000000001"


_RlSnmpEngineID_Object = MibScalar
rlSnmpEngineID = _RlSnmpEngineID_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 1, 3),
    _RlSnmpEngineID_Type()
)
rlSnmpEngineID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSnmpEngineID.setStatus("current")
_RlSNMPv3IpAddrToIndexTable_Object = MibTable
rlSNMPv3IpAddrToIndexTable = _RlSNMPv3IpAddrToIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 1, 4)
)
if mibBuilder.loadTexts:
    rlSNMPv3IpAddrToIndexTable.setStatus("current")
_RlSNMPv3IpAddrToIndexEntry_Object = MibTableRow
rlSNMPv3IpAddrToIndexEntry = _RlSNMPv3IpAddrToIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 1, 4, 1)
)
rlSNMPv3IpAddrToIndexEntry.setIndexNames(
    (0, "RADLAN-SNMP-MIB", "rlSNMPv3IpAddrToIndexAddrType"),
    (0, "RADLAN-SNMP-MIB", "rlSNMPv3IpAddrToIndexAddr"),
)
if mibBuilder.loadTexts:
    rlSNMPv3IpAddrToIndexEntry.setStatus("current")
_RlSNMPv3IpAddrToIndexAddrType_Type = InetAddressType
_RlSNMPv3IpAddrToIndexAddrType_Object = MibTableColumn
rlSNMPv3IpAddrToIndexAddrType = _RlSNMPv3IpAddrToIndexAddrType_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 1, 4, 1, 1),
    _RlSNMPv3IpAddrToIndexAddrType_Type()
)
rlSNMPv3IpAddrToIndexAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSNMPv3IpAddrToIndexAddrType.setStatus("current")
_RlSNMPv3IpAddrToIndexAddr_Type = InetAddress
_RlSNMPv3IpAddrToIndexAddr_Object = MibTableColumn
rlSNMPv3IpAddrToIndexAddr = _RlSNMPv3IpAddrToIndexAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 1, 4, 1, 2),
    _RlSNMPv3IpAddrToIndexAddr_Type()
)
rlSNMPv3IpAddrToIndexAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSNMPv3IpAddrToIndexAddr.setStatus("current")


class _RlSNMPv3IpAddrToIndexMappedIndex_Type(OctetString):
    """Custom type rlSNMPv3IpAddrToIndexMappedIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_RlSNMPv3IpAddrToIndexMappedIndex_Type.__name__ = "OctetString"
_RlSNMPv3IpAddrToIndexMappedIndex_Object = MibTableColumn
rlSNMPv3IpAddrToIndexMappedIndex = _RlSNMPv3IpAddrToIndexMappedIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 1, 4, 1, 3),
    _RlSNMPv3IpAddrToIndexMappedIndex_Type()
)
rlSNMPv3IpAddrToIndexMappedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSNMPv3IpAddrToIndexMappedIndex.setStatus("current")
_RlTargetAddrExtTable_Object = MibTable
rlTargetAddrExtTable = _RlTargetAddrExtTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 1, 5)
)
if mibBuilder.loadTexts:
    rlTargetAddrExtTable.setStatus("current")
_RlTargetAddrExtEntry_Object = MibTableRow
rlTargetAddrExtEntry = _RlTargetAddrExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 1, 5, 1)
)
if mibBuilder.loadTexts:
    rlTargetAddrExtEntry.setStatus("current")


class _RlTargetAddrMagicUsedInIndex_Type(OctetString):
    """Custom type rlTargetAddrMagicUsedInIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_RlTargetAddrMagicUsedInIndex_Type.__name__ = "OctetString"
_RlTargetAddrMagicUsedInIndex_Object = MibTableColumn
rlTargetAddrMagicUsedInIndex = _RlTargetAddrMagicUsedInIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 1, 5, 1, 1),
    _RlTargetAddrMagicUsedInIndex_Type()
)
rlTargetAddrMagicUsedInIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlTargetAddrMagicUsedInIndex.setStatus("current")
_RlInet2EngineIdTable_Object = MibTable
rlInet2EngineIdTable = _RlInet2EngineIdTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 1, 6)
)
if mibBuilder.loadTexts:
    rlInet2EngineIdTable.setStatus("current")
_RlInet2EngineIdEntry_Object = MibTableRow
rlInet2EngineIdEntry = _RlInet2EngineIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 1, 6, 1)
)
rlInet2EngineIdEntry.setIndexNames(
    (0, "RADLAN-SNMP-MIB", "rlInet2EngineIdAddressType"),
    (0, "RADLAN-SNMP-MIB", "rlInet2EngineIdAddress"),
)
if mibBuilder.loadTexts:
    rlInet2EngineIdEntry.setStatus("current")
_RlInet2EngineIdAddressType_Type = InetAddressType
_RlInet2EngineIdAddressType_Object = MibTableColumn
rlInet2EngineIdAddressType = _RlInet2EngineIdAddressType_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 1, 6, 1, 1),
    _RlInet2EngineIdAddressType_Type()
)
rlInet2EngineIdAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlInet2EngineIdAddressType.setStatus("current")
_RlInet2EngineIdAddress_Type = InetAddress
_RlInet2EngineIdAddress_Object = MibTableColumn
rlInet2EngineIdAddress = _RlInet2EngineIdAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 1, 6, 1, 2),
    _RlInet2EngineIdAddress_Type()
)
rlInet2EngineIdAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlInet2EngineIdAddress.setStatus("current")
_RlInet2EngineIdEngineId_Type = SnmpEngineID
_RlInet2EngineIdEngineId_Object = MibTableColumn
rlInet2EngineIdEngineId = _RlInet2EngineIdEngineId_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 1, 6, 1, 3),
    _RlInet2EngineIdEngineId_Type()
)
rlInet2EngineIdEngineId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlInet2EngineIdEngineId.setStatus("current")


class _RlInet2EngineIdStatus_Type(RowStatus):
    """Custom type rlInet2EngineIdStatus based on RowStatus"""


_RlInet2EngineIdStatus_Object = MibTableColumn
rlInet2EngineIdStatus = _RlInet2EngineIdStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 1, 6, 1, 4),
    _RlInet2EngineIdStatus_Type()
)
rlInet2EngineIdStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlInet2EngineIdStatus.setStatus("current")
_RlUsmUserExtTable_Object = MibTable
rlUsmUserExtTable = _RlUsmUserExtTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 1, 8)
)
if mibBuilder.loadTexts:
    rlUsmUserExtTable.setStatus("current")
_RlUsmUserExtEntry_Object = MibTableRow
rlUsmUserExtEntry = _RlUsmUserExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 1, 8, 1)
)
if mibBuilder.loadTexts:
    rlUsmUserExtEntry.setStatus("current")


class _RlUsmUserAuthPassword_Type(DisplayString):
    """Custom type rlUsmUserAuthPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlUsmUserAuthPassword_Type.__name__ = "DisplayString"
_RlUsmUserAuthPassword_Object = MibTableColumn
rlUsmUserAuthPassword = _RlUsmUserAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 1, 8, 1, 1),
    _RlUsmUserAuthPassword_Type()
)
rlUsmUserAuthPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlUsmUserAuthPassword.setStatus("current")


class _RlUsmUserPrivPassword_Type(DisplayString):
    """Custom type rlUsmUserPrivPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlUsmUserPrivPassword_Type.__name__ = "DisplayString"
_RlUsmUserPrivPassword_Object = MibTableColumn
rlUsmUserPrivPassword = _RlUsmUserPrivPassword_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 1, 8, 1, 2),
    _RlUsmUserPrivPassword_Type()
)
rlUsmUserPrivPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlUsmUserPrivPassword.setStatus("current")
_RlSNMPDomains_ObjectIdentity = ObjectIdentity
rlSNMPDomains = _RlSNMPDomains_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 98, 2)
)
_RlSnmpUDPMridDomain_ObjectIdentity = ObjectIdentity
rlSnmpUDPMridDomain = _RlSnmpUDPMridDomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 98, 2, 1)
)
if mibBuilder.loadTexts:
    rlSnmpUDPMridDomain.setStatus("current")
_RlSnmpUdpIpv6MridDomain_ObjectIdentity = ObjectIdentity
rlSnmpUdpIpv6MridDomain = _RlSnmpUdpIpv6MridDomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 98, 2, 2)
)
if mibBuilder.loadTexts:
    rlSnmpUdpIpv6MridDomain.setStatus("current")
_RlSnmpUdpIpv6zMridDomain_ObjectIdentity = ObjectIdentity
rlSnmpUdpIpv6zMridDomain = _RlSnmpUdpIpv6zMridDomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 98, 2, 3)
)
if mibBuilder.loadTexts:
    rlSnmpUdpIpv6zMridDomain.setStatus("current")
_RlSnmpRequestMridTable_Object = MibTable
rlSnmpRequestMridTable = _RlSnmpRequestMridTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 3)
)
if mibBuilder.loadTexts:
    rlSnmpRequestMridTable.setStatus("current")
_RlSnmpRequestMridEntry_Object = MibTableRow
rlSnmpRequestMridEntry = _RlSnmpRequestMridEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 3, 1)
)
rlSnmpRequestMridEntry.setIndexNames(
    (0, "RADLAN-SNMP-MIB", "rlSnmpRequestManagedMrid"),
)
if mibBuilder.loadTexts:
    rlSnmpRequestMridEntry.setStatus("current")
_RlSnmpRequestManagedMrid_Type = Integer32
_RlSnmpRequestManagedMrid_Object = MibTableColumn
rlSnmpRequestManagedMrid = _RlSnmpRequestManagedMrid_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 3, 1, 1),
    _RlSnmpRequestManagedMrid_Type()
)
rlSnmpRequestManagedMrid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSnmpRequestManagedMrid.setStatus("current")


class _RlSnmpRequestMridStatus_Type(Integer32):
    """Custom type rlSnmpRequestMridStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enable", 1)
    )


_RlSnmpRequestMridStatus_Type.__name__ = "Integer32"
_RlSnmpRequestMridStatus_Object = MibTableColumn
rlSnmpRequestMridStatus = _RlSnmpRequestMridStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 3, 1, 2),
    _RlSnmpRequestMridStatus_Type()
)
rlSnmpRequestMridStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSnmpRequestMridStatus.setStatus("current")


class _RlSNMPenable_Type(Integer32):
    """Custom type rlSNMPenable based on Integer32"""
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


_RlSNMPenable_Type.__name__ = "Integer32"
_RlSNMPenable_Object = MibScalar
rlSNMPenable = _RlSNMPenable_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 4),
    _RlSNMPenable_Type()
)
rlSNMPenable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSNMPenable.setStatus("current")
_RndCommunityInetTable_Object = MibTable
rndCommunityInetTable = _RndCommunityInetTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 5)
)
if mibBuilder.loadTexts:
    rndCommunityInetTable.setStatus("current")
_RndCommunityInetEntry_Object = MibTableRow
rndCommunityInetEntry = _RndCommunityInetEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 5, 1)
)
rndCommunityInetEntry.setIndexNames(
    (0, "RADLAN-SNMP-MIB", "rndCommunityInetMngStationAddrType"),
    (0, "RADLAN-SNMP-MIB", "rndCommunityInetMngStationAddr"),
    (1, "RADLAN-SNMP-MIB", "rndCommunityInetString"),
)
if mibBuilder.loadTexts:
    rndCommunityInetEntry.setStatus("current")
_RndCommunityInetMngStationAddrType_Type = InetAddressType
_RndCommunityInetMngStationAddrType_Object = MibTableColumn
rndCommunityInetMngStationAddrType = _RndCommunityInetMngStationAddrType_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 5, 1, 1),
    _RndCommunityInetMngStationAddrType_Type()
)
rndCommunityInetMngStationAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rndCommunityInetMngStationAddrType.setStatus("current")
_RndCommunityInetMngStationAddr_Type = InetAddress
_RndCommunityInetMngStationAddr_Object = MibTableColumn
rndCommunityInetMngStationAddr = _RndCommunityInetMngStationAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 5, 1, 2),
    _RndCommunityInetMngStationAddr_Type()
)
rndCommunityInetMngStationAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rndCommunityInetMngStationAddr.setStatus("current")


class _RndCommunityInetString_Type(DisplayString):
    """Custom type rndCommunityInetString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_RndCommunityInetString_Type.__name__ = "DisplayString"
_RndCommunityInetString_Object = MibTableColumn
rndCommunityInetString = _RndCommunityInetString_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 5, 1, 3),
    _RndCommunityInetString_Type()
)
rndCommunityInetString.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rndCommunityInetString.setStatus("current")


class _RndCommunityInetAccess_Type(Integer32):
    """Custom type rndCommunityInetAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("readOnly", 1),
          ("readWrite", 2),
          ("super", 3))
    )


_RndCommunityInetAccess_Type.__name__ = "Integer32"
_RndCommunityInetAccess_Object = MibTableColumn
rndCommunityInetAccess = _RndCommunityInetAccess_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 5, 1, 4),
    _RndCommunityInetAccess_Type()
)
rndCommunityInetAccess.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rndCommunityInetAccess.setStatus("current")


class _RndCommunityInetTrapsEnable_Type(Integer32):
    """Custom type rndCommunityInetTrapsEnable based on Integer32"""
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
        *(("snmpV1", 1),
          ("snmpV2", 2),
          ("snmpV3", 3),
          ("trapsDisable", 4))
    )


_RndCommunityInetTrapsEnable_Type.__name__ = "Integer32"
_RndCommunityInetTrapsEnable_Object = MibTableColumn
rndCommunityInetTrapsEnable = _RndCommunityInetTrapsEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 5, 1, 5),
    _RndCommunityInetTrapsEnable_Type()
)
rndCommunityInetTrapsEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rndCommunityInetTrapsEnable.setStatus("current")


class _RndCommunityInetStatus_Type(Integer32):
    """Custom type rndCommunityInetStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("invalid", 2))
    )


_RndCommunityInetStatus_Type.__name__ = "Integer32"
_RndCommunityInetStatus_Object = MibTableColumn
rndCommunityInetStatus = _RndCommunityInetStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 5, 1, 6),
    _RndCommunityInetStatus_Type()
)
rndCommunityInetStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rndCommunityInetStatus.setStatus("current")


class _RndCommunityInetPortSecurity_Type(Integer32):
    """Custom type rndCommunityInetPortSecurity based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_RndCommunityInetPortSecurity_Type.__name__ = "Integer32"
_RndCommunityInetPortSecurity_Object = MibTableColumn
rndCommunityInetPortSecurity = _RndCommunityInetPortSecurity_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 5, 1, 7),
    _RndCommunityInetPortSecurity_Type()
)
rndCommunityInetPortSecurity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rndCommunityInetPortSecurity.setStatus("current")


class _RndCommunityInetOwner_Type(DisplayString):
    """Custom type rndCommunityInetOwner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RndCommunityInetOwner_Type.__name__ = "DisplayString"
_RndCommunityInetOwner_Object = MibTableColumn
rndCommunityInetOwner = _RndCommunityInetOwner_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 5, 1, 8),
    _RndCommunityInetOwner_Type()
)
rndCommunityInetOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rndCommunityInetOwner.setStatus("current")


class _RndCommunityInetTrapDestPort_Type(Integer32):
    """Custom type rndCommunityInetTrapDestPort based on Integer32"""
    defaultValue = 162

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RndCommunityInetTrapDestPort_Type.__name__ = "Integer32"
_RndCommunityInetTrapDestPort_Object = MibTableColumn
rndCommunityInetTrapDestPort = _RndCommunityInetTrapDestPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 5, 1, 9),
    _RndCommunityInetTrapDestPort_Type()
)
rndCommunityInetTrapDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rndCommunityInetTrapDestPort.setStatus("current")
_RndCommunityInetAltAddrType_Type = InetAddressType
_RndCommunityInetAltAddrType_Object = MibTableColumn
rndCommunityInetAltAddrType = _RndCommunityInetAltAddrType_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 5, 1, 10),
    _RndCommunityInetAltAddrType_Type()
)
rndCommunityInetAltAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rndCommunityInetAltAddrType.setStatus("current")
_RndCommunityInetAltAddr_Type = InetAddress
_RndCommunityInetAltAddr_Object = MibTableColumn
rndCommunityInetAltAddr = _RndCommunityInetAltAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 5, 1, 11),
    _RndCommunityInetAltAddr_Type()
)
rndCommunityInetAltAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rndCommunityInetAltAddr.setStatus("current")
_RlMridInetTable_Object = MibTable
rlMridInetTable = _RlMridInetTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 6)
)
if mibBuilder.loadTexts:
    rlMridInetTable.setStatus("current")
_RlMridInetEntry_Object = MibTableRow
rlMridInetEntry = _RlMridInetEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 6, 1)
)
rlMridInetEntry.setIndexNames(
    (0, "RADLAN-SNMP-MIB", "rndCommunityInetMngStationAddrType"),
    (0, "RADLAN-SNMP-MIB", "rndCommunityInetMngStationAddr"),
    (1, "RADLAN-SNMP-MIB", "rndCommunityInetString"),
)
if mibBuilder.loadTexts:
    rlMridInetEntry.setStatus("current")
_RlMridInetConnection_Type = Integer32
_RlMridInetConnection_Object = MibTableColumn
rlMridInetConnection = _RlMridInetConnection_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 6, 1, 1),
    _RlMridInetConnection_Type()
)
rlMridInetConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMridInetConnection.setStatus("current")
_RlInetManagedMrid_Type = Integer32
_RlInetManagedMrid_Object = MibTableColumn
rlInetManagedMrid = _RlInetManagedMrid_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 6, 1, 2),
    _RlInetManagedMrid_Type()
)
rlInetManagedMrid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlInetManagedMrid.setStatus("current")
_RlEvents_ObjectIdentity = ObjectIdentity
rlEvents = _RlEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 98, 7)
)
_RlEventsPollerId_Type = Integer32
_RlEventsPollerId_Object = MibScalar
rlEventsPollerId = _RlEventsPollerId_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 7, 1),
    _RlEventsPollerId_Type()
)
rlEventsPollerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlEventsPollerId.setStatus("current")


class _RlEventsDefaultPollingInterval_Type(TimeTicks):
    """Custom type rlEventsDefaultPollingInterval based on TimeTicks"""
    subtypeSpec = TimeTicks.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RlEventsDefaultPollingInterval_Type.__name__ = "TimeTicks"
_RlEventsDefaultPollingInterval_Object = MibScalar
rlEventsDefaultPollingInterval = _RlEventsDefaultPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 7, 2),
    _RlEventsDefaultPollingInterval_Type()
)
rlEventsDefaultPollingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlEventsDefaultPollingInterval.setStatus("current")
_RlEventsDeleteEvents_Type = Integer32
_RlEventsDeleteEvents_Object = MibScalar
rlEventsDeleteEvents = _RlEventsDeleteEvents_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 7, 3),
    _RlEventsDeleteEvents_Type()
)
rlEventsDeleteEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlEventsDeleteEvents.setStatus("current")
_RlEventsMaskTable_Object = MibTable
rlEventsMaskTable = _RlEventsMaskTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 7, 4)
)
if mibBuilder.loadTexts:
    rlEventsMaskTable.setStatus("current")
_RlEventsMaskEntry_Object = MibTableRow
rlEventsMaskEntry = _RlEventsMaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 7, 4, 1)
)
rlEventsMaskEntry.setIndexNames(
    (0, "RADLAN-SNMP-MIB", "rlEventsMaskPollerId"),
)
if mibBuilder.loadTexts:
    rlEventsMaskEntry.setStatus("current")
_RlEventsMaskPollerId_Type = Integer32
_RlEventsMaskPollerId_Object = MibTableColumn
rlEventsMaskPollerId = _RlEventsMaskPollerId_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 7, 4, 1, 1),
    _RlEventsMaskPollerId_Type()
)
rlEventsMaskPollerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlEventsMaskPollerId.setStatus("current")
_RlEventsMaskMask_Type = OctetString
_RlEventsMaskMask_Object = MibTableColumn
rlEventsMaskMask = _RlEventsMaskMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 7, 4, 1, 2),
    _RlEventsMaskMask_Type()
)
rlEventsMaskMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlEventsMaskMask.setStatus("current")
_RlEventsTable_Object = MibTable
rlEventsTable = _RlEventsTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 7, 5)
)
if mibBuilder.loadTexts:
    rlEventsTable.setStatus("current")
_RlEventsEntry_Object = MibTableRow
rlEventsEntry = _RlEventsEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 7, 5, 1)
)
rlEventsEntry.setIndexNames(
    (0, "RADLAN-SNMP-MIB", "rlEventsPoller"),
    (1, "RADLAN-SNMP-MIB", "rlEventId"),
)
if mibBuilder.loadTexts:
    rlEventsEntry.setStatus("current")
_RlEventsPoller_Type = Integer32
_RlEventsPoller_Object = MibTableColumn
rlEventsPoller = _RlEventsPoller_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 7, 5, 1, 1),
    _RlEventsPoller_Type()
)
rlEventsPoller.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlEventsPoller.setStatus("current")
_RlEventId_Type = ObjectIdentifier
_RlEventId_Object = MibTableColumn
rlEventId = _RlEventId_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 7, 5, 1, 2),
    _RlEventId_Type()
)
rlEventId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlEventId.setStatus("current")
_RlEventIndexInMask_Type = Integer32
_RlEventIndexInMask_Object = MibTableColumn
rlEventIndexInMask = _RlEventIndexInMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 7, 5, 1, 3),
    _RlEventIndexInMask_Type()
)
rlEventIndexInMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlEventIndexInMask.setStatus("current")
_RlEventsStatus_Type = RowStatus
_RlEventsStatus_Object = MibTableColumn
rlEventsStatus = _RlEventsStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 7, 5, 1, 4),
    _RlEventsStatus_Type()
)
rlEventsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlEventsStatus.setStatus("current")
_RlEventsPollingControlTable_Object = MibTable
rlEventsPollingControlTable = _RlEventsPollingControlTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 7, 6)
)
if mibBuilder.loadTexts:
    rlEventsPollingControlTable.setStatus("current")
_RlEventsPollingControlEntry_Object = MibTableRow
rlEventsPollingControlEntry = _RlEventsPollingControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 7, 6, 1)
)
rlEventsPollingControlEntry.setIndexNames(
    (0, "RADLAN-SNMP-MIB", "rlEventsPollingControlPollerId"),
)
if mibBuilder.loadTexts:
    rlEventsPollingControlEntry.setStatus("current")
_RlEventsPollingControlPollerId_Type = Integer32
_RlEventsPollingControlPollerId_Object = MibTableColumn
rlEventsPollingControlPollerId = _RlEventsPollingControlPollerId_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 7, 6, 1, 1),
    _RlEventsPollingControlPollerId_Type()
)
rlEventsPollingControlPollerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlEventsPollingControlPollerId.setStatus("current")


class _RlEventsPollingControlPollingInterval_Type(TimeTicks):
    """Custom type rlEventsPollingControlPollingInterval based on TimeTicks"""
    subtypeSpec = TimeTicks.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RlEventsPollingControlPollingInterval_Type.__name__ = "TimeTicks"
_RlEventsPollingControlPollingInterval_Object = MibTableColumn
rlEventsPollingControlPollingInterval = _RlEventsPollingControlPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 7, 6, 1, 2),
    _RlEventsPollingControlPollingInterval_Type()
)
rlEventsPollingControlPollingInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlEventsPollingControlPollingInterval.setStatus("current")
snmpTargetAddrExtEntry.registerAugmentions(
    ("RADLAN-SNMP-MIB",
     "rlTargetAddrExtEntry")
)
rlTargetAddrExtEntry.setIndexNames(*snmpTargetAddrExtEntry.getIndexNames())
usmUserEntry.registerAugmentions(
    ("RADLAN-SNMP-MIB",
     "rlUsmUserExtEntry")
)
rlUsmUserExtEntry.setIndexNames(*usmUserEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-SNMP-MIB",
    **{"RlSnmpUDPMridAddress": RlSnmpUDPMridAddress,
       "RlSnmpUDPIpv6MridAddress": RlSnmpUDPIpv6MridAddress,
       "RlSnmpUDPIpv6zMridAddress": RlSnmpUDPIpv6zMridAddress,
       "rlSNMP": rlSNMP,
       "rlSNMPv3": rlSNMPv3,
       "rlTargetParamsTestingLevel": rlTargetParamsTestingLevel,
       "rlNotifyFilterTestingLevel": rlNotifyFilterTestingLevel,
       "rlSnmpEngineID": rlSnmpEngineID,
       "rlSNMPv3IpAddrToIndexTable": rlSNMPv3IpAddrToIndexTable,
       "rlSNMPv3IpAddrToIndexEntry": rlSNMPv3IpAddrToIndexEntry,
       "rlSNMPv3IpAddrToIndexAddrType": rlSNMPv3IpAddrToIndexAddrType,
       "rlSNMPv3IpAddrToIndexAddr": rlSNMPv3IpAddrToIndexAddr,
       "rlSNMPv3IpAddrToIndexMappedIndex": rlSNMPv3IpAddrToIndexMappedIndex,
       "rlTargetAddrExtTable": rlTargetAddrExtTable,
       "rlTargetAddrExtEntry": rlTargetAddrExtEntry,
       "rlTargetAddrMagicUsedInIndex": rlTargetAddrMagicUsedInIndex,
       "rlInet2EngineIdTable": rlInet2EngineIdTable,
       "rlInet2EngineIdEntry": rlInet2EngineIdEntry,
       "rlInet2EngineIdAddressType": rlInet2EngineIdAddressType,
       "rlInet2EngineIdAddress": rlInet2EngineIdAddress,
       "rlInet2EngineIdEngineId": rlInet2EngineIdEngineId,
       "rlInet2EngineIdStatus": rlInet2EngineIdStatus,
       "rlUsmUserExtTable": rlUsmUserExtTable,
       "rlUsmUserExtEntry": rlUsmUserExtEntry,
       "rlUsmUserAuthPassword": rlUsmUserAuthPassword,
       "rlUsmUserPrivPassword": rlUsmUserPrivPassword,
       "rlSNMPDomains": rlSNMPDomains,
       "rlSnmpUDPMridDomain": rlSnmpUDPMridDomain,
       "rlSnmpUdpIpv6MridDomain": rlSnmpUdpIpv6MridDomain,
       "rlSnmpUdpIpv6zMridDomain": rlSnmpUdpIpv6zMridDomain,
       "rlSnmpRequestMridTable": rlSnmpRequestMridTable,
       "rlSnmpRequestMridEntry": rlSnmpRequestMridEntry,
       "rlSnmpRequestManagedMrid": rlSnmpRequestManagedMrid,
       "rlSnmpRequestMridStatus": rlSnmpRequestMridStatus,
       "rlSNMPenable": rlSNMPenable,
       "rndCommunityInetTable": rndCommunityInetTable,
       "rndCommunityInetEntry": rndCommunityInetEntry,
       "rndCommunityInetMngStationAddrType": rndCommunityInetMngStationAddrType,
       "rndCommunityInetMngStationAddr": rndCommunityInetMngStationAddr,
       "rndCommunityInetString": rndCommunityInetString,
       "rndCommunityInetAccess": rndCommunityInetAccess,
       "rndCommunityInetTrapsEnable": rndCommunityInetTrapsEnable,
       "rndCommunityInetStatus": rndCommunityInetStatus,
       "rndCommunityInetPortSecurity": rndCommunityInetPortSecurity,
       "rndCommunityInetOwner": rndCommunityInetOwner,
       "rndCommunityInetTrapDestPort": rndCommunityInetTrapDestPort,
       "rndCommunityInetAltAddrType": rndCommunityInetAltAddrType,
       "rndCommunityInetAltAddr": rndCommunityInetAltAddr,
       "rlMridInetTable": rlMridInetTable,
       "rlMridInetEntry": rlMridInetEntry,
       "rlMridInetConnection": rlMridInetConnection,
       "rlInetManagedMrid": rlInetManagedMrid,
       "rlEvents": rlEvents,
       "rlEventsPollerId": rlEventsPollerId,
       "rlEventsDefaultPollingInterval": rlEventsDefaultPollingInterval,
       "rlEventsDeleteEvents": rlEventsDeleteEvents,
       "rlEventsMaskTable": rlEventsMaskTable,
       "rlEventsMaskEntry": rlEventsMaskEntry,
       "rlEventsMaskPollerId": rlEventsMaskPollerId,
       "rlEventsMaskMask": rlEventsMaskMask,
       "rlEventsTable": rlEventsTable,
       "rlEventsEntry": rlEventsEntry,
       "rlEventsPoller": rlEventsPoller,
       "rlEventId": rlEventId,
       "rlEventIndexInMask": rlEventIndexInMask,
       "rlEventsStatus": rlEventsStatus,
       "rlEventsPollingControlTable": rlEventsPollingControlTable,
       "rlEventsPollingControlEntry": rlEventsPollingControlEntry,
       "rlEventsPollingControlPollerId": rlEventsPollingControlPollerId,
       "rlEventsPollingControlPollingInterval": rlEventsPollingControlPollingInterval}
)
