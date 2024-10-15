# SNMP MIB module (RAPID-CITY-BAY-STACK) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RAPID-CITY-BAY-STACK
# Produced by pysmi-1.5.4 at Mon Oct 14 22:44:34 2024
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

(rcBayStack,) = mibBuilder.importSymbols(
    "RAPID-CITY",
    "rcBayStack")

(rcMltId,) = mibBuilder.importSymbols(
    "RC-MLT-MIB",
    "rcMltId")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

rcBayStackMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 40, 1)
)
rcBayStackMIB.setRevisions(
        ("2007-12-14 00:00",
         "2004-09-29 00:00",
         "2004-07-20 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcBayStackObjects_ObjectIdentity = ObjectIdentity
rcBayStackObjects = _RcBayStackObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 40, 1, 1)
)
_RcBayStackTftpExt_ObjectIdentity = ObjectIdentity
rcBayStackTftpExt = _RcBayStackTftpExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 40, 1, 1, 1)
)


class _RcBayStackTftpAction_Type(Integer32):
    """Custom type rcBayStackTftpAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("deleteSshDsaAuthKey", 3),
          ("downloadSshPublicKeys", 2),
          ("none", 1))
    )


_RcBayStackTftpAction_Type.__name__ = "Integer32"
_RcBayStackTftpAction_Object = MibScalar
rcBayStackTftpAction = _RcBayStackTftpAction_Object(
    (1, 3, 6, 1, 4, 1, 2272, 40, 1, 1, 1, 1),
    _RcBayStackTftpAction_Type()
)
rcBayStackTftpAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcBayStackTftpAction.setStatus("current")
_RcBayStackSshSessionTable_Object = MibTable
rcBayStackSshSessionTable = _RcBayStackSshSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 40, 1, 1, 2)
)
if mibBuilder.loadTexts:
    rcBayStackSshSessionTable.setStatus("current")
_RcBayStackSshSessionEntry_Object = MibTableRow
rcBayStackSshSessionEntry = _RcBayStackSshSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2272, 40, 1, 1, 2, 1)
)
rcBayStackSshSessionEntry.setIndexNames(
    (0, "RAPID-CITY-BAY-STACK", "rcBayStackSshSessionId"),
)
if mibBuilder.loadTexts:
    rcBayStackSshSessionEntry.setStatus("current")


class _RcBayStackSshSessionId_Type(Integer32):
    """Custom type rcBayStackSshSessionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RcBayStackSshSessionId_Type.__name__ = "Integer32"
_RcBayStackSshSessionId_Object = MibTableColumn
rcBayStackSshSessionId = _RcBayStackSshSessionId_Object(
    (1, 3, 6, 1, 4, 1, 2272, 40, 1, 1, 2, 1, 1),
    _RcBayStackSshSessionId_Type()
)
rcBayStackSshSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcBayStackSshSessionId.setStatus("current")
_RcBayStackSshSessionIp_Type = IpAddress
_RcBayStackSshSessionIp_Object = MibTableColumn
rcBayStackSshSessionIp = _RcBayStackSshSessionIp_Object(
    (1, 3, 6, 1, 4, 1, 2272, 40, 1, 1, 2, 1, 2),
    _RcBayStackSshSessionIp_Type()
)
rcBayStackSshSessionIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcBayStackSshSessionIp.setStatus("current")
_RcBayStackSshSessionInetAddressType_Type = InetAddressType
_RcBayStackSshSessionInetAddressType_Object = MibTableColumn
rcBayStackSshSessionInetAddressType = _RcBayStackSshSessionInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2272, 40, 1, 1, 2, 1, 3),
    _RcBayStackSshSessionInetAddressType_Type()
)
rcBayStackSshSessionInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcBayStackSshSessionInetAddressType.setStatus("current")
_RcBayStackSshSessionInetAddress_Type = InetAddress
_RcBayStackSshSessionInetAddress_Object = MibTableColumn
rcBayStackSshSessionInetAddress = _RcBayStackSshSessionInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 2272, 40, 1, 1, 2, 1, 4),
    _RcBayStackSshSessionInetAddress_Type()
)
rcBayStackSshSessionInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcBayStackSshSessionInetAddress.setStatus("current")
_RcBayStackSshExt_ObjectIdentity = ObjectIdentity
rcBayStackSshExt = _RcBayStackSshExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 40, 1, 1, 3)
)


class _RcBayStackSshDsaHostKeyStatus_Type(Integer32):
    """Custom type rcBayStackSshDsaHostKeyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("generated", 2),
          ("generating", 3),
          ("notGenerated", 1))
    )


_RcBayStackSshDsaHostKeyStatus_Type.__name__ = "Integer32"
_RcBayStackSshDsaHostKeyStatus_Object = MibScalar
rcBayStackSshDsaHostKeyStatus = _RcBayStackSshDsaHostKeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 2272, 40, 1, 1, 3, 1),
    _RcBayStackSshDsaHostKeyStatus_Type()
)
rcBayStackSshDsaHostKeyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcBayStackSshDsaHostKeyStatus.setStatus("current")
_RcBayStackTraps_ObjectIdentity = ObjectIdentity
rcBayStackTraps = _RcBayStackTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 40, 1, 21)
)
_RcBayStackTraps0_ObjectIdentity = ObjectIdentity
rcBayStackTraps0 = _RcBayStackTraps0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 40, 1, 21, 0)
)

# Managed Objects groups


# Notification objects

rcMltConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2272, 40, 1, 21, 0, 1)
)
rcMltConfigError.setObjects(
    ("RC-MLT-MIB", "rcMltId")
)
if mibBuilder.loadTexts:
    rcMltConfigError.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAPID-CITY-BAY-STACK",
    **{"rcBayStackMIB": rcBayStackMIB,
       "rcBayStackObjects": rcBayStackObjects,
       "rcBayStackTftpExt": rcBayStackTftpExt,
       "rcBayStackTftpAction": rcBayStackTftpAction,
       "rcBayStackSshSessionTable": rcBayStackSshSessionTable,
       "rcBayStackSshSessionEntry": rcBayStackSshSessionEntry,
       "rcBayStackSshSessionId": rcBayStackSshSessionId,
       "rcBayStackSshSessionIp": rcBayStackSshSessionIp,
       "rcBayStackSshSessionInetAddressType": rcBayStackSshSessionInetAddressType,
       "rcBayStackSshSessionInetAddress": rcBayStackSshSessionInetAddress,
       "rcBayStackSshExt": rcBayStackSshExt,
       "rcBayStackSshDsaHostKeyStatus": rcBayStackSshDsaHostKeyStatus,
       "rcBayStackTraps": rcBayStackTraps,
       "rcBayStackTraps0": rcBayStackTraps0,
       "rcMltConfigError": rcMltConfigError}
)
