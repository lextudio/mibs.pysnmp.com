# SNMP MIB module (PAIRGAIN-IISP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PAIRGAIN-IISP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:36:23 2024
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

(AtmTrafficDescrParamIndex,) = mibBuilder.importSymbols(
    "ATM-MIB",
    "AtmTrafficDescrParamIndex")

(AtmAddr,) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmAddr")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(pgIISPMIB,) = mibBuilder.importSymbols(
    "PAIRGAIN-COMMON-HD-MIB",
    "pgIISPMIB")

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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

pgIISP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 13, 1)
)


# Types definitions



class NetPrefix(OctetString):
    """Custom type NetPrefix based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(13, 13),
    )




# TEXTUAL-CONVENTIONS



class PgAtmAddrPrefix(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )



class PgAtmPrefixLength(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 152),
    )



# MIB Managed Objects in the order of their OIDs

_PgIISPMIBObjects_ObjectIdentity = ObjectIdentity
pgIISPMIBObjects = _PgIISPMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 13, 1, 1)
)


class _PgIISPRouteAddrIndexNext_Type(Integer32):
    """Custom type pgIISPRouteAddrIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PgIISPRouteAddrIndexNext_Type.__name__ = "Integer32"
_PgIISPRouteAddrIndexNext_Object = MibScalar
pgIISPRouteAddrIndexNext = _PgIISPRouteAddrIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 13, 1, 1, 1),
    _PgIISPRouteAddrIndexNext_Type()
)
pgIISPRouteAddrIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgIISPRouteAddrIndexNext.setStatus("current")
_PgIISPRouteAddrTable_Object = MibTable
pgIISPRouteAddrTable = _PgIISPRouteAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 13, 1, 1, 2)
)
if mibBuilder.loadTexts:
    pgIISPRouteAddrTable.setStatus("current")
_PgIISPRouteAddrEntry_Object = MibTableRow
pgIISPRouteAddrEntry = _PgIISPRouteAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 13, 1, 1, 2, 1)
)
pgIISPRouteAddrEntry.setIndexNames(
    (0, "PAIRGAIN-IISP-MIB", "pgIISPRouteAddrIndex"),
    (0, "PAIRGAIN-IISP-MIB", "pgIISPRouteAddrAddress"),
    (0, "PAIRGAIN-IISP-MIB", "pgIISPRouteAddrPrefixLength"),
)
if mibBuilder.loadTexts:
    pgIISPRouteAddrEntry.setStatus("current")


class _PgIISPRouteAddrIndex_Type(Integer32):
    """Custom type pgIISPRouteAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PgIISPRouteAddrIndex_Type.__name__ = "Integer32"
_PgIISPRouteAddrIndex_Object = MibTableColumn
pgIISPRouteAddrIndex = _PgIISPRouteAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 13, 1, 1, 2, 1, 1),
    _PgIISPRouteAddrIndex_Type()
)
pgIISPRouteAddrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgIISPRouteAddrIndex.setStatus("current")
_PgIISPRouteAddrRowStatus_Type = RowStatus
_PgIISPRouteAddrRowStatus_Object = MibTableColumn
pgIISPRouteAddrRowStatus = _PgIISPRouteAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 13, 1, 1, 2, 1, 2),
    _PgIISPRouteAddrRowStatus_Type()
)
pgIISPRouteAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pgIISPRouteAddrRowStatus.setStatus("current")
_PgIISPRouteAddrAddress_Type = PgAtmAddrPrefix
_PgIISPRouteAddrAddress_Object = MibTableColumn
pgIISPRouteAddrAddress = _PgIISPRouteAddrAddress_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 13, 1, 1, 2, 1, 3),
    _PgIISPRouteAddrAddress_Type()
)
pgIISPRouteAddrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgIISPRouteAddrAddress.setStatus("current")
_PgIISPRouteAddrPrefixLength_Type = PgAtmPrefixLength
_PgIISPRouteAddrPrefixLength_Object = MibTableColumn
pgIISPRouteAddrPrefixLength = _PgIISPRouteAddrPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 13, 1, 1, 2, 1, 4),
    _PgIISPRouteAddrPrefixLength_Type()
)
pgIISPRouteAddrPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgIISPRouteAddrPrefixLength.setStatus("current")
_PgIISPRouteAddrIfIndex_Type = InterfaceIndex
_PgIISPRouteAddrIfIndex_Object = MibTableColumn
pgIISPRouteAddrIfIndex = _PgIISPRouteAddrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 13, 1, 1, 2, 1, 5),
    _PgIISPRouteAddrIfIndex_Type()
)
pgIISPRouteAddrIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgIISPRouteAddrIfIndex.setStatus("current")


class _PgIISPRouteAddrType_Type(Integer32):
    """Custom type pgIISPRouteAddrType based on Integer32"""
    defaultValue = 4

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
        *(("exterior", 4),
          ("internal", 3),
          ("other", 1),
          ("reject", 2))
    )


_PgIISPRouteAddrType_Type.__name__ = "Integer32"
_PgIISPRouteAddrType_Object = MibTableColumn
pgIISPRouteAddrType = _PgIISPRouteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 13, 1, 1, 2, 1, 6),
    _PgIISPRouteAddrType_Type()
)
pgIISPRouteAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgIISPRouteAddrType.setStatus("current")


class _PgIISPRouteAddrAdminStatus_Type(Integer32):
    """Custom type pgIISPRouteAddrAdminStatus based on Integer32"""
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


_PgIISPRouteAddrAdminStatus_Type.__name__ = "Integer32"
_PgIISPRouteAddrAdminStatus_Object = MibTableColumn
pgIISPRouteAddrAdminStatus = _PgIISPRouteAddrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 13, 1, 1, 2, 1, 7),
    _PgIISPRouteAddrAdminStatus_Type()
)
pgIISPRouteAddrAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgIISPRouteAddrAdminStatus.setStatus("current")


class _PgIISPRouteAddrOperStatus_Type(Integer32):
    """Custom type pgIISPRouteAddrOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("advertised", 3),
          ("inactive", 1))
    )


_PgIISPRouteAddrOperStatus_Type.__name__ = "Integer32"
_PgIISPRouteAddrOperStatus_Object = MibTableColumn
pgIISPRouteAddrOperStatus = _PgIISPRouteAddrOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 13, 1, 1, 2, 1, 8),
    _PgIISPRouteAddrOperStatus_Type()
)
pgIISPRouteAddrOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgIISPRouteAddrOperStatus.setStatus("current")
_PgIISPRouteAddrTimeStamp_Type = TimeStamp
_PgIISPRouteAddrTimeStamp_Object = MibTableColumn
pgIISPRouteAddrTimeStamp = _PgIISPRouteAddrTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 13, 1, 1, 2, 1, 9),
    _PgIISPRouteAddrTimeStamp_Type()
)
pgIISPRouteAddrTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgIISPRouteAddrTimeStamp.setStatus("current")


class _PgIISPNetPrefixIndexNext_Type(Integer32):
    """Custom type pgIISPNetPrefixIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PgIISPNetPrefixIndexNext_Type.__name__ = "Integer32"
_PgIISPNetPrefixIndexNext_Object = MibScalar
pgIISPNetPrefixIndexNext = _PgIISPNetPrefixIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 13, 1, 1, 3),
    _PgIISPNetPrefixIndexNext_Type()
)
pgIISPNetPrefixIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgIISPNetPrefixIndexNext.setStatus("current")
_PgIISPNetPrefixTable_Object = MibTable
pgIISPNetPrefixTable = _PgIISPNetPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 13, 1, 1, 4)
)
if mibBuilder.loadTexts:
    pgIISPNetPrefixTable.setStatus("current")
_PgIISPNetPrefixEntry_Object = MibTableRow
pgIISPNetPrefixEntry = _PgIISPNetPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 13, 1, 1, 4, 1)
)
pgIISPNetPrefixEntry.setIndexNames(
    (0, "PAIRGAIN-IISP-MIB", "pgIISPNetPrefixIndex"),
    (0, "PAIRGAIN-IISP-MIB", "pgIISPNetPrefixPort"),
    (0, "PAIRGAIN-IISP-MIB", "pgIISPNetPrefixPrefix"),
)
if mibBuilder.loadTexts:
    pgIISPNetPrefixEntry.setStatus("current")


class _PgIISPNetPrefixIndex_Type(Integer32):
    """Custom type pgIISPNetPrefixIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PgIISPNetPrefixIndex_Type.__name__ = "Integer32"
_PgIISPNetPrefixIndex_Object = MibTableColumn
pgIISPNetPrefixIndex = _PgIISPNetPrefixIndex_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 13, 1, 1, 4, 1, 1),
    _PgIISPNetPrefixIndex_Type()
)
pgIISPNetPrefixIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgIISPNetPrefixIndex.setStatus("current")
_PgIISPNetPrefixRowStatus_Type = RowStatus
_PgIISPNetPrefixRowStatus_Object = MibTableColumn
pgIISPNetPrefixRowStatus = _PgIISPNetPrefixRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 13, 1, 1, 4, 1, 2),
    _PgIISPNetPrefixRowStatus_Type()
)
pgIISPNetPrefixRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pgIISPNetPrefixRowStatus.setStatus("current")


class _PgIISPNetPrefixPort_Type(Integer32):
    """Custom type pgIISPNetPrefixPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PgIISPNetPrefixPort_Type.__name__ = "Integer32"
_PgIISPNetPrefixPort_Object = MibTableColumn
pgIISPNetPrefixPort = _PgIISPNetPrefixPort_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 13, 1, 1, 4, 1, 3),
    _PgIISPNetPrefixPort_Type()
)
pgIISPNetPrefixPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgIISPNetPrefixPort.setStatus("current")
_PgIISPNetPrefixPrefix_Type = NetPrefix
_PgIISPNetPrefixPrefix_Object = MibTableColumn
pgIISPNetPrefixPrefix = _PgIISPNetPrefixPrefix_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 13, 1, 1, 4, 1, 4),
    _PgIISPNetPrefixPrefix_Type()
)
pgIISPNetPrefixPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgIISPNetPrefixPrefix.setStatus("current")


class _PgIISPNetPrefixFormat_Type(Integer32):
    """Custom type pgIISPNetPrefixFormat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dcc", 1),
          ("e164", 3),
          ("icd", 2))
    )


_PgIISPNetPrefixFormat_Type.__name__ = "Integer32"
_PgIISPNetPrefixFormat_Object = MibTableColumn
pgIISPNetPrefixFormat = _PgIISPNetPrefixFormat_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 13, 1, 1, 4, 1, 5),
    _PgIISPNetPrefixFormat_Type()
)
pgIISPNetPrefixFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgIISPNetPrefixFormat.setStatus("current")


class _PgIISPNetPrefixLength_Type(Integer32):
    """Custom type pgIISPNetPrefixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 152),
    )


_PgIISPNetPrefixLength_Type.__name__ = "Integer32"
_PgIISPNetPrefixLength_Object = MibTableColumn
pgIISPNetPrefixLength = _PgIISPNetPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 13, 1, 1, 4, 1, 6),
    _PgIISPNetPrefixLength_Type()
)
pgIISPNetPrefixLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgIISPNetPrefixLength.setStatus("current")


class _PgIISPNetPrefixStatus_Type(Integer32):
    """Custom type pgIISPNetPrefixStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_PgIISPNetPrefixStatus_Type.__name__ = "Integer32"
_PgIISPNetPrefixStatus_Object = MibTableColumn
pgIISPNetPrefixStatus = _PgIISPNetPrefixStatus_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 13, 1, 1, 4, 1, 7),
    _PgIISPNetPrefixStatus_Type()
)
pgIISPNetPrefixStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgIISPNetPrefixStatus.setStatus("current")
_PgIISPAtmAddrPrefix_Type = AtmAddr
_PgIISPAtmAddrPrefix_Object = MibScalar
pgIISPAtmAddrPrefix = _PgIISPAtmAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 13, 1, 1, 5),
    _PgIISPAtmAddrPrefix_Type()
)
pgIISPAtmAddrPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgIISPAtmAddrPrefix.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PAIRGAIN-IISP-MIB",
    **{"PgAtmAddrPrefix": PgAtmAddrPrefix,
       "PgAtmPrefixLength": PgAtmPrefixLength,
       "NetPrefix": NetPrefix,
       "pgIISP": pgIISP,
       "pgIISPMIBObjects": pgIISPMIBObjects,
       "pgIISPRouteAddrIndexNext": pgIISPRouteAddrIndexNext,
       "pgIISPRouteAddrTable": pgIISPRouteAddrTable,
       "pgIISPRouteAddrEntry": pgIISPRouteAddrEntry,
       "pgIISPRouteAddrIndex": pgIISPRouteAddrIndex,
       "pgIISPRouteAddrRowStatus": pgIISPRouteAddrRowStatus,
       "pgIISPRouteAddrAddress": pgIISPRouteAddrAddress,
       "pgIISPRouteAddrPrefixLength": pgIISPRouteAddrPrefixLength,
       "pgIISPRouteAddrIfIndex": pgIISPRouteAddrIfIndex,
       "pgIISPRouteAddrType": pgIISPRouteAddrType,
       "pgIISPRouteAddrAdminStatus": pgIISPRouteAddrAdminStatus,
       "pgIISPRouteAddrOperStatus": pgIISPRouteAddrOperStatus,
       "pgIISPRouteAddrTimeStamp": pgIISPRouteAddrTimeStamp,
       "pgIISPNetPrefixIndexNext": pgIISPNetPrefixIndexNext,
       "pgIISPNetPrefixTable": pgIISPNetPrefixTable,
       "pgIISPNetPrefixEntry": pgIISPNetPrefixEntry,
       "pgIISPNetPrefixIndex": pgIISPNetPrefixIndex,
       "pgIISPNetPrefixRowStatus": pgIISPNetPrefixRowStatus,
       "pgIISPNetPrefixPort": pgIISPNetPrefixPort,
       "pgIISPNetPrefixPrefix": pgIISPNetPrefixPrefix,
       "pgIISPNetPrefixFormat": pgIISPNetPrefixFormat,
       "pgIISPNetPrefixLength": pgIISPNetPrefixLength,
       "pgIISPNetPrefixStatus": pgIISPNetPrefixStatus,
       "pgIISPAtmAddrPrefix": pgIISPAtmAddrPrefix}
)
