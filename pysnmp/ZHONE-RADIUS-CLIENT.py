# SNMP MIB module (ZHONE-RADIUS-CLIENT) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHONE-RADIUS-CLIENT
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:42 2024
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(zhoneModules,
 zhoneRadius) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneModules",
    "zhoneRadius")


# MODULE-IDENTITY

comRadiusClient = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 6, 112)
)
comRadiusClient.setRevisions(
        ("2006-11-15 14:07",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZhoneRadiusClient_ObjectIdentity = ObjectIdentity
zhoneRadiusClient = _ZhoneRadiusClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 14, 1)
)
if mibBuilder.loadTexts:
    zhoneRadiusClient.setStatus("current")
_ZhoneRadiusClientTable_Object = MibTable
zhoneRadiusClientTable = _ZhoneRadiusClientTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 14, 1, 1)
)
if mibBuilder.loadTexts:
    zhoneRadiusClientTable.setStatus("current")
_ZhoneRadiusClientEntry_Object = MibTableRow
zhoneRadiusClientEntry = _ZhoneRadiusClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 14, 1, 1, 1)
)
zhoneRadiusClientEntry.setIndexNames(
    (0, "ZHONE-RADIUS-CLIENT", "zhoneRadiusClientIndex"),
    (0, "ZHONE-RADIUS-CLIENT", "zhoneRadiusClientId"),
)
if mibBuilder.loadTexts:
    zhoneRadiusClientEntry.setStatus("current")


class _ZhoneRadiusClientIndex_Type(Integer32):
    """Custom type zhoneRadiusClientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2137483647),
    )


_ZhoneRadiusClientIndex_Type.__name__ = "Integer32"
_ZhoneRadiusClientIndex_Object = MibTableColumn
zhoneRadiusClientIndex = _ZhoneRadiusClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 14, 1, 1, 1, 1),
    _ZhoneRadiusClientIndex_Type()
)
zhoneRadiusClientIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneRadiusClientIndex.setStatus("current")


class _ZhoneRadiusClientId_Type(Integer32):
    """Custom type zhoneRadiusClientId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2137483647),
    )


_ZhoneRadiusClientId_Type.__name__ = "Integer32"
_ZhoneRadiusClientId_Object = MibTableColumn
zhoneRadiusClientId = _ZhoneRadiusClientId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 14, 1, 1, 1, 2),
    _ZhoneRadiusClientId_Type()
)
zhoneRadiusClientId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneRadiusClientId.setStatus("current")
_ZhoneRadiusClientRowStatus_Type = RowStatus
_ZhoneRadiusClientRowStatus_Object = MibTableColumn
zhoneRadiusClientRowStatus = _ZhoneRadiusClientRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 14, 1, 1, 1, 3),
    _ZhoneRadiusClientRowStatus_Type()
)
zhoneRadiusClientRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneRadiusClientRowStatus.setStatus("current")
_ZhoneRadiusClientServerName_Type = DisplayString
_ZhoneRadiusClientServerName_Object = MibTableColumn
zhoneRadiusClientServerName = _ZhoneRadiusClientServerName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 14, 1, 1, 1, 4),
    _ZhoneRadiusClientServerName_Type()
)
zhoneRadiusClientServerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneRadiusClientServerName.setStatus("current")


class _ZhoneRadiusClientUdpPortNumber_Type(Integer32):
    """Custom type zhoneRadiusClientUdpPortNumber based on Integer32"""
    defaultValue = 1812

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZhoneRadiusClientUdpPortNumber_Type.__name__ = "Integer32"
_ZhoneRadiusClientUdpPortNumber_Object = MibTableColumn
zhoneRadiusClientUdpPortNumber = _ZhoneRadiusClientUdpPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 14, 1, 1, 1, 5),
    _ZhoneRadiusClientUdpPortNumber_Type()
)
zhoneRadiusClientUdpPortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneRadiusClientUdpPortNumber.setStatus("current")
_ZhoneRadiusClientSharedSecret_Type = DisplayString
_ZhoneRadiusClientSharedSecret_Object = MibTableColumn
zhoneRadiusClientSharedSecret = _ZhoneRadiusClientSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 14, 1, 1, 1, 6),
    _ZhoneRadiusClientSharedSecret_Type()
)
zhoneRadiusClientSharedSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneRadiusClientSharedSecret.setStatus("current")


class _ZhoneRadiusClientRetryCount_Type(Integer32):
    """Custom type zhoneRadiusClientRetryCount based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ZhoneRadiusClientRetryCount_Type.__name__ = "Integer32"
_ZhoneRadiusClientRetryCount_Object = MibTableColumn
zhoneRadiusClientRetryCount = _ZhoneRadiusClientRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 14, 1, 1, 1, 7),
    _ZhoneRadiusClientRetryCount_Type()
)
zhoneRadiusClientRetryCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneRadiusClientRetryCount.setStatus("current")


class _ZhoneRadiusClientRetryInterval_Type(Integer32):
    """Custom type zhoneRadiusClientRetryInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_ZhoneRadiusClientRetryInterval_Type.__name__ = "Integer32"
_ZhoneRadiusClientRetryInterval_Object = MibTableColumn
zhoneRadiusClientRetryInterval = _ZhoneRadiusClientRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 14, 1, 1, 1, 8),
    _ZhoneRadiusClientRetryInterval_Type()
)
zhoneRadiusClientRetryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneRadiusClientRetryInterval.setStatus("current")

# Managed Objects groups

zhoneRadiusObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 4, 14, 2)
)
zhoneRadiusObjectGroup.setObjects(
      *(("ZHONE-RADIUS-CLIENT", "zhoneRadiusClientServerName"),
        ("ZHONE-RADIUS-CLIENT", "zhoneRadiusClientUdpPortNumber"),
        ("ZHONE-RADIUS-CLIENT", "zhoneRadiusClientSharedSecret"),
        ("ZHONE-RADIUS-CLIENT", "zhoneRadiusClientRetryCount"),
        ("ZHONE-RADIUS-CLIENT", "zhoneRadiusClientRetryInterval"))
)
if mibBuilder.loadTexts:
    zhoneRadiusObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHONE-RADIUS-CLIENT",
    **{"zhoneRadiusClient": zhoneRadiusClient,
       "zhoneRadiusClientTable": zhoneRadiusClientTable,
       "zhoneRadiusClientEntry": zhoneRadiusClientEntry,
       "zhoneRadiusClientIndex": zhoneRadiusClientIndex,
       "zhoneRadiusClientId": zhoneRadiusClientId,
       "zhoneRadiusClientRowStatus": zhoneRadiusClientRowStatus,
       "zhoneRadiusClientServerName": zhoneRadiusClientServerName,
       "zhoneRadiusClientUdpPortNumber": zhoneRadiusClientUdpPortNumber,
       "zhoneRadiusClientSharedSecret": zhoneRadiusClientSharedSecret,
       "zhoneRadiusClientRetryCount": zhoneRadiusClientRetryCount,
       "zhoneRadiusClientRetryInterval": zhoneRadiusClientRetryInterval,
       "zhoneRadiusObjectGroup": zhoneRadiusObjectGroup,
       "comRadiusClient": comRadiusClient}
)
