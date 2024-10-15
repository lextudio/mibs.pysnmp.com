# SNMP MIB module (RFC1414-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RFC1414-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:47:32 2024
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
 TimeTicks,
 Unsigned32,
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(tcpConnLocalAddress,
 tcpConnLocalPort,
 tcpConnRemAddress,
 tcpConnRemPort) = mibBuilder.importSymbols(
    "TCP-MIB",
    "tcpConnLocalAddress",
    "tcpConnLocalPort",
    "tcpConnRemAddress",
    "tcpConnRemPort")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ident_ObjectIdentity = ObjectIdentity
ident = _Ident_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 24)
)
_IdentInfo_ObjectIdentity = ObjectIdentity
identInfo = _IdentInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 24, 1)
)
_IdentTable_Object = MibTable
identTable = _IdentTable_Object(
    (1, 3, 6, 1, 2, 1, 24, 1, 1)
)
if mibBuilder.loadTexts:
    identTable.setStatus("mandatory")
_IdentEntry_Object = MibTableRow
identEntry = _IdentEntry_Object(
    (1, 3, 6, 1, 2, 1, 24, 1, 1, 1)
)
identEntry.setIndexNames(
    (0, "TCP-MIB", "tcpConnLocalAddress"),
    (0, "TCP-MIB", "tcpConnLocalPort"),
    (0, "TCP-MIB", "tcpConnRemAddress"),
    (0, "TCP-MIB", "tcpConnRemPort"),
)
if mibBuilder.loadTexts:
    identEntry.setStatus("mandatory")


class _IdentStatus_Type(Integer32):
    """Custom type identStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noError", 1),
          ("unknownError", 2))
    )


_IdentStatus_Type.__name__ = "Integer32"
_IdentStatus_Object = MibTableColumn
identStatus = _IdentStatus_Object(
    (1, 3, 6, 1, 2, 1, 24, 1, 1, 1, 1),
    _IdentStatus_Type()
)
identStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identStatus.setStatus("mandatory")


class _IdentOpSys_Type(OctetString):
    """Custom type identOpSys based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_IdentOpSys_Type.__name__ = "OctetString"
_IdentOpSys_Object = MibTableColumn
identOpSys = _IdentOpSys_Object(
    (1, 3, 6, 1, 2, 1, 24, 1, 1, 1, 2),
    _IdentOpSys_Type()
)
identOpSys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identOpSys.setStatus("mandatory")


class _IdentCharset_Type(OctetString):
    """Custom type identCharset based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_IdentCharset_Type.__name__ = "OctetString"
_IdentCharset_Object = MibTableColumn
identCharset = _IdentCharset_Object(
    (1, 3, 6, 1, 2, 1, 24, 1, 1, 1, 3),
    _IdentCharset_Type()
)
identCharset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identCharset.setStatus("mandatory")


class _IdentUserid_Type(OctetString):
    """Custom type identUserid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IdentUserid_Type.__name__ = "OctetString"
_IdentUserid_Object = MibTableColumn
identUserid = _IdentUserid_Object(
    (1, 3, 6, 1, 2, 1, 24, 1, 1, 1, 4),
    _IdentUserid_Type()
)
identUserid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identUserid.setStatus("mandatory")


class _IdentMisc_Type(OctetString):
    """Custom type identMisc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IdentMisc_Type.__name__ = "OctetString"
_IdentMisc_Object = MibTableColumn
identMisc = _IdentMisc_Object(
    (1, 3, 6, 1, 2, 1, 24, 1, 1, 1, 5),
    _IdentMisc_Type()
)
identMisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identMisc.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RFC1414-MIB",
    **{"ident": ident,
       "identInfo": identInfo,
       "identTable": identTable,
       "identEntry": identEntry,
       "identStatus": identStatus,
       "identOpSys": identOpSys,
       "identCharset": identCharset,
       "identUserid": identUserid,
       "identMisc": identMisc}
)
