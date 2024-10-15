# SNMP MIB module (NETSCREEN-CERTIFICATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETSCREEN-CERTIFICATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:26:43 2024
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

(netscreenVpn,
 netscreenVpnMibModule) = mibBuilder.importSymbols(
    "NETSCREEN-SMI",
    "netscreenVpn",
    "netscreenVpnMibModule")

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

netscreenCertificateMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 4, 0, 7)
)
netscreenCertificateMibModule.setRevisions(
        ("2004-05-03 00:00",
         "2004-03-03 00:00",
         "2003-11-12 00:00",
         "2001-09-28 00:00",
         "2001-05-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NsVpnCert_ObjectIdentity = ObjectIdentity
nsVpnCert = _NsVpnCert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 4, 7)
)
_NsVpnCertDefTable_Object = MibTable
nsVpnCertDefTable = _NsVpnCertDefTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 7, 1)
)
if mibBuilder.loadTexts:
    nsVpnCertDefTable.setStatus("current")
_NsVpnCertDefEntry_Object = MibTableRow
nsVpnCertDefEntry = _NsVpnCertDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 7, 1, 1)
)
nsVpnCertDefEntry.setIndexNames(
    (0, "NETSCREEN-CERTIFICATE-MIB", "nsVpnCertDefIndex"),
)
if mibBuilder.loadTexts:
    nsVpnCertDefEntry.setStatus("current")


class _NsVpnCertDefIndex_Type(Integer32):
    """Custom type nsVpnCertDefIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsVpnCertDefIndex_Type.__name__ = "Integer32"
_NsVpnCertDefIndex_Object = MibTableColumn
nsVpnCertDefIndex = _NsVpnCertDefIndex_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 7, 1, 1, 1),
    _NsVpnCertDefIndex_Type()
)
nsVpnCertDefIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnCertDefIndex.setStatus("current")


class _NsVpnCertDefLdap_Type(DisplayString):
    """Custom type nsVpnCertDefLdap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsVpnCertDefLdap_Type.__name__ = "DisplayString"
_NsVpnCertDefLdap_Object = MibTableColumn
nsVpnCertDefLdap = _NsVpnCertDefLdap_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 7, 1, 1, 2),
    _NsVpnCertDefLdap_Type()
)
nsVpnCertDefLdap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnCertDefLdap.setStatus("current")


class _NsVpnCertDefCrlUrl_Type(DisplayString):
    """Custom type nsVpnCertDefCrlUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsVpnCertDefCrlUrl_Type.__name__ = "DisplayString"
_NsVpnCertDefCrlUrl_Object = MibTableColumn
nsVpnCertDefCrlUrl = _NsVpnCertDefCrlUrl_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 7, 1, 1, 3),
    _NsVpnCertDefCrlUrl_Type()
)
nsVpnCertDefCrlUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnCertDefCrlUrl.setStatus("current")


class _NsVpnCertDefRefresh_Type(DisplayString):
    """Custom type nsVpnCertDefRefresh based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsVpnCertDefRefresh_Type.__name__ = "DisplayString"
_NsVpnCertDefRefresh_Object = MibTableColumn
nsVpnCertDefRefresh = _NsVpnCertDefRefresh_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 7, 1, 1, 4),
    _NsVpnCertDefRefresh_Type()
)
nsVpnCertDefRefresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnCertDefRefresh.setStatus("current")


class _NsVpnCertDefX509_Type(Integer32):
    """Custom type nsVpnCertDefX509 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("partial", 0))
    )


_NsVpnCertDefX509_Type.__name__ = "Integer32"
_NsVpnCertDefX509_Object = MibTableColumn
nsVpnCertDefX509 = _NsVpnCertDefX509_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 7, 1, 1, 5),
    _NsVpnCertDefX509_Type()
)
nsVpnCertDefX509.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnCertDefX509.setStatus("current")
_NsVpnCertDefVsys_Type = Integer32
_NsVpnCertDefVsys_Object = MibTableColumn
nsVpnCertDefVsys = _NsVpnCertDefVsys_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 7, 1, 1, 6),
    _NsVpnCertDefVsys_Type()
)
nsVpnCertDefVsys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnCertDefVsys.setStatus("current")
_NsVpnCertCfgTable_Object = MibTable
nsVpnCertCfgTable = _NsVpnCertCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 7, 2)
)
if mibBuilder.loadTexts:
    nsVpnCertCfgTable.setStatus("current")
_NsVpnCertCfgEntry_Object = MibTableRow
nsVpnCertCfgEntry = _NsVpnCertCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 7, 2, 1)
)
nsVpnCertCfgEntry.setIndexNames(
    (0, "NETSCREEN-CERTIFICATE-MIB", "nsVpnCertCfgIndex"),
)
if mibBuilder.loadTexts:
    nsVpnCertCfgEntry.setStatus("current")


class _NsVpnCertCfgIndex_Type(Integer32):
    """Custom type nsVpnCertCfgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsVpnCertCfgIndex_Type.__name__ = "Integer32"
_NsVpnCertCfgIndex_Object = MibTableColumn
nsVpnCertCfgIndex = _NsVpnCertCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 7, 2, 1, 1),
    _NsVpnCertCfgIndex_Type()
)
nsVpnCertCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnCertCfgIndex.setStatus("current")


class _NsVpnCertCfgType_Type(Integer32):
    """Custom type nsVpnCertCfgType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ca", 0),
          ("local", 1))
    )


_NsVpnCertCfgType_Type.__name__ = "Integer32"
_NsVpnCertCfgType_Object = MibTableColumn
nsVpnCertCfgType = _NsVpnCertCfgType_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 7, 2, 1, 2),
    _NsVpnCertCfgType_Type()
)
nsVpnCertCfgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnCertCfgType.setStatus("current")


class _NsVpnCertCfgSubject_Type(DisplayString):
    """Custom type nsVpnCertCfgSubject based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsVpnCertCfgSubject_Type.__name__ = "DisplayString"
_NsVpnCertCfgSubject_Object = MibTableColumn
nsVpnCertCfgSubject = _NsVpnCertCfgSubject_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 7, 2, 1, 3),
    _NsVpnCertCfgSubject_Type()
)
nsVpnCertCfgSubject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnCertCfgSubject.setStatus("current")


class _NsVpnCertCfgExpire_Type(DisplayString):
    """Custom type nsVpnCertCfgExpire based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsVpnCertCfgExpire_Type.__name__ = "DisplayString"
_NsVpnCertCfgExpire_Object = MibTableColumn
nsVpnCertCfgExpire = _NsVpnCertCfgExpire_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 7, 2, 1, 4),
    _NsVpnCertCfgExpire_Type()
)
nsVpnCertCfgExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnCertCfgExpire.setStatus("current")


class _NsVpnCertCfgIssuer_Type(DisplayString):
    """Custom type nsVpnCertCfgIssuer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NsVpnCertCfgIssuer_Type.__name__ = "DisplayString"
_NsVpnCertCfgIssuer_Object = MibTableColumn
nsVpnCertCfgIssuer = _NsVpnCertCfgIssuer_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 7, 2, 1, 5),
    _NsVpnCertCfgIssuer_Type()
)
nsVpnCertCfgIssuer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnCertCfgIssuer.setStatus("current")
_NsVpnCertCfgVsys_Type = Integer32
_NsVpnCertCfgVsys_Object = MibTableColumn
nsVpnCertCfgVsys = _NsVpnCertCfgVsys_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 7, 2, 1, 6),
    _NsVpnCertCfgVsys_Type()
)
nsVpnCertCfgVsys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnCertCfgVsys.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSCREEN-CERTIFICATE-MIB",
    **{"netscreenCertificateMibModule": netscreenCertificateMibModule,
       "nsVpnCert": nsVpnCert,
       "nsVpnCertDefTable": nsVpnCertDefTable,
       "nsVpnCertDefEntry": nsVpnCertDefEntry,
       "nsVpnCertDefIndex": nsVpnCertDefIndex,
       "nsVpnCertDefLdap": nsVpnCertDefLdap,
       "nsVpnCertDefCrlUrl": nsVpnCertDefCrlUrl,
       "nsVpnCertDefRefresh": nsVpnCertDefRefresh,
       "nsVpnCertDefX509": nsVpnCertDefX509,
       "nsVpnCertDefVsys": nsVpnCertDefVsys,
       "nsVpnCertCfgTable": nsVpnCertCfgTable,
       "nsVpnCertCfgEntry": nsVpnCertCfgEntry,
       "nsVpnCertCfgIndex": nsVpnCertCfgIndex,
       "nsVpnCertCfgType": nsVpnCertCfgType,
       "nsVpnCertCfgSubject": nsVpnCertCfgSubject,
       "nsVpnCertCfgExpire": nsVpnCertCfgExpire,
       "nsVpnCertCfgIssuer": nsVpnCertCfgIssuer,
       "nsVpnCertCfgVsys": nsVpnCertCfgVsys}
)
