# SNMP MIB module (ASCEND-RADIUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-RADIUS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:39 2024
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

(radiusGroup,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "radiusGroup")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RadiusNumAuthServers_Type = Integer32
_RadiusNumAuthServers_Object = MibScalar
radiusNumAuthServers = _RadiusNumAuthServers_Object(
    (1, 3, 6, 1, 4, 1, 529, 13, 1),
    _RadiusNumAuthServers_Type()
)
radiusNumAuthServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusNumAuthServers.setStatus("mandatory")
_RadiusNumAcctServers_Type = Integer32
_RadiusNumAcctServers_Object = MibScalar
radiusNumAcctServers = _RadiusNumAcctServers_Object(
    (1, 3, 6, 1, 4, 1, 529, 13, 2),
    _RadiusNumAcctServers_Type()
)
radiusNumAcctServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusNumAcctServers.setStatus("mandatory")
_RadiusAuthStatsTable_Object = MibTable
radiusAuthStatsTable = _RadiusAuthStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 13, 3)
)
if mibBuilder.loadTexts:
    radiusAuthStatsTable.setStatus("mandatory")
_RadiusAuthStatsEntry_Object = MibTableRow
radiusAuthStatsEntry = _RadiusAuthStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 13, 3, 1)
)
radiusAuthStatsEntry.setIndexNames(
    (0, "ASCEND-RADIUS-MIB", "radAuthServerIndex"),
)
if mibBuilder.loadTexts:
    radiusAuthStatsEntry.setStatus("mandatory")
_RadAuthServerIndex_Type = Integer32
_RadAuthServerIndex_Object = MibTableColumn
radAuthServerIndex = _RadAuthServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 13, 3, 1, 1),
    _RadAuthServerIndex_Type()
)
radAuthServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radAuthServerIndex.setStatus("mandatory")
_RadAuthLoginRqstSent_Type = Integer32
_RadAuthLoginRqstSent_Object = MibTableColumn
radAuthLoginRqstSent = _RadAuthLoginRqstSent_Object(
    (1, 3, 6, 1, 4, 1, 529, 13, 3, 1, 2),
    _RadAuthLoginRqstSent_Type()
)
radAuthLoginRqstSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radAuthLoginRqstSent.setStatus("mandatory")
_RadAuthOtherRqstSent_Type = Integer32
_RadAuthOtherRqstSent_Object = MibTableColumn
radAuthOtherRqstSent = _RadAuthOtherRqstSent_Object(
    (1, 3, 6, 1, 4, 1, 529, 13, 3, 1, 3),
    _RadAuthOtherRqstSent_Type()
)
radAuthOtherRqstSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radAuthOtherRqstSent.setStatus("mandatory")
_RadAuthRqstTimedOut_Type = Integer32
_RadAuthRqstTimedOut_Object = MibTableColumn
radAuthRqstTimedOut = _RadAuthRqstTimedOut_Object(
    (1, 3, 6, 1, 4, 1, 529, 13, 3, 1, 4),
    _RadAuthRqstTimedOut_Type()
)
radAuthRqstTimedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radAuthRqstTimedOut.setStatus("mandatory")
_RadAuthOtherRqstTimedOut_Type = Integer32
_RadAuthOtherRqstTimedOut_Object = MibTableColumn
radAuthOtherRqstTimedOut = _RadAuthOtherRqstTimedOut_Object(
    (1, 3, 6, 1, 4, 1, 529, 13, 3, 1, 5),
    _RadAuthOtherRqstTimedOut_Type()
)
radAuthOtherRqstTimedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radAuthOtherRqstTimedOut.setStatus("mandatory")
_RadAuthRspRcvd_Type = Integer32
_RadAuthRspRcvd_Object = MibTableColumn
radAuthRspRcvd = _RadAuthRspRcvd_Object(
    (1, 3, 6, 1, 4, 1, 529, 13, 3, 1, 6),
    _RadAuthRspRcvd_Type()
)
radAuthRspRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radAuthRspRcvd.setStatus("mandatory")
_RadAuthOtherRspRcvd_Type = Integer32
_RadAuthOtherRspRcvd_Object = MibTableColumn
radAuthOtherRspRcvd = _RadAuthOtherRspRcvd_Object(
    (1, 3, 6, 1, 4, 1, 529, 13, 3, 1, 7),
    _RadAuthOtherRspRcvd_Type()
)
radAuthOtherRspRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radAuthOtherRspRcvd.setStatus("mandatory")
_RadAuthUnexpRspRcvd_Type = Integer32
_RadAuthUnexpRspRcvd_Object = MibTableColumn
radAuthUnexpRspRcvd = _RadAuthUnexpRspRcvd_Object(
    (1, 3, 6, 1, 4, 1, 529, 13, 3, 1, 8),
    _RadAuthUnexpRspRcvd_Type()
)
radAuthUnexpRspRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radAuthUnexpRspRcvd.setStatus("mandatory")
_RadAuthBadRspRcvd_Type = Integer32
_RadAuthBadRspRcvd_Object = MibTableColumn
radAuthBadRspRcvd = _RadAuthBadRspRcvd_Object(
    (1, 3, 6, 1, 4, 1, 529, 13, 3, 1, 9),
    _RadAuthBadRspRcvd_Type()
)
radAuthBadRspRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radAuthBadRspRcvd.setStatus("mandatory")
_RadAuthAckRspRcvd_Type = Integer32
_RadAuthAckRspRcvd_Object = MibTableColumn
radAuthAckRspRcvd = _RadAuthAckRspRcvd_Object(
    (1, 3, 6, 1, 4, 1, 529, 13, 3, 1, 10),
    _RadAuthAckRspRcvd_Type()
)
radAuthAckRspRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radAuthAckRspRcvd.setStatus("mandatory")
_RadAuthHostIPAddress_Type = IpAddress
_RadAuthHostIPAddress_Object = MibTableColumn
radAuthHostIPAddress = _RadAuthHostIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 13, 3, 1, 11),
    _RadAuthHostIPAddress_Type()
)
radAuthHostIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radAuthHostIPAddress.setStatus("mandatory")


class _RadAuthCurrentServerFlag_Type(Integer32):
    """Custom type radAuthCurrentServerFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("current", 2),
          ("standby", 1))
    )


_RadAuthCurrentServerFlag_Type.__name__ = "Integer32"
_RadAuthCurrentServerFlag_Object = MibTableColumn
radAuthCurrentServerFlag = _RadAuthCurrentServerFlag_Object(
    (1, 3, 6, 1, 4, 1, 529, 13, 3, 1, 12),
    _RadAuthCurrentServerFlag_Type()
)
radAuthCurrentServerFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radAuthCurrentServerFlag.setStatus("mandatory")
_RadiusAcctStatsTable_Object = MibTable
radiusAcctStatsTable = _RadiusAcctStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 13, 4)
)
if mibBuilder.loadTexts:
    radiusAcctStatsTable.setStatus("mandatory")
_RadiusAcctStatsEntry_Object = MibTableRow
radiusAcctStatsEntry = _RadiusAcctStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 13, 4, 1)
)
radiusAcctStatsEntry.setIndexNames(
    (0, "ASCEND-RADIUS-MIB", "radAcctServerIndex"),
)
if mibBuilder.loadTexts:
    radiusAcctStatsEntry.setStatus("mandatory")
_RadAcctServerIndex_Type = Integer32
_RadAcctServerIndex_Object = MibTableColumn
radAcctServerIndex = _RadAcctServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 13, 4, 1, 1),
    _RadAcctServerIndex_Type()
)
radAcctServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radAcctServerIndex.setStatus("mandatory")
_RadAcctRqstSent_Type = Integer32
_RadAcctRqstSent_Object = MibTableColumn
radAcctRqstSent = _RadAcctRqstSent_Object(
    (1, 3, 6, 1, 4, 1, 529, 13, 4, 1, 2),
    _RadAcctRqstSent_Type()
)
radAcctRqstSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radAcctRqstSent.setStatus("mandatory")
_RadAcctRqstTimedOut_Type = Integer32
_RadAcctRqstTimedOut_Object = MibTableColumn
radAcctRqstTimedOut = _RadAcctRqstTimedOut_Object(
    (1, 3, 6, 1, 4, 1, 529, 13, 4, 1, 3),
    _RadAcctRqstTimedOut_Type()
)
radAcctRqstTimedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radAcctRqstTimedOut.setStatus("mandatory")
_RadAcctRspRcvd_Type = Integer32
_RadAcctRspRcvd_Object = MibTableColumn
radAcctRspRcvd = _RadAcctRspRcvd_Object(
    (1, 3, 6, 1, 4, 1, 529, 13, 4, 1, 4),
    _RadAcctRspRcvd_Type()
)
radAcctRspRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radAcctRspRcvd.setStatus("mandatory")
_RadAcctUnexpRspRcvd_Type = Integer32
_RadAcctUnexpRspRcvd_Object = MibTableColumn
radAcctUnexpRspRcvd = _RadAcctUnexpRspRcvd_Object(
    (1, 3, 6, 1, 4, 1, 529, 13, 4, 1, 5),
    _RadAcctUnexpRspRcvd_Type()
)
radAcctUnexpRspRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radAcctUnexpRspRcvd.setStatus("mandatory")
_RadAcctHostIPAddress_Type = IpAddress
_RadAcctHostIPAddress_Object = MibTableColumn
radAcctHostIPAddress = _RadAcctHostIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 13, 4, 1, 6),
    _RadAcctHostIPAddress_Type()
)
radAcctHostIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radAcctHostIPAddress.setStatus("mandatory")


class _RadAcctCurrentServerFlag_Type(Integer32):
    """Custom type radAcctCurrentServerFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_RadAcctCurrentServerFlag_Type.__name__ = "Integer32"
_RadAcctCurrentServerFlag_Object = MibTableColumn
radAcctCurrentServerFlag = _RadAcctCurrentServerFlag_Object(
    (1, 3, 6, 1, 4, 1, 529, 13, 4, 1, 7),
    _RadAcctCurrentServerFlag_Type()
)
radAcctCurrentServerFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radAcctCurrentServerFlag.setStatus("mandatory")


class _RadiusNewNASPortIDFormat_Type(Integer32):
    """Custom type radiusNewNASPortIDFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_RadiusNewNASPortIDFormat_Type.__name__ = "Integer32"
_RadiusNewNASPortIDFormat_Object = MibScalar
radiusNewNASPortIDFormat = _RadiusNewNASPortIDFormat_Object(
    (1, 3, 6, 1, 4, 1, 529, 13, 5),
    _RadiusNewNASPortIDFormat_Type()
)
radiusNewNASPortIDFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusNewNASPortIDFormat.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-RADIUS-MIB",
    **{"radiusNumAuthServers": radiusNumAuthServers,
       "radiusNumAcctServers": radiusNumAcctServers,
       "radiusAuthStatsTable": radiusAuthStatsTable,
       "radiusAuthStatsEntry": radiusAuthStatsEntry,
       "radAuthServerIndex": radAuthServerIndex,
       "radAuthLoginRqstSent": radAuthLoginRqstSent,
       "radAuthOtherRqstSent": radAuthOtherRqstSent,
       "radAuthRqstTimedOut": radAuthRqstTimedOut,
       "radAuthOtherRqstTimedOut": radAuthOtherRqstTimedOut,
       "radAuthRspRcvd": radAuthRspRcvd,
       "radAuthOtherRspRcvd": radAuthOtherRspRcvd,
       "radAuthUnexpRspRcvd": radAuthUnexpRspRcvd,
       "radAuthBadRspRcvd": radAuthBadRspRcvd,
       "radAuthAckRspRcvd": radAuthAckRspRcvd,
       "radAuthHostIPAddress": radAuthHostIPAddress,
       "radAuthCurrentServerFlag": radAuthCurrentServerFlag,
       "radiusAcctStatsTable": radiusAcctStatsTable,
       "radiusAcctStatsEntry": radiusAcctStatsEntry,
       "radAcctServerIndex": radAcctServerIndex,
       "radAcctRqstSent": radAcctRqstSent,
       "radAcctRqstTimedOut": radAcctRqstTimedOut,
       "radAcctRspRcvd": radAcctRspRcvd,
       "radAcctUnexpRspRcvd": radAcctUnexpRspRcvd,
       "radAcctHostIPAddress": radAcctHostIPAddress,
       "radAcctCurrentServerFlag": radAcctCurrentServerFlag,
       "radiusNewNASPortIDFormat": radiusNewNASPortIDFormat}
)
