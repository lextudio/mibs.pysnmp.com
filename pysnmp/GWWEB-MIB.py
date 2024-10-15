# SNMP MIB module (GWWEB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GWWEB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:49:29 2024
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
 enterprises,
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
    "enterprises",
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

_Novell_ObjectIdentity = ObjectIdentity
novell = _Novell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23)
)
_MibDoc_ObjectIdentity = ObjectIdentity
mibDoc = _MibDoc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2)
)
_GwWeb_ObjectIdentity = ObjectIdentity
gwWeb = _GwWeb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 77)
)
_GwWebAccess_ObjectIdentity = ObjectIdentity
gwWebAccess = _GwWebAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 77, 1)
)
_GwWebAccessTable_Object = MibTable
gwWebAccessTable = _GwWebAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 77, 1, 1)
)
if mibBuilder.loadTexts:
    gwWebAccessTable.setStatus("mandatory")
_WebAccessEntry_Object = MibTableRow
webAccessEntry = _WebAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 77, 1, 1, 1)
)
webAccessEntry.setIndexNames(
    (0, "GWWEB-MIB", "gwWebAccessIndex"),
)
if mibBuilder.loadTexts:
    webAccessEntry.setStatus("mandatory")
_GwWebAccessIndex_Type = Integer32
_GwWebAccessIndex_Object = MibTableColumn
gwWebAccessIndex = _GwWebAccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 77, 1, 1, 1, 1),
    _GwWebAccessIndex_Type()
)
gwWebAccessIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwWebAccessIndex.setStatus("mandatory")


class _GwWebAccessName_Type(DisplayString):
    """Custom type gwWebAccessName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GwWebAccessName_Type.__name__ = "DisplayString"
_GwWebAccessName_Object = MibTableColumn
gwWebAccessName = _GwWebAccessName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 77, 1, 1, 1, 2),
    _GwWebAccessName_Type()
)
gwWebAccessName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwWebAccessName.setStatus("mandatory")
_GwWebAccessCompletedRequests_Type = Counter32
_GwWebAccessCompletedRequests_Object = MibTableColumn
gwWebAccessCompletedRequests = _GwWebAccessCompletedRequests_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 77, 1, 1, 1, 3),
    _GwWebAccessCompletedRequests_Type()
)
gwWebAccessCompletedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwWebAccessCompletedRequests.setStatus("mandatory")
_GwWebAccessFailedRequests_Type = Counter32
_GwWebAccessFailedRequests_Object = MibTableColumn
gwWebAccessFailedRequests = _GwWebAccessFailedRequests_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 77, 1, 1, 1, 4),
    _GwWebAccessFailedRequests_Type()
)
gwWebAccessFailedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwWebAccessFailedRequests.setStatus("mandatory")
_GwWebAccessTotalThreads_Type = Counter32
_GwWebAccessTotalThreads_Object = MibTableColumn
gwWebAccessTotalThreads = _GwWebAccessTotalThreads_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 77, 1, 1, 1, 5),
    _GwWebAccessTotalThreads_Type()
)
gwWebAccessTotalThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwWebAccessTotalThreads.setStatus("mandatory")
_GwWebAccessBusyThreads_Type = Counter32
_GwWebAccessBusyThreads_Object = MibTableColumn
gwWebAccessBusyThreads = _GwWebAccessBusyThreads_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 77, 1, 1, 1, 6),
    _GwWebAccessBusyThreads_Type()
)
gwWebAccessBusyThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwWebAccessBusyThreads.setStatus("mandatory")
_GwWebAccessPeakBusyThreads_Type = Counter32
_GwWebAccessPeakBusyThreads_Object = MibScalar
gwWebAccessPeakBusyThreads = _GwWebAccessPeakBusyThreads_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 77, 1, 1, 1, 7),
    _GwWebAccessPeakBusyThreads_Type()
)
gwWebAccessPeakBusyThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwWebAccessPeakBusyThreads.setStatus("mandatory")
_GwWebAccessCurrentUsers_Type = Counter32
_GwWebAccessCurrentUsers_Object = MibTableColumn
gwWebAccessCurrentUsers = _GwWebAccessCurrentUsers_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 77, 1, 1, 1, 8),
    _GwWebAccessCurrentUsers_Type()
)
gwWebAccessCurrentUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwWebAccessCurrentUsers.setStatus("mandatory")
_GwWebAccessTotalUsers_Type = Counter32
_GwWebAccessTotalUsers_Object = MibTableColumn
gwWebAccessTotalUsers = _GwWebAccessTotalUsers_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 77, 1, 1, 1, 9),
    _GwWebAccessTotalUsers_Type()
)
gwWebAccessTotalUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwWebAccessTotalUsers.setStatus("mandatory")
_GwWebAccessPeakUsers_Type = Counter32
_GwWebAccessPeakUsers_Object = MibTableColumn
gwWebAccessPeakUsers = _GwWebAccessPeakUsers_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 77, 1, 1, 1, 10),
    _GwWebAccessPeakUsers_Type()
)
gwWebAccessPeakUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwWebAccessPeakUsers.setStatus("mandatory")
_GwWebAccessUptime_Type = TimeTicks
_GwWebAccessUptime_Object = MibTableColumn
gwWebAccessUptime = _GwWebAccessUptime_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 77, 1, 1, 1, 11),
    _GwWebAccessUptime_Type()
)
gwWebAccessUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwWebAccessUptime.setStatus("mandatory")


class _GwWebAccessOS_Type(DisplayString):
    """Custom type gwWebAccessOS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_GwWebAccessOS_Type.__name__ = "DisplayString"
_GwWebAccessOS_Object = MibTableColumn
gwWebAccessOS = _GwWebAccessOS_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 77, 1, 1, 1, 12),
    _GwWebAccessOS_Type()
)
gwWebAccessOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwWebAccessOS.setStatus("mandatory")


class _GwWebAccessVersion_Type(DisplayString):
    """Custom type gwWebAccessVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_GwWebAccessVersion_Type.__name__ = "DisplayString"
_GwWebAccessVersion_Object = MibTableColumn
gwWebAccessVersion = _GwWebAccessVersion_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 77, 1, 1, 1, 13),
    _GwWebAccessVersion_Type()
)
gwWebAccessVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwWebAccessVersion.setStatus("mandatory")
_GwWebAccessHTTPPort_Type = Integer32
_GwWebAccessHTTPPort_Object = MibTableColumn
gwWebAccessHTTPPort = _GwWebAccessHTTPPort_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 77, 1, 1, 1, 14),
    _GwWebAccessHTTPPort_Type()
)
gwWebAccessHTTPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwWebAccessHTTPPort.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GWWEB-MIB",
    **{"novell": novell,
       "mibDoc": mibDoc,
       "gwWeb": gwWeb,
       "gwWebAccess": gwWebAccess,
       "gwWebAccessTable": gwWebAccessTable,
       "webAccessEntry": webAccessEntry,
       "gwWebAccessIndex": gwWebAccessIndex,
       "gwWebAccessName": gwWebAccessName,
       "gwWebAccessCompletedRequests": gwWebAccessCompletedRequests,
       "gwWebAccessFailedRequests": gwWebAccessFailedRequests,
       "gwWebAccessTotalThreads": gwWebAccessTotalThreads,
       "gwWebAccessBusyThreads": gwWebAccessBusyThreads,
       "gwWebAccessPeakBusyThreads": gwWebAccessPeakBusyThreads,
       "gwWebAccessCurrentUsers": gwWebAccessCurrentUsers,
       "gwWebAccessTotalUsers": gwWebAccessTotalUsers,
       "gwWebAccessPeakUsers": gwWebAccessPeakUsers,
       "gwWebAccessUptime": gwWebAccessUptime,
       "gwWebAccessOS": gwWebAccessOS,
       "gwWebAccessVersion": gwWebAccessVersion,
       "gwWebAccessHTTPPort": gwWebAccessHTTPPort}
)
