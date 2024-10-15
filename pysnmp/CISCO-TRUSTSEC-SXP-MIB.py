# SNMP MIB module (CISCO-TRUSTSEC-SXP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-TRUSTSEC-SXP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:09:54 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoVrfName,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoVrfName")

(CtsPassword,
 CtsPasswordEncryptionType,
 CtsSecurityGroupTag) = mibBuilder.importSymbols(
    "CISCO-TRUSTSEC-TC-MIB",
    "CtsPassword",
    "CtsPasswordEncryptionType",
    "CtsSecurityGroupTag")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

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
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoTrustSecSxpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 720)
)
ciscoTrustSecSxpMIB.setRevisions(
        ("2012-04-17 00:00",
         "2010-11-24 00:00",
         "2010-02-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoTrustSecSxpMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoTrustSecSxpMIBNotifs = _CiscoTrustSecSxpMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 0)
)
_CiscoTrustSecSxpMIBObjects_ObjectIdentity = ObjectIdentity
ciscoTrustSecSxpMIBObjects = _CiscoTrustSecSxpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1)
)
_CtsxSxpGlobalObjects_ObjectIdentity = ObjectIdentity
ctsxSxpGlobalObjects = _CtsxSxpGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 1)
)
_CtsxSxpEnable_Type = TruthValue
_CtsxSxpEnable_Object = MibScalar
ctsxSxpEnable = _CtsxSxpEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 1, 1),
    _CtsxSxpEnable_Type()
)
ctsxSxpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsxSxpEnable.setStatus("current")
_CtsxSxpConfigDefaultPasswordType_Type = CtsPasswordEncryptionType
_CtsxSxpConfigDefaultPasswordType_Object = MibScalar
ctsxSxpConfigDefaultPasswordType = _CtsxSxpConfigDefaultPasswordType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 1, 2),
    _CtsxSxpConfigDefaultPasswordType_Type()
)
ctsxSxpConfigDefaultPasswordType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsxSxpConfigDefaultPasswordType.setStatus("current")
_CtsxSxpConfigDefaultPassword_Type = CtsPassword
_CtsxSxpConfigDefaultPassword_Object = MibScalar
ctsxSxpConfigDefaultPassword = _CtsxSxpConfigDefaultPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 1, 3),
    _CtsxSxpConfigDefaultPassword_Type()
)
ctsxSxpConfigDefaultPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsxSxpConfigDefaultPassword.setStatus("current")
_CtsxSxpViewDefaultPasswordType_Type = CtsPasswordEncryptionType
_CtsxSxpViewDefaultPasswordType_Object = MibScalar
ctsxSxpViewDefaultPasswordType = _CtsxSxpViewDefaultPasswordType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 1, 4),
    _CtsxSxpViewDefaultPasswordType_Type()
)
ctsxSxpViewDefaultPasswordType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsxSxpViewDefaultPasswordType.setStatus("current")
_CtsxSxpViewDefaultPassword_Type = CtsPassword
_CtsxSxpViewDefaultPassword_Object = MibScalar
ctsxSxpViewDefaultPassword = _CtsxSxpViewDefaultPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 1, 5),
    _CtsxSxpViewDefaultPassword_Type()
)
ctsxSxpViewDefaultPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsxSxpViewDefaultPassword.setStatus("current")
_CtsxSxpDefaultSourceAddrType_Type = InetAddressType
_CtsxSxpDefaultSourceAddrType_Object = MibScalar
ctsxSxpDefaultSourceAddrType = _CtsxSxpDefaultSourceAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 1, 6),
    _CtsxSxpDefaultSourceAddrType_Type()
)
ctsxSxpDefaultSourceAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsxSxpDefaultSourceAddrType.setStatus("current")
_CtsxSxpDefaultSourceAddr_Type = InetAddress
_CtsxSxpDefaultSourceAddr_Object = MibScalar
ctsxSxpDefaultSourceAddr = _CtsxSxpDefaultSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 1, 7),
    _CtsxSxpDefaultSourceAddr_Type()
)
ctsxSxpDefaultSourceAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsxSxpDefaultSourceAddr.setStatus("current")
_CtsxSxpRetryPeriod_Type = Unsigned32
_CtsxSxpRetryPeriod_Object = MibScalar
ctsxSxpRetryPeriod = _CtsxSxpRetryPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 1, 8),
    _CtsxSxpRetryPeriod_Type()
)
ctsxSxpRetryPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsxSxpRetryPeriod.setStatus("current")
if mibBuilder.loadTexts:
    ctsxSxpRetryPeriod.setUnits("seconds")
_CtsxSxpReconPeriod_Type = Unsigned32
_CtsxSxpReconPeriod_Object = MibScalar
ctsxSxpReconPeriod = _CtsxSxpReconPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 1, 9),
    _CtsxSxpReconPeriod_Type()
)
ctsxSxpReconPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsxSxpReconPeriod.setStatus("current")
if mibBuilder.loadTexts:
    ctsxSxpReconPeriod.setUnits("seconds")
_CtsxSxpBindingChangesLogEnable_Type = TruthValue
_CtsxSxpBindingChangesLogEnable_Object = MibScalar
ctsxSxpBindingChangesLogEnable = _CtsxSxpBindingChangesLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 1, 10),
    _CtsxSxpBindingChangesLogEnable_Type()
)
ctsxSxpBindingChangesLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsxSxpBindingChangesLogEnable.setStatus("current")
_CtsxSgtMapExpansionLimit_Type = Gauge32
_CtsxSgtMapExpansionLimit_Object = MibScalar
ctsxSgtMapExpansionLimit = _CtsxSgtMapExpansionLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 1, 11),
    _CtsxSgtMapExpansionLimit_Type()
)
ctsxSgtMapExpansionLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsxSgtMapExpansionLimit.setStatus("current")
_CtsxSgtMapExpansionCount_Type = Gauge32
_CtsxSgtMapExpansionCount_Object = MibScalar
ctsxSgtMapExpansionCount = _CtsxSgtMapExpansionCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 1, 12),
    _CtsxSgtMapExpansionCount_Type()
)
ctsxSgtMapExpansionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsxSgtMapExpansionCount.setStatus("current")
_CtsxSxpAdminNodeId_Type = Unsigned32
_CtsxSxpAdminNodeId_Object = MibScalar
ctsxSxpAdminNodeId = _CtsxSxpAdminNodeId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 1, 13),
    _CtsxSxpAdminNodeId_Type()
)
ctsxSxpAdminNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsxSxpAdminNodeId.setStatus("current")
_CtsxSxpNodeIdInterface_Type = InterfaceIndexOrZero
_CtsxSxpNodeIdInterface_Object = MibScalar
ctsxSxpNodeIdInterface = _CtsxSxpNodeIdInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 1, 14),
    _CtsxSxpNodeIdInterface_Type()
)
ctsxSxpNodeIdInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsxSxpNodeIdInterface.setStatus("current")
_CtsxSxpNodeIdIpAddrType_Type = InetAddressType
_CtsxSxpNodeIdIpAddrType_Object = MibScalar
ctsxSxpNodeIdIpAddrType = _CtsxSxpNodeIdIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 1, 15),
    _CtsxSxpNodeIdIpAddrType_Type()
)
ctsxSxpNodeIdIpAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsxSxpNodeIdIpAddrType.setStatus("current")
_CtsxSxpNodeIdIpAddr_Type = InetAddress
_CtsxSxpNodeIdIpAddr_Object = MibScalar
ctsxSxpNodeIdIpAddr = _CtsxSxpNodeIdIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 1, 16),
    _CtsxSxpNodeIdIpAddr_Type()
)
ctsxSxpNodeIdIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsxSxpNodeIdIpAddr.setStatus("current")
_CtsxSxpOperNodeId_Type = Unsigned32
_CtsxSxpOperNodeId_Object = MibScalar
ctsxSxpOperNodeId = _CtsxSxpOperNodeId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 1, 17),
    _CtsxSxpOperNodeId_Type()
)
ctsxSxpOperNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsxSxpOperNodeId.setStatus("current")


class _CtsxSxpSpeakerMinHoldTime_Type(Unsigned32):
    """Custom type ctsxSxpSpeakerMinHoldTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_CtsxSxpSpeakerMinHoldTime_Type.__name__ = "Unsigned32"
_CtsxSxpSpeakerMinHoldTime_Object = MibScalar
ctsxSxpSpeakerMinHoldTime = _CtsxSxpSpeakerMinHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 1, 18),
    _CtsxSxpSpeakerMinHoldTime_Type()
)
ctsxSxpSpeakerMinHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsxSxpSpeakerMinHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    ctsxSxpSpeakerMinHoldTime.setUnits("seconds")


class _CtsxSxpListenerMinHoldTime_Type(Unsigned32):
    """Custom type ctsxSxpListenerMinHoldTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_CtsxSxpListenerMinHoldTime_Type.__name__ = "Unsigned32"
_CtsxSxpListenerMinHoldTime_Object = MibScalar
ctsxSxpListenerMinHoldTime = _CtsxSxpListenerMinHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 1, 19),
    _CtsxSxpListenerMinHoldTime_Type()
)
ctsxSxpListenerMinHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsxSxpListenerMinHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    ctsxSxpListenerMinHoldTime.setUnits("seconds")


class _CtsxSxpListenerMaxHoldTime_Type(Unsigned32):
    """Custom type ctsxSxpListenerMaxHoldTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_CtsxSxpListenerMaxHoldTime_Type.__name__ = "Unsigned32"
_CtsxSxpListenerMaxHoldTime_Object = MibScalar
ctsxSxpListenerMaxHoldTime = _CtsxSxpListenerMaxHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 1, 20),
    _CtsxSxpListenerMaxHoldTime_Type()
)
ctsxSxpListenerMaxHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsxSxpListenerMaxHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    ctsxSxpListenerMaxHoldTime.setUnits("seconds")


class _CtsxSxpVersionSupport_Type(Integer32):
    """Custom type ctsxSxpVersionSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("four", 5),
          ("one", 2),
          ("three", 4),
          ("two", 3),
          ("unknown", 1))
    )


_CtsxSxpVersionSupport_Type.__name__ = "Integer32"
_CtsxSxpVersionSupport_Object = MibScalar
ctsxSxpVersionSupport = _CtsxSxpVersionSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 1, 21),
    _CtsxSxpVersionSupport_Type()
)
ctsxSxpVersionSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsxSxpVersionSupport.setStatus("current")
_CtsxSxpConnectionObjects_ObjectIdentity = ObjectIdentity
ctsxSxpConnectionObjects = _CtsxSxpConnectionObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 2)
)
_CtsxSxpConnectionTable_Object = MibTable
ctsxSxpConnectionTable = _CtsxSxpConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ctsxSxpConnectionTable.setStatus("current")
_CtsxSxpConnectionEntry_Object = MibTableRow
ctsxSxpConnectionEntry = _CtsxSxpConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 2, 1, 1)
)
ctsxSxpConnectionEntry.setIndexNames(
    (0, "CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpConnVrfName"),
    (0, "CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpConnPeerAddrType"),
    (0, "CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpConnPeerAddr"),
)
if mibBuilder.loadTexts:
    ctsxSxpConnectionEntry.setStatus("current")
_CtsxSxpConnVrfName_Type = CiscoVrfName
_CtsxSxpConnVrfName_Object = MibTableColumn
ctsxSxpConnVrfName = _CtsxSxpConnVrfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 2, 1, 1, 1),
    _CtsxSxpConnVrfName_Type()
)
ctsxSxpConnVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctsxSxpConnVrfName.setStatus("current")
_CtsxSxpConnPeerAddrType_Type = InetAddressType
_CtsxSxpConnPeerAddrType_Object = MibTableColumn
ctsxSxpConnPeerAddrType = _CtsxSxpConnPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 2, 1, 1, 2),
    _CtsxSxpConnPeerAddrType_Type()
)
ctsxSxpConnPeerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctsxSxpConnPeerAddrType.setStatus("current")


class _CtsxSxpConnPeerAddr_Type(InetAddress):
    """Custom type ctsxSxpConnPeerAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CtsxSxpConnPeerAddr_Type.__name__ = "InetAddress"
_CtsxSxpConnPeerAddr_Object = MibTableColumn
ctsxSxpConnPeerAddr = _CtsxSxpConnPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 2, 1, 1, 3),
    _CtsxSxpConnPeerAddr_Type()
)
ctsxSxpConnPeerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctsxSxpConnPeerAddr.setStatus("current")


class _CtsxSxpConnSourceAddrType_Type(InetAddressType):
    """Custom type ctsxSxpConnSourceAddrType based on InetAddressType"""


_CtsxSxpConnSourceAddrType_Object = MibTableColumn
ctsxSxpConnSourceAddrType = _CtsxSxpConnSourceAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 2, 1, 1, 4),
    _CtsxSxpConnSourceAddrType_Type()
)
ctsxSxpConnSourceAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctsxSxpConnSourceAddrType.setStatus("current")
_CtsxSxpConnSourceAddr_Type = InetAddress
_CtsxSxpConnSourceAddr_Object = MibTableColumn
ctsxSxpConnSourceAddr = _CtsxSxpConnSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 2, 1, 1, 5),
    _CtsxSxpConnSourceAddr_Type()
)
ctsxSxpConnSourceAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctsxSxpConnSourceAddr.setStatus("current")
_CtsxSxpConnOperSourceAddrType_Type = InetAddressType
_CtsxSxpConnOperSourceAddrType_Object = MibTableColumn
ctsxSxpConnOperSourceAddrType = _CtsxSxpConnOperSourceAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 2, 1, 1, 6),
    _CtsxSxpConnOperSourceAddrType_Type()
)
ctsxSxpConnOperSourceAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsxSxpConnOperSourceAddrType.setStatus("current")
_CtsxSxpConnOperSourceAddr_Type = InetAddress
_CtsxSxpConnOperSourceAddr_Object = MibTableColumn
ctsxSxpConnOperSourceAddr = _CtsxSxpConnOperSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 2, 1, 1, 7),
    _CtsxSxpConnOperSourceAddr_Type()
)
ctsxSxpConnOperSourceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsxSxpConnOperSourceAddr.setStatus("current")


class _CtsxSxpConnPasswordUsed_Type(Integer32):
    """Custom type ctsxSxpConnPasswordUsed based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("connectionSpecific", 3),
          ("default", 2),
          ("none", 1))
    )


_CtsxSxpConnPasswordUsed_Type.__name__ = "Integer32"
_CtsxSxpConnPasswordUsed_Object = MibTableColumn
ctsxSxpConnPasswordUsed = _CtsxSxpConnPasswordUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 2, 1, 1, 8),
    _CtsxSxpConnPasswordUsed_Type()
)
ctsxSxpConnPasswordUsed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctsxSxpConnPasswordUsed.setStatus("current")


class _CtsxSxpConnConfigPasswordType_Type(CtsPasswordEncryptionType):
    """Custom type ctsxSxpConnConfigPasswordType based on CtsPasswordEncryptionType"""


_CtsxSxpConnConfigPasswordType_Object = MibTableColumn
ctsxSxpConnConfigPasswordType = _CtsxSxpConnConfigPasswordType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 2, 1, 1, 9),
    _CtsxSxpConnConfigPasswordType_Type()
)
ctsxSxpConnConfigPasswordType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctsxSxpConnConfigPasswordType.setStatus("current")
_CtsxSxpConnConfigPassword_Type = CtsPassword
_CtsxSxpConnConfigPassword_Object = MibTableColumn
ctsxSxpConnConfigPassword = _CtsxSxpConnConfigPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 2, 1, 1, 10),
    _CtsxSxpConnConfigPassword_Type()
)
ctsxSxpConnConfigPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctsxSxpConnConfigPassword.setStatus("current")
_CtsxSxpConnViewPasswordType_Type = CtsPasswordEncryptionType
_CtsxSxpConnViewPasswordType_Object = MibTableColumn
ctsxSxpConnViewPasswordType = _CtsxSxpConnViewPasswordType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 2, 1, 1, 11),
    _CtsxSxpConnViewPasswordType_Type()
)
ctsxSxpConnViewPasswordType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsxSxpConnViewPasswordType.setStatus("current")
_CtsxSxpConnViewPassword_Type = CtsPassword
_CtsxSxpConnViewPassword_Object = MibTableColumn
ctsxSxpConnViewPassword = _CtsxSxpConnViewPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 2, 1, 1, 12),
    _CtsxSxpConnViewPassword_Type()
)
ctsxSxpConnViewPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsxSxpConnViewPassword.setStatus("current")


class _CtsxSxpConnModeLocation_Type(Integer32):
    """Custom type ctsxSxpConnModeLocation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("peer", 2))
    )


_CtsxSxpConnModeLocation_Type.__name__ = "Integer32"
_CtsxSxpConnModeLocation_Object = MibTableColumn
ctsxSxpConnModeLocation = _CtsxSxpConnModeLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 2, 1, 1, 13),
    _CtsxSxpConnModeLocation_Type()
)
ctsxSxpConnModeLocation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctsxSxpConnModeLocation.setStatus("current")


class _CtsxSxpConnMode_Type(Integer32):
    """Custom type ctsxSxpConnMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("listener", 2),
          ("speaker", 1))
    )


_CtsxSxpConnMode_Type.__name__ = "Integer32"
_CtsxSxpConnMode_Object = MibTableColumn
ctsxSxpConnMode = _CtsxSxpConnMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 2, 1, 1, 14),
    _CtsxSxpConnMode_Type()
)
ctsxSxpConnMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctsxSxpConnMode.setStatus("current")
_CtsxSxpConnInstance_Type = Unsigned32
_CtsxSxpConnInstance_Object = MibTableColumn
ctsxSxpConnInstance = _CtsxSxpConnInstance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 2, 1, 1, 15),
    _CtsxSxpConnInstance_Type()
)
ctsxSxpConnInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsxSxpConnInstance.setStatus("current")
_CtsxSxpConnStatusLastChange_Type = Unsigned32
_CtsxSxpConnStatusLastChange_Object = MibTableColumn
ctsxSxpConnStatusLastChange = _CtsxSxpConnStatusLastChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 2, 1, 1, 16),
    _CtsxSxpConnStatusLastChange_Type()
)
ctsxSxpConnStatusLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsxSxpConnStatusLastChange.setStatus("current")
if mibBuilder.loadTexts:
    ctsxSxpConnStatusLastChange.setUnits("seconds")


class _CtsxSxpConnStatus_Type(Integer32):
    """Custom type ctsxSxpConnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("deleteHoldDown", 5),
          ("off", 2),
          ("on", 3),
          ("other", 1),
          ("pendingOn", 4))
    )


_CtsxSxpConnStatus_Type.__name__ = "Integer32"
_CtsxSxpConnStatus_Object = MibTableColumn
ctsxSxpConnStatus = _CtsxSxpConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 2, 1, 1, 17),
    _CtsxSxpConnStatus_Type()
)
ctsxSxpConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsxSxpConnStatus.setStatus("current")
_CtsxSxpVrfId_Type = Unsigned32
_CtsxSxpVrfId_Object = MibTableColumn
ctsxSxpVrfId = _CtsxSxpVrfId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 2, 1, 1, 18),
    _CtsxSxpVrfId_Type()
)
ctsxSxpVrfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsxSxpVrfId.setStatus("current")


class _CtsxSxpConnStorageType_Type(StorageType):
    """Custom type ctsxSxpConnStorageType based on StorageType"""


_CtsxSxpConnStorageType_Object = MibTableColumn
ctsxSxpConnStorageType = _CtsxSxpConnStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 2, 1, 1, 19),
    _CtsxSxpConnStorageType_Type()
)
ctsxSxpConnStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctsxSxpConnStorageType.setStatus("current")
_CtsxSxpConnRowStatus_Type = RowStatus
_CtsxSxpConnRowStatus_Object = MibTableColumn
ctsxSxpConnRowStatus = _CtsxSxpConnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 2, 1, 1, 20),
    _CtsxSxpConnRowStatus_Type()
)
ctsxSxpConnRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctsxSxpConnRowStatus.setStatus("current")


class _CtsxSxpConnVersion_Type(Integer32):
    """Custom type ctsxSxpConnVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("four", 5),
          ("one", 2),
          ("three", 4),
          ("two", 3),
          ("unknown", 1))
    )


_CtsxSxpConnVersion_Type.__name__ = "Integer32"
_CtsxSxpConnVersion_Object = MibTableColumn
ctsxSxpConnVersion = _CtsxSxpConnVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 2, 1, 1, 21),
    _CtsxSxpConnVersion_Type()
)
ctsxSxpConnVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsxSxpConnVersion.setStatus("current")


class _CtsxSxpConnSpeakerMinHoldTime_Type(Unsigned32):
    """Custom type ctsxSxpConnSpeakerMinHoldTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65534),
        ValueRangeConstraint(65535, 65535),
    )


_CtsxSxpConnSpeakerMinHoldTime_Type.__name__ = "Unsigned32"
_CtsxSxpConnSpeakerMinHoldTime_Object = MibTableColumn
ctsxSxpConnSpeakerMinHoldTime = _CtsxSxpConnSpeakerMinHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 2, 1, 1, 22),
    _CtsxSxpConnSpeakerMinHoldTime_Type()
)
ctsxSxpConnSpeakerMinHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctsxSxpConnSpeakerMinHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    ctsxSxpConnSpeakerMinHoldTime.setUnits("seconds")


class _CtsxSxpConnListenerMinHoldTime_Type(Unsigned32):
    """Custom type ctsxSxpConnListenerMinHoldTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65534),
        ValueRangeConstraint(65535, 65535),
    )


_CtsxSxpConnListenerMinHoldTime_Type.__name__ = "Unsigned32"
_CtsxSxpConnListenerMinHoldTime_Object = MibTableColumn
ctsxSxpConnListenerMinHoldTime = _CtsxSxpConnListenerMinHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 2, 1, 1, 23),
    _CtsxSxpConnListenerMinHoldTime_Type()
)
ctsxSxpConnListenerMinHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctsxSxpConnListenerMinHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    ctsxSxpConnListenerMinHoldTime.setUnits("seconds")


class _CtsxSxpConnListenerMaxHoldTime_Type(Unsigned32):
    """Custom type ctsxSxpConnListenerMaxHoldTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65534),
        ValueRangeConstraint(65535, 65535),
    )


_CtsxSxpConnListenerMaxHoldTime_Type.__name__ = "Unsigned32"
_CtsxSxpConnListenerMaxHoldTime_Object = MibTableColumn
ctsxSxpConnListenerMaxHoldTime = _CtsxSxpConnListenerMaxHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 2, 1, 1, 24),
    _CtsxSxpConnListenerMaxHoldTime_Type()
)
ctsxSxpConnListenerMaxHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctsxSxpConnListenerMaxHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    ctsxSxpConnListenerMaxHoldTime.setUnits("seconds")
_CtsxSxpConnHoldTime_Type = Unsigned32
_CtsxSxpConnHoldTime_Object = MibTableColumn
ctsxSxpConnHoldTime = _CtsxSxpConnHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 2, 1, 1, 25),
    _CtsxSxpConnHoldTime_Type()
)
ctsxSxpConnHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsxSxpConnHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    ctsxSxpConnHoldTime.setUnits("seconds")


class _CtsxSxpConnCapability_Type(Bits):
    """Custom type ctsxSxpConnCapability based on Bits"""
    namedValues = NamedValues(
        *(("ipv4", 0),
          ("ipv6", 1),
          ("subnet", 2))
    )

_CtsxSxpConnCapability_Type.__name__ = "Bits"
_CtsxSxpConnCapability_Object = MibTableColumn
ctsxSxpConnCapability = _CtsxSxpConnCapability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 2, 1, 1, 26),
    _CtsxSxpConnCapability_Type()
)
ctsxSxpConnCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsxSxpConnCapability.setStatus("current")
_CtsxSxpSgtObjects_ObjectIdentity = ObjectIdentity
ctsxSxpSgtObjects = _CtsxSxpSgtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 3)
)
_CtsxIpSgtMappingTable_Object = MibTable
ctsxIpSgtMappingTable = _CtsxIpSgtMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ctsxIpSgtMappingTable.setStatus("current")
_CtsxIpSgtMappingEntry_Object = MibTableRow
ctsxIpSgtMappingEntry = _CtsxIpSgtMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 3, 1, 1)
)
ctsxIpSgtMappingEntry.setIndexNames(
    (0, "CISCO-TRUSTSEC-SXP-MIB", "ctsxIpSgtMappingVrfId"),
    (0, "CISCO-TRUSTSEC-SXP-MIB", "ctsxIpSgtMappingAddrType"),
    (0, "CISCO-TRUSTSEC-SXP-MIB", "ctsxIpSgtMappingAddr"),
    (0, "CISCO-TRUSTSEC-SXP-MIB", "ctsxIpSgtMappingPeerAddrType"),
    (0, "CISCO-TRUSTSEC-SXP-MIB", "ctsxIpSgtMappingPeerAddr"),
)
if mibBuilder.loadTexts:
    ctsxIpSgtMappingEntry.setStatus("current")
_CtsxIpSgtMappingVrfId_Type = Unsigned32
_CtsxIpSgtMappingVrfId_Object = MibTableColumn
ctsxIpSgtMappingVrfId = _CtsxIpSgtMappingVrfId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 3, 1, 1, 1),
    _CtsxIpSgtMappingVrfId_Type()
)
ctsxIpSgtMappingVrfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctsxIpSgtMappingVrfId.setStatus("current")
_CtsxIpSgtMappingAddrType_Type = InetAddressType
_CtsxIpSgtMappingAddrType_Object = MibTableColumn
ctsxIpSgtMappingAddrType = _CtsxIpSgtMappingAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 3, 1, 1, 2),
    _CtsxIpSgtMappingAddrType_Type()
)
ctsxIpSgtMappingAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctsxIpSgtMappingAddrType.setStatus("current")


class _CtsxIpSgtMappingAddr_Type(InetAddress):
    """Custom type ctsxIpSgtMappingAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_CtsxIpSgtMappingAddr_Type.__name__ = "InetAddress"
_CtsxIpSgtMappingAddr_Object = MibTableColumn
ctsxIpSgtMappingAddr = _CtsxIpSgtMappingAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 3, 1, 1, 3),
    _CtsxIpSgtMappingAddr_Type()
)
ctsxIpSgtMappingAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctsxIpSgtMappingAddr.setStatus("current")
_CtsxIpSgtMappingPeerAddrType_Type = InetAddressType
_CtsxIpSgtMappingPeerAddrType_Object = MibTableColumn
ctsxIpSgtMappingPeerAddrType = _CtsxIpSgtMappingPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 3, 1, 1, 4),
    _CtsxIpSgtMappingPeerAddrType_Type()
)
ctsxIpSgtMappingPeerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctsxIpSgtMappingPeerAddrType.setStatus("current")


class _CtsxIpSgtMappingPeerAddr_Type(InetAddress):
    """Custom type ctsxIpSgtMappingPeerAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_CtsxIpSgtMappingPeerAddr_Type.__name__ = "InetAddress"
_CtsxIpSgtMappingPeerAddr_Object = MibTableColumn
ctsxIpSgtMappingPeerAddr = _CtsxIpSgtMappingPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 3, 1, 1, 5),
    _CtsxIpSgtMappingPeerAddr_Type()
)
ctsxIpSgtMappingPeerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctsxIpSgtMappingPeerAddr.setStatus("current")
_CtsxIpSgtMappingSgt_Type = CtsSecurityGroupTag
_CtsxIpSgtMappingSgt_Object = MibTableColumn
ctsxIpSgtMappingSgt = _CtsxIpSgtMappingSgt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 3, 1, 1, 6),
    _CtsxIpSgtMappingSgt_Type()
)
ctsxIpSgtMappingSgt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsxIpSgtMappingSgt.setStatus("current")
_CtsxIpSgtMappingInstance_Type = Unsigned32
_CtsxIpSgtMappingInstance_Object = MibTableColumn
ctsxIpSgtMappingInstance = _CtsxIpSgtMappingInstance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 3, 1, 1, 7),
    _CtsxIpSgtMappingInstance_Type()
)
ctsxIpSgtMappingInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsxIpSgtMappingInstance.setStatus("current")
_CtsxIpSgtMappingVrfName_Type = CiscoVrfName
_CtsxIpSgtMappingVrfName_Object = MibTableColumn
ctsxIpSgtMappingVrfName = _CtsxIpSgtMappingVrfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 3, 1, 1, 8),
    _CtsxIpSgtMappingVrfName_Type()
)
ctsxIpSgtMappingVrfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsxIpSgtMappingVrfName.setStatus("current")


class _CtsxIpSgtMappingStatus_Type(Integer32):
    """Custom type ctsxIpSgtMappingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("other", 1))
    )


_CtsxIpSgtMappingStatus_Type.__name__ = "Integer32"
_CtsxIpSgtMappingStatus_Object = MibTableColumn
ctsxIpSgtMappingStatus = _CtsxIpSgtMappingStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 3, 1, 1, 9),
    _CtsxIpSgtMappingStatus_Type()
)
ctsxIpSgtMappingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsxIpSgtMappingStatus.setStatus("current")
_CtsxSxpSgtMapTable_Object = MibTable
ctsxSxpSgtMapTable = _CtsxSxpSgtMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ctsxSxpSgtMapTable.setStatus("current")
_CtsxSxpSgtMapEntry_Object = MibTableRow
ctsxSxpSgtMapEntry = _CtsxSxpSgtMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 3, 2, 1)
)
ctsxSxpSgtMapEntry.setIndexNames(
    (0, "CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpSgtMapVrfId"),
    (0, "CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpSgtMapAddrType"),
    (0, "CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpSgtMapAddr"),
    (0, "CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpSgtMapAddrPrefixLength"),
    (0, "CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpSgtMapPeerAddrType"),
    (0, "CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpSgtMapPeerAddr"),
)
if mibBuilder.loadTexts:
    ctsxSxpSgtMapEntry.setStatus("current")
_CtsxSxpSgtMapVrfId_Type = Unsigned32
_CtsxSxpSgtMapVrfId_Object = MibTableColumn
ctsxSxpSgtMapVrfId = _CtsxSxpSgtMapVrfId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 3, 2, 1, 1),
    _CtsxSxpSgtMapVrfId_Type()
)
ctsxSxpSgtMapVrfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctsxSxpSgtMapVrfId.setStatus("current")
_CtsxSxpSgtMapAddrType_Type = InetAddressType
_CtsxSxpSgtMapAddrType_Object = MibTableColumn
ctsxSxpSgtMapAddrType = _CtsxSxpSgtMapAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 3, 2, 1, 2),
    _CtsxSxpSgtMapAddrType_Type()
)
ctsxSxpSgtMapAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctsxSxpSgtMapAddrType.setStatus("current")


class _CtsxSxpSgtMapAddr_Type(InetAddress):
    """Custom type ctsxSxpSgtMapAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_CtsxSxpSgtMapAddr_Type.__name__ = "InetAddress"
_CtsxSxpSgtMapAddr_Object = MibTableColumn
ctsxSxpSgtMapAddr = _CtsxSxpSgtMapAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 3, 2, 1, 3),
    _CtsxSxpSgtMapAddr_Type()
)
ctsxSxpSgtMapAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctsxSxpSgtMapAddr.setStatus("current")
_CtsxSxpSgtMapAddrPrefixLength_Type = InetAddressPrefixLength
_CtsxSxpSgtMapAddrPrefixLength_Object = MibTableColumn
ctsxSxpSgtMapAddrPrefixLength = _CtsxSxpSgtMapAddrPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 3, 2, 1, 4),
    _CtsxSxpSgtMapAddrPrefixLength_Type()
)
ctsxSxpSgtMapAddrPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctsxSxpSgtMapAddrPrefixLength.setStatus("current")
_CtsxSxpSgtMapPeerAddrType_Type = InetAddressType
_CtsxSxpSgtMapPeerAddrType_Object = MibTableColumn
ctsxSxpSgtMapPeerAddrType = _CtsxSxpSgtMapPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 3, 2, 1, 5),
    _CtsxSxpSgtMapPeerAddrType_Type()
)
ctsxSxpSgtMapPeerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctsxSxpSgtMapPeerAddrType.setStatus("current")


class _CtsxSxpSgtMapPeerAddr_Type(InetAddress):
    """Custom type ctsxSxpSgtMapPeerAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_CtsxSxpSgtMapPeerAddr_Type.__name__ = "InetAddress"
_CtsxSxpSgtMapPeerAddr_Object = MibTableColumn
ctsxSxpSgtMapPeerAddr = _CtsxSxpSgtMapPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 3, 2, 1, 6),
    _CtsxSxpSgtMapPeerAddr_Type()
)
ctsxSxpSgtMapPeerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctsxSxpSgtMapPeerAddr.setStatus("current")
_CtsxSxpSgtMapSgt_Type = CtsSecurityGroupTag
_CtsxSxpSgtMapSgt_Object = MibTableColumn
ctsxSxpSgtMapSgt = _CtsxSxpSgtMapSgt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 3, 2, 1, 7),
    _CtsxSxpSgtMapSgt_Type()
)
ctsxSxpSgtMapSgt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsxSxpSgtMapSgt.setStatus("current")
_CtsxSxpSgtMapInstance_Type = Unsigned32
_CtsxSxpSgtMapInstance_Object = MibTableColumn
ctsxSxpSgtMapInstance = _CtsxSxpSgtMapInstance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 3, 2, 1, 8),
    _CtsxSxpSgtMapInstance_Type()
)
ctsxSxpSgtMapInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsxSxpSgtMapInstance.setStatus("current")
_CtsxSxpSgtMapVrfName_Type = CiscoVrfName
_CtsxSxpSgtMapVrfName_Object = MibTableColumn
ctsxSxpSgtMapVrfName = _CtsxSxpSgtMapVrfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 3, 2, 1, 9),
    _CtsxSxpSgtMapVrfName_Type()
)
ctsxSxpSgtMapVrfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsxSxpSgtMapVrfName.setStatus("current")
_CtsxSxpSgtMapPeerSeq_Type = OctetString
_CtsxSxpSgtMapPeerSeq_Object = MibTableColumn
ctsxSxpSgtMapPeerSeq = _CtsxSxpSgtMapPeerSeq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 3, 2, 1, 10),
    _CtsxSxpSgtMapPeerSeq_Type()
)
ctsxSxpSgtMapPeerSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsxSxpSgtMapPeerSeq.setStatus("current")


class _CtsxSxpSgtMapStatus_Type(Integer32):
    """Custom type ctsxSxpSgtMapStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("other", 1))
    )


_CtsxSxpSgtMapStatus_Type.__name__ = "Integer32"
_CtsxSxpSgtMapStatus_Object = MibTableColumn
ctsxSxpSgtMapStatus = _CtsxSxpSgtMapStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 3, 2, 1, 11),
    _CtsxSxpSgtMapStatus_Type()
)
ctsxSxpSgtMapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsxSxpSgtMapStatus.setStatus("current")
_CiscoTrustSecSxpMIBNotifsControl_ObjectIdentity = ObjectIdentity
ciscoTrustSecSxpMIBNotifsControl = _CiscoTrustSecSxpMIBNotifsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 4)
)
_CtsxSxpConnSourceAddrErrNotifEnable_Type = TruthValue
_CtsxSxpConnSourceAddrErrNotifEnable_Object = MibScalar
ctsxSxpConnSourceAddrErrNotifEnable = _CtsxSxpConnSourceAddrErrNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 4, 1),
    _CtsxSxpConnSourceAddrErrNotifEnable_Type()
)
ctsxSxpConnSourceAddrErrNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsxSxpConnSourceAddrErrNotifEnable.setStatus("current")
_CtsxSxpMsgParseErrNotifEnable_Type = TruthValue
_CtsxSxpMsgParseErrNotifEnable_Object = MibScalar
ctsxSxpMsgParseErrNotifEnable = _CtsxSxpMsgParseErrNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 4, 2),
    _CtsxSxpMsgParseErrNotifEnable_Type()
)
ctsxSxpMsgParseErrNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsxSxpMsgParseErrNotifEnable.setStatus("current")
_CtsxSxpConnConfigErrNotifEnable_Type = TruthValue
_CtsxSxpConnConfigErrNotifEnable_Object = MibScalar
ctsxSxpConnConfigErrNotifEnable = _CtsxSxpConnConfigErrNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 4, 3),
    _CtsxSxpConnConfigErrNotifEnable_Type()
)
ctsxSxpConnConfigErrNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsxSxpConnConfigErrNotifEnable.setStatus("current")
_CtsxSxpBindingErrNotifEnable_Type = TruthValue
_CtsxSxpBindingErrNotifEnable_Object = MibScalar
ctsxSxpBindingErrNotifEnable = _CtsxSxpBindingErrNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 4, 4),
    _CtsxSxpBindingErrNotifEnable_Type()
)
ctsxSxpBindingErrNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsxSxpBindingErrNotifEnable.setStatus("current")
_CtsxSxpConnUpNotifEnable_Type = TruthValue
_CtsxSxpConnUpNotifEnable_Object = MibScalar
ctsxSxpConnUpNotifEnable = _CtsxSxpConnUpNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 4, 5),
    _CtsxSxpConnUpNotifEnable_Type()
)
ctsxSxpConnUpNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsxSxpConnUpNotifEnable.setStatus("current")
_CtsxSxpConnDownNotifEnable_Type = TruthValue
_CtsxSxpConnDownNotifEnable_Object = MibScalar
ctsxSxpConnDownNotifEnable = _CtsxSxpConnDownNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 4, 6),
    _CtsxSxpConnDownNotifEnable_Type()
)
ctsxSxpConnDownNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsxSxpConnDownNotifEnable.setStatus("current")
_CtsxSxpExpansionFailNotifEnable_Type = TruthValue
_CtsxSxpExpansionFailNotifEnable_Object = MibScalar
ctsxSxpExpansionFailNotifEnable = _CtsxSxpExpansionFailNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 4, 7),
    _CtsxSxpExpansionFailNotifEnable_Type()
)
ctsxSxpExpansionFailNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsxSxpExpansionFailNotifEnable.setStatus("current")
_CtsxSxpOperNodeIdChangeNotifEnable_Type = TruthValue
_CtsxSxpOperNodeIdChangeNotifEnable_Object = MibScalar
ctsxSxpOperNodeIdChangeNotifEnable = _CtsxSxpOperNodeIdChangeNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 4, 8),
    _CtsxSxpOperNodeIdChangeNotifEnable_Type()
)
ctsxSxpOperNodeIdChangeNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsxSxpOperNodeIdChangeNotifEnable.setStatus("current")
_CtsxSxpBindingConflictNotifEnable_Type = TruthValue
_CtsxSxpBindingConflictNotifEnable_Object = MibScalar
ctsxSxpBindingConflictNotifEnable = _CtsxSxpBindingConflictNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 4, 9),
    _CtsxSxpBindingConflictNotifEnable_Type()
)
ctsxSxpBindingConflictNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsxSxpBindingConflictNotifEnable.setStatus("current")
_CiscoTrustSecSxpMIBNotifsOnlyInfo_ObjectIdentity = ObjectIdentity
ciscoTrustSecSxpMIBNotifsOnlyInfo = _CiscoTrustSecSxpMIBNotifsOnlyInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 5)
)
_CtsxSgtMapExpansionVrf_Type = CiscoVrfName
_CtsxSgtMapExpansionVrf_Object = MibScalar
ctsxSgtMapExpansionVrf = _CtsxSgtMapExpansionVrf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 5, 1),
    _CtsxSgtMapExpansionVrf_Type()
)
ctsxSgtMapExpansionVrf.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ctsxSgtMapExpansionVrf.setStatus("current")
_CtsxSgtMapExpansionAddrType_Type = InetAddressType
_CtsxSgtMapExpansionAddrType_Object = MibScalar
ctsxSgtMapExpansionAddrType = _CtsxSgtMapExpansionAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 5, 2),
    _CtsxSgtMapExpansionAddrType_Type()
)
ctsxSgtMapExpansionAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ctsxSgtMapExpansionAddrType.setStatus("current")
_CtsxSgtMapExpansionAddr_Type = InetAddress
_CtsxSgtMapExpansionAddr_Object = MibScalar
ctsxSgtMapExpansionAddr = _CtsxSgtMapExpansionAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 5, 3),
    _CtsxSgtMapExpansionAddr_Type()
)
ctsxSgtMapExpansionAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ctsxSgtMapExpansionAddr.setStatus("current")
_CtsxSgtMapExpansionAddrPrefixLength_Type = InetAddressPrefixLength
_CtsxSgtMapExpansionAddrPrefixLength_Object = MibScalar
ctsxSgtMapExpansionAddrPrefixLength = _CtsxSgtMapExpansionAddrPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 5, 4),
    _CtsxSgtMapExpansionAddrPrefixLength_Type()
)
ctsxSgtMapExpansionAddrPrefixLength.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ctsxSgtMapExpansionAddrPrefixLength.setStatus("current")
_CtsxSxpNotifErrMsg_Type = SnmpAdminString
_CtsxSxpNotifErrMsg_Object = MibScalar
ctsxSxpNotifErrMsg = _CtsxSxpNotifErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 5, 5),
    _CtsxSxpNotifErrMsg_Type()
)
ctsxSxpNotifErrMsg.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ctsxSxpNotifErrMsg.setStatus("current")
_CtsxSgtMapConflictingVrfName_Type = CiscoVrfName
_CtsxSgtMapConflictingVrfName_Object = MibScalar
ctsxSgtMapConflictingVrfName = _CtsxSgtMapConflictingVrfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 5, 6),
    _CtsxSgtMapConflictingVrfName_Type()
)
ctsxSgtMapConflictingVrfName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ctsxSgtMapConflictingVrfName.setStatus("current")
_CtsxSgtMapConflictingAddrType_Type = InetAddressType
_CtsxSgtMapConflictingAddrType_Object = MibScalar
ctsxSgtMapConflictingAddrType = _CtsxSgtMapConflictingAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 5, 7),
    _CtsxSgtMapConflictingAddrType_Type()
)
ctsxSgtMapConflictingAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ctsxSgtMapConflictingAddrType.setStatus("current")
_CtsxSgtMapConflictingAddr_Type = InetAddress
_CtsxSgtMapConflictingAddr_Object = MibScalar
ctsxSgtMapConflictingAddr = _CtsxSgtMapConflictingAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 5, 8),
    _CtsxSgtMapConflictingAddr_Type()
)
ctsxSgtMapConflictingAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ctsxSgtMapConflictingAddr.setStatus("current")
_CtsxSgtMapConflictingOldSgt_Type = CtsSecurityGroupTag
_CtsxSgtMapConflictingOldSgt_Object = MibScalar
ctsxSgtMapConflictingOldSgt = _CtsxSgtMapConflictingOldSgt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 5, 9),
    _CtsxSgtMapConflictingOldSgt_Type()
)
ctsxSgtMapConflictingOldSgt.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ctsxSgtMapConflictingOldSgt.setStatus("current")
_CtsxSgtMapConflictingNewSgt_Type = CtsSecurityGroupTag
_CtsxSgtMapConflictingNewSgt_Object = MibScalar
ctsxSgtMapConflictingNewSgt = _CtsxSgtMapConflictingNewSgt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 5, 10),
    _CtsxSgtMapConflictingNewSgt_Type()
)
ctsxSgtMapConflictingNewSgt.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ctsxSgtMapConflictingNewSgt.setStatus("current")
_CtsxSxpOldOperNodeId_Type = Unsigned32
_CtsxSxpOldOperNodeId_Object = MibScalar
ctsxSxpOldOperNodeId = _CtsxSxpOldOperNodeId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 1, 5, 11),
    _CtsxSxpOldOperNodeId_Type()
)
ctsxSxpOldOperNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ctsxSxpOldOperNodeId.setStatus("current")
_CiscoTrustSecSxpMIBConform_ObjectIdentity = ObjectIdentity
ciscoTrustSecSxpMIBConform = _CiscoTrustSecSxpMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 2)
)
_CiscoTrustSecSxpMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoTrustSecSxpMIBCompliances = _CiscoTrustSecSxpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 2, 1)
)
_CiscoTrustSecSxpMIBGroups_ObjectIdentity = ObjectIdentity
ciscoTrustSecSxpMIBGroups = _CiscoTrustSecSxpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 2, 2)
)

# Managed Objects groups

ctsxSxpGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 2, 2, 1)
)
ctsxSxpGlobalGroup.setObjects(
      *(("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpEnable"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpConfigDefaultPasswordType"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpConfigDefaultPassword"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpViewDefaultPasswordType"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpViewDefaultPassword"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpDefaultSourceAddrType"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpDefaultSourceAddr"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpRetryPeriod"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpReconPeriod"))
)
if mibBuilder.loadTexts:
    ctsxSxpGlobalGroup.setStatus("current")

ctsxSxpConnectionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 2, 2, 2)
)
ctsxSxpConnectionGroup.setObjects(
      *(("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpConnSourceAddrType"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpConnSourceAddr"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpConnOperSourceAddrType"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpConnOperSourceAddr"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpConnPasswordUsed"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpConnConfigPasswordType"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpConnConfigPassword"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpConnViewPasswordType"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpConnViewPassword"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpConnModeLocation"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpConnMode"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpConnInstance"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpConnStatusLastChange"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpConnStatus"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpVrfId"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpConnStorageType"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpConnRowStatus"))
)
if mibBuilder.loadTexts:
    ctsxSxpConnectionGroup.setStatus("current")

ctsxIpSgtMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 2, 2, 3)
)
ctsxIpSgtMappingGroup.setObjects(
      *(("CISCO-TRUSTSEC-SXP-MIB", "ctsxIpSgtMappingSgt"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxIpSgtMappingInstance"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxIpSgtMappingVrfName"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxIpSgtMappingStatus"))
)
if mibBuilder.loadTexts:
    ctsxIpSgtMappingGroup.setStatus("current")

ctsxSxpVersionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 2, 2, 4)
)
ctsxSxpVersionGroup.setObjects(
    ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpConnVersion")
)
if mibBuilder.loadTexts:
    ctsxSxpVersionGroup.setStatus("current")

ctsxSxpBindingLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 2, 2, 5)
)
ctsxSxpBindingLogGroup.setObjects(
    ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpBindingChangesLogEnable")
)
if mibBuilder.loadTexts:
    ctsxSxpBindingLogGroup.setStatus("current")

ctsxSxpBindingNotifInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 2, 2, 6)
)
ctsxSxpBindingNotifInfoGroup.setObjects(
      *(("CISCO-TRUSTSEC-SXP-MIB", "ctsxSgtMapExpansionVrf"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSgtMapExpansionAddrType"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSgtMapExpansionAddr"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSgtMapExpansionAddrPrefixLength"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSgtMapConflictingVrfName"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSgtMapConflictingAddrType"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSgtMapConflictingAddr"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSgtMapConflictingOldSgt"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSgtMapConflictingNewSgt"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpOldOperNodeId"))
)
if mibBuilder.loadTexts:
    ctsxSxpBindingNotifInfoGroup.setStatus("current")

ctsxSxpNotifErrMsgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 2, 2, 7)
)
ctsxSxpNotifErrMsgGroup.setObjects(
    ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpNotifErrMsg")
)
if mibBuilder.loadTexts:
    ctsxSxpNotifErrMsgGroup.setStatus("current")

ctsxSxpNodeIdInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 2, 2, 8)
)
ctsxSxpNodeIdInfoGroup.setObjects(
      *(("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpAdminNodeId"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpNodeIdInterface"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpNodeIdIpAddrType"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpNodeIdIpAddr"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpOperNodeId"))
)
if mibBuilder.loadTexts:
    ctsxSxpNodeIdInfoGroup.setStatus("current")

ctsxSxpSgtMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 2, 2, 9)
)
ctsxSxpSgtMapGroup.setObjects(
      *(("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpSgtMapSgt"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpSgtMapInstance"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpSgtMapVrfName"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpSgtMapStatus"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSgtMapExpansionLimit"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSgtMapExpansionCount"))
)
if mibBuilder.loadTexts:
    ctsxSxpSgtMapGroup.setStatus("current")

ctsxNotifsControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 2, 2, 10)
)
ctsxNotifsControlGroup.setObjects(
      *(("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpConnSourceAddrErrNotifEnable"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpMsgParseErrNotifEnable"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpConnConfigErrNotifEnable"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpBindingErrNotifEnable"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpConnUpNotifEnable"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpConnDownNotifEnable"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpExpansionFailNotifEnable"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpOperNodeIdChangeNotifEnable"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpBindingConflictNotifEnable"))
)
if mibBuilder.loadTexts:
    ctsxNotifsControlGroup.setStatus("current")

ctsxSxpGlobalHoldTimeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 2, 2, 12)
)
ctsxSxpGlobalHoldTimeGroup.setObjects(
      *(("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpSpeakerMinHoldTime"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpListenerMinHoldTime"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpListenerMaxHoldTime"))
)
if mibBuilder.loadTexts:
    ctsxSxpGlobalHoldTimeGroup.setStatus("current")

ctsxSxpConnHoldTimeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 2, 2, 13)
)
ctsxSxpConnHoldTimeGroup.setObjects(
      *(("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpConnSpeakerMinHoldTime"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpConnListenerMinHoldTime"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpConnListenerMaxHoldTime"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpConnHoldTime"))
)
if mibBuilder.loadTexts:
    ctsxSxpConnHoldTimeGroup.setStatus("current")

ctsxSxpConnCapbilityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 2, 2, 14)
)
ctsxSxpConnCapbilityGroup.setObjects(
    ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpConnCapability")
)
if mibBuilder.loadTexts:
    ctsxSxpConnCapbilityGroup.setStatus("current")

ctsxSxpVersionSupportGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 2, 2, 15)
)
ctsxSxpVersionSupportGroup.setObjects(
    ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpVersionSupport")
)
if mibBuilder.loadTexts:
    ctsxSxpVersionSupportGroup.setStatus("current")

ctsxSgtMapPeerSeqGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 2, 2, 16)
)
ctsxSgtMapPeerSeqGroup.setObjects(
    ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpSgtMapPeerSeq")
)
if mibBuilder.loadTexts:
    ctsxSgtMapPeerSeqGroup.setStatus("current")


# Notification objects

ctsxSxpConnSourceAddrErrNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 0, 1)
)
ctsxSxpConnSourceAddrErrNotif.setObjects(
      *(("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpConnOperSourceAddrType"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpConnOperSourceAddr"))
)
if mibBuilder.loadTexts:
    ctsxSxpConnSourceAddrErrNotif.setStatus(
        "current"
    )

ctsxSxpMsgParseErrNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 0, 2)
)
ctsxSxpMsgParseErrNotif.setObjects(
      *(("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpConnOperSourceAddrType"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpConnOperSourceAddr"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpNotifErrMsg"))
)
if mibBuilder.loadTexts:
    ctsxSxpMsgParseErrNotif.setStatus(
        "current"
    )

ctsxSxpConnConfigErrNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 0, 3)
)
ctsxSxpConnConfigErrNotif.setObjects(
      *(("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpConnOperSourceAddrType"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpConnOperSourceAddr"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpNotifErrMsg"))
)
if mibBuilder.loadTexts:
    ctsxSxpConnConfigErrNotif.setStatus(
        "current"
    )

ctsxSxpBindingErrNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 0, 4)
)
ctsxSxpBindingErrNotif.setObjects(
      *(("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpSgtMapSgt"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpSgtMapInstance"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpSgtMapVrfName"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpNotifErrMsg"))
)
if mibBuilder.loadTexts:
    ctsxSxpBindingErrNotif.setStatus(
        "current"
    )

ctsxSxpConnUpNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 0, 5)
)
ctsxSxpConnUpNotif.setObjects(
      *(("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpConnOperSourceAddrType"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpConnOperSourceAddr"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpConnInstance"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpConnStatus"))
)
if mibBuilder.loadTexts:
    ctsxSxpConnUpNotif.setStatus(
        "current"
    )

ctsxSxpConnDownNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 0, 6)
)
ctsxSxpConnDownNotif.setObjects(
      *(("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpConnOperSourceAddrType"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpConnOperSourceAddr"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpConnInstance"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpConnStatus"))
)
if mibBuilder.loadTexts:
    ctsxSxpConnDownNotif.setStatus(
        "current"
    )

ctsxSxpExpansionFailNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 0, 7)
)
ctsxSxpExpansionFailNotif.setObjects(
      *(("CISCO-TRUSTSEC-SXP-MIB", "ctsxSgtMapExpansionLimit"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSgtMapExpansionCount"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSgtMapExpansionVrf"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSgtMapExpansionAddrType"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSgtMapExpansionAddr"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSgtMapExpansionAddrPrefixLength"))
)
if mibBuilder.loadTexts:
    ctsxSxpExpansionFailNotif.setStatus(
        "current"
    )

ctsxSxpOperNodeIdChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 0, 8)
)
ctsxSxpOperNodeIdChangeNotif.setObjects(
      *(("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpOldOperNodeId"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpOperNodeId"))
)
if mibBuilder.loadTexts:
    ctsxSxpOperNodeIdChangeNotif.setStatus(
        "current"
    )

ctsxSxpBindingConflictNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 0, 9)
)
ctsxSxpBindingConflictNotif.setObjects(
      *(("CISCO-TRUSTSEC-SXP-MIB", "ctsxSgtMapConflictingVrfName"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSgtMapConflictingAddrType"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSgtMapConflictingAddr"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSgtMapConflictingOldSgt"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSgtMapConflictingNewSgt"))
)
if mibBuilder.loadTexts:
    ctsxSxpBindingConflictNotif.setStatus(
        "current"
    )


# Notifications groups

ctsxNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 2, 2, 11)
)
ctsxNotifsGroup.setObjects(
      *(("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpConnSourceAddrErrNotif"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpMsgParseErrNotif"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpConnConfigErrNotif"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpBindingErrNotif"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpConnUpNotif"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpConnDownNotif"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpExpansionFailNotif"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpOperNodeIdChangeNotif"),
        ("CISCO-TRUSTSEC-SXP-MIB", "ctsxSxpBindingConflictNotif"))
)
if mibBuilder.loadTexts:
    ctsxNotifsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoTrustSecSxpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoTrustSecSxpMIBCompliance.setStatus(
        "deprecated"
    )

ciscoTrustSecSxpMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoTrustSecSxpMIBCompliance2.setStatus(
        "deprecated"
    )

ciscoTrustSecSxpMIBCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 720, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoTrustSecSxpMIBCompliance3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-TRUSTSEC-SXP-MIB",
    **{"ciscoTrustSecSxpMIB": ciscoTrustSecSxpMIB,
       "ciscoTrustSecSxpMIBNotifs": ciscoTrustSecSxpMIBNotifs,
       "ctsxSxpConnSourceAddrErrNotif": ctsxSxpConnSourceAddrErrNotif,
       "ctsxSxpMsgParseErrNotif": ctsxSxpMsgParseErrNotif,
       "ctsxSxpConnConfigErrNotif": ctsxSxpConnConfigErrNotif,
       "ctsxSxpBindingErrNotif": ctsxSxpBindingErrNotif,
       "ctsxSxpConnUpNotif": ctsxSxpConnUpNotif,
       "ctsxSxpConnDownNotif": ctsxSxpConnDownNotif,
       "ctsxSxpExpansionFailNotif": ctsxSxpExpansionFailNotif,
       "ctsxSxpOperNodeIdChangeNotif": ctsxSxpOperNodeIdChangeNotif,
       "ctsxSxpBindingConflictNotif": ctsxSxpBindingConflictNotif,
       "ciscoTrustSecSxpMIBObjects": ciscoTrustSecSxpMIBObjects,
       "ctsxSxpGlobalObjects": ctsxSxpGlobalObjects,
       "ctsxSxpEnable": ctsxSxpEnable,
       "ctsxSxpConfigDefaultPasswordType": ctsxSxpConfigDefaultPasswordType,
       "ctsxSxpConfigDefaultPassword": ctsxSxpConfigDefaultPassword,
       "ctsxSxpViewDefaultPasswordType": ctsxSxpViewDefaultPasswordType,
       "ctsxSxpViewDefaultPassword": ctsxSxpViewDefaultPassword,
       "ctsxSxpDefaultSourceAddrType": ctsxSxpDefaultSourceAddrType,
       "ctsxSxpDefaultSourceAddr": ctsxSxpDefaultSourceAddr,
       "ctsxSxpRetryPeriod": ctsxSxpRetryPeriod,
       "ctsxSxpReconPeriod": ctsxSxpReconPeriod,
       "ctsxSxpBindingChangesLogEnable": ctsxSxpBindingChangesLogEnable,
       "ctsxSgtMapExpansionLimit": ctsxSgtMapExpansionLimit,
       "ctsxSgtMapExpansionCount": ctsxSgtMapExpansionCount,
       "ctsxSxpAdminNodeId": ctsxSxpAdminNodeId,
       "ctsxSxpNodeIdInterface": ctsxSxpNodeIdInterface,
       "ctsxSxpNodeIdIpAddrType": ctsxSxpNodeIdIpAddrType,
       "ctsxSxpNodeIdIpAddr": ctsxSxpNodeIdIpAddr,
       "ctsxSxpOperNodeId": ctsxSxpOperNodeId,
       "ctsxSxpSpeakerMinHoldTime": ctsxSxpSpeakerMinHoldTime,
       "ctsxSxpListenerMinHoldTime": ctsxSxpListenerMinHoldTime,
       "ctsxSxpListenerMaxHoldTime": ctsxSxpListenerMaxHoldTime,
       "ctsxSxpVersionSupport": ctsxSxpVersionSupport,
       "ctsxSxpConnectionObjects": ctsxSxpConnectionObjects,
       "ctsxSxpConnectionTable": ctsxSxpConnectionTable,
       "ctsxSxpConnectionEntry": ctsxSxpConnectionEntry,
       "ctsxSxpConnVrfName": ctsxSxpConnVrfName,
       "ctsxSxpConnPeerAddrType": ctsxSxpConnPeerAddrType,
       "ctsxSxpConnPeerAddr": ctsxSxpConnPeerAddr,
       "ctsxSxpConnSourceAddrType": ctsxSxpConnSourceAddrType,
       "ctsxSxpConnSourceAddr": ctsxSxpConnSourceAddr,
       "ctsxSxpConnOperSourceAddrType": ctsxSxpConnOperSourceAddrType,
       "ctsxSxpConnOperSourceAddr": ctsxSxpConnOperSourceAddr,
       "ctsxSxpConnPasswordUsed": ctsxSxpConnPasswordUsed,
       "ctsxSxpConnConfigPasswordType": ctsxSxpConnConfigPasswordType,
       "ctsxSxpConnConfigPassword": ctsxSxpConnConfigPassword,
       "ctsxSxpConnViewPasswordType": ctsxSxpConnViewPasswordType,
       "ctsxSxpConnViewPassword": ctsxSxpConnViewPassword,
       "ctsxSxpConnModeLocation": ctsxSxpConnModeLocation,
       "ctsxSxpConnMode": ctsxSxpConnMode,
       "ctsxSxpConnInstance": ctsxSxpConnInstance,
       "ctsxSxpConnStatusLastChange": ctsxSxpConnStatusLastChange,
       "ctsxSxpConnStatus": ctsxSxpConnStatus,
       "ctsxSxpVrfId": ctsxSxpVrfId,
       "ctsxSxpConnStorageType": ctsxSxpConnStorageType,
       "ctsxSxpConnRowStatus": ctsxSxpConnRowStatus,
       "ctsxSxpConnVersion": ctsxSxpConnVersion,
       "ctsxSxpConnSpeakerMinHoldTime": ctsxSxpConnSpeakerMinHoldTime,
       "ctsxSxpConnListenerMinHoldTime": ctsxSxpConnListenerMinHoldTime,
       "ctsxSxpConnListenerMaxHoldTime": ctsxSxpConnListenerMaxHoldTime,
       "ctsxSxpConnHoldTime": ctsxSxpConnHoldTime,
       "ctsxSxpConnCapability": ctsxSxpConnCapability,
       "ctsxSxpSgtObjects": ctsxSxpSgtObjects,
       "ctsxIpSgtMappingTable": ctsxIpSgtMappingTable,
       "ctsxIpSgtMappingEntry": ctsxIpSgtMappingEntry,
       "ctsxIpSgtMappingVrfId": ctsxIpSgtMappingVrfId,
       "ctsxIpSgtMappingAddrType": ctsxIpSgtMappingAddrType,
       "ctsxIpSgtMappingAddr": ctsxIpSgtMappingAddr,
       "ctsxIpSgtMappingPeerAddrType": ctsxIpSgtMappingPeerAddrType,
       "ctsxIpSgtMappingPeerAddr": ctsxIpSgtMappingPeerAddr,
       "ctsxIpSgtMappingSgt": ctsxIpSgtMappingSgt,
       "ctsxIpSgtMappingInstance": ctsxIpSgtMappingInstance,
       "ctsxIpSgtMappingVrfName": ctsxIpSgtMappingVrfName,
       "ctsxIpSgtMappingStatus": ctsxIpSgtMappingStatus,
       "ctsxSxpSgtMapTable": ctsxSxpSgtMapTable,
       "ctsxSxpSgtMapEntry": ctsxSxpSgtMapEntry,
       "ctsxSxpSgtMapVrfId": ctsxSxpSgtMapVrfId,
       "ctsxSxpSgtMapAddrType": ctsxSxpSgtMapAddrType,
       "ctsxSxpSgtMapAddr": ctsxSxpSgtMapAddr,
       "ctsxSxpSgtMapAddrPrefixLength": ctsxSxpSgtMapAddrPrefixLength,
       "ctsxSxpSgtMapPeerAddrType": ctsxSxpSgtMapPeerAddrType,
       "ctsxSxpSgtMapPeerAddr": ctsxSxpSgtMapPeerAddr,
       "ctsxSxpSgtMapSgt": ctsxSxpSgtMapSgt,
       "ctsxSxpSgtMapInstance": ctsxSxpSgtMapInstance,
       "ctsxSxpSgtMapVrfName": ctsxSxpSgtMapVrfName,
       "ctsxSxpSgtMapPeerSeq": ctsxSxpSgtMapPeerSeq,
       "ctsxSxpSgtMapStatus": ctsxSxpSgtMapStatus,
       "ciscoTrustSecSxpMIBNotifsControl": ciscoTrustSecSxpMIBNotifsControl,
       "ctsxSxpConnSourceAddrErrNotifEnable": ctsxSxpConnSourceAddrErrNotifEnable,
       "ctsxSxpMsgParseErrNotifEnable": ctsxSxpMsgParseErrNotifEnable,
       "ctsxSxpConnConfigErrNotifEnable": ctsxSxpConnConfigErrNotifEnable,
       "ctsxSxpBindingErrNotifEnable": ctsxSxpBindingErrNotifEnable,
       "ctsxSxpConnUpNotifEnable": ctsxSxpConnUpNotifEnable,
       "ctsxSxpConnDownNotifEnable": ctsxSxpConnDownNotifEnable,
       "ctsxSxpExpansionFailNotifEnable": ctsxSxpExpansionFailNotifEnable,
       "ctsxSxpOperNodeIdChangeNotifEnable": ctsxSxpOperNodeIdChangeNotifEnable,
       "ctsxSxpBindingConflictNotifEnable": ctsxSxpBindingConflictNotifEnable,
       "ciscoTrustSecSxpMIBNotifsOnlyInfo": ciscoTrustSecSxpMIBNotifsOnlyInfo,
       "ctsxSgtMapExpansionVrf": ctsxSgtMapExpansionVrf,
       "ctsxSgtMapExpansionAddrType": ctsxSgtMapExpansionAddrType,
       "ctsxSgtMapExpansionAddr": ctsxSgtMapExpansionAddr,
       "ctsxSgtMapExpansionAddrPrefixLength": ctsxSgtMapExpansionAddrPrefixLength,
       "ctsxSxpNotifErrMsg": ctsxSxpNotifErrMsg,
       "ctsxSgtMapConflictingVrfName": ctsxSgtMapConflictingVrfName,
       "ctsxSgtMapConflictingAddrType": ctsxSgtMapConflictingAddrType,
       "ctsxSgtMapConflictingAddr": ctsxSgtMapConflictingAddr,
       "ctsxSgtMapConflictingOldSgt": ctsxSgtMapConflictingOldSgt,
       "ctsxSgtMapConflictingNewSgt": ctsxSgtMapConflictingNewSgt,
       "ctsxSxpOldOperNodeId": ctsxSxpOldOperNodeId,
       "ciscoTrustSecSxpMIBConform": ciscoTrustSecSxpMIBConform,
       "ciscoTrustSecSxpMIBCompliances": ciscoTrustSecSxpMIBCompliances,
       "ciscoTrustSecSxpMIBCompliance": ciscoTrustSecSxpMIBCompliance,
       "ciscoTrustSecSxpMIBCompliance2": ciscoTrustSecSxpMIBCompliance2,
       "ciscoTrustSecSxpMIBCompliance3": ciscoTrustSecSxpMIBCompliance3,
       "ciscoTrustSecSxpMIBGroups": ciscoTrustSecSxpMIBGroups,
       "ctsxSxpGlobalGroup": ctsxSxpGlobalGroup,
       "ctsxSxpConnectionGroup": ctsxSxpConnectionGroup,
       "ctsxIpSgtMappingGroup": ctsxIpSgtMappingGroup,
       "ctsxSxpVersionGroup": ctsxSxpVersionGroup,
       "ctsxSxpBindingLogGroup": ctsxSxpBindingLogGroup,
       "ctsxSxpBindingNotifInfoGroup": ctsxSxpBindingNotifInfoGroup,
       "ctsxSxpNotifErrMsgGroup": ctsxSxpNotifErrMsgGroup,
       "ctsxSxpNodeIdInfoGroup": ctsxSxpNodeIdInfoGroup,
       "ctsxSxpSgtMapGroup": ctsxSxpSgtMapGroup,
       "ctsxNotifsControlGroup": ctsxNotifsControlGroup,
       "ctsxNotifsGroup": ctsxNotifsGroup,
       "ctsxSxpGlobalHoldTimeGroup": ctsxSxpGlobalHoldTimeGroup,
       "ctsxSxpConnHoldTimeGroup": ctsxSxpConnHoldTimeGroup,
       "ctsxSxpConnCapbilityGroup": ctsxSxpConnCapbilityGroup,
       "ctsxSxpVersionSupportGroup": ctsxSxpVersionSupportGroup,
       "ctsxSgtMapPeerSeqGroup": ctsxSgtMapPeerSeqGroup}
)
