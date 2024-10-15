# SNMP MIB module (RUCKUS-ZD-AAA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RUCKUS-ZD-AAA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:48:52 2024
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(ruckusZDWLANModule,) = mibBuilder.importSymbols(
    "RUCKUS-ROOT-MIB",
    "ruckusZDWLANModule")

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

ruckusZDAAAMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuckusZDAAAObjects_ObjectIdentity = ObjectIdentity
ruckusZDAAAObjects = _RuckusZDAAAObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 3, 1)
)
_RuckusZDAAAConfig_ObjectIdentity = ObjectIdentity
ruckusZDAAAConfig = _RuckusZDAAAConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 3, 1, 1)
)
_RuckusZDAAAConfigTable_Object = MibTable
ruckusZDAAAConfigTable = _RuckusZDAAAConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ruckusZDAAAConfigTable.setStatus("current")
_RuckusZDAAAConfigEntry_Object = MibTableRow
ruckusZDAAAConfigEntry = _RuckusZDAAAConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 3, 1, 1, 1, 1)
)
ruckusZDAAAConfigEntry.setIndexNames(
    (0, "RUCKUS-ZD-AAA-MIB", "ruckusZDAAAConfigID"),
)
if mibBuilder.loadTexts:
    ruckusZDAAAConfigEntry.setStatus("current")


class _RuckusZDAAAConfigID_Type(Integer32):
    """Custom type ruckusZDAAAConfigID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 32),
    )


_RuckusZDAAAConfigID_Type.__name__ = "Integer32"
_RuckusZDAAAConfigID_Object = MibTableColumn
ruckusZDAAAConfigID = _RuckusZDAAAConfigID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 3, 1, 1, 1, 1, 1),
    _RuckusZDAAAConfigID_Type()
)
ruckusZDAAAConfigID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruckusZDAAAConfigID.setStatus("current")


class _RuckusZDAAAConfigName_Type(OctetString):
    """Custom type ruckusZDAAAConfigName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_RuckusZDAAAConfigName_Type.__name__ = "OctetString"
_RuckusZDAAAConfigName_Object = MibTableColumn
ruckusZDAAAConfigName = _RuckusZDAAAConfigName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 3, 1, 1, 1, 1, 2),
    _RuckusZDAAAConfigName_Type()
)
ruckusZDAAAConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDAAAConfigName.setStatus("current")


class _RuckusZDAAAConfigServiceType_Type(Integer32):
    """Custom type ruckusZDAAAConfigServiceType based on Integer32"""
    defaultValue = 3

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
        *(("aaa-accounting", 4),
          ("aaa-authentication", 3),
          ("active-directory", 1),
          ("ldap-directory", 2))
    )


_RuckusZDAAAConfigServiceType_Type.__name__ = "Integer32"
_RuckusZDAAAConfigServiceType_Object = MibTableColumn
ruckusZDAAAConfigServiceType = _RuckusZDAAAConfigServiceType_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 3, 1, 1, 1, 1, 3),
    _RuckusZDAAAConfigServiceType_Type()
)
ruckusZDAAAConfigServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDAAAConfigServiceType.setStatus("current")
_RuckusZDAAAConfigRowStatus_Type = RowStatus
_RuckusZDAAAConfigRowStatus_Object = MibTableColumn
ruckusZDAAAConfigRowStatus = _RuckusZDAAAConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 3, 1, 1, 1, 1, 10),
    _RuckusZDAAAConfigRowStatus_Type()
)
ruckusZDAAAConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusZDAAAConfigRowStatus.setStatus("current")
_RuckusZDAAASvrTable_Object = MibTable
ruckusZDAAASvrTable = _RuckusZDAAASvrTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ruckusZDAAASvrTable.setStatus("current")
_RuckusZDAAASvrEntry_Object = MibTableRow
ruckusZDAAASvrEntry = _RuckusZDAAASvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 3, 1, 1, 2, 1)
)
ruckusZDAAASvrEntry.setIndexNames(
    (0, "RUCKUS-ZD-AAA-MIB", "ruckusZDAAAConfigID"),
)
if mibBuilder.loadTexts:
    ruckusZDAAASvrEntry.setStatus("current")


class _RuckusZDAAARadiusBackupControl_Type(Integer32):
    """Custom type ruckusZDAAARadiusBackupControl based on Integer32"""
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


_RuckusZDAAARadiusBackupControl_Type.__name__ = "Integer32"
_RuckusZDAAARadiusBackupControl_Object = MibTableColumn
ruckusZDAAARadiusBackupControl = _RuckusZDAAARadiusBackupControl_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 3, 1, 1, 2, 1, 5),
    _RuckusZDAAARadiusBackupControl_Type()
)
ruckusZDAAARadiusBackupControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDAAARadiusBackupControl.setStatus("current")


class _RuckusZDAAARadiusPrimarySvrIpAddress_Type(OctetString):
    """Custom type ruckusZDAAARadiusPrimarySvrIpAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 40),
    )


_RuckusZDAAARadiusPrimarySvrIpAddress_Type.__name__ = "OctetString"
_RuckusZDAAARadiusPrimarySvrIpAddress_Object = MibTableColumn
ruckusZDAAARadiusPrimarySvrIpAddress = _RuckusZDAAARadiusPrimarySvrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 3, 1, 1, 2, 1, 10),
    _RuckusZDAAARadiusPrimarySvrIpAddress_Type()
)
ruckusZDAAARadiusPrimarySvrIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDAAARadiusPrimarySvrIpAddress.setStatus("current")
_RuckusZDAAARadiusPrimarySvrPort_Type = Integer32
_RuckusZDAAARadiusPrimarySvrPort_Object = MibTableColumn
ruckusZDAAARadiusPrimarySvrPort = _RuckusZDAAARadiusPrimarySvrPort_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 3, 1, 1, 2, 1, 11),
    _RuckusZDAAARadiusPrimarySvrPort_Type()
)
ruckusZDAAARadiusPrimarySvrPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDAAARadiusPrimarySvrPort.setStatus("current")


class _RuckusZDAAARadiusPrimarySvrPasswd_Type(OctetString):
    """Custom type ruckusZDAAARadiusPrimarySvrPasswd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuckusZDAAARadiusPrimarySvrPasswd_Type.__name__ = "OctetString"
_RuckusZDAAARadiusPrimarySvrPasswd_Object = MibTableColumn
ruckusZDAAARadiusPrimarySvrPasswd = _RuckusZDAAARadiusPrimarySvrPasswd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 3, 1, 1, 2, 1, 12),
    _RuckusZDAAARadiusPrimarySvrPasswd_Type()
)
ruckusZDAAARadiusPrimarySvrPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDAAARadiusPrimarySvrPasswd.setStatus("current")


class _RuckusZDAAARadiusSecondarySvrIpAddress_Type(OctetString):
    """Custom type ruckusZDAAARadiusSecondarySvrIpAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 40),
    )


_RuckusZDAAARadiusSecondarySvrIpAddress_Type.__name__ = "OctetString"
_RuckusZDAAARadiusSecondarySvrIpAddress_Object = MibTableColumn
ruckusZDAAARadiusSecondarySvrIpAddress = _RuckusZDAAARadiusSecondarySvrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 3, 1, 1, 2, 1, 15),
    _RuckusZDAAARadiusSecondarySvrIpAddress_Type()
)
ruckusZDAAARadiusSecondarySvrIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDAAARadiusSecondarySvrIpAddress.setStatus("current")
_RuckusZDAAARadiusSecondarySvrPort_Type = Integer32
_RuckusZDAAARadiusSecondarySvrPort_Object = MibTableColumn
ruckusZDAAARadiusSecondarySvrPort = _RuckusZDAAARadiusSecondarySvrPort_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 3, 1, 1, 2, 1, 16),
    _RuckusZDAAARadiusSecondarySvrPort_Type()
)
ruckusZDAAARadiusSecondarySvrPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDAAARadiusSecondarySvrPort.setStatus("current")


class _RuckusZDAAARadiusSecondarySvrPasswd_Type(OctetString):
    """Custom type ruckusZDAAARadiusSecondarySvrPasswd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuckusZDAAARadiusSecondarySvrPasswd_Type.__name__ = "OctetString"
_RuckusZDAAARadiusSecondarySvrPasswd_Object = MibTableColumn
ruckusZDAAARadiusSecondarySvrPasswd = _RuckusZDAAARadiusSecondarySvrPasswd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 3, 1, 1, 2, 1, 17),
    _RuckusZDAAARadiusSecondarySvrPasswd_Type()
)
ruckusZDAAARadiusSecondarySvrPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDAAARadiusSecondarySvrPasswd.setStatus("current")


class _RuckusZDAAARadiusFailoverTimeout_Type(Integer32):
    """Custom type ruckusZDAAARadiusFailoverTimeout based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 10),
    )


_RuckusZDAAARadiusFailoverTimeout_Type.__name__ = "Integer32"
_RuckusZDAAARadiusFailoverTimeout_Object = MibTableColumn
ruckusZDAAARadiusFailoverTimeout = _RuckusZDAAARadiusFailoverTimeout_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 3, 1, 1, 2, 1, 20),
    _RuckusZDAAARadiusFailoverTimeout_Type()
)
ruckusZDAAARadiusFailoverTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDAAARadiusFailoverTimeout.setStatus("current")


class _RuckusZDAAARadiusFailoverRetry_Type(Integer32):
    """Custom type ruckusZDAAARadiusFailoverRetry based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_RuckusZDAAARadiusFailoverRetry_Type.__name__ = "Integer32"
_RuckusZDAAARadiusFailoverRetry_Object = MibTableColumn
ruckusZDAAARadiusFailoverRetry = _RuckusZDAAARadiusFailoverRetry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 3, 1, 1, 2, 1, 21),
    _RuckusZDAAARadiusFailoverRetry_Type()
)
ruckusZDAAARadiusFailoverRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDAAARadiusFailoverRetry.setStatus("current")


class _RuckusZDAAARadiusFailoverReconnectPrimary_Type(Integer32):
    """Custom type ruckusZDAAARadiusFailoverReconnectPrimary based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_RuckusZDAAARadiusFailoverReconnectPrimary_Type.__name__ = "Integer32"
_RuckusZDAAARadiusFailoverReconnectPrimary_Object = MibTableColumn
ruckusZDAAARadiusFailoverReconnectPrimary = _RuckusZDAAARadiusFailoverReconnectPrimary_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 3, 1, 1, 2, 1, 22),
    _RuckusZDAAARadiusFailoverReconnectPrimary_Type()
)
ruckusZDAAARadiusFailoverReconnectPrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDAAARadiusFailoverReconnectPrimary.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUCKUS-ZD-AAA-MIB",
    **{"ruckusZDAAAMIB": ruckusZDAAAMIB,
       "ruckusZDAAAObjects": ruckusZDAAAObjects,
       "ruckusZDAAAConfig": ruckusZDAAAConfig,
       "ruckusZDAAAConfigTable": ruckusZDAAAConfigTable,
       "ruckusZDAAAConfigEntry": ruckusZDAAAConfigEntry,
       "ruckusZDAAAConfigID": ruckusZDAAAConfigID,
       "ruckusZDAAAConfigName": ruckusZDAAAConfigName,
       "ruckusZDAAAConfigServiceType": ruckusZDAAAConfigServiceType,
       "ruckusZDAAAConfigRowStatus": ruckusZDAAAConfigRowStatus,
       "ruckusZDAAASvrTable": ruckusZDAAASvrTable,
       "ruckusZDAAASvrEntry": ruckusZDAAASvrEntry,
       "ruckusZDAAARadiusBackupControl": ruckusZDAAARadiusBackupControl,
       "ruckusZDAAARadiusPrimarySvrIpAddress": ruckusZDAAARadiusPrimarySvrIpAddress,
       "ruckusZDAAARadiusPrimarySvrPort": ruckusZDAAARadiusPrimarySvrPort,
       "ruckusZDAAARadiusPrimarySvrPasswd": ruckusZDAAARadiusPrimarySvrPasswd,
       "ruckusZDAAARadiusSecondarySvrIpAddress": ruckusZDAAARadiusSecondarySvrIpAddress,
       "ruckusZDAAARadiusSecondarySvrPort": ruckusZDAAARadiusSecondarySvrPort,
       "ruckusZDAAARadiusSecondarySvrPasswd": ruckusZDAAARadiusSecondarySvrPasswd,
       "ruckusZDAAARadiusFailoverTimeout": ruckusZDAAARadiusFailoverTimeout,
       "ruckusZDAAARadiusFailoverRetry": ruckusZDAAARadiusFailoverRetry,
       "ruckusZDAAARadiusFailoverReconnectPrimary": ruckusZDAAARadiusFailoverReconnectPrimary}
)
