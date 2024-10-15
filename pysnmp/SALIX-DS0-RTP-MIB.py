# SNMP MIB module (SALIX-DS0-RTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SALIX-DS0-RTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:23 2024
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

(platform1,) = mibBuilder.importSymbols(
    "SALIX-MIB",
    "platform1")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

salixDsx0RtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SalixDsx0RtpMIBObjects_ObjectIdentity = ObjectIdentity
salixDsx0RtpMIBObjects = _SalixDsx0RtpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 3, 1)
)
_SalixDsx0RtpConnectionTable_Object = MibTable
salixDsx0RtpConnectionTable = _SalixDsx0RtpConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    salixDsx0RtpConnectionTable.setStatus("current")
_SalixDsx0RtpConnectionEntry_Object = MibTableRow
salixDsx0RtpConnectionEntry = _SalixDsx0RtpConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 3, 1, 1, 1)
)
salixDsx0RtpConnectionEntry.setIndexNames(
    (0, "SALIX-DS0-RTP-MIB", "salixDsx0RtpConnectionInterface"),
    (0, "SALIX-DS0-RTP-MIB", "salixDsx0RtpConnectionSrcIpAddress"),
    (0, "SALIX-DS0-RTP-MIB", "salixDsx0RtpConnectionSrcPort"),
    (0, "SALIX-DS0-RTP-MIB", "salixDsx0RtpConnectionDestIpAddress"),
    (0, "SALIX-DS0-RTP-MIB", "salixDsx0RtpConnectionDestPort"),
)
if mibBuilder.loadTexts:
    salixDsx0RtpConnectionEntry.setStatus("current")
_SalixDsx0RtpConnectionInterface_Type = InterfaceIndex
_SalixDsx0RtpConnectionInterface_Object = MibTableColumn
salixDsx0RtpConnectionInterface = _SalixDsx0RtpConnectionInterface_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 3, 1, 1, 1, 1),
    _SalixDsx0RtpConnectionInterface_Type()
)
salixDsx0RtpConnectionInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    salixDsx0RtpConnectionInterface.setStatus("current")
_SalixDsx0RtpConnectionSrcIpAddress_Type = IpAddress
_SalixDsx0RtpConnectionSrcIpAddress_Object = MibTableColumn
salixDsx0RtpConnectionSrcIpAddress = _SalixDsx0RtpConnectionSrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 3, 1, 1, 1, 2),
    _SalixDsx0RtpConnectionSrcIpAddress_Type()
)
salixDsx0RtpConnectionSrcIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    salixDsx0RtpConnectionSrcIpAddress.setStatus("current")


class _SalixDsx0RtpConnectionSrcPort_Type(Integer32):
    """Custom type salixDsx0RtpConnectionSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SalixDsx0RtpConnectionSrcPort_Type.__name__ = "Integer32"
_SalixDsx0RtpConnectionSrcPort_Object = MibTableColumn
salixDsx0RtpConnectionSrcPort = _SalixDsx0RtpConnectionSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 3, 1, 1, 1, 3),
    _SalixDsx0RtpConnectionSrcPort_Type()
)
salixDsx0RtpConnectionSrcPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    salixDsx0RtpConnectionSrcPort.setStatus("current")
_SalixDsx0RtpConnectionDestIpAddress_Type = IpAddress
_SalixDsx0RtpConnectionDestIpAddress_Object = MibTableColumn
salixDsx0RtpConnectionDestIpAddress = _SalixDsx0RtpConnectionDestIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 3, 1, 1, 1, 4),
    _SalixDsx0RtpConnectionDestIpAddress_Type()
)
salixDsx0RtpConnectionDestIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    salixDsx0RtpConnectionDestIpAddress.setStatus("current")


class _SalixDsx0RtpConnectionDestPort_Type(Integer32):
    """Custom type salixDsx0RtpConnectionDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SalixDsx0RtpConnectionDestPort_Type.__name__ = "Integer32"
_SalixDsx0RtpConnectionDestPort_Object = MibTableColumn
salixDsx0RtpConnectionDestPort = _SalixDsx0RtpConnectionDestPort_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 3, 1, 1, 1, 5),
    _SalixDsx0RtpConnectionDestPort_Type()
)
salixDsx0RtpConnectionDestPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    salixDsx0RtpConnectionDestPort.setStatus("current")


class _SalixDsx0RtpConnectionDirection_Type(Integer32):
    """Custom type salixDsx0RtpConnectionDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 3),
          ("dsx02rtp", 2),
          ("rtp2dsx0", 1))
    )


_SalixDsx0RtpConnectionDirection_Type.__name__ = "Integer32"
_SalixDsx0RtpConnectionDirection_Object = MibTableColumn
salixDsx0RtpConnectionDirection = _SalixDsx0RtpConnectionDirection_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 3, 1, 1, 1, 6),
    _SalixDsx0RtpConnectionDirection_Type()
)
salixDsx0RtpConnectionDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixDsx0RtpConnectionDirection.setStatus("current")


class _SalixDsx0RtpConnectionOperStatus_Type(Integer32):
    """Custom type salixDsx0RtpConnectionOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("unknown", 3),
          ("up", 1))
    )


_SalixDsx0RtpConnectionOperStatus_Type.__name__ = "Integer32"
_SalixDsx0RtpConnectionOperStatus_Object = MibTableColumn
salixDsx0RtpConnectionOperStatus = _SalixDsx0RtpConnectionOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 3, 1, 1, 1, 7),
    _SalixDsx0RtpConnectionOperStatus_Type()
)
salixDsx0RtpConnectionOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixDsx0RtpConnectionOperStatus.setStatus("current")
_SalixDsx0RtpConnectionRowStatus_Type = RowStatus
_SalixDsx0RtpConnectionRowStatus_Object = MibTableColumn
salixDsx0RtpConnectionRowStatus = _SalixDsx0RtpConnectionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 3, 1, 1, 1, 8),
    _SalixDsx0RtpConnectionRowStatus_Type()
)
salixDsx0RtpConnectionRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    salixDsx0RtpConnectionRowStatus.setStatus("current")
_SalixDsx0RtpMIBTraps_ObjectIdentity = ObjectIdentity
salixDsx0RtpMIBTraps = _SalixDsx0RtpMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 3, 2)
)
_SalixDsx0RtpMIBTrapPrefix_ObjectIdentity = ObjectIdentity
salixDsx0RtpMIBTrapPrefix = _SalixDsx0RtpMIBTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 3, 2, 0)
)
_SalixDsx0RtpMIBCompliance_ObjectIdentity = ObjectIdentity
salixDsx0RtpMIBCompliance = _SalixDsx0RtpMIBCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 3, 3)
)
_SalixDsx0RtpGroups_ObjectIdentity = ObjectIdentity
salixDsx0RtpGroups = _SalixDsx0RtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 3, 3, 1)
)
_SalixDsx0RtpCompliances_ObjectIdentity = ObjectIdentity
salixDsx0RtpCompliances = _SalixDsx0RtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 3, 3, 2)
)

# Managed Objects groups

salixDsx0RtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 3, 3, 1, 3)
)
salixDsx0RtpGroup.setObjects(
      *(("SALIX-DS0-RTP-MIB", "salixDsx0RtpConnectionDirection"),
        ("SALIX-DS0-RTP-MIB", "salixDsx0RtpConnectionOperStatus"),
        ("SALIX-DS0-RTP-MIB", "salixDsx0RtpConnectionRowStatus"))
)
if mibBuilder.loadTexts:
    salixDsx0RtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

salixDsx0RtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 3, 3, 2, 1)
)
if mibBuilder.loadTexts:
    salixDsx0RtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SALIX-DS0-RTP-MIB",
    **{"salixDsx0RtpMIB": salixDsx0RtpMIB,
       "salixDsx0RtpMIBObjects": salixDsx0RtpMIBObjects,
       "salixDsx0RtpConnectionTable": salixDsx0RtpConnectionTable,
       "salixDsx0RtpConnectionEntry": salixDsx0RtpConnectionEntry,
       "salixDsx0RtpConnectionInterface": salixDsx0RtpConnectionInterface,
       "salixDsx0RtpConnectionSrcIpAddress": salixDsx0RtpConnectionSrcIpAddress,
       "salixDsx0RtpConnectionSrcPort": salixDsx0RtpConnectionSrcPort,
       "salixDsx0RtpConnectionDestIpAddress": salixDsx0RtpConnectionDestIpAddress,
       "salixDsx0RtpConnectionDestPort": salixDsx0RtpConnectionDestPort,
       "salixDsx0RtpConnectionDirection": salixDsx0RtpConnectionDirection,
       "salixDsx0RtpConnectionOperStatus": salixDsx0RtpConnectionOperStatus,
       "salixDsx0RtpConnectionRowStatus": salixDsx0RtpConnectionRowStatus,
       "salixDsx0RtpMIBTraps": salixDsx0RtpMIBTraps,
       "salixDsx0RtpMIBTrapPrefix": salixDsx0RtpMIBTrapPrefix,
       "salixDsx0RtpMIBCompliance": salixDsx0RtpMIBCompliance,
       "salixDsx0RtpGroups": salixDsx0RtpGroups,
       "salixDsx0RtpGroup": salixDsx0RtpGroup,
       "salixDsx0RtpCompliances": salixDsx0RtpCompliances,
       "salixDsx0RtpCompliance": salixDsx0RtpCompliance}
)
