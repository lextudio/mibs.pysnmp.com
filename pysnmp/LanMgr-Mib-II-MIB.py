# SNMP MIB module (LanMgr-Mib-II-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LanMgr-Mib-II-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:19:37 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Lanmanager_ObjectIdentity = ObjectIdentity
lanmanager = _Lanmanager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 77)
)
_Lanmgr_2_ObjectIdentity = ObjectIdentity
lanmgr_2 = _Lanmgr_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 77, 1)
)
_Common_ObjectIdentity = ObjectIdentity
common = _Common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 77, 1, 1)
)
_ComVersionMaj_Type = OctetString
_ComVersionMaj_Object = MibScalar
comVersionMaj = _ComVersionMaj_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 1, 1),
    _ComVersionMaj_Type()
)
comVersionMaj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comVersionMaj.setStatus("mandatory")
_ComVersionMin_Type = OctetString
_ComVersionMin_Object = MibScalar
comVersionMin = _ComVersionMin_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 1, 2),
    _ComVersionMin_Type()
)
comVersionMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comVersionMin.setStatus("mandatory")
_ComType_Type = OctetString
_ComType_Object = MibScalar
comType = _ComType_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 1, 3),
    _ComType_Type()
)
comType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comType.setStatus("mandatory")
_ComStatStart_Type = Integer32
_ComStatStart_Object = MibScalar
comStatStart = _ComStatStart_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 1, 4),
    _ComStatStart_Type()
)
comStatStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comStatStart.setStatus("mandatory")
_ComStatNumNetIOs_Type = Counter32
_ComStatNumNetIOs_Object = MibScalar
comStatNumNetIOs = _ComStatNumNetIOs_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 1, 5),
    _ComStatNumNetIOs_Type()
)
comStatNumNetIOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comStatNumNetIOs.setStatus("mandatory")
_ComStatFiNetIOs_Type = Counter32
_ComStatFiNetIOs_Object = MibScalar
comStatFiNetIOs = _ComStatFiNetIOs_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 1, 6),
    _ComStatFiNetIOs_Type()
)
comStatFiNetIOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comStatFiNetIOs.setStatus("mandatory")
_ComStatFcNetIOs_Type = Counter32
_ComStatFcNetIOs_Object = MibScalar
comStatFcNetIOs = _ComStatFcNetIOs_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 1, 7),
    _ComStatFcNetIOs_Type()
)
comStatFcNetIOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comStatFcNetIOs.setStatus("mandatory")
_Server_ObjectIdentity = ObjectIdentity
server = _Server_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 77, 1, 2)
)


class _SvDescription_Type(DisplayString):
    """Custom type svDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SvDescription_Type.__name__ = "DisplayString"
_SvDescription_Object = MibScalar
svDescription = _SvDescription_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 2, 1),
    _SvDescription_Type()
)
svDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svDescription.setStatus("mandatory")
_SvSvcNumber_Type = Integer32
_SvSvcNumber_Object = MibScalar
svSvcNumber = _SvSvcNumber_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 2, 2),
    _SvSvcNumber_Type()
)
svSvcNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svSvcNumber.setStatus("mandatory")
_SvSvcTable_Object = MibTable
svSvcTable = _SvSvcTable_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 2, 3)
)
if mibBuilder.loadTexts:
    svSvcTable.setStatus("mandatory")
_SvSvcEntry_Object = MibTableRow
svSvcEntry = _SvSvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 2, 3, 1)
)
svSvcEntry.setIndexNames(
    (0, "LanMgr-Mib-II-MIB", "svSvcName"),
)
if mibBuilder.loadTexts:
    svSvcEntry.setStatus("mandatory")


class _SvSvcName_Type(DisplayString):
    """Custom type svSvcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_SvSvcName_Type.__name__ = "DisplayString"
_SvSvcName_Object = MibTableColumn
svSvcName = _SvSvcName_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 2, 3, 1, 1),
    _SvSvcName_Type()
)
svSvcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svSvcName.setStatus("mandatory")


class _SvSvcInstalledState_Type(Integer32):
    """Custom type svSvcInstalledState based on Integer32"""
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
        *(("install-pending", 2),
          ("installed", 4),
          ("uninstall-pending", 3),
          ("uninstalled", 1))
    )


_SvSvcInstalledState_Type.__name__ = "Integer32"
_SvSvcInstalledState_Object = MibTableColumn
svSvcInstalledState = _SvSvcInstalledState_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 2, 3, 1, 2),
    _SvSvcInstalledState_Type()
)
svSvcInstalledState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svSvcInstalledState.setStatus("mandatory")


class _SvSvcOperatingState_Type(Integer32):
    """Custom type svSvcOperatingState based on Integer32"""
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
        *(("active", 1),
          ("continue-pending", 2),
          ("pause-pending", 3),
          ("paused", 4))
    )


_SvSvcOperatingState_Type.__name__ = "Integer32"
_SvSvcOperatingState_Object = MibTableColumn
svSvcOperatingState = _SvSvcOperatingState_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 2, 3, 1, 3),
    _SvSvcOperatingState_Type()
)
svSvcOperatingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svSvcOperatingState.setStatus("mandatory")


class _SvSvcCanBeUninstalled_Type(Integer32):
    """Custom type svSvcCanBeUninstalled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("can-be-uninstalled", 2),
          ("cannot-be-uninstalled", 1))
    )


_SvSvcCanBeUninstalled_Type.__name__ = "Integer32"
_SvSvcCanBeUninstalled_Object = MibTableColumn
svSvcCanBeUninstalled = _SvSvcCanBeUninstalled_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 2, 3, 1, 4),
    _SvSvcCanBeUninstalled_Type()
)
svSvcCanBeUninstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svSvcCanBeUninstalled.setStatus("mandatory")


class _SvSvcCanBePaused_Type(Integer32):
    """Custom type svSvcCanBePaused based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("can-be-paused", 2),
          ("cannot-be-paused", 1))
    )


_SvSvcCanBePaused_Type.__name__ = "Integer32"
_SvSvcCanBePaused_Object = MibTableColumn
svSvcCanBePaused = _SvSvcCanBePaused_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 2, 3, 1, 5),
    _SvSvcCanBePaused_Type()
)
svSvcCanBePaused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svSvcCanBePaused.setStatus("mandatory")
_SvStatOpens_Type = Counter32
_SvStatOpens_Object = MibScalar
svStatOpens = _SvStatOpens_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 2, 4),
    _SvStatOpens_Type()
)
svStatOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svStatOpens.setStatus("mandatory")
_SvStatDevOpens_Type = Counter32
_SvStatDevOpens_Object = MibScalar
svStatDevOpens = _SvStatDevOpens_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 2, 5),
    _SvStatDevOpens_Type()
)
svStatDevOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svStatDevOpens.setStatus("mandatory")
_SvStatQueuedJobs_Type = Counter32
_SvStatQueuedJobs_Object = MibScalar
svStatQueuedJobs = _SvStatQueuedJobs_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 2, 6),
    _SvStatQueuedJobs_Type()
)
svStatQueuedJobs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svStatQueuedJobs.setStatus("mandatory")
_SvStatSOpens_Type = Counter32
_SvStatSOpens_Object = MibScalar
svStatSOpens = _SvStatSOpens_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 2, 7),
    _SvStatSOpens_Type()
)
svStatSOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svStatSOpens.setStatus("mandatory")
_SvStatErrorOuts_Type = Counter32
_SvStatErrorOuts_Object = MibScalar
svStatErrorOuts = _SvStatErrorOuts_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 2, 8),
    _SvStatErrorOuts_Type()
)
svStatErrorOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svStatErrorOuts.setStatus("mandatory")
_SvStatPwErrors_Type = Counter32
_SvStatPwErrors_Object = MibScalar
svStatPwErrors = _SvStatPwErrors_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 2, 9),
    _SvStatPwErrors_Type()
)
svStatPwErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svStatPwErrors.setStatus("mandatory")
_SvStatPermErrors_Type = Counter32
_SvStatPermErrors_Object = MibScalar
svStatPermErrors = _SvStatPermErrors_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 2, 10),
    _SvStatPermErrors_Type()
)
svStatPermErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svStatPermErrors.setStatus("mandatory")
_SvStatSysErrors_Type = Counter32
_SvStatSysErrors_Object = MibScalar
svStatSysErrors = _SvStatSysErrors_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 2, 11),
    _SvStatSysErrors_Type()
)
svStatSysErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svStatSysErrors.setStatus("mandatory")
_SvStatSentBytes_Type = Counter32
_SvStatSentBytes_Object = MibScalar
svStatSentBytes = _SvStatSentBytes_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 2, 12),
    _SvStatSentBytes_Type()
)
svStatSentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svStatSentBytes.setStatus("mandatory")
_SvStatRcvdBytes_Type = Counter32
_SvStatRcvdBytes_Object = MibScalar
svStatRcvdBytes = _SvStatRcvdBytes_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 2, 13),
    _SvStatRcvdBytes_Type()
)
svStatRcvdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svStatRcvdBytes.setStatus("mandatory")
_SvStatAvResponse_Type = Integer32
_SvStatAvResponse_Object = MibScalar
svStatAvResponse = _SvStatAvResponse_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 2, 14),
    _SvStatAvResponse_Type()
)
svStatAvResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svStatAvResponse.setStatus("mandatory")


class _SvSecurityMode_Type(Integer32):
    """Custom type svSecurityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("share-level", 1),
          ("user-level", 2))
    )


_SvSecurityMode_Type.__name__ = "Integer32"
_SvSecurityMode_Object = MibScalar
svSecurityMode = _SvSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 2, 15),
    _SvSecurityMode_Type()
)
svSecurityMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svSecurityMode.setStatus("mandatory")
_SvUsers_Type = Integer32
_SvUsers_Object = MibScalar
svUsers = _SvUsers_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 2, 16),
    _SvUsers_Type()
)
svUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svUsers.setStatus("mandatory")
_SvStatReqBufsNeeded_Type = Counter32
_SvStatReqBufsNeeded_Object = MibScalar
svStatReqBufsNeeded = _SvStatReqBufsNeeded_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 2, 17),
    _SvStatReqBufsNeeded_Type()
)
svStatReqBufsNeeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svStatReqBufsNeeded.setStatus("mandatory")
_SvStatBigBufsNeeded_Type = Counter32
_SvStatBigBufsNeeded_Object = MibScalar
svStatBigBufsNeeded = _SvStatBigBufsNeeded_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 2, 18),
    _SvStatBigBufsNeeded_Type()
)
svStatBigBufsNeeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svStatBigBufsNeeded.setStatus("mandatory")
_SvSessionNumber_Type = Integer32
_SvSessionNumber_Object = MibScalar
svSessionNumber = _SvSessionNumber_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 2, 19),
    _SvSessionNumber_Type()
)
svSessionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svSessionNumber.setStatus("mandatory")
_SvSessionTable_Object = MibTable
svSessionTable = _SvSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 2, 20)
)
if mibBuilder.loadTexts:
    svSessionTable.setStatus("mandatory")
_SvSessionEntry_Object = MibTableRow
svSessionEntry = _SvSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 2, 20, 1)
)
svSessionEntry.setIndexNames(
    (0, "LanMgr-Mib-II-MIB", "svSesClientName"),
    (0, "LanMgr-Mib-II-MIB", "svSesUserName"),
)
if mibBuilder.loadTexts:
    svSessionEntry.setStatus("mandatory")


class _SvSesClientName_Type(DisplayString):
    """Custom type svSesClientName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_SvSesClientName_Type.__name__ = "DisplayString"
_SvSesClientName_Object = MibTableColumn
svSesClientName = _SvSesClientName_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 2, 20, 1, 1),
    _SvSesClientName_Type()
)
svSesClientName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svSesClientName.setStatus("mandatory")


class _SvSesUserName_Type(DisplayString):
    """Custom type svSesUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_SvSesUserName_Type.__name__ = "DisplayString"
_SvSesUserName_Object = MibTableColumn
svSesUserName = _SvSesUserName_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 2, 20, 1, 2),
    _SvSesUserName_Type()
)
svSesUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svSesUserName.setStatus("mandatory")
_SvSesNumOpens_Type = Integer32
_SvSesNumOpens_Object = MibTableColumn
svSesNumOpens = _SvSesNumOpens_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 2, 20, 1, 4),
    _SvSesNumOpens_Type()
)
svSesNumOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svSesNumOpens.setStatus("mandatory")
_SvSesTime_Type = Counter32
_SvSesTime_Object = MibTableColumn
svSesTime = _SvSesTime_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 2, 20, 1, 5),
    _SvSesTime_Type()
)
svSesTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svSesTime.setStatus("mandatory")
_SvSesIdleTime_Type = Counter32
_SvSesIdleTime_Object = MibTableColumn
svSesIdleTime = _SvSesIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 2, 20, 1, 6),
    _SvSesIdleTime_Type()
)
svSesIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svSesIdleTime.setStatus("mandatory")


class _SvSesClientType_Type(Integer32):
    """Custom type svSesClientType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("afp-1-1", 8),
          ("afp-2-0", 9),
          ("dos-lm", 2),
          ("dos-lm-2", 3),
          ("dos-lm-2-1", 6),
          ("down-level", 1),
          ("nt-3-1", 10),
          ("os2-lm-1", 4),
          ("os2-lm-2", 5),
          ("os2-lm-2-1", 7))
    )


_SvSesClientType_Type.__name__ = "Integer32"
_SvSesClientType_Object = MibTableColumn
svSesClientType = _SvSesClientType_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 2, 20, 1, 7),
    _SvSesClientType_Type()
)
svSesClientType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svSesClientType.setStatus("mandatory")


class _SvSesState_Type(Integer32):
    """Custom type svSesState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("deleted", 2))
    )


_SvSesState_Type.__name__ = "Integer32"
_SvSesState_Object = MibTableColumn
svSesState = _SvSesState_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 2, 20, 1, 8),
    _SvSesState_Type()
)
svSesState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svSesState.setStatus("mandatory")
_SvAutoDisconnects_Type = Integer32
_SvAutoDisconnects_Object = MibScalar
svAutoDisconnects = _SvAutoDisconnects_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 2, 21),
    _SvAutoDisconnects_Type()
)
svAutoDisconnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svAutoDisconnects.setStatus("mandatory")
_SvDisConTime_Type = Integer32
_SvDisConTime_Object = MibScalar
svDisConTime = _SvDisConTime_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 2, 22),
    _SvDisConTime_Type()
)
svDisConTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svDisConTime.setStatus("mandatory")
_SvAuditLogSize_Type = Integer32
_SvAuditLogSize_Object = MibScalar
svAuditLogSize = _SvAuditLogSize_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 2, 23),
    _SvAuditLogSize_Type()
)
svAuditLogSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svAuditLogSize.setStatus("mandatory")
_SvUserNumber_Type = Integer32
_SvUserNumber_Object = MibScalar
svUserNumber = _SvUserNumber_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 2, 24),
    _SvUserNumber_Type()
)
svUserNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svUserNumber.setStatus("mandatory")
_SvUserTable_Object = MibTable
svUserTable = _SvUserTable_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 2, 25)
)
if mibBuilder.loadTexts:
    svUserTable.setStatus("mandatory")
_SvUserEntry_Object = MibTableRow
svUserEntry = _SvUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 2, 25, 1)
)
svUserEntry.setIndexNames(
    (0, "LanMgr-Mib-II-MIB", "svUserName"),
)
if mibBuilder.loadTexts:
    svUserEntry.setStatus("mandatory")


class _SvUserName_Type(DisplayString):
    """Custom type svUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_SvUserName_Type.__name__ = "DisplayString"
_SvUserName_Object = MibTableColumn
svUserName = _SvUserName_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 2, 25, 1, 1),
    _SvUserName_Type()
)
svUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svUserName.setStatus("mandatory")
_SvShareNumber_Type = Integer32
_SvShareNumber_Object = MibScalar
svShareNumber = _SvShareNumber_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 2, 26),
    _SvShareNumber_Type()
)
svShareNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svShareNumber.setStatus("mandatory")
_SvShareTable_Object = MibTable
svShareTable = _SvShareTable_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 2, 27)
)
if mibBuilder.loadTexts:
    svShareTable.setStatus("mandatory")
_SvShareEntry_Object = MibTableRow
svShareEntry = _SvShareEntry_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 2, 27, 1)
)
svShareEntry.setIndexNames(
    (0, "LanMgr-Mib-II-MIB", "svShareName"),
)
if mibBuilder.loadTexts:
    svShareEntry.setStatus("mandatory")


class _SvShareName_Type(DisplayString):
    """Custom type svShareName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_SvShareName_Type.__name__ = "DisplayString"
_SvShareName_Object = MibTableColumn
svShareName = _SvShareName_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 2, 27, 1, 1),
    _SvShareName_Type()
)
svShareName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svShareName.setStatus("mandatory")


class _SvSharePath_Type(DisplayString):
    """Custom type svSharePath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SvSharePath_Type.__name__ = "DisplayString"
_SvSharePath_Object = MibTableColumn
svSharePath = _SvSharePath_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 2, 27, 1, 2),
    _SvSharePath_Type()
)
svSharePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svSharePath.setStatus("mandatory")


class _SvShareComment_Type(DisplayString):
    """Custom type svShareComment based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SvShareComment_Type.__name__ = "DisplayString"
_SvShareComment_Object = MibTableColumn
svShareComment = _SvShareComment_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 2, 27, 1, 3),
    _SvShareComment_Type()
)
svShareComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svShareComment.setStatus("mandatory")
_SvPrintQNumber_Type = Integer32
_SvPrintQNumber_Object = MibScalar
svPrintQNumber = _SvPrintQNumber_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 2, 28),
    _SvPrintQNumber_Type()
)
svPrintQNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svPrintQNumber.setStatus("mandatory")
_SvPrintQTable_Object = MibTable
svPrintQTable = _SvPrintQTable_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 2, 29)
)
if mibBuilder.loadTexts:
    svPrintQTable.setStatus("mandatory")
_SvPrintQEntry_Object = MibTableRow
svPrintQEntry = _SvPrintQEntry_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 2, 29, 1)
)
svPrintQEntry.setIndexNames(
    (0, "LanMgr-Mib-II-MIB", "svPrintQName"),
)
if mibBuilder.loadTexts:
    svPrintQEntry.setStatus("mandatory")


class _SvPrintQName_Type(DisplayString):
    """Custom type svPrintQName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_SvPrintQName_Type.__name__ = "DisplayString"
_SvPrintQName_Object = MibTableColumn
svPrintQName = _SvPrintQName_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 2, 29, 1, 1),
    _SvPrintQName_Type()
)
svPrintQName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svPrintQName.setStatus("mandatory")
_SvPrintQNumJobs_Type = Integer32
_SvPrintQNumJobs_Object = MibTableColumn
svPrintQNumJobs = _SvPrintQNumJobs_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 2, 29, 1, 2),
    _SvPrintQNumJobs_Type()
)
svPrintQNumJobs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svPrintQNumJobs.setStatus("mandatory")
_Workstation_ObjectIdentity = ObjectIdentity
workstation = _Workstation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 77, 1, 3)
)
_WkstaStatSessStarts_Type = Counter32
_WkstaStatSessStarts_Object = MibScalar
wkstaStatSessStarts = _WkstaStatSessStarts_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 3, 1),
    _WkstaStatSessStarts_Type()
)
wkstaStatSessStarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wkstaStatSessStarts.setStatus("mandatory")
_WkstaStatSessFails_Type = Counter32
_WkstaStatSessFails_Object = MibScalar
wkstaStatSessFails = _WkstaStatSessFails_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 3, 2),
    _WkstaStatSessFails_Type()
)
wkstaStatSessFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wkstaStatSessFails.setStatus("mandatory")
_WkstaStatUses_Type = Counter32
_WkstaStatUses_Object = MibScalar
wkstaStatUses = _WkstaStatUses_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 3, 3),
    _WkstaStatUses_Type()
)
wkstaStatUses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wkstaStatUses.setStatus("mandatory")
_WkstaStatUseFails_Type = Counter32
_WkstaStatUseFails_Object = MibScalar
wkstaStatUseFails = _WkstaStatUseFails_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 3, 4),
    _WkstaStatUseFails_Type()
)
wkstaStatUseFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wkstaStatUseFails.setStatus("mandatory")
_WkstaStatAutoRecs_Type = Counter32
_WkstaStatAutoRecs_Object = MibScalar
wkstaStatAutoRecs = _WkstaStatAutoRecs_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 3, 5),
    _WkstaStatAutoRecs_Type()
)
wkstaStatAutoRecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wkstaStatAutoRecs.setStatus("mandatory")
_WkstaErrorLogSize_Type = Integer32
_WkstaErrorLogSize_Object = MibScalar
wkstaErrorLogSize = _WkstaErrorLogSize_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 3, 6),
    _WkstaErrorLogSize_Type()
)
wkstaErrorLogSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wkstaErrorLogSize.setStatus("mandatory")
_WkstaUseNumber_Type = Integer32
_WkstaUseNumber_Object = MibScalar
wkstaUseNumber = _WkstaUseNumber_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 3, 7),
    _WkstaUseNumber_Type()
)
wkstaUseNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wkstaUseNumber.setStatus("mandatory")
_WkstaUseTable_Object = MibTable
wkstaUseTable = _WkstaUseTable_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 3, 8)
)
if mibBuilder.loadTexts:
    wkstaUseTable.setStatus("mandatory")
_WkstaUseEntry_Object = MibTableRow
wkstaUseEntry = _WkstaUseEntry_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 3, 8, 1)
)
wkstaUseEntry.setIndexNames(
    (0, "LanMgr-Mib-II-MIB", "useLocalName"),
    (0, "LanMgr-Mib-II-MIB", "useRemote"),
)
if mibBuilder.loadTexts:
    wkstaUseEntry.setStatus("mandatory")


class _UseLocalName_Type(DisplayString):
    """Custom type useLocalName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_UseLocalName_Type.__name__ = "DisplayString"
_UseLocalName_Object = MibTableColumn
useLocalName = _UseLocalName_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 3, 8, 1, 1),
    _UseLocalName_Type()
)
useLocalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    useLocalName.setStatus("mandatory")


class _UseRemote_Type(DisplayString):
    """Custom type useRemote based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_UseRemote_Type.__name__ = "DisplayString"
_UseRemote_Object = MibTableColumn
useRemote = _UseRemote_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 3, 8, 1, 2),
    _UseRemote_Type()
)
useRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    useRemote.setStatus("mandatory")


class _UseStatus_Type(Integer32):
    """Custom type useStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("use-connecting", 5),
          ("use-network-error", 4),
          ("use-ok", 1),
          ("use-paused", 2),
          ("use-reconnecting", 6),
          ("use-session-lost", 3))
    )


_UseStatus_Type.__name__ = "Integer32"
_UseStatus_Object = MibTableColumn
useStatus = _UseStatus_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 3, 8, 1, 3),
    _UseStatus_Type()
)
useStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    useStatus.setStatus("mandatory")
_Domain_ObjectIdentity = ObjectIdentity
domain = _Domain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 77, 1, 4)
)


class _DomPrimaryDomain_Type(DisplayString):
    """Custom type domPrimaryDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_DomPrimaryDomain_Type.__name__ = "DisplayString"
_DomPrimaryDomain_Object = MibScalar
domPrimaryDomain = _DomPrimaryDomain_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 4, 1),
    _DomPrimaryDomain_Type()
)
domPrimaryDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    domPrimaryDomain.setStatus("mandatory")


class _DomLogonDomain_Type(DisplayString):
    """Custom type domLogonDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_DomLogonDomain_Type.__name__ = "DisplayString"
_DomLogonDomain_Object = MibScalar
domLogonDomain = _DomLogonDomain_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 4, 2),
    _DomLogonDomain_Type()
)
domLogonDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    domLogonDomain.setStatus("mandatory")
_DomOtherDomainNumber_Type = Integer32
_DomOtherDomainNumber_Object = MibScalar
domOtherDomainNumber = _DomOtherDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 4, 3),
    _DomOtherDomainNumber_Type()
)
domOtherDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    domOtherDomainNumber.setStatus("mandatory")
_DomOtherDomainTable_Object = MibTable
domOtherDomainTable = _DomOtherDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 4, 4)
)
if mibBuilder.loadTexts:
    domOtherDomainTable.setStatus("mandatory")
_DomOtherDomainEntry_Object = MibTableRow
domOtherDomainEntry = _DomOtherDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 4, 4, 1)
)
domOtherDomainEntry.setIndexNames(
    (0, "LanMgr-Mib-II-MIB", "domOtherName"),
)
if mibBuilder.loadTexts:
    domOtherDomainEntry.setStatus("mandatory")


class _DomOtherName_Type(DisplayString):
    """Custom type domOtherName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_DomOtherName_Type.__name__ = "DisplayString"
_DomOtherName_Object = MibTableColumn
domOtherName = _DomOtherName_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 4, 4, 1, 1),
    _DomOtherName_Type()
)
domOtherName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    domOtherName.setStatus("mandatory")
_DomServerNumber_Type = Integer32
_DomServerNumber_Object = MibScalar
domServerNumber = _DomServerNumber_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 4, 5),
    _DomServerNumber_Type()
)
domServerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    domServerNumber.setStatus("mandatory")
_DomServerTable_Object = MibTable
domServerTable = _DomServerTable_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 4, 6)
)
if mibBuilder.loadTexts:
    domServerTable.setStatus("mandatory")
_DomServerEntry_Object = MibTableRow
domServerEntry = _DomServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 4, 6, 1)
)
domServerEntry.setIndexNames(
    (0, "LanMgr-Mib-II-MIB", "domServerName"),
)
if mibBuilder.loadTexts:
    domServerEntry.setStatus("mandatory")


class _DomServerName_Type(DisplayString):
    """Custom type domServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_DomServerName_Type.__name__ = "DisplayString"
_DomServerName_Object = MibTableColumn
domServerName = _DomServerName_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 4, 6, 1, 1),
    _DomServerName_Type()
)
domServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    domServerName.setStatus("mandatory")
_DomLogonNumber_Type = Integer32
_DomLogonNumber_Object = MibScalar
domLogonNumber = _DomLogonNumber_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 4, 7),
    _DomLogonNumber_Type()
)
domLogonNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    domLogonNumber.setStatus("mandatory")
_DomLogonTable_Object = MibTable
domLogonTable = _DomLogonTable_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 4, 8)
)
if mibBuilder.loadTexts:
    domLogonTable.setStatus("mandatory")
_DomLogonEntry_Object = MibTableRow
domLogonEntry = _DomLogonEntry_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 4, 8, 1)
)
domLogonEntry.setIndexNames(
    (0, "LanMgr-Mib-II-MIB", "domLogonUser"),
    (0, "LanMgr-Mib-II-MIB", "domLogonMachine"),
)
if mibBuilder.loadTexts:
    domLogonEntry.setStatus("mandatory")


class _DomLogonUser_Type(DisplayString):
    """Custom type domLogonUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_DomLogonUser_Type.__name__ = "DisplayString"
_DomLogonUser_Object = MibTableColumn
domLogonUser = _DomLogonUser_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 4, 8, 1, 1),
    _DomLogonUser_Type()
)
domLogonUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    domLogonUser.setStatus("mandatory")


class _DomLogonMachine_Type(DisplayString):
    """Custom type domLogonMachine based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_DomLogonMachine_Type.__name__ = "DisplayString"
_DomLogonMachine_Object = MibTableColumn
domLogonMachine = _DomLogonMachine_Object(
    (1, 3, 6, 1, 4, 1, 77, 1, 4, 8, 1, 2),
    _DomLogonMachine_Type()
)
domLogonMachine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    domLogonMachine.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LanMgr-Mib-II-MIB",
    **{"lanmanager": lanmanager,
       "lanmgr-2": lanmgr_2,
       "common": common,
       "comVersionMaj": comVersionMaj,
       "comVersionMin": comVersionMin,
       "comType": comType,
       "comStatStart": comStatStart,
       "comStatNumNetIOs": comStatNumNetIOs,
       "comStatFiNetIOs": comStatFiNetIOs,
       "comStatFcNetIOs": comStatFcNetIOs,
       "server": server,
       "svDescription": svDescription,
       "svSvcNumber": svSvcNumber,
       "svSvcTable": svSvcTable,
       "svSvcEntry": svSvcEntry,
       "svSvcName": svSvcName,
       "svSvcInstalledState": svSvcInstalledState,
       "svSvcOperatingState": svSvcOperatingState,
       "svSvcCanBeUninstalled": svSvcCanBeUninstalled,
       "svSvcCanBePaused": svSvcCanBePaused,
       "svStatOpens": svStatOpens,
       "svStatDevOpens": svStatDevOpens,
       "svStatQueuedJobs": svStatQueuedJobs,
       "svStatSOpens": svStatSOpens,
       "svStatErrorOuts": svStatErrorOuts,
       "svStatPwErrors": svStatPwErrors,
       "svStatPermErrors": svStatPermErrors,
       "svStatSysErrors": svStatSysErrors,
       "svStatSentBytes": svStatSentBytes,
       "svStatRcvdBytes": svStatRcvdBytes,
       "svStatAvResponse": svStatAvResponse,
       "svSecurityMode": svSecurityMode,
       "svUsers": svUsers,
       "svStatReqBufsNeeded": svStatReqBufsNeeded,
       "svStatBigBufsNeeded": svStatBigBufsNeeded,
       "svSessionNumber": svSessionNumber,
       "svSessionTable": svSessionTable,
       "svSessionEntry": svSessionEntry,
       "svSesClientName": svSesClientName,
       "svSesUserName": svSesUserName,
       "svSesNumOpens": svSesNumOpens,
       "svSesTime": svSesTime,
       "svSesIdleTime": svSesIdleTime,
       "svSesClientType": svSesClientType,
       "svSesState": svSesState,
       "svAutoDisconnects": svAutoDisconnects,
       "svDisConTime": svDisConTime,
       "svAuditLogSize": svAuditLogSize,
       "svUserNumber": svUserNumber,
       "svUserTable": svUserTable,
       "svUserEntry": svUserEntry,
       "svUserName": svUserName,
       "svShareNumber": svShareNumber,
       "svShareTable": svShareTable,
       "svShareEntry": svShareEntry,
       "svShareName": svShareName,
       "svSharePath": svSharePath,
       "svShareComment": svShareComment,
       "svPrintQNumber": svPrintQNumber,
       "svPrintQTable": svPrintQTable,
       "svPrintQEntry": svPrintQEntry,
       "svPrintQName": svPrintQName,
       "svPrintQNumJobs": svPrintQNumJobs,
       "workstation": workstation,
       "wkstaStatSessStarts": wkstaStatSessStarts,
       "wkstaStatSessFails": wkstaStatSessFails,
       "wkstaStatUses": wkstaStatUses,
       "wkstaStatUseFails": wkstaStatUseFails,
       "wkstaStatAutoRecs": wkstaStatAutoRecs,
       "wkstaErrorLogSize": wkstaErrorLogSize,
       "wkstaUseNumber": wkstaUseNumber,
       "wkstaUseTable": wkstaUseTable,
       "wkstaUseEntry": wkstaUseEntry,
       "useLocalName": useLocalName,
       "useRemote": useRemote,
       "useStatus": useStatus,
       "domain": domain,
       "domPrimaryDomain": domPrimaryDomain,
       "domLogonDomain": domLogonDomain,
       "domOtherDomainNumber": domOtherDomainNumber,
       "domOtherDomainTable": domOtherDomainTable,
       "domOtherDomainEntry": domOtherDomainEntry,
       "domOtherName": domOtherName,
       "domServerNumber": domServerNumber,
       "domServerTable": domServerTable,
       "domServerEntry": domServerEntry,
       "domServerName": domServerName,
       "domLogonNumber": domLogonNumber,
       "domLogonTable": domLogonTable,
       "domLogonEntry": domLogonEntry,
       "domLogonUser": domLogonUser,
       "domLogonMachine": domLogonMachine}
)
