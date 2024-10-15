# SNMP MIB module (JUNIPER-RSVP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-RSVP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:14:08 2024
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

(jnxMibs,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxMibs")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

jnxRsvpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 30)
)
jnxRsvpMIB.setRevisions(
        ("2007-06-28 09:30",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxRsvpOperation_ObjectIdentity = ObjectIdentity
jnxRsvpOperation = _JnxRsvpOperation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 30, 1)
)
_JnxRsvpSessionTable_Object = MibTable
jnxRsvpSessionTable = _JnxRsvpSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 30, 1, 1)
)
if mibBuilder.loadTexts:
    jnxRsvpSessionTable.setStatus("current")
_JnxRsvpSessionEntry_Object = MibTableRow
jnxRsvpSessionEntry = _JnxRsvpSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 30, 1, 1, 1)
)
jnxRsvpSessionEntry.setIndexNames(
    (0, "JUNIPER-RSVP-MIB", "jnxRsvpSessionName"),
    (0, "JUNIPER-RSVP-MIB", "jnxRsvpSessionIndex"),
)
if mibBuilder.loadTexts:
    jnxRsvpSessionEntry.setStatus("current")


class _JnxRsvpSessionName_Type(DisplayString):
    """Custom type jnxRsvpSessionName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_JnxRsvpSessionName_Type.__name__ = "DisplayString"
_JnxRsvpSessionName_Object = MibTableColumn
jnxRsvpSessionName = _JnxRsvpSessionName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 30, 1, 1, 1, 1),
    _JnxRsvpSessionName_Type()
)
jnxRsvpSessionName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxRsvpSessionName.setStatus("current")
_JnxRsvpSessionIndex_Type = Unsigned32
_JnxRsvpSessionIndex_Object = MibTableColumn
jnxRsvpSessionIndex = _JnxRsvpSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 30, 1, 1, 1, 2),
    _JnxRsvpSessionIndex_Type()
)
jnxRsvpSessionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxRsvpSessionIndex.setStatus("current")


class _JnxRsvpSessionState_Type(Integer32):
    """Custom type jnxRsvpSessionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_JnxRsvpSessionState_Type.__name__ = "Integer32"
_JnxRsvpSessionState_Object = MibTableColumn
jnxRsvpSessionState = _JnxRsvpSessionState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 30, 1, 1, 1, 3),
    _JnxRsvpSessionState_Type()
)
jnxRsvpSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRsvpSessionState.setStatus("current")
_JnxRsvpSessionFrom_Type = IpAddress
_JnxRsvpSessionFrom_Object = MibTableColumn
jnxRsvpSessionFrom = _JnxRsvpSessionFrom_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 30, 1, 1, 1, 4),
    _JnxRsvpSessionFrom_Type()
)
jnxRsvpSessionFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRsvpSessionFrom.setStatus("current")
_JnxRsvpSessionTo_Type = IpAddress
_JnxRsvpSessionTo_Object = MibTableColumn
jnxRsvpSessionTo = _JnxRsvpSessionTo_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 30, 1, 1, 1, 5),
    _JnxRsvpSessionTo_Type()
)
jnxRsvpSessionTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRsvpSessionTo.setStatus("current")


class _JnxRsvpSessionLspId_Type(Unsigned32):
    """Custom type jnxRsvpSessionLspId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JnxRsvpSessionLspId_Type.__name__ = "Unsigned32"
_JnxRsvpSessionLspId_Object = MibTableColumn
jnxRsvpSessionLspId = _JnxRsvpSessionLspId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 30, 1, 1, 1, 6),
    _JnxRsvpSessionLspId_Type()
)
jnxRsvpSessionLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRsvpSessionLspId.setStatus("current")


class _JnxRsvpSessionTunnelId_Type(Unsigned32):
    """Custom type jnxRsvpSessionTunnelId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JnxRsvpSessionTunnelId_Type.__name__ = "Unsigned32"
_JnxRsvpSessionTunnelId_Object = MibTableColumn
jnxRsvpSessionTunnelId = _JnxRsvpSessionTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 30, 1, 1, 1, 7),
    _JnxRsvpSessionTunnelId_Type()
)
jnxRsvpSessionTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRsvpSessionTunnelId.setStatus("current")


class _JnxRsvpSessionPathType_Type(Integer32):
    """Custom type jnxRsvpSessionPathType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2),
          ("unknown", 3))
    )


_JnxRsvpSessionPathType_Type.__name__ = "Integer32"
_JnxRsvpSessionPathType_Object = MibTableColumn
jnxRsvpSessionPathType = _JnxRsvpSessionPathType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 30, 1, 1, 1, 8),
    _JnxRsvpSessionPathType_Type()
)
jnxRsvpSessionPathType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRsvpSessionPathType.setStatus("current")


class _JnxRsvpSessionRole_Type(Integer32):
    """Custom type jnxRsvpSessionRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("egress", 3),
          ("ingress", 1),
          ("transit", 2))
    )


_JnxRsvpSessionRole_Type.__name__ = "Integer32"
_JnxRsvpSessionRole_Object = MibTableColumn
jnxRsvpSessionRole = _JnxRsvpSessionRole_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 30, 1, 1, 1, 9),
    _JnxRsvpSessionRole_Type()
)
jnxRsvpSessionRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRsvpSessionRole.setStatus("current")
_JnxRsvpSessionDiscontinuityTime_Type = TimeStamp
_JnxRsvpSessionDiscontinuityTime_Object = MibTableColumn
jnxRsvpSessionDiscontinuityTime = _JnxRsvpSessionDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 30, 1, 1, 1, 10),
    _JnxRsvpSessionDiscontinuityTime_Type()
)
jnxRsvpSessionDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRsvpSessionDiscontinuityTime.setStatus("current")
_JnxRsvpSessionMplsOctets_Type = Counter64
_JnxRsvpSessionMplsOctets_Object = MibTableColumn
jnxRsvpSessionMplsOctets = _JnxRsvpSessionMplsOctets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 30, 1, 1, 1, 11),
    _JnxRsvpSessionMplsOctets_Type()
)
jnxRsvpSessionMplsOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRsvpSessionMplsOctets.setStatus("current")
_JnxRsvpSessionMplsPackets_Type = Counter64
_JnxRsvpSessionMplsPackets_Object = MibTableColumn
jnxRsvpSessionMplsPackets = _JnxRsvpSessionMplsPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 30, 1, 1, 1, 12),
    _JnxRsvpSessionMplsPackets_Type()
)
jnxRsvpSessionMplsPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRsvpSessionMplsPackets.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-RSVP-MIB",
    **{"jnxRsvpMIB": jnxRsvpMIB,
       "jnxRsvpOperation": jnxRsvpOperation,
       "jnxRsvpSessionTable": jnxRsvpSessionTable,
       "jnxRsvpSessionEntry": jnxRsvpSessionEntry,
       "jnxRsvpSessionName": jnxRsvpSessionName,
       "jnxRsvpSessionIndex": jnxRsvpSessionIndex,
       "jnxRsvpSessionState": jnxRsvpSessionState,
       "jnxRsvpSessionFrom": jnxRsvpSessionFrom,
       "jnxRsvpSessionTo": jnxRsvpSessionTo,
       "jnxRsvpSessionLspId": jnxRsvpSessionLspId,
       "jnxRsvpSessionTunnelId": jnxRsvpSessionTunnelId,
       "jnxRsvpSessionPathType": jnxRsvpSessionPathType,
       "jnxRsvpSessionRole": jnxRsvpSessionRole,
       "jnxRsvpSessionDiscontinuityTime": jnxRsvpSessionDiscontinuityTime,
       "jnxRsvpSessionMplsOctets": jnxRsvpSessionMplsOctets,
       "jnxRsvpSessionMplsPackets": jnxRsvpSessionMplsPackets}
)
