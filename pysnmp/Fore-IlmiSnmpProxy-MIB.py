# SNMP MIB module (Fore-IlmiSnmpProxy-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Fore-IlmiSnmpProxy-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:47:05 2024
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

(ilmisnmp,) = mibBuilder.importSymbols(
    "Fore-Common-MIB",
    "ilmisnmp")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

foreIlmiSnmpProxyModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 326, 1, 10, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IspTable_Object = MibTable
ispTable = _IspTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 10, 2)
)
if mibBuilder.loadTexts:
    ispTable.setStatus("current")
_IspEntry_Object = MibTableRow
ispEntry = _IspEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 10, 2, 1)
)
ispEntry.setIndexNames(
    (0, "Fore-IlmiSnmpProxy-MIB", "ispPort"),
    (0, "Fore-IlmiSnmpProxy-MIB", "ispVPI"),
    (0, "Fore-IlmiSnmpProxy-MIB", "ispIndex"),
)
if mibBuilder.loadTexts:
    ispEntry.setStatus("current")
_IspPort_Type = Integer32
_IspPort_Object = MibTableColumn
ispPort = _IspPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 10, 2, 1, 1),
    _IspPort_Type()
)
ispPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ispPort.setStatus("current")
_IspVPI_Type = Integer32
_IspVPI_Object = MibTableColumn
ispVPI = _IspVPI_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 10, 2, 1, 2),
    _IspVPI_Type()
)
ispVPI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ispVPI.setStatus("current")
_IspIndex_Type = Integer32
_IspIndex_Object = MibTableColumn
ispIndex = _IspIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 10, 2, 1, 3),
    _IspIndex_Type()
)
ispIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ispIndex.setStatus("current")


class _IspOperation_Type(Integer32):
    """Custom type ispOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("get", 1),
          ("getnext", 2))
    )


_IspOperation_Type.__name__ = "Integer32"
_IspOperation_Object = MibTableColumn
ispOperation = _IspOperation_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 10, 2, 1, 4),
    _IspOperation_Type()
)
ispOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ispOperation.setStatus("current")
_IspOID_Type = ObjectIdentifier
_IspOID_Object = MibTableColumn
ispOID = _IspOID_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 10, 2, 1, 5),
    _IspOID_Type()
)
ispOID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ispOID.setStatus("current")


class _IspConfStatus_Type(Integer32):
    """Custom type ispConfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doEveryIlmiRestart", 2),
          ("doOnce", 1))
    )


_IspConfStatus_Type.__name__ = "Integer32"
_IspConfStatus_Object = MibTableColumn
ispConfStatus = _IspConfStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 10, 2, 1, 6),
    _IspConfStatus_Type()
)
ispConfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ispConfStatus.setStatus("current")


class _IspOperStatus_Type(Integer32):
    """Custom type ispOperStatus based on Integer32"""
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
        *(("failure", 4),
          ("idle", 1),
          ("inProgress", 2),
          ("success", 3))
    )


_IspOperStatus_Type.__name__ = "Integer32"
_IspOperStatus_Object = MibTableColumn
ispOperStatus = _IspOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 10, 2, 1, 7),
    _IspOperStatus_Type()
)
ispOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ispOperStatus.setStatus("current")
_IspCommunityName_Type = DisplayString
_IspCommunityName_Object = MibTableColumn
ispCommunityName = _IspCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 10, 2, 1, 8),
    _IspCommunityName_Type()
)
ispCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ispCommunityName.setStatus("current")
_IspRespOID_Type = ObjectIdentifier
_IspRespOID_Object = MibTableColumn
ispRespOID = _IspRespOID_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 10, 2, 1, 9),
    _IspRespOID_Type()
)
ispRespOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ispRespOID.setStatus("current")
_IspValue_Type = OctetString
_IspValue_Object = MibTableColumn
ispValue = _IspValue_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 10, 2, 1, 10),
    _IspValue_Type()
)
ispValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ispValue.setStatus("current")
_IspRowStatus_Type = RowStatus
_IspRowStatus_Object = MibTableColumn
ispRowStatus = _IspRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 10, 2, 1, 11),
    _IspRowStatus_Type()
)
ispRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ispRowStatus.setStatus("current")
_IspNextIndex_Type = Integer32
_IspNextIndex_Object = MibScalar
ispNextIndex = _IspNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 10, 2, 2),
    _IspNextIndex_Type()
)
ispNextIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ispNextIndex.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Fore-IlmiSnmpProxy-MIB",
    **{"foreIlmiSnmpProxyModule": foreIlmiSnmpProxyModule,
       "ispTable": ispTable,
       "ispEntry": ispEntry,
       "ispPort": ispPort,
       "ispVPI": ispVPI,
       "ispIndex": ispIndex,
       "ispOperation": ispOperation,
       "ispOID": ispOID,
       "ispConfStatus": ispConfStatus,
       "ispOperStatus": ispOperStatus,
       "ispCommunityName": ispCommunityName,
       "ispRespOID": ispRespOID,
       "ispValue": ispValue,
       "ispRowStatus": ispRowStatus,
       "ispNextIndex": ispNextIndex}
)
