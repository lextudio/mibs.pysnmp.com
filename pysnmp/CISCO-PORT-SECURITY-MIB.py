# SNMP MIB module (CISCO-PORT-SECURITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-PORT-SECURITY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:06:58 2024
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

(vtpVlanName,) = mibBuilder.importSymbols(
    "CISCO-VTP-MIB",
    "vtpVlanName")

(ifIndex,
 ifName) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex",
    "ifName")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

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

ciscoPortSecurityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 315)
)
ciscoPortSecurityMIB.setRevisions(
        ("2009-05-08 00:00",
         "2005-05-04 00:00",
         "2005-03-12 00:00",
         "2004-08-07 00:00",
         "2004-03-08 00:00",
         "2004-02-10 00:00",
         "2003-07-01 00:00",
         "2003-02-24 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ClearSecureMacAddrType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("all", 4),
          ("done", 0),
          ("dynamic", 1),
          ("static", 2),
          ("sticky", 3))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoPortSecurityMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoPortSecurityMIBNotifs = _CiscoPortSecurityMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 0)
)
_CpsInterfaceNotifs_ObjectIdentity = ObjectIdentity
cpsInterfaceNotifs = _CpsInterfaceNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 0, 0)
)
_CiscoPortSecurityMIBObjects_ObjectIdentity = ObjectIdentity
ciscoPortSecurityMIBObjects = _CiscoPortSecurityMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 1)
)
_CpsGlobalObjects_ObjectIdentity = ObjectIdentity
cpsGlobalObjects = _CpsGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 1, 1)
)


class _CpsGlobalMaxSecureAddress_Type(Integer32):
    """Custom type cpsGlobalMaxSecureAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CpsGlobalMaxSecureAddress_Type.__name__ = "Integer32"
_CpsGlobalMaxSecureAddress_Object = MibScalar
cpsGlobalMaxSecureAddress = _CpsGlobalMaxSecureAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 1, 1, 1),
    _CpsGlobalMaxSecureAddress_Type()
)
cpsGlobalMaxSecureAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsGlobalMaxSecureAddress.setStatus("current")


class _CpsGlobalTotalSecureAddress_Type(Integer32):
    """Custom type cpsGlobalTotalSecureAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpsGlobalTotalSecureAddress_Type.__name__ = "Integer32"
_CpsGlobalTotalSecureAddress_Object = MibScalar
cpsGlobalTotalSecureAddress = _CpsGlobalTotalSecureAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 1, 1, 2),
    _CpsGlobalTotalSecureAddress_Type()
)
cpsGlobalTotalSecureAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsGlobalTotalSecureAddress.setStatus("current")
_CpsGlobalPortSecurityEnable_Type = TruthValue
_CpsGlobalPortSecurityEnable_Object = MibScalar
cpsGlobalPortSecurityEnable = _CpsGlobalPortSecurityEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 1, 1, 3),
    _CpsGlobalPortSecurityEnable_Type()
)
cpsGlobalPortSecurityEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsGlobalPortSecurityEnable.setStatus("current")


class _CpsGlobalSNMPNotifRate_Type(Integer32):
    """Custom type cpsGlobalSNMPNotifRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_CpsGlobalSNMPNotifRate_Type.__name__ = "Integer32"
_CpsGlobalSNMPNotifRate_Object = MibScalar
cpsGlobalSNMPNotifRate = _CpsGlobalSNMPNotifRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 1, 1, 4),
    _CpsGlobalSNMPNotifRate_Type()
)
cpsGlobalSNMPNotifRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsGlobalSNMPNotifRate.setStatus("current")
if mibBuilder.loadTexts:
    cpsGlobalSNMPNotifRate.setUnits("notifs per second")
_CpsGlobalSNMPNotifControl_Type = TruthValue
_CpsGlobalSNMPNotifControl_Object = MibScalar
cpsGlobalSNMPNotifControl = _CpsGlobalSNMPNotifControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 1, 1, 5),
    _CpsGlobalSNMPNotifControl_Type()
)
cpsGlobalSNMPNotifControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsGlobalSNMPNotifControl.setStatus("current")
_CpsGlobalClearSecureMacAddresses_Type = ClearSecureMacAddrType
_CpsGlobalClearSecureMacAddresses_Object = MibScalar
cpsGlobalClearSecureMacAddresses = _CpsGlobalClearSecureMacAddresses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 1, 1, 6),
    _CpsGlobalClearSecureMacAddresses_Type()
)
cpsGlobalClearSecureMacAddresses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsGlobalClearSecureMacAddresses.setStatus("current")
_CpsInterfaceObjects_ObjectIdentity = ObjectIdentity
cpsInterfaceObjects = _CpsInterfaceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 1, 2)
)
_CpsIfConfigTable_Object = MibTable
cpsIfConfigTable = _CpsIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cpsIfConfigTable.setStatus("current")
_CpsIfConfigEntry_Object = MibTableRow
cpsIfConfigEntry = _CpsIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 1, 2, 1, 1)
)
cpsIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cpsIfConfigEntry.setStatus("current")
_CpsIfPortSecurityEnable_Type = TruthValue
_CpsIfPortSecurityEnable_Object = MibTableColumn
cpsIfPortSecurityEnable = _CpsIfPortSecurityEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 1, 2, 1, 1, 1),
    _CpsIfPortSecurityEnable_Type()
)
cpsIfPortSecurityEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsIfPortSecurityEnable.setStatus("current")


class _CpsIfPortSecurityStatus_Type(Integer32):
    """Custom type cpsIfPortSecurityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("securedown", 2),
          ("secureup", 1),
          ("shutdown", 3))
    )


_CpsIfPortSecurityStatus_Type.__name__ = "Integer32"
_CpsIfPortSecurityStatus_Object = MibTableColumn
cpsIfPortSecurityStatus = _CpsIfPortSecurityStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 1, 2, 1, 1, 2),
    _CpsIfPortSecurityStatus_Type()
)
cpsIfPortSecurityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsIfPortSecurityStatus.setStatus("current")


class _CpsIfMaxSecureMacAddr_Type(Integer32):
    """Custom type cpsIfMaxSecureMacAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CpsIfMaxSecureMacAddr_Type.__name__ = "Integer32"
_CpsIfMaxSecureMacAddr_Object = MibTableColumn
cpsIfMaxSecureMacAddr = _CpsIfMaxSecureMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 1, 2, 1, 1, 3),
    _CpsIfMaxSecureMacAddr_Type()
)
cpsIfMaxSecureMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsIfMaxSecureMacAddr.setStatus("current")


class _CpsIfCurrentSecureMacAddrCount_Type(Integer32):
    """Custom type cpsIfCurrentSecureMacAddrCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpsIfCurrentSecureMacAddrCount_Type.__name__ = "Integer32"
_CpsIfCurrentSecureMacAddrCount_Object = MibTableColumn
cpsIfCurrentSecureMacAddrCount = _CpsIfCurrentSecureMacAddrCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 1, 2, 1, 1, 4),
    _CpsIfCurrentSecureMacAddrCount_Type()
)
cpsIfCurrentSecureMacAddrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsIfCurrentSecureMacAddrCount.setStatus("current")


class _CpsIfSecureMacAddrAgingTime_Type(Integer32):
    """Custom type cpsIfSecureMacAddrAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_CpsIfSecureMacAddrAgingTime_Type.__name__ = "Integer32"
_CpsIfSecureMacAddrAgingTime_Object = MibTableColumn
cpsIfSecureMacAddrAgingTime = _CpsIfSecureMacAddrAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 1, 2, 1, 1, 5),
    _CpsIfSecureMacAddrAgingTime_Type()
)
cpsIfSecureMacAddrAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsIfSecureMacAddrAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    cpsIfSecureMacAddrAgingTime.setUnits("minutes")


class _CpsIfSecureMacAddrAgingType_Type(Integer32):
    """Custom type cpsIfSecureMacAddrAgingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absolute", 1),
          ("inactivity", 2))
    )


_CpsIfSecureMacAddrAgingType_Type.__name__ = "Integer32"
_CpsIfSecureMacAddrAgingType_Object = MibTableColumn
cpsIfSecureMacAddrAgingType = _CpsIfSecureMacAddrAgingType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 1, 2, 1, 1, 6),
    _CpsIfSecureMacAddrAgingType_Type()
)
cpsIfSecureMacAddrAgingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsIfSecureMacAddrAgingType.setStatus("current")
_CpsIfStaticMacAddrAgingEnable_Type = TruthValue
_CpsIfStaticMacAddrAgingEnable_Object = MibTableColumn
cpsIfStaticMacAddrAgingEnable = _CpsIfStaticMacAddrAgingEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 1, 2, 1, 1, 7),
    _CpsIfStaticMacAddrAgingEnable_Type()
)
cpsIfStaticMacAddrAgingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsIfStaticMacAddrAgingEnable.setStatus("current")


class _CpsIfViolationAction_Type(Integer32):
    """Custom type cpsIfViolationAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("drop", 3),
          ("dropNotify", 2),
          ("shutdown", 1))
    )


_CpsIfViolationAction_Type.__name__ = "Integer32"
_CpsIfViolationAction_Object = MibTableColumn
cpsIfViolationAction = _CpsIfViolationAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 1, 2, 1, 1, 8),
    _CpsIfViolationAction_Type()
)
cpsIfViolationAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsIfViolationAction.setStatus("current")
_CpsIfViolationCount_Type = Counter32
_CpsIfViolationCount_Object = MibTableColumn
cpsIfViolationCount = _CpsIfViolationCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 1, 2, 1, 1, 9),
    _CpsIfViolationCount_Type()
)
cpsIfViolationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsIfViolationCount.setStatus("current")
_CpsIfSecureLastMacAddress_Type = MacAddress
_CpsIfSecureLastMacAddress_Object = MibTableColumn
cpsIfSecureLastMacAddress = _CpsIfSecureLastMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 1, 2, 1, 1, 10),
    _CpsIfSecureLastMacAddress_Type()
)
cpsIfSecureLastMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsIfSecureLastMacAddress.setStatus("current")
_CpsIfClearSecureAddresses_Type = TruthValue
_CpsIfClearSecureAddresses_Object = MibTableColumn
cpsIfClearSecureAddresses = _CpsIfClearSecureAddresses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 1, 2, 1, 1, 11),
    _CpsIfClearSecureAddresses_Type()
)
cpsIfClearSecureAddresses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsIfClearSecureAddresses.setStatus("deprecated")
_CpsIfUnicastFloodingEnable_Type = TruthValue
_CpsIfUnicastFloodingEnable_Object = MibTableColumn
cpsIfUnicastFloodingEnable = _CpsIfUnicastFloodingEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 1, 2, 1, 1, 12),
    _CpsIfUnicastFloodingEnable_Type()
)
cpsIfUnicastFloodingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsIfUnicastFloodingEnable.setStatus("current")
_CpsIfShutdownTimeout_Type = Unsigned32
_CpsIfShutdownTimeout_Object = MibTableColumn
cpsIfShutdownTimeout = _CpsIfShutdownTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 1, 2, 1, 1, 13),
    _CpsIfShutdownTimeout_Type()
)
cpsIfShutdownTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsIfShutdownTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cpsIfShutdownTimeout.setUnits("minutes")
_CpsIfClearSecureMacAddresses_Type = ClearSecureMacAddrType
_CpsIfClearSecureMacAddresses_Object = MibTableColumn
cpsIfClearSecureMacAddresses = _CpsIfClearSecureMacAddresses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 1, 2, 1, 1, 14),
    _CpsIfClearSecureMacAddresses_Type()
)
cpsIfClearSecureMacAddresses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsIfClearSecureMacAddresses.setStatus("current")
_CpsIfStickyEnable_Type = TruthValue
_CpsIfStickyEnable_Object = MibTableColumn
cpsIfStickyEnable = _CpsIfStickyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 1, 2, 1, 1, 15),
    _CpsIfStickyEnable_Type()
)
cpsIfStickyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsIfStickyEnable.setStatus("current")
_CpsIfInvalidSrcRateLimitEnable_Type = TruthValue
_CpsIfInvalidSrcRateLimitEnable_Object = MibTableColumn
cpsIfInvalidSrcRateLimitEnable = _CpsIfInvalidSrcRateLimitEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 1, 2, 1, 1, 16),
    _CpsIfInvalidSrcRateLimitEnable_Type()
)
cpsIfInvalidSrcRateLimitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsIfInvalidSrcRateLimitEnable.setStatus("current")


class _CpsIfInvalidSrcRateLimitValue_Type(Integer32):
    """Custom type cpsIfInvalidSrcRateLimitValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1000),
    )


_CpsIfInvalidSrcRateLimitValue_Type.__name__ = "Integer32"
_CpsIfInvalidSrcRateLimitValue_Object = MibTableColumn
cpsIfInvalidSrcRateLimitValue = _CpsIfInvalidSrcRateLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 1, 2, 1, 1, 17),
    _CpsIfInvalidSrcRateLimitValue_Type()
)
cpsIfInvalidSrcRateLimitValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsIfInvalidSrcRateLimitValue.setStatus("current")
if mibBuilder.loadTexts:
    cpsIfInvalidSrcRateLimitValue.setUnits("Packets per second")
_CpsIfSecureLastMacAddrVlanId_Type = VlanIndex
_CpsIfSecureLastMacAddrVlanId_Object = MibTableColumn
cpsIfSecureLastMacAddrVlanId = _CpsIfSecureLastMacAddrVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 1, 2, 1, 1, 18),
    _CpsIfSecureLastMacAddrVlanId_Type()
)
cpsIfSecureLastMacAddrVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsIfSecureLastMacAddrVlanId.setStatus("current")
_CpsSecureMacAddressTable_Object = MibTable
cpsSecureMacAddressTable = _CpsSecureMacAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cpsSecureMacAddressTable.setStatus("deprecated")
_CpsSecureMacAddressEntry_Object = MibTableRow
cpsSecureMacAddressEntry = _CpsSecureMacAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 1, 2, 2, 1)
)
cpsSecureMacAddressEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-PORT-SECURITY-MIB", "cpsSecureMacAddress"),
)
if mibBuilder.loadTexts:
    cpsSecureMacAddressEntry.setStatus("deprecated")
_CpsSecureMacAddress_Type = MacAddress
_CpsSecureMacAddress_Object = MibTableColumn
cpsSecureMacAddress = _CpsSecureMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 1, 2, 2, 1, 1),
    _CpsSecureMacAddress_Type()
)
cpsSecureMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpsSecureMacAddress.setStatus("deprecated")


class _CpsSecureMacAddrType_Type(Integer32):
    """Custom type cpsSecureMacAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_CpsSecureMacAddrType_Type.__name__ = "Integer32"
_CpsSecureMacAddrType_Object = MibTableColumn
cpsSecureMacAddrType = _CpsSecureMacAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 1, 2, 2, 1, 2),
    _CpsSecureMacAddrType_Type()
)
cpsSecureMacAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsSecureMacAddrType.setStatus("deprecated")


class _CpsSecureMacAddrRemainingAge_Type(Integer32):
    """Custom type cpsSecureMacAddrRemainingAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_CpsSecureMacAddrRemainingAge_Type.__name__ = "Integer32"
_CpsSecureMacAddrRemainingAge_Object = MibTableColumn
cpsSecureMacAddrRemainingAge = _CpsSecureMacAddrRemainingAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 1, 2, 2, 1, 3),
    _CpsSecureMacAddrRemainingAge_Type()
)
cpsSecureMacAddrRemainingAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsSecureMacAddrRemainingAge.setStatus("deprecated")
if mibBuilder.loadTexts:
    cpsSecureMacAddrRemainingAge.setUnits("minutes")
_CpsSecureMacAddrRowStatus_Type = RowStatus
_CpsSecureMacAddrRowStatus_Object = MibTableColumn
cpsSecureMacAddrRowStatus = _CpsSecureMacAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 1, 2, 2, 1, 4),
    _CpsSecureMacAddrRowStatus_Type()
)
cpsSecureMacAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpsSecureMacAddrRowStatus.setStatus("deprecated")
_CpsIfVlanSecureMacAddrTable_Object = MibTable
cpsIfVlanSecureMacAddrTable = _CpsIfVlanSecureMacAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cpsIfVlanSecureMacAddrTable.setStatus("current")
_CpsIfVlanSecureMacAddrEntry_Object = MibTableRow
cpsIfVlanSecureMacAddrEntry = _CpsIfVlanSecureMacAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 1, 2, 3, 1)
)
cpsIfVlanSecureMacAddrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-PORT-SECURITY-MIB", "cpsIfVlanSecureMacAddress"),
    (0, "CISCO-PORT-SECURITY-MIB", "cpsIfVlanSecureVlanIndex"),
)
if mibBuilder.loadTexts:
    cpsIfVlanSecureMacAddrEntry.setStatus("current")
_CpsIfVlanSecureMacAddress_Type = MacAddress
_CpsIfVlanSecureMacAddress_Object = MibTableColumn
cpsIfVlanSecureMacAddress = _CpsIfVlanSecureMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 1, 2, 3, 1, 1),
    _CpsIfVlanSecureMacAddress_Type()
)
cpsIfVlanSecureMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpsIfVlanSecureMacAddress.setStatus("current")
_CpsIfVlanSecureVlanIndex_Type = VlanIndex
_CpsIfVlanSecureVlanIndex_Object = MibTableColumn
cpsIfVlanSecureVlanIndex = _CpsIfVlanSecureVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 1, 2, 3, 1, 2),
    _CpsIfVlanSecureVlanIndex_Type()
)
cpsIfVlanSecureVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpsIfVlanSecureVlanIndex.setStatus("current")


class _CpsIfVlanSecureMacAddrType_Type(Integer32):
    """Custom type cpsIfVlanSecureMacAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1),
          ("sticky", 3))
    )


_CpsIfVlanSecureMacAddrType_Type.__name__ = "Integer32"
_CpsIfVlanSecureMacAddrType_Object = MibTableColumn
cpsIfVlanSecureMacAddrType = _CpsIfVlanSecureMacAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 1, 2, 3, 1, 3),
    _CpsIfVlanSecureMacAddrType_Type()
)
cpsIfVlanSecureMacAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsIfVlanSecureMacAddrType.setStatus("current")
_CpsIfVlanSecureMacAddrRemainAge_Type = Unsigned32
_CpsIfVlanSecureMacAddrRemainAge_Object = MibTableColumn
cpsIfVlanSecureMacAddrRemainAge = _CpsIfVlanSecureMacAddrRemainAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 1, 2, 3, 1, 4),
    _CpsIfVlanSecureMacAddrRemainAge_Type()
)
cpsIfVlanSecureMacAddrRemainAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsIfVlanSecureMacAddrRemainAge.setStatus("current")
if mibBuilder.loadTexts:
    cpsIfVlanSecureMacAddrRemainAge.setUnits("minutes")
_CpsIfVlanSecureMacAddrRowStatus_Type = RowStatus
_CpsIfVlanSecureMacAddrRowStatus_Object = MibTableColumn
cpsIfVlanSecureMacAddrRowStatus = _CpsIfVlanSecureMacAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 1, 2, 3, 1, 5),
    _CpsIfVlanSecureMacAddrRowStatus_Type()
)
cpsIfVlanSecureMacAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpsIfVlanSecureMacAddrRowStatus.setStatus("current")
_CpsIfVlanTable_Object = MibTable
cpsIfVlanTable = _CpsIfVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 1, 2, 4)
)
if mibBuilder.loadTexts:
    cpsIfVlanTable.setStatus("obsolete")
_CpsIfVlanEntry_Object = MibTableRow
cpsIfVlanEntry = _CpsIfVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 1, 2, 4, 1)
)
cpsIfVlanEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-PORT-SECURITY-MIB", "cpsIfVlanIndex"),
)
if mibBuilder.loadTexts:
    cpsIfVlanEntry.setStatus("obsolete")
_CpsIfVlanIndex_Type = VlanIndex
_CpsIfVlanIndex_Object = MibTableColumn
cpsIfVlanIndex = _CpsIfVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 1, 2, 4, 1, 1),
    _CpsIfVlanIndex_Type()
)
cpsIfVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpsIfVlanIndex.setStatus("obsolete")


class _CpsIfVlanMaxSecureMacAddr_Type(Unsigned32):
    """Custom type cpsIfVlanMaxSecureMacAddr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CpsIfVlanMaxSecureMacAddr_Type.__name__ = "Unsigned32"
_CpsIfVlanMaxSecureMacAddr_Object = MibTableColumn
cpsIfVlanMaxSecureMacAddr = _CpsIfVlanMaxSecureMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 1, 2, 4, 1, 2),
    _CpsIfVlanMaxSecureMacAddr_Type()
)
cpsIfVlanMaxSecureMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsIfVlanMaxSecureMacAddr.setStatus("obsolete")


class _CpsIfVlanCurSecureMacAddrCount_Type(Unsigned32):
    """Custom type cpsIfVlanCurSecureMacAddrCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpsIfVlanCurSecureMacAddrCount_Type.__name__ = "Unsigned32"
_CpsIfVlanCurSecureMacAddrCount_Object = MibTableColumn
cpsIfVlanCurSecureMacAddrCount = _CpsIfVlanCurSecureMacAddrCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 1, 2, 4, 1, 3),
    _CpsIfVlanCurSecureMacAddrCount_Type()
)
cpsIfVlanCurSecureMacAddrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsIfVlanCurSecureMacAddrCount.setStatus("obsolete")
_CpsIfMultiVlanTable_Object = MibTable
cpsIfMultiVlanTable = _CpsIfMultiVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 1, 2, 5)
)
if mibBuilder.loadTexts:
    cpsIfMultiVlanTable.setStatus("current")
_CpsIfMultiVlanEntry_Object = MibTableRow
cpsIfMultiVlanEntry = _CpsIfMultiVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 1, 2, 5, 1)
)
cpsIfMultiVlanEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-PORT-SECURITY-MIB", "cpsIfMultiVlanIndex"),
)
if mibBuilder.loadTexts:
    cpsIfMultiVlanEntry.setStatus("current")
_CpsIfMultiVlanIndex_Type = VlanIndex
_CpsIfMultiVlanIndex_Object = MibTableColumn
cpsIfMultiVlanIndex = _CpsIfMultiVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 1, 2, 5, 1, 1),
    _CpsIfMultiVlanIndex_Type()
)
cpsIfMultiVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpsIfMultiVlanIndex.setStatus("current")


class _CpsIfMultiVlanMaxSecureMacAddr_Type(Unsigned32):
    """Custom type cpsIfMultiVlanMaxSecureMacAddr based on Unsigned32"""
    defaultValue = 1


_CpsIfMultiVlanMaxSecureMacAddr_Object = MibTableColumn
cpsIfMultiVlanMaxSecureMacAddr = _CpsIfMultiVlanMaxSecureMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 1, 2, 5, 1, 2),
    _CpsIfMultiVlanMaxSecureMacAddr_Type()
)
cpsIfMultiVlanMaxSecureMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpsIfMultiVlanMaxSecureMacAddr.setStatus("current")
_CpsIfMultiVlanSecureMacAddrCount_Type = Unsigned32
_CpsIfMultiVlanSecureMacAddrCount_Object = MibTableColumn
cpsIfMultiVlanSecureMacAddrCount = _CpsIfMultiVlanSecureMacAddrCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 1, 2, 5, 1, 3),
    _CpsIfMultiVlanSecureMacAddrCount_Type()
)
cpsIfMultiVlanSecureMacAddrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsIfMultiVlanSecureMacAddrCount.setStatus("current")


class _CpsIfMultiVlanClearSecureMacAddr_Type(ClearSecureMacAddrType):
    """Custom type cpsIfMultiVlanClearSecureMacAddr based on ClearSecureMacAddrType"""


_CpsIfMultiVlanClearSecureMacAddr_Object = MibTableColumn
cpsIfMultiVlanClearSecureMacAddr = _CpsIfMultiVlanClearSecureMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 1, 2, 5, 1, 4),
    _CpsIfMultiVlanClearSecureMacAddr_Type()
)
cpsIfMultiVlanClearSecureMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpsIfMultiVlanClearSecureMacAddr.setStatus("current")
_CpsIfMultiVlanRowStatus_Type = RowStatus
_CpsIfMultiVlanRowStatus_Object = MibTableColumn
cpsIfMultiVlanRowStatus = _CpsIfMultiVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 1, 2, 5, 1, 5),
    _CpsIfMultiVlanRowStatus_Type()
)
cpsIfMultiVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpsIfMultiVlanRowStatus.setStatus("current")
_CiscoPortSecurityMIBConform_ObjectIdentity = ObjectIdentity
ciscoPortSecurityMIBConform = _CiscoPortSecurityMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 2)
)
_CiscoPortSecurityMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoPortSecurityMIBCompliances = _CiscoPortSecurityMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 2, 1)
)
_CiscoPortSecurityMIBGroups_ObjectIdentity = ObjectIdentity
ciscoPortSecurityMIBGroups = _CiscoPortSecurityMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 2, 2)
)

# Managed Objects groups

cpsGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 2, 2, 1)
)
cpsGlobalGroup.setObjects(
      *(("CISCO-PORT-SECURITY-MIB", "cpsGlobalMaxSecureAddress"),
        ("CISCO-PORT-SECURITY-MIB", "cpsGlobalTotalSecureAddress"),
        ("CISCO-PORT-SECURITY-MIB", "cpsGlobalPortSecurityEnable"),
        ("CISCO-PORT-SECURITY-MIB", "cpsGlobalSNMPNotifRate"),
        ("CISCO-PORT-SECURITY-MIB", "cpsGlobalSNMPNotifControl"))
)
if mibBuilder.loadTexts:
    cpsGlobalGroup.setStatus("current")

cpsInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 2, 2, 2)
)
cpsInterfaceGroup.setObjects(
      *(("CISCO-PORT-SECURITY-MIB", "cpsIfPortSecurityEnable"),
        ("CISCO-PORT-SECURITY-MIB", "cpsIfPortSecurityStatus"),
        ("CISCO-PORT-SECURITY-MIB", "cpsIfMaxSecureMacAddr"),
        ("CISCO-PORT-SECURITY-MIB", "cpsIfCurrentSecureMacAddrCount"),
        ("CISCO-PORT-SECURITY-MIB", "cpsIfSecureMacAddrAgingType"),
        ("CISCO-PORT-SECURITY-MIB", "cpsIfSecureMacAddrAgingTime"),
        ("CISCO-PORT-SECURITY-MIB", "cpsIfStaticMacAddrAgingEnable"),
        ("CISCO-PORT-SECURITY-MIB", "cpsIfViolationAction"),
        ("CISCO-PORT-SECURITY-MIB", "cpsIfViolationCount"),
        ("CISCO-PORT-SECURITY-MIB", "cpsIfClearSecureAddresses"),
        ("CISCO-PORT-SECURITY-MIB", "cpsSecureMacAddrType"),
        ("CISCO-PORT-SECURITY-MIB", "cpsSecureMacAddrRemainingAge"),
        ("CISCO-PORT-SECURITY-MIB", "cpsSecureMacAddrRowStatus"))
)
if mibBuilder.loadTexts:
    cpsInterfaceGroup.setStatus("deprecated")

cpsExtInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 2, 2, 3)
)
cpsExtInterfaceGroup.setObjects(
    ("CISCO-PORT-SECURITY-MIB", "cpsIfSecureLastMacAddress")
)
if mibBuilder.loadTexts:
    cpsExtInterfaceGroup.setStatus("current")

cpsUnicastFloodingInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 2, 2, 5)
)
cpsUnicastFloodingInterfaceGroup.setObjects(
    ("CISCO-PORT-SECURITY-MIB", "cpsIfUnicastFloodingEnable")
)
if mibBuilder.loadTexts:
    cpsUnicastFloodingInterfaceGroup.setStatus("current")

cpsShutdownTimeoutInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 2, 2, 6)
)
cpsShutdownTimeoutInterfaceGroup.setObjects(
    ("CISCO-PORT-SECURITY-MIB", "cpsIfShutdownTimeout")
)
if mibBuilder.loadTexts:
    cpsShutdownTimeoutInterfaceGroup.setStatus("current")

cpsIfVlanSecureMacAddrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 2, 2, 8)
)
cpsIfVlanSecureMacAddrGroup.setObjects(
      *(("CISCO-PORT-SECURITY-MIB", "cpsIfVlanSecureMacAddrType"),
        ("CISCO-PORT-SECURITY-MIB", "cpsIfVlanSecureMacAddrRemainAge"),
        ("CISCO-PORT-SECURITY-MIB", "cpsIfVlanSecureMacAddrRowStatus"))
)
if mibBuilder.loadTexts:
    cpsIfVlanSecureMacAddrGroup.setStatus("current")

cpsInterfaceGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 2, 2, 9)
)
cpsInterfaceGroup1.setObjects(
      *(("CISCO-PORT-SECURITY-MIB", "cpsIfPortSecurityEnable"),
        ("CISCO-PORT-SECURITY-MIB", "cpsIfPortSecurityStatus"),
        ("CISCO-PORT-SECURITY-MIB", "cpsIfMaxSecureMacAddr"),
        ("CISCO-PORT-SECURITY-MIB", "cpsIfCurrentSecureMacAddrCount"),
        ("CISCO-PORT-SECURITY-MIB", "cpsIfSecureMacAddrAgingType"),
        ("CISCO-PORT-SECURITY-MIB", "cpsIfSecureMacAddrAgingTime"),
        ("CISCO-PORT-SECURITY-MIB", "cpsIfStaticMacAddrAgingEnable"),
        ("CISCO-PORT-SECURITY-MIB", "cpsIfViolationAction"),
        ("CISCO-PORT-SECURITY-MIB", "cpsIfViolationCount"),
        ("CISCO-PORT-SECURITY-MIB", "cpsIfClearSecureAddresses"))
)
if mibBuilder.loadTexts:
    cpsInterfaceGroup1.setStatus("deprecated")

cpsExtConfigInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 2, 2, 10)
)
cpsExtConfigInterfaceGroup.setObjects(
      *(("CISCO-PORT-SECURITY-MIB", "cpsIfShutdownTimeout"),
        ("CISCO-PORT-SECURITY-MIB", "cpsIfUnicastFloodingEnable"))
)
if mibBuilder.loadTexts:
    cpsExtConfigInterfaceGroup.setStatus("deprecated")

cpsIfVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 2, 2, 11)
)
cpsIfVlanGroup.setObjects(
      *(("CISCO-PORT-SECURITY-MIB", "cpsIfVlanMaxSecureMacAddr"),
        ("CISCO-PORT-SECURITY-MIB", "cpsIfVlanCurSecureMacAddrCount"))
)
if mibBuilder.loadTexts:
    cpsIfVlanGroup.setStatus("obsolete")

cpsGlobalClearAddressGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 2, 2, 12)
)
cpsGlobalClearAddressGroup.setObjects(
    ("CISCO-PORT-SECURITY-MIB", "cpsGlobalClearSecureMacAddresses")
)
if mibBuilder.loadTexts:
    cpsGlobalClearAddressGroup.setStatus("current")

cpsInterfaceGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 2, 2, 13)
)
cpsInterfaceGroup2.setObjects(
      *(("CISCO-PORT-SECURITY-MIB", "cpsIfPortSecurityEnable"),
        ("CISCO-PORT-SECURITY-MIB", "cpsIfPortSecurityStatus"),
        ("CISCO-PORT-SECURITY-MIB", "cpsIfMaxSecureMacAddr"),
        ("CISCO-PORT-SECURITY-MIB", "cpsIfCurrentSecureMacAddrCount"),
        ("CISCO-PORT-SECURITY-MIB", "cpsIfSecureMacAddrAgingType"),
        ("CISCO-PORT-SECURITY-MIB", "cpsIfSecureMacAddrAgingTime"),
        ("CISCO-PORT-SECURITY-MIB", "cpsIfStaticMacAddrAgingEnable"),
        ("CISCO-PORT-SECURITY-MIB", "cpsIfViolationAction"),
        ("CISCO-PORT-SECURITY-MIB", "cpsIfViolationCount"),
        ("CISCO-PORT-SECURITY-MIB", "cpsIfClearSecureMacAddresses"),
        ("CISCO-PORT-SECURITY-MIB", "cpsIfInvalidSrcRateLimitEnable"),
        ("CISCO-PORT-SECURITY-MIB", "cpsIfInvalidSrcRateLimitValue"),
        ("CISCO-PORT-SECURITY-MIB", "cpsIfStickyEnable"))
)
if mibBuilder.loadTexts:
    cpsInterfaceGroup2.setStatus("current")

cpsIfMultiVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 2, 2, 15)
)
cpsIfMultiVlanGroup.setObjects(
      *(("CISCO-PORT-SECURITY-MIB", "cpsIfMultiVlanMaxSecureMacAddr"),
        ("CISCO-PORT-SECURITY-MIB", "cpsIfMultiVlanSecureMacAddrCount"),
        ("CISCO-PORT-SECURITY-MIB", "cpsIfMultiVlanClearSecureMacAddr"),
        ("CISCO-PORT-SECURITY-MIB", "cpsIfMultiVlanRowStatus"))
)
if mibBuilder.loadTexts:
    cpsIfMultiVlanGroup.setStatus("current")

cpsExtInterfaceGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 2, 2, 17)
)
cpsExtInterfaceGroup1.setObjects(
    ("CISCO-PORT-SECURITY-MIB", "cpsIfSecureLastMacAddrVlanId")
)
if mibBuilder.loadTexts:
    cpsExtInterfaceGroup1.setStatus("current")


# Notification objects

cpsSecureMacAddrViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 0, 0, 1)
)
cpsSecureMacAddrViolation.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"),
        ("CISCO-PORT-SECURITY-MIB", "cpsIfSecureLastMacAddress"))
)
if mibBuilder.loadTexts:
    cpsSecureMacAddrViolation.setStatus(
        "current"
    )

cpsTrunkSecureMacAddrViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 0, 0, 2)
)
cpsTrunkSecureMacAddrViolation.setObjects(
      *(("IF-MIB", "ifName"),
        ("CISCO-VTP-MIB", "vtpVlanName"),
        ("CISCO-PORT-SECURITY-MIB", "cpsIfSecureLastMacAddress"))
)
if mibBuilder.loadTexts:
    cpsTrunkSecureMacAddrViolation.setStatus(
        "deprecated"
    )

cpsIfVlanSecureMacAddrViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 0, 0, 3)
)
cpsIfVlanSecureMacAddrViolation.setObjects(
      *(("IF-MIB", "ifName"),
        ("CISCO-PORT-SECURITY-MIB", "cpsIfSecureLastMacAddrVlanId"),
        ("CISCO-PORT-SECURITY-MIB", "cpsIfSecureLastMacAddress"))
)
if mibBuilder.loadTexts:
    cpsIfVlanSecureMacAddrViolation.setStatus(
        "current"
    )


# Notifications groups

cpsNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 2, 2, 4)
)
cpsNotificationGroup.setObjects(
    ("CISCO-PORT-SECURITY-MIB", "cpsSecureMacAddrViolation")
)
if mibBuilder.loadTexts:
    cpsNotificationGroup.setStatus(
        "current"
    )

cpsTrunkSecureNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 2, 2, 14)
)
cpsTrunkSecureNotificationGroup.setObjects(
    ("CISCO-PORT-SECURITY-MIB", "cpsTrunkSecureMacAddrViolation")
)
if mibBuilder.loadTexts:
    cpsTrunkSecureNotificationGroup.setStatus(
        "deprecated"
    )

cpsIfVlanSecureNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 2, 2, 16)
)
cpsIfVlanSecureNotificationGroup.setObjects(
    ("CISCO-PORT-SECURITY-MIB", "cpsIfVlanSecureMacAddrViolation")
)
if mibBuilder.loadTexts:
    cpsIfVlanSecureNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoPortSecurityMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoPortSecurityMIBCompliance.setStatus(
        "deprecated"
    )

ciscoPortSecurityMIBCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoPortSecurityMIBCompliance1.setStatus(
        "deprecated"
    )

ciscoPortSecurityMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoPortSecurityMIBCompliance2.setStatus(
        "obsolete"
    )

ciscoPortSecurityMIBCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoPortSecurityMIBCompliance3.setStatus(
        "obsolete"
    )

ciscoPortSecurityMIBCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 315, 2, 1, 5)
)
if mibBuilder.loadTexts:
    ciscoPortSecurityMIBCompliance4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-PORT-SECURITY-MIB",
    **{"ClearSecureMacAddrType": ClearSecureMacAddrType,
       "ciscoPortSecurityMIB": ciscoPortSecurityMIB,
       "ciscoPortSecurityMIBNotifs": ciscoPortSecurityMIBNotifs,
       "cpsInterfaceNotifs": cpsInterfaceNotifs,
       "cpsSecureMacAddrViolation": cpsSecureMacAddrViolation,
       "cpsTrunkSecureMacAddrViolation": cpsTrunkSecureMacAddrViolation,
       "cpsIfVlanSecureMacAddrViolation": cpsIfVlanSecureMacAddrViolation,
       "ciscoPortSecurityMIBObjects": ciscoPortSecurityMIBObjects,
       "cpsGlobalObjects": cpsGlobalObjects,
       "cpsGlobalMaxSecureAddress": cpsGlobalMaxSecureAddress,
       "cpsGlobalTotalSecureAddress": cpsGlobalTotalSecureAddress,
       "cpsGlobalPortSecurityEnable": cpsGlobalPortSecurityEnable,
       "cpsGlobalSNMPNotifRate": cpsGlobalSNMPNotifRate,
       "cpsGlobalSNMPNotifControl": cpsGlobalSNMPNotifControl,
       "cpsGlobalClearSecureMacAddresses": cpsGlobalClearSecureMacAddresses,
       "cpsInterfaceObjects": cpsInterfaceObjects,
       "cpsIfConfigTable": cpsIfConfigTable,
       "cpsIfConfigEntry": cpsIfConfigEntry,
       "cpsIfPortSecurityEnable": cpsIfPortSecurityEnable,
       "cpsIfPortSecurityStatus": cpsIfPortSecurityStatus,
       "cpsIfMaxSecureMacAddr": cpsIfMaxSecureMacAddr,
       "cpsIfCurrentSecureMacAddrCount": cpsIfCurrentSecureMacAddrCount,
       "cpsIfSecureMacAddrAgingTime": cpsIfSecureMacAddrAgingTime,
       "cpsIfSecureMacAddrAgingType": cpsIfSecureMacAddrAgingType,
       "cpsIfStaticMacAddrAgingEnable": cpsIfStaticMacAddrAgingEnable,
       "cpsIfViolationAction": cpsIfViolationAction,
       "cpsIfViolationCount": cpsIfViolationCount,
       "cpsIfSecureLastMacAddress": cpsIfSecureLastMacAddress,
       "cpsIfClearSecureAddresses": cpsIfClearSecureAddresses,
       "cpsIfUnicastFloodingEnable": cpsIfUnicastFloodingEnable,
       "cpsIfShutdownTimeout": cpsIfShutdownTimeout,
       "cpsIfClearSecureMacAddresses": cpsIfClearSecureMacAddresses,
       "cpsIfStickyEnable": cpsIfStickyEnable,
       "cpsIfInvalidSrcRateLimitEnable": cpsIfInvalidSrcRateLimitEnable,
       "cpsIfInvalidSrcRateLimitValue": cpsIfInvalidSrcRateLimitValue,
       "cpsIfSecureLastMacAddrVlanId": cpsIfSecureLastMacAddrVlanId,
       "cpsSecureMacAddressTable": cpsSecureMacAddressTable,
       "cpsSecureMacAddressEntry": cpsSecureMacAddressEntry,
       "cpsSecureMacAddress": cpsSecureMacAddress,
       "cpsSecureMacAddrType": cpsSecureMacAddrType,
       "cpsSecureMacAddrRemainingAge": cpsSecureMacAddrRemainingAge,
       "cpsSecureMacAddrRowStatus": cpsSecureMacAddrRowStatus,
       "cpsIfVlanSecureMacAddrTable": cpsIfVlanSecureMacAddrTable,
       "cpsIfVlanSecureMacAddrEntry": cpsIfVlanSecureMacAddrEntry,
       "cpsIfVlanSecureMacAddress": cpsIfVlanSecureMacAddress,
       "cpsIfVlanSecureVlanIndex": cpsIfVlanSecureVlanIndex,
       "cpsIfVlanSecureMacAddrType": cpsIfVlanSecureMacAddrType,
       "cpsIfVlanSecureMacAddrRemainAge": cpsIfVlanSecureMacAddrRemainAge,
       "cpsIfVlanSecureMacAddrRowStatus": cpsIfVlanSecureMacAddrRowStatus,
       "cpsIfVlanTable": cpsIfVlanTable,
       "cpsIfVlanEntry": cpsIfVlanEntry,
       "cpsIfVlanIndex": cpsIfVlanIndex,
       "cpsIfVlanMaxSecureMacAddr": cpsIfVlanMaxSecureMacAddr,
       "cpsIfVlanCurSecureMacAddrCount": cpsIfVlanCurSecureMacAddrCount,
       "cpsIfMultiVlanTable": cpsIfMultiVlanTable,
       "cpsIfMultiVlanEntry": cpsIfMultiVlanEntry,
       "cpsIfMultiVlanIndex": cpsIfMultiVlanIndex,
       "cpsIfMultiVlanMaxSecureMacAddr": cpsIfMultiVlanMaxSecureMacAddr,
       "cpsIfMultiVlanSecureMacAddrCount": cpsIfMultiVlanSecureMacAddrCount,
       "cpsIfMultiVlanClearSecureMacAddr": cpsIfMultiVlanClearSecureMacAddr,
       "cpsIfMultiVlanRowStatus": cpsIfMultiVlanRowStatus,
       "ciscoPortSecurityMIBConform": ciscoPortSecurityMIBConform,
       "ciscoPortSecurityMIBCompliances": ciscoPortSecurityMIBCompliances,
       "ciscoPortSecurityMIBCompliance": ciscoPortSecurityMIBCompliance,
       "ciscoPortSecurityMIBCompliance1": ciscoPortSecurityMIBCompliance1,
       "ciscoPortSecurityMIBCompliance2": ciscoPortSecurityMIBCompliance2,
       "ciscoPortSecurityMIBCompliance3": ciscoPortSecurityMIBCompliance3,
       "ciscoPortSecurityMIBCompliance4": ciscoPortSecurityMIBCompliance4,
       "ciscoPortSecurityMIBGroups": ciscoPortSecurityMIBGroups,
       "cpsGlobalGroup": cpsGlobalGroup,
       "cpsInterfaceGroup": cpsInterfaceGroup,
       "cpsExtInterfaceGroup": cpsExtInterfaceGroup,
       "cpsNotificationGroup": cpsNotificationGroup,
       "cpsUnicastFloodingInterfaceGroup": cpsUnicastFloodingInterfaceGroup,
       "cpsShutdownTimeoutInterfaceGroup": cpsShutdownTimeoutInterfaceGroup,
       "cpsIfVlanSecureMacAddrGroup": cpsIfVlanSecureMacAddrGroup,
       "cpsInterfaceGroup1": cpsInterfaceGroup1,
       "cpsExtConfigInterfaceGroup": cpsExtConfigInterfaceGroup,
       "cpsIfVlanGroup": cpsIfVlanGroup,
       "cpsGlobalClearAddressGroup": cpsGlobalClearAddressGroup,
       "cpsInterfaceGroup2": cpsInterfaceGroup2,
       "cpsTrunkSecureNotificationGroup": cpsTrunkSecureNotificationGroup,
       "cpsIfMultiVlanGroup": cpsIfMultiVlanGroup,
       "cpsIfVlanSecureNotificationGroup": cpsIfVlanSecureNotificationGroup,
       "cpsExtInterfaceGroup1": cpsExtInterfaceGroup1}
)
