# SNMP MIB module (Wellfleet-FTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-FTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:17 2024
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

(wfFtpGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfFtpGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfFtp_ObjectIdentity = ObjectIdentity
wfFtp = _WfFtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 10, 1)
)


class _WfFtpDelete_Type(Integer32):
    """Custom type wfFtpDelete based on Integer32"""
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


_WfFtpDelete_Type.__name__ = "Integer32"
_WfFtpDelete_Object = MibScalar
wfFtpDelete = _WfFtpDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 10, 1, 1),
    _WfFtpDelete_Type()
)
wfFtpDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFtpDelete.setStatus("mandatory")


class _WfFtpDisable_Type(Integer32):
    """Custom type wfFtpDisable based on Integer32"""
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


_WfFtpDisable_Type.__name__ = "Integer32"
_WfFtpDisable_Object = MibScalar
wfFtpDisable = _WfFtpDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 10, 1, 2),
    _WfFtpDisable_Type()
)
wfFtpDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFtpDisable.setStatus("mandatory")


class _WfFtpDefaultVolume_Type(Integer32):
    """Custom type wfFtpDefaultVolume based on Integer32"""
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


_WfFtpDefaultVolume_Type.__name__ = "Integer32"
_WfFtpDefaultVolume_Object = MibScalar
wfFtpDefaultVolume = _WfFtpDefaultVolume_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 10, 1, 3),
    _WfFtpDefaultVolume_Type()
)
wfFtpDefaultVolume.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFtpDefaultVolume.setStatus("mandatory")


class _WfFtpLoginRetries_Type(Integer32):
    """Custom type wfFtpLoginRetries based on Integer32"""
    defaultValue = 3


_WfFtpLoginRetries_Object = MibScalar
wfFtpLoginRetries = _WfFtpLoginRetries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 10, 1, 4),
    _WfFtpLoginRetries_Type()
)
wfFtpLoginRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFtpLoginRetries.setStatus("mandatory")


class _WfFtpIdleTimeOut_Type(Integer32):
    """Custom type wfFtpIdleTimeOut based on Integer32"""
    defaultValue = 900


_WfFtpIdleTimeOut_Object = MibScalar
wfFtpIdleTimeOut = _WfFtpIdleTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 10, 1, 5),
    _WfFtpIdleTimeOut_Type()
)
wfFtpIdleTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFtpIdleTimeOut.setStatus("mandatory")


class _WfFtpMaxSessions_Type(Integer32):
    """Custom type wfFtpMaxSessions based on Integer32"""
    defaultValue = 3


_WfFtpMaxSessions_Object = MibScalar
wfFtpMaxSessions = _WfFtpMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 10, 1, 6),
    _WfFtpMaxSessions_Type()
)
wfFtpMaxSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFtpMaxSessions.setStatus("mandatory")


class _WfFtpType_Type(Integer32):
    """Custom type wfFtpType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 1),
          ("binary", 2))
    )


_WfFtpType_Type.__name__ = "Integer32"
_WfFtpType_Object = MibScalar
wfFtpType = _WfFtpType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 10, 1, 7),
    _WfFtpType_Type()
)
wfFtpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFtpType.setStatus("mandatory")


class _WfFtpCtrlIpTos_Type(Integer32):
    """Custom type wfFtpCtrlIpTos based on Integer32"""
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


_WfFtpCtrlIpTos_Type.__name__ = "Integer32"
_WfFtpCtrlIpTos_Object = MibScalar
wfFtpCtrlIpTos = _WfFtpCtrlIpTos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 10, 1, 8),
    _WfFtpCtrlIpTos_Type()
)
wfFtpCtrlIpTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFtpCtrlIpTos.setStatus("obsolete")


class _WfFtpDataIpTos_Type(Integer32):
    """Custom type wfFtpDataIpTos based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("highthroughput", 2),
          ("normal", 1))
    )


_WfFtpDataIpTos_Type.__name__ = "Integer32"
_WfFtpDataIpTos_Object = MibScalar
wfFtpDataIpTos = _WfFtpDataIpTos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 10, 1, 9),
    _WfFtpDataIpTos_Type()
)
wfFtpDataIpTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFtpDataIpTos.setStatus("obsolete")


class _WfFtpTcpWindowSize_Type(Integer32):
    """Custom type wfFtpTcpWindowSize based on Integer32"""
    defaultValue = 60000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5000, 64000),
    )


_WfFtpTcpWindowSize_Type.__name__ = "Integer32"
_WfFtpTcpWindowSize_Object = MibScalar
wfFtpTcpWindowSize = _WfFtpTcpWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 10, 1, 10),
    _WfFtpTcpWindowSize_Type()
)
wfFtpTcpWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFtpTcpWindowSize.setStatus("mandatory")
_WfFtpLogins_Type = Counter32
_WfFtpLogins_Object = MibScalar
wfFtpLogins = _WfFtpLogins_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 10, 1, 11),
    _WfFtpLogins_Type()
)
wfFtpLogins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFtpLogins.setStatus("mandatory")
_WfFtpManagerLoginFails_Type = Counter32
_WfFtpManagerLoginFails_Object = MibScalar
wfFtpManagerLoginFails = _WfFtpManagerLoginFails_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 10, 1, 12),
    _WfFtpManagerLoginFails_Type()
)
wfFtpManagerLoginFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFtpManagerLoginFails.setStatus("mandatory")
_WfFtpOtherLoginFails_Type = Counter32
_WfFtpOtherLoginFails_Object = MibScalar
wfFtpOtherLoginFails = _WfFtpOtherLoginFails_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 10, 1, 13),
    _WfFtpOtherLoginFails_Type()
)
wfFtpOtherLoginFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFtpOtherLoginFails.setStatus("mandatory")
_WfFtpXfers_Type = Counter32
_WfFtpXfers_Object = MibScalar
wfFtpXfers = _WfFtpXfers_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 10, 1, 14),
    _WfFtpXfers_Type()
)
wfFtpXfers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFtpXfers.setStatus("mandatory")
_WfFtpInFiles_Type = Counter32
_WfFtpInFiles_Object = MibScalar
wfFtpInFiles = _WfFtpInFiles_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 10, 1, 15),
    _WfFtpInFiles_Type()
)
wfFtpInFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFtpInFiles.setStatus("mandatory")
_WfFtpOutFiles_Type = Counter32
_WfFtpOutFiles_Object = MibScalar
wfFtpOutFiles = _WfFtpOutFiles_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 10, 1, 16),
    _WfFtpOutFiles_Type()
)
wfFtpOutFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFtpOutFiles.setStatus("mandatory")
_WfFtpInErrs_Type = Counter32
_WfFtpInErrs_Object = MibScalar
wfFtpInErrs = _WfFtpInErrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 10, 1, 17),
    _WfFtpInErrs_Type()
)
wfFtpInErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFtpInErrs.setStatus("mandatory")
_WfFtpOutErrs_Type = Counter32
_WfFtpOutErrs_Object = MibScalar
wfFtpOutErrs = _WfFtpOutErrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 10, 1, 18),
    _WfFtpOutErrs_Type()
)
wfFtpOutErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFtpOutErrs.setStatus("mandatory")
_WfFtpAborts_Type = Counter32
_WfFtpAborts_Object = MibScalar
wfFtpAborts = _WfFtpAborts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 10, 1, 19),
    _WfFtpAborts_Type()
)
wfFtpAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFtpAborts.setStatus("mandatory")
_WfFtpInXferRate_Type = Gauge32
_WfFtpInXferRate_Object = MibScalar
wfFtpInXferRate = _WfFtpInXferRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 10, 1, 20),
    _WfFtpInXferRate_Type()
)
wfFtpInXferRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFtpInXferRate.setStatus("mandatory")
_WfFtpOutXferRate_Type = Gauge32
_WfFtpOutXferRate_Object = MibScalar
wfFtpOutXferRate = _WfFtpOutXferRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 10, 1, 21),
    _WfFtpOutXferRate_Type()
)
wfFtpOutXferRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFtpOutXferRate.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-FTP-MIB",
    **{"wfFtp": wfFtp,
       "wfFtpDelete": wfFtpDelete,
       "wfFtpDisable": wfFtpDisable,
       "wfFtpDefaultVolume": wfFtpDefaultVolume,
       "wfFtpLoginRetries": wfFtpLoginRetries,
       "wfFtpIdleTimeOut": wfFtpIdleTimeOut,
       "wfFtpMaxSessions": wfFtpMaxSessions,
       "wfFtpType": wfFtpType,
       "wfFtpCtrlIpTos": wfFtpCtrlIpTos,
       "wfFtpDataIpTos": wfFtpDataIpTos,
       "wfFtpTcpWindowSize": wfFtpTcpWindowSize,
       "wfFtpLogins": wfFtpLogins,
       "wfFtpManagerLoginFails": wfFtpManagerLoginFails,
       "wfFtpOtherLoginFails": wfFtpOtherLoginFails,
       "wfFtpXfers": wfFtpXfers,
       "wfFtpInFiles": wfFtpInFiles,
       "wfFtpOutFiles": wfFtpOutFiles,
       "wfFtpInErrs": wfFtpInErrs,
       "wfFtpOutErrs": wfFtpOutErrs,
       "wfFtpAborts": wfFtpAborts,
       "wfFtpInXferRate": wfFtpInXferRate,
       "wfFtpOutXferRate": wfFtpOutXferRate}
)
