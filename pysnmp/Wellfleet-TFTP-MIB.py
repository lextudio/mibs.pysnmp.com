# SNMP MIB module (Wellfleet-TFTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-TFTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:19 2024
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

(wfInternet,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfInternet")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfTftp_ObjectIdentity = ObjectIdentity
wfTftp = _WfTftp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 6)
)


class _WfTftpDisable_Type(Integer32):
    """Custom type wfTftpDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfTftpDisable_Type.__name__ = "Integer32"
_WfTftpDisable_Object = MibScalar
wfTftpDisable = _WfTftpDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 6, 1),
    _WfTftpDisable_Type()
)
wfTftpDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTftpDisable.setStatus("mandatory")


class _WfTftpDefaultVolume_Type(Integer32):
    """Custom type wfTftpDefaultVolume based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              65,
              100,
              101,
              200,
              201,
              300,
              301,
              400,
              401,
              500,
              501,
              600,
              601,
              700,
              701,
              800,
              801,
              900,
              901,
              1000,
              1001,
              1100,
              1101,
              1200,
              1201,
              1300,
              1301,
              1400,
              1401)
        )
    )
    namedValues = NamedValues(
        *(("volume1", 1),
          ("volume10", 10),
          ("volume10a", 1000),
          ("volume10b", 1001),
          ("volume11", 11),
          ("volume11a", 1100),
          ("volume11b", 1101),
          ("volume12", 12),
          ("volume12a", 1200),
          ("volume12b", 1201),
          ("volume13", 13),
          ("volume13a", 1300),
          ("volume13b", 1301),
          ("volume14", 14),
          ("volume14a", 1400),
          ("volume14b", 1401),
          ("volume1a", 100),
          ("volume1b", 101),
          ("volume2", 2),
          ("volume2a", 200),
          ("volume2b", 201),
          ("volume3", 3),
          ("volume3a", 300),
          ("volume3b", 301),
          ("volume4", 4),
          ("volume4a", 400),
          ("volume4b", 401),
          ("volume5", 5),
          ("volume5a", 500),
          ("volume5b", 501),
          ("volume6", 6),
          ("volume6a", 600),
          ("volume6b", 601),
          ("volume7", 7),
          ("volume7a", 700),
          ("volume7b", 701),
          ("volume8", 8),
          ("volume8a", 800),
          ("volume8b", 801),
          ("volume9", 9),
          ("volume9a", 900),
          ("volume9b", 901),
          ("volumea", 65))
    )


_WfTftpDefaultVolume_Type.__name__ = "Integer32"
_WfTftpDefaultVolume_Object = MibScalar
wfTftpDefaultVolume = _WfTftpDefaultVolume_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 6, 2),
    _WfTftpDefaultVolume_Type()
)
wfTftpDefaultVolume.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTftpDefaultVolume.setStatus("mandatory")
_WfTftpXfers_Type = Counter32
_WfTftpXfers_Object = MibScalar
wfTftpXfers = _WfTftpXfers_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 6, 3),
    _WfTftpXfers_Type()
)
wfTftpXfers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTftpXfers.setStatus("mandatory")


class _WfTftpTimeOut_Type(Integer32):
    """Custom type wfTftpTimeOut based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_WfTftpTimeOut_Type.__name__ = "Integer32"
_WfTftpTimeOut_Object = MibScalar
wfTftpTimeOut = _WfTftpTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 6, 4),
    _WfTftpTimeOut_Type()
)
wfTftpTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTftpTimeOut.setStatus("mandatory")


class _WfTftpCloseTimeOut_Type(Integer32):
    """Custom type wfTftpCloseTimeOut based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_WfTftpCloseTimeOut_Type.__name__ = "Integer32"
_WfTftpCloseTimeOut_Object = MibScalar
wfTftpCloseTimeOut = _WfTftpCloseTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 6, 5),
    _WfTftpCloseTimeOut_Type()
)
wfTftpCloseTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTftpCloseTimeOut.setStatus("mandatory")


class _WfTftpRexmit_Type(Integer32):
    """Custom type wfTftpRexmit based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_WfTftpRexmit_Type.__name__ = "Integer32"
_WfTftpRexmit_Object = MibScalar
wfTftpRexmit = _WfTftpRexmit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 6, 6),
    _WfTftpRexmit_Type()
)
wfTftpRexmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTftpRexmit.setStatus("mandatory")


class _WfTftpIpTos_Type(Integer32):
    """Custom type wfTftpIpTos based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lowdelay", 2),
          ("normal", 1))
    )


_WfTftpIpTos_Type.__name__ = "Integer32"
_WfTftpIpTos_Object = MibScalar
wfTftpIpTos = _WfTftpIpTos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 6, 7),
    _WfTftpIpTos_Type()
)
wfTftpIpTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTftpIpTos.setStatus("obsolete")
_WfTftpInFiles_Type = Counter32
_WfTftpInFiles_Object = MibScalar
wfTftpInFiles = _WfTftpInFiles_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 6, 8),
    _WfTftpInFiles_Type()
)
wfTftpInFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTftpInFiles.setStatus("mandatory")
_WfTftpOutFiles_Type = Counter32
_WfTftpOutFiles_Object = MibScalar
wfTftpOutFiles = _WfTftpOutFiles_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 6, 9),
    _WfTftpOutFiles_Type()
)
wfTftpOutFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTftpOutFiles.setStatus("mandatory")
_WfTftpInWRQ_Type = Counter32
_WfTftpInWRQ_Object = MibScalar
wfTftpInWRQ = _WfTftpInWRQ_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 6, 10),
    _WfTftpInWRQ_Type()
)
wfTftpInWRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTftpInWRQ.setStatus("mandatory")
_WfTftpOutWRQ_Type = Counter32
_WfTftpOutWRQ_Object = MibScalar
wfTftpOutWRQ = _WfTftpOutWRQ_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 6, 11),
    _WfTftpOutWRQ_Type()
)
wfTftpOutWRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTftpOutWRQ.setStatus("mandatory")
_WfTftpInRRQ_Type = Counter32
_WfTftpInRRQ_Object = MibScalar
wfTftpInRRQ = _WfTftpInRRQ_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 6, 12),
    _WfTftpInRRQ_Type()
)
wfTftpInRRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTftpInRRQ.setStatus("mandatory")
_WfTftpOutRRQ_Type = Counter32
_WfTftpOutRRQ_Object = MibScalar
wfTftpOutRRQ = _WfTftpOutRRQ_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 6, 13),
    _WfTftpOutRRQ_Type()
)
wfTftpOutRRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTftpOutRRQ.setStatus("mandatory")
_WfTftpRexmitPkts_Type = Counter32
_WfTftpRexmitPkts_Object = MibScalar
wfTftpRexmitPkts = _WfTftpRexmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 6, 14),
    _WfTftpRexmitPkts_Type()
)
wfTftpRexmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTftpRexmitPkts.setStatus("mandatory")
_WfTftpInErr_Type = Counter32
_WfTftpInErr_Object = MibScalar
wfTftpInErr = _WfTftpInErr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 6, 15),
    _WfTftpInErr_Type()
)
wfTftpInErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTftpInErr.setStatus("mandatory")
_WfTftpOutErr_Type = Counter32
_WfTftpOutErr_Object = MibScalar
wfTftpOutErr = _WfTftpOutErr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 6, 16),
    _WfTftpOutErr_Type()
)
wfTftpOutErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTftpOutErr.setStatus("mandatory")
_WfTftpAborts_Type = Counter32
_WfTftpAborts_Object = MibScalar
wfTftpAborts = _WfTftpAborts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 6, 17),
    _WfTftpAborts_Type()
)
wfTftpAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTftpAborts.setStatus("mandatory")


class _WfTftpDelete_Type(Integer32):
    """Custom type wfTftpDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfTftpDelete_Type.__name__ = "Integer32"
_WfTftpDelete_Object = MibScalar
wfTftpDelete = _WfTftpDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 6, 18),
    _WfTftpDelete_Type()
)
wfTftpDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTftpDelete.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-TFTP-MIB",
    **{"wfTftp": wfTftp,
       "wfTftpDisable": wfTftpDisable,
       "wfTftpDefaultVolume": wfTftpDefaultVolume,
       "wfTftpXfers": wfTftpXfers,
       "wfTftpTimeOut": wfTftpTimeOut,
       "wfTftpCloseTimeOut": wfTftpCloseTimeOut,
       "wfTftpRexmit": wfTftpRexmit,
       "wfTftpIpTos": wfTftpIpTos,
       "wfTftpInFiles": wfTftpInFiles,
       "wfTftpOutFiles": wfTftpOutFiles,
       "wfTftpInWRQ": wfTftpInWRQ,
       "wfTftpOutWRQ": wfTftpOutWRQ,
       "wfTftpInRRQ": wfTftpInRRQ,
       "wfTftpOutRRQ": wfTftpOutRRQ,
       "wfTftpRexmitPkts": wfTftpRexmitPkts,
       "wfTftpInErr": wfTftpInErr,
       "wfTftpOutErr": wfTftpOutErr,
       "wfTftpAborts": wfTftpAborts,
       "wfTftpDelete": wfTftpDelete}
)
