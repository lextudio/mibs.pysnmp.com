# SNMP MIB module (BAY-STACK-IP-FWD-NH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAY-STACK-IP-FWD-NH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:00 2024
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

(bayStackMibs,) = mibBuilder.importSymbols(
    "SYNOPTICS-ROOT-MIB",
    "bayStackMibs")


# MODULE-IDENTITY

bayStackIpFwdNhMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 35)
)
bayStackIpFwdNhMib.setRevisions(
        ("2009-09-30 00:00",
         "2009-09-11 00:00",
         "2009-08-26 00:00",
         "2009-08-21 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BayStackIpFwdNhNotifications_ObjectIdentity = ObjectIdentity
bayStackIpFwdNhNotifications = _BayStackIpFwdNhNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 35, 0)
)
_BayStackIpFwdNhObjects_ObjectIdentity = ObjectIdentity
bayStackIpFwdNhObjects = _BayStackIpFwdNhObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 35, 1)
)
_BsifnScalars_ObjectIdentity = ObjectIdentity
bsifnScalars = _BsifnScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 35, 1, 1)
)
_BsifnIpForwardingNextHopAdminEnabled_Type = TruthValue
_BsifnIpForwardingNextHopAdminEnabled_Object = MibScalar
bsifnIpForwardingNextHopAdminEnabled = _BsifnIpForwardingNextHopAdminEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 35, 1, 1, 1),
    _BsifnIpForwardingNextHopAdminEnabled_Type()
)
bsifnIpForwardingNextHopAdminEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsifnIpForwardingNextHopAdminEnabled.setStatus("current")
_BsifnIpForwardingNextHopOperEnabled_Type = TruthValue
_BsifnIpForwardingNextHopOperEnabled_Object = MibScalar
bsifnIpForwardingNextHopOperEnabled = _BsifnIpForwardingNextHopOperEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 35, 1, 1, 2),
    _BsifnIpForwardingNextHopOperEnabled_Type()
)
bsifnIpForwardingNextHopOperEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsifnIpForwardingNextHopOperEnabled.setStatus("current")
_BsifnPolicyTable_Object = MibTable
bsifnPolicyTable = _BsifnPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 35, 1, 2)
)
if mibBuilder.loadTexts:
    bsifnPolicyTable.setStatus("current")
_BsifnPolicyEntry_Object = MibTableRow
bsifnPolicyEntry = _BsifnPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 35, 1, 2, 1)
)
bsifnPolicyEntry.setIndexNames(
    (1, "BAY-STACK-IP-FWD-NH-MIB", "bsifnPolicyName"),
)
if mibBuilder.loadTexts:
    bsifnPolicyEntry.setStatus("current")


class _BsifnPolicyName_Type(SnmpAdminString):
    """Custom type bsifnPolicyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BsifnPolicyName_Type.__name__ = "SnmpAdminString"
_BsifnPolicyName_Object = MibTableColumn
bsifnPolicyName = _BsifnPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 35, 1, 2, 1, 1),
    _BsifnPolicyName_Type()
)
bsifnPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsifnPolicyName.setStatus("current")
_BsifnPolicyMatchInetAddressType_Type = InetAddressType
_BsifnPolicyMatchInetAddressType_Object = MibTableColumn
bsifnPolicyMatchInetAddressType = _BsifnPolicyMatchInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 35, 1, 2, 1, 2),
    _BsifnPolicyMatchInetAddressType_Type()
)
bsifnPolicyMatchInetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsifnPolicyMatchInetAddressType.setStatus("current")
_BsifnPolicyMatchInetAddress_Type = InetAddress
_BsifnPolicyMatchInetAddress_Object = MibTableColumn
bsifnPolicyMatchInetAddress = _BsifnPolicyMatchInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 35, 1, 2, 1, 3),
    _BsifnPolicyMatchInetAddress_Type()
)
bsifnPolicyMatchInetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsifnPolicyMatchInetAddress.setStatus("current")
_BsifnPolicyMatchInetAddressMask_Type = InetAddressPrefixLength
_BsifnPolicyMatchInetAddressMask_Object = MibTableColumn
bsifnPolicyMatchInetAddressMask = _BsifnPolicyMatchInetAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 35, 1, 2, 1, 4),
    _BsifnPolicyMatchInetAddressMask_Type()
)
bsifnPolicyMatchInetAddressMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsifnPolicyMatchInetAddressMask.setStatus("current")
_BsifnPolicyMatchPortMin_Type = InetPortNumber
_BsifnPolicyMatchPortMin_Object = MibTableColumn
bsifnPolicyMatchPortMin = _BsifnPolicyMatchPortMin_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 35, 1, 2, 1, 5),
    _BsifnPolicyMatchPortMin_Type()
)
bsifnPolicyMatchPortMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsifnPolicyMatchPortMin.setStatus("current")
_BsifnPolicyMatchPortMax_Type = InetPortNumber
_BsifnPolicyMatchPortMax_Object = MibTableColumn
bsifnPolicyMatchPortMax = _BsifnPolicyMatchPortMax_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 35, 1, 2, 1, 6),
    _BsifnPolicyMatchPortMax_Type()
)
bsifnPolicyMatchPortMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsifnPolicyMatchPortMax.setStatus("current")
_BsifnPolicySetNextHopInetAddressType_Type = InetAddressType
_BsifnPolicySetNextHopInetAddressType_Object = MibTableColumn
bsifnPolicySetNextHopInetAddressType = _BsifnPolicySetNextHopInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 35, 1, 2, 1, 7),
    _BsifnPolicySetNextHopInetAddressType_Type()
)
bsifnPolicySetNextHopInetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsifnPolicySetNextHopInetAddressType.setStatus("current")
_BsifnPolicySetNextHopInetAddress_Type = InetAddress
_BsifnPolicySetNextHopInetAddress_Object = MibTableColumn
bsifnPolicySetNextHopInetAddress = _BsifnPolicySetNextHopInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 35, 1, 2, 1, 8),
    _BsifnPolicySetNextHopInetAddress_Type()
)
bsifnPolicySetNextHopInetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsifnPolicySetNextHopInetAddress.setStatus("current")
_BsifnPolicyRowStatus_Type = RowStatus
_BsifnPolicyRowStatus_Object = MibTableColumn
bsifnPolicyRowStatus = _BsifnPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 35, 1, 2, 1, 9),
    _BsifnPolicyRowStatus_Type()
)
bsifnPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsifnPolicyRowStatus.setStatus("current")
_BsifnPolicyInterfaceTable_Object = MibTable
bsifnPolicyInterfaceTable = _BsifnPolicyInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 35, 1, 3)
)
if mibBuilder.loadTexts:
    bsifnPolicyInterfaceTable.setStatus("current")
_BsifnPolicyInterfaceEntry_Object = MibTableRow
bsifnPolicyInterfaceEntry = _BsifnPolicyInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 35, 1, 3, 1)
)
bsifnPolicyInterfaceEntry.setIndexNames(
    (0, "BAY-STACK-IP-FWD-NH-MIB", "bsifnPolicyInterfaceIndex"),
    (1, "BAY-STACK-IP-FWD-NH-MIB", "bsifnPolicyInterfacePolicyName"),
)
if mibBuilder.loadTexts:
    bsifnPolicyInterfaceEntry.setStatus("current")
_BsifnPolicyInterfaceIndex_Type = InterfaceIndex
_BsifnPolicyInterfaceIndex_Object = MibTableColumn
bsifnPolicyInterfaceIndex = _BsifnPolicyInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 35, 1, 3, 1, 1),
    _BsifnPolicyInterfaceIndex_Type()
)
bsifnPolicyInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsifnPolicyInterfaceIndex.setStatus("current")


class _BsifnPolicyInterfacePolicyName_Type(SnmpAdminString):
    """Custom type bsifnPolicyInterfacePolicyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BsifnPolicyInterfacePolicyName_Type.__name__ = "SnmpAdminString"
_BsifnPolicyInterfacePolicyName_Object = MibTableColumn
bsifnPolicyInterfacePolicyName = _BsifnPolicyInterfacePolicyName_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 35, 1, 3, 1, 2),
    _BsifnPolicyInterfacePolicyName_Type()
)
bsifnPolicyInterfacePolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsifnPolicyInterfacePolicyName.setStatus("current")


class _BsifnPolicyInterfaceMode_Type(Integer32):
    """Custom type bsifnPolicyInterfaceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("normalRouting", 2))
    )


_BsifnPolicyInterfaceMode_Type.__name__ = "Integer32"
_BsifnPolicyInterfaceMode_Object = MibTableColumn
bsifnPolicyInterfaceMode = _BsifnPolicyInterfaceMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 35, 1, 3, 1, 3),
    _BsifnPolicyInterfaceMode_Type()
)
bsifnPolicyInterfaceMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsifnPolicyInterfaceMode.setStatus("current")


class _BsifnPolicyInterfaceOperationalStatus_Type(Integer32):
    """Custom type bsifnPolicyInterfaceOperationalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_BsifnPolicyInterfaceOperationalStatus_Type.__name__ = "Integer32"
_BsifnPolicyInterfaceOperationalStatus_Object = MibTableColumn
bsifnPolicyInterfaceOperationalStatus = _BsifnPolicyInterfaceOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 35, 1, 3, 1, 4),
    _BsifnPolicyInterfaceOperationalStatus_Type()
)
bsifnPolicyInterfaceOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsifnPolicyInterfaceOperationalStatus.setStatus("current")


class _BsifnPolicyInterfaceAction_Type(Integer32):
    """Custom type bsifnPolicyInterfaceAction based on Integer32"""
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
        *(("drop", 1),
          ("enable", 3),
          ("normalRouting", 2),
          ("notApplicable", 4))
    )


_BsifnPolicyInterfaceAction_Type.__name__ = "Integer32"
_BsifnPolicyInterfaceAction_Object = MibTableColumn
bsifnPolicyInterfaceAction = _BsifnPolicyInterfaceAction_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 35, 1, 3, 1, 5),
    _BsifnPolicyInterfaceAction_Type()
)
bsifnPolicyInterfaceAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsifnPolicyInterfaceAction.setStatus("current")
_BsifnPolicyInterfaceRowStatus_Type = RowStatus
_BsifnPolicyInterfaceRowStatus_Object = MibTableColumn
bsifnPolicyInterfaceRowStatus = _BsifnPolicyInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 35, 1, 3, 1, 6),
    _BsifnPolicyInterfaceRowStatus_Type()
)
bsifnPolicyInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsifnPolicyInterfaceRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAY-STACK-IP-FWD-NH-MIB",
    **{"bayStackIpFwdNhMib": bayStackIpFwdNhMib,
       "bayStackIpFwdNhNotifications": bayStackIpFwdNhNotifications,
       "bayStackIpFwdNhObjects": bayStackIpFwdNhObjects,
       "bsifnScalars": bsifnScalars,
       "bsifnIpForwardingNextHopAdminEnabled": bsifnIpForwardingNextHopAdminEnabled,
       "bsifnIpForwardingNextHopOperEnabled": bsifnIpForwardingNextHopOperEnabled,
       "bsifnPolicyTable": bsifnPolicyTable,
       "bsifnPolicyEntry": bsifnPolicyEntry,
       "bsifnPolicyName": bsifnPolicyName,
       "bsifnPolicyMatchInetAddressType": bsifnPolicyMatchInetAddressType,
       "bsifnPolicyMatchInetAddress": bsifnPolicyMatchInetAddress,
       "bsifnPolicyMatchInetAddressMask": bsifnPolicyMatchInetAddressMask,
       "bsifnPolicyMatchPortMin": bsifnPolicyMatchPortMin,
       "bsifnPolicyMatchPortMax": bsifnPolicyMatchPortMax,
       "bsifnPolicySetNextHopInetAddressType": bsifnPolicySetNextHopInetAddressType,
       "bsifnPolicySetNextHopInetAddress": bsifnPolicySetNextHopInetAddress,
       "bsifnPolicyRowStatus": bsifnPolicyRowStatus,
       "bsifnPolicyInterfaceTable": bsifnPolicyInterfaceTable,
       "bsifnPolicyInterfaceEntry": bsifnPolicyInterfaceEntry,
       "bsifnPolicyInterfaceIndex": bsifnPolicyInterfaceIndex,
       "bsifnPolicyInterfacePolicyName": bsifnPolicyInterfacePolicyName,
       "bsifnPolicyInterfaceMode": bsifnPolicyInterfaceMode,
       "bsifnPolicyInterfaceOperationalStatus": bsifnPolicyInterfaceOperationalStatus,
       "bsifnPolicyInterfaceAction": bsifnPolicyInterfaceAction,
       "bsifnPolicyInterfaceRowStatus": bsifnPolicyInterfaceRowStatus}
)
