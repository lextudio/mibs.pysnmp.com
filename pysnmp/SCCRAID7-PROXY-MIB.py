# SNMP MIB module (SCCRAID7-PROXY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SCCRAID7-PROXY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:50:01 2024
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

(raid7proxy,) = mibBuilder.importSymbols(
    "SCC-ENTERPRISE-MIB",
    "raid7proxy")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Raid7Agent_ObjectIdentity = ObjectIdentity
raid7Agent = _Raid7Agent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1386, 2, 2, 1)
)
_Raid7proxyMibVersion_Type = Integer32
_Raid7proxyMibVersion_Object = MibScalar
raid7proxyMibVersion = _Raid7proxyMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 1386, 2, 2, 1, 1),
    _Raid7proxyMibVersion_Type()
)
raid7proxyMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raid7proxyMibVersion.setStatus("mandatory")
_Raid7proxyAgentVersion_Type = Integer32
_Raid7proxyAgentVersion_Object = MibScalar
raid7proxyAgentVersion = _Raid7proxyAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 1386, 2, 2, 1, 2),
    _Raid7proxyAgentVersion_Type()
)
raid7proxyAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raid7proxyAgentVersion.setStatus("mandatory")
_Raid7CacheLifetime_Type = Gauge32
_Raid7CacheLifetime_Object = MibScalar
raid7CacheLifetime = _Raid7CacheLifetime_Object(
    (1, 3, 6, 1, 4, 1, 1386, 2, 2, 1, 3),
    _Raid7CacheLifetime_Type()
)
raid7CacheLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raid7CacheLifetime.setStatus("mandatory")
_Raid7CacheTimeouts_Type = Counter32
_Raid7CacheTimeouts_Object = MibScalar
raid7CacheTimeouts = _Raid7CacheTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 1386, 2, 2, 1, 4),
    _Raid7CacheTimeouts_Type()
)
raid7CacheTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raid7CacheTimeouts.setStatus("mandatory")
_Raid7BadValues_Type = Counter32
_Raid7BadValues_Object = MibScalar
raid7BadValues = _Raid7BadValues_Object(
    (1, 3, 6, 1, 4, 1, 1386, 2, 2, 1, 5),
    _Raid7BadValues_Type()
)
raid7BadValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raid7BadValues.setStatus("mandatory")
_Raid7Link_ObjectIdentity = ObjectIdentity
raid7Link = _Raid7Link_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1386, 2, 2, 2)
)


class _Raid7LinkName_Type(DisplayString):
    """Custom type raid7LinkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Raid7LinkName_Type.__name__ = "DisplayString"
_Raid7LinkName_Object = MibScalar
raid7LinkName = _Raid7LinkName_Object(
    (1, 3, 6, 1, 4, 1, 1386, 2, 2, 2, 1),
    _Raid7LinkName_Type()
)
raid7LinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raid7LinkName.setStatus("mandatory")


class _Raid7LinkStatus_Type(Integer32):
    """Custom type raid7LinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("openfailed", 2),
          ("operational", 1),
          ("quiet", 3))
    )


_Raid7LinkStatus_Type.__name__ = "Integer32"
_Raid7LinkStatus_Object = MibScalar
raid7LinkStatus = _Raid7LinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 1386, 2, 2, 2, 2),
    _Raid7LinkStatus_Type()
)
raid7LinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raid7LinkStatus.setStatus("mandatory")
_Raid7LinkInactivityTime_Type = Gauge32
_Raid7LinkInactivityTime_Object = MibScalar
raid7LinkInactivityTime = _Raid7LinkInactivityTime_Object(
    (1, 3, 6, 1, 4, 1, 1386, 2, 2, 2, 3),
    _Raid7LinkInactivityTime_Type()
)
raid7LinkInactivityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raid7LinkInactivityTime.setStatus("mandatory")
_Raid7LinkRcvBytes_Type = Counter32
_Raid7LinkRcvBytes_Object = MibScalar
raid7LinkRcvBytes = _Raid7LinkRcvBytes_Object(
    (1, 3, 6, 1, 4, 1, 1386, 2, 2, 2, 4),
    _Raid7LinkRcvBytes_Type()
)
raid7LinkRcvBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raid7LinkRcvBytes.setStatus("mandatory")
_Raid7LinkXmtBytes_Type = Counter32
_Raid7LinkXmtBytes_Object = MibScalar
raid7LinkXmtBytes = _Raid7LinkXmtBytes_Object(
    (1, 3, 6, 1, 4, 1, 1386, 2, 2, 2, 5),
    _Raid7LinkXmtBytes_Type()
)
raid7LinkXmtBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raid7LinkXmtBytes.setStatus("mandatory")
_Raid7LinkRcvFrames_Type = Counter32
_Raid7LinkRcvFrames_Object = MibScalar
raid7LinkRcvFrames = _Raid7LinkRcvFrames_Object(
    (1, 3, 6, 1, 4, 1, 1386, 2, 2, 2, 6),
    _Raid7LinkRcvFrames_Type()
)
raid7LinkRcvFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raid7LinkRcvFrames.setStatus("mandatory")
_Raid7LinkXmtFrames_Type = Counter32
_Raid7LinkXmtFrames_Object = MibScalar
raid7LinkXmtFrames = _Raid7LinkXmtFrames_Object(
    (1, 3, 6, 1, 4, 1, 1386, 2, 2, 2, 7),
    _Raid7LinkXmtFrames_Type()
)
raid7LinkXmtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raid7LinkXmtFrames.setStatus("mandatory")
_Raid7LinkFramingErrors_Type = Counter32
_Raid7LinkFramingErrors_Object = MibScalar
raid7LinkFramingErrors = _Raid7LinkFramingErrors_Object(
    (1, 3, 6, 1, 4, 1, 1386, 2, 2, 2, 8),
    _Raid7LinkFramingErrors_Type()
)
raid7LinkFramingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raid7LinkFramingErrors.setStatus("mandatory")
_Raid7LinkChecksumErrors_Type = Counter32
_Raid7LinkChecksumErrors_Object = MibScalar
raid7LinkChecksumErrors = _Raid7LinkChecksumErrors_Object(
    (1, 3, 6, 1, 4, 1, 1386, 2, 2, 2, 9),
    _Raid7LinkChecksumErrors_Type()
)
raid7LinkChecksumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raid7LinkChecksumErrors.setStatus("mandatory")
_Raid7LinkBadVersions_Type = Counter32
_Raid7LinkBadVersions_Object = MibScalar
raid7LinkBadVersions = _Raid7LinkBadVersions_Object(
    (1, 3, 6, 1, 4, 1, 1386, 2, 2, 2, 10),
    _Raid7LinkBadVersions_Type()
)
raid7LinkBadVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raid7LinkBadVersions.setStatus("mandatory")
_Raid7LinkBadIds_Type = Counter32
_Raid7LinkBadIds_Object = MibScalar
raid7LinkBadIds = _Raid7LinkBadIds_Object(
    (1, 3, 6, 1, 4, 1, 1386, 2, 2, 2, 11),
    _Raid7LinkBadIds_Type()
)
raid7LinkBadIds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raid7LinkBadIds.setStatus("mandatory")
_Raid7LinkBadInstances_Type = Counter32
_Raid7LinkBadInstances_Object = MibScalar
raid7LinkBadInstances = _Raid7LinkBadInstances_Object(
    (1, 3, 6, 1, 4, 1, 1386, 2, 2, 2, 12),
    _Raid7LinkBadInstances_Type()
)
raid7LinkBadInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raid7LinkBadInstances.setStatus("mandatory")

# Managed Objects groups


# Notification objects

raid7LinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1386, 2, 2, 0, 1)
)
raid7LinkUp.setObjects(
      *(("SCCRAID7-PROXY-MIB", "raid7LinkName"),
        ("SCCRAID7-PROXY-MIB", "raid7LinkStatus"))
)
if mibBuilder.loadTexts:
    raid7LinkUp.setStatus(
        ""
    )

raid7LinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1386, 2, 2, 0, 2)
)
raid7LinkDown.setObjects(
      *(("SCCRAID7-PROXY-MIB", "raid7LinkName"),
        ("SCCRAID7-PROXY-MIB", "raid7LinkStatus"))
)
if mibBuilder.loadTexts:
    raid7LinkDown.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SCCRAID7-PROXY-MIB",
    **{"raid7LinkUp": raid7LinkUp,
       "raid7LinkDown": raid7LinkDown,
       "raid7Agent": raid7Agent,
       "raid7proxyMibVersion": raid7proxyMibVersion,
       "raid7proxyAgentVersion": raid7proxyAgentVersion,
       "raid7CacheLifetime": raid7CacheLifetime,
       "raid7CacheTimeouts": raid7CacheTimeouts,
       "raid7BadValues": raid7BadValues,
       "raid7Link": raid7Link,
       "raid7LinkName": raid7LinkName,
       "raid7LinkStatus": raid7LinkStatus,
       "raid7LinkInactivityTime": raid7LinkInactivityTime,
       "raid7LinkRcvBytes": raid7LinkRcvBytes,
       "raid7LinkXmtBytes": raid7LinkXmtBytes,
       "raid7LinkRcvFrames": raid7LinkRcvFrames,
       "raid7LinkXmtFrames": raid7LinkXmtFrames,
       "raid7LinkFramingErrors": raid7LinkFramingErrors,
       "raid7LinkChecksumErrors": raid7LinkChecksumErrors,
       "raid7LinkBadVersions": raid7LinkBadVersions,
       "raid7LinkBadIds": raid7LinkBadIds,
       "raid7LinkBadInstances": raid7LinkBadInstances}
)
