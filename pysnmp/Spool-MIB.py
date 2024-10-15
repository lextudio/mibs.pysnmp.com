# SNMP MIB module (Spool-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Spool-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:00:21 2024
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

_Sni_ObjectIdentity = ObjectIdentity
sni = _Sni_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231)
)
_SniProductMibs_ObjectIdentity = ObjectIdentity
sniProductMibs = _SniProductMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2)
)
_SniSpool_ObjectIdentity = ObjectIdentity
sniSpool = _SniSpool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 12)
)
_SniSpoolObjects_ObjectIdentity = ObjectIdentity
sniSpoolObjects = _SniSpoolObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1)
)
_SniSpoolDevTable_ObjectIdentity = ObjectIdentity
sniSpoolDevTable = _SniSpoolDevTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 1)
)
_SpoolDevTabNum_Type = Integer32
_SpoolDevTabNum_Object = MibScalar
spoolDevTabNum = _SpoolDevTabNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 1, 1),
    _SpoolDevTabNum_Type()
)
spoolDevTabNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolDevTabNum.setStatus("mandatory")
_SpoolDevTab_Object = MibTable
spoolDevTab = _SpoolDevTab_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 1, 2)
)
if mibBuilder.loadTexts:
    spoolDevTab.setStatus("mandatory")
_SpoolDevTabEntry_Object = MibTableRow
spoolDevTabEntry = _SpoolDevTabEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 1, 2, 1)
)
spoolDevTabEntry.setIndexNames(
    (0, "Spool-MIB", "spoolDevTabIndex"),
)
if mibBuilder.loadTexts:
    spoolDevTabEntry.setStatus("mandatory")
_SpoolDevTabIndex_Type = Integer32
_SpoolDevTabIndex_Object = MibTableColumn
spoolDevTabIndex = _SpoolDevTabIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 1, 2, 1, 1),
    _SpoolDevTabIndex_Type()
)
spoolDevTabIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolDevTabIndex.setStatus("mandatory")


class _SpoolDevName_Type(DisplayString):
    """Custom type spoolDevName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SpoolDevName_Type.__name__ = "DisplayString"
_SpoolDevName_Object = MibTableColumn
spoolDevName = _SpoolDevName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 1, 2, 1, 2),
    _SpoolDevName_Type()
)
spoolDevName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolDevName.setStatus("mandatory")


class _SpoolDevState_Type(Integer32):
    """Custom type spoolDevState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("error", 3),
          ("inactive", 2))
    )


_SpoolDevState_Type.__name__ = "Integer32"
_SpoolDevState_Object = MibTableColumn
spoolDevState = _SpoolDevState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 1, 2, 1, 3),
    _SpoolDevState_Type()
)
spoolDevState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spoolDevState.setStatus("mandatory")


class _SpoolDevSpoolin_Type(Integer32):
    """Custom type spoolDevSpoolin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_SpoolDevSpoolin_Type.__name__ = "Integer32"
_SpoolDevSpoolin_Object = MibTableColumn
spoolDevSpoolin = _SpoolDevSpoolin_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 1, 2, 1, 4),
    _SpoolDevSpoolin_Type()
)
spoolDevSpoolin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spoolDevSpoolin.setStatus("mandatory")


class _SpoolDevSpoolout_Type(Integer32):
    """Custom type spoolDevSpoolout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_SpoolDevSpoolout_Type.__name__ = "Integer32"
_SpoolDevSpoolout_Object = MibTableColumn
spoolDevSpoolout = _SpoolDevSpoolout_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 1, 2, 1, 5),
    _SpoolDevSpoolout_Type()
)
spoolDevSpoolout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spoolDevSpoolout.setStatus("mandatory")
_SpoolDevErrorMsg_Type = DisplayString
_SpoolDevErrorMsg_Object = MibTableColumn
spoolDevErrorMsg = _SpoolDevErrorMsg_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 1, 2, 1, 6),
    _SpoolDevErrorMsg_Type()
)
spoolDevErrorMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolDevErrorMsg.setStatus("mandatory")


class _SpoolDevStaDate_Type(DisplayString):
    """Custom type spoolDevStaDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SpoolDevStaDate_Type.__name__ = "DisplayString"
_SpoolDevStaDate_Object = MibTableColumn
spoolDevStaDate = _SpoolDevStaDate_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 1, 2, 1, 7),
    _SpoolDevStaDate_Type()
)
spoolDevStaDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolDevStaDate.setStatus("mandatory")


class _SpoolDevPriority_Type(Integer32):
    """Custom type spoolDevPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SpoolDevPriority_Type.__name__ = "Integer32"
_SpoolDevPriority_Object = MibTableColumn
spoolDevPriority = _SpoolDevPriority_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 1, 2, 1, 8),
    _SpoolDevPriority_Type()
)
spoolDevPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolDevPriority.setStatus("mandatory")


class _SpoolDevWaitingJobs_Type(Integer32):
    """Custom type spoolDevWaitingJobs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967296),
    )


_SpoolDevWaitingJobs_Type.__name__ = "Integer32"
_SpoolDevWaitingJobs_Object = MibTableColumn
spoolDevWaitingJobs = _SpoolDevWaitingJobs_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 1, 2, 1, 9),
    _SpoolDevWaitingJobs_Type()
)
spoolDevWaitingJobs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolDevWaitingJobs.setStatus("mandatory")


class _SpoolDevCurForm_Type(DisplayString):
    """Custom type spoolDevCurForm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SpoolDevCurForm_Type.__name__ = "DisplayString"
_SpoolDevCurForm_Object = MibTableColumn
spoolDevCurForm = _SpoolDevCurForm_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 1, 2, 1, 10),
    _SpoolDevCurForm_Type()
)
spoolDevCurForm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolDevCurForm.setStatus("mandatory")
_SpoolDevActJid_Type = DisplayString
_SpoolDevActJid_Object = MibTableColumn
spoolDevActJid = _SpoolDevActJid_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 1, 2, 1, 11),
    _SpoolDevActJid_Type()
)
spoolDevActJid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolDevActJid.setStatus("mandatory")


class _SpoolDevHost_Type(DisplayString):
    """Custom type spoolDevHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SpoolDevHost_Type.__name__ = "DisplayString"
_SpoolDevHost_Object = MibTableColumn
spoolDevHost = _SpoolDevHost_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 1, 2, 1, 12),
    _SpoolDevHost_Type()
)
spoolDevHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolDevHost.setStatus("mandatory")


class _SpoolDevAdmin_Type(DisplayString):
    """Custom type spoolDevAdmin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SpoolDevAdmin_Type.__name__ = "DisplayString"
_SpoolDevAdmin_Object = MibTableColumn
spoolDevAdmin = _SpoolDevAdmin_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 1, 2, 1, 13),
    _SpoolDevAdmin_Type()
)
spoolDevAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolDevAdmin.setStatus("mandatory")


class _SpoolDevPcl_Type(DisplayString):
    """Custom type spoolDevPcl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SpoolDevPcl_Type.__name__ = "DisplayString"
_SpoolDevPcl_Object = MibTableColumn
spoolDevPcl = _SpoolDevPcl_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 1, 2, 1, 14),
    _SpoolDevPcl_Type()
)
spoolDevPcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolDevPcl.setStatus("mandatory")


class _SpoolDevDftForm_Type(DisplayString):
    """Custom type spoolDevDftForm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SpoolDevDftForm_Type.__name__ = "DisplayString"
_SpoolDevDftForm_Object = MibTableColumn
spoolDevDftForm = _SpoolDevDftForm_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 1, 2, 1, 15),
    _SpoolDevDftForm_Type()
)
spoolDevDftForm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolDevDftForm.setStatus("mandatory")


class _SpoolDevSupervisor_Type(DisplayString):
    """Custom type spoolDevSupervisor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SpoolDevSupervisor_Type.__name__ = "DisplayString"
_SpoolDevSupervisor_Object = MibTableColumn
spoolDevSupervisor = _SpoolDevSupervisor_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 1, 2, 1, 16),
    _SpoolDevSupervisor_Type()
)
spoolDevSupervisor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolDevSupervisor.setStatus("mandatory")


class _SpoolDevAdmComment_Type(DisplayString):
    """Custom type spoolDevAdmComment based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SpoolDevAdmComment_Type.__name__ = "DisplayString"
_SpoolDevAdmComment_Object = MibTableColumn
spoolDevAdmComment = _SpoolDevAdmComment_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 1, 2, 1, 17),
    _SpoolDevAdmComment_Type()
)
spoolDevAdmComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spoolDevAdmComment.setStatus("mandatory")


class _SpoolDevUsrComment_Type(DisplayString):
    """Custom type spoolDevUsrComment based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SpoolDevUsrComment_Type.__name__ = "DisplayString"
_SpoolDevUsrComment_Object = MibTableColumn
spoolDevUsrComment = _SpoolDevUsrComment_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 1, 2, 1, 18),
    _SpoolDevUsrComment_Type()
)
spoolDevUsrComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolDevUsrComment.setStatus("mandatory")


class _SpoolDevEnablePoll_Type(Integer32):
    """Custom type spoolDevEnablePoll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_SpoolDevEnablePoll_Type.__name__ = "Integer32"
_SpoolDevEnablePoll_Object = MibTableColumn
spoolDevEnablePoll = _SpoolDevEnablePoll_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 1, 2, 1, 19),
    _SpoolDevEnablePoll_Type()
)
spoolDevEnablePoll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spoolDevEnablePoll.setStatus("mandatory")
_SniSpoolSrvTable_ObjectIdentity = ObjectIdentity
sniSpoolSrvTable = _SniSpoolSrvTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 2)
)
_SpoolSrvTabNum_Type = Integer32
_SpoolSrvTabNum_Object = MibScalar
spoolSrvTabNum = _SpoolSrvTabNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 2, 1),
    _SpoolSrvTabNum_Type()
)
spoolSrvTabNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolSrvTabNum.setStatus("mandatory")
_SpoolSrvTab_Object = MibTable
spoolSrvTab = _SpoolSrvTab_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 2, 2)
)
if mibBuilder.loadTexts:
    spoolSrvTab.setStatus("mandatory")
_SpoolSrvTabEntry_Object = MibTableRow
spoolSrvTabEntry = _SpoolSrvTabEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 2, 2, 1)
)
spoolSrvTabEntry.setIndexNames(
    (0, "Spool-MIB", "spoolSrvTabIndex"),
)
if mibBuilder.loadTexts:
    spoolSrvTabEntry.setStatus("mandatory")
_SpoolSrvTabIndex_Type = Integer32
_SpoolSrvTabIndex_Object = MibTableColumn
spoolSrvTabIndex = _SpoolSrvTabIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 2, 2, 1, 1),
    _SpoolSrvTabIndex_Type()
)
spoolSrvTabIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolSrvTabIndex.setStatus("mandatory")


class _SpoolSrvName_Type(DisplayString):
    """Custom type spoolSrvName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SpoolSrvName_Type.__name__ = "DisplayString"
_SpoolSrvName_Object = MibTableColumn
spoolSrvName = _SpoolSrvName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 2, 2, 1, 2),
    _SpoolSrvName_Type()
)
spoolSrvName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolSrvName.setStatus("mandatory")


class _SpoolSrvAdmin_Type(DisplayString):
    """Custom type spoolSrvAdmin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SpoolSrvAdmin_Type.__name__ = "DisplayString"
_SpoolSrvAdmin_Object = MibTableColumn
spoolSrvAdmin = _SpoolSrvAdmin_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 2, 2, 1, 3),
    _SpoolSrvAdmin_Type()
)
spoolSrvAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolSrvAdmin.setStatus("mandatory")


class _SpoolSrvHost_Type(DisplayString):
    """Custom type spoolSrvHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SpoolSrvHost_Type.__name__ = "DisplayString"
_SpoolSrvHost_Object = MibTableColumn
spoolSrvHost = _SpoolSrvHost_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 2, 2, 1, 4),
    _SpoolSrvHost_Type()
)
spoolSrvHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolSrvHost.setStatus("mandatory")


class _SpoolSrvSchedPolicy_Type(DisplayString):
    """Custom type spoolSrvSchedPolicy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SpoolSrvSchedPolicy_Type.__name__ = "DisplayString"
_SpoolSrvSchedPolicy_Object = MibTableColumn
spoolSrvSchedPolicy = _SpoolSrvSchedPolicy_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 2, 2, 1, 5),
    _SpoolSrvSchedPolicy_Type()
)
spoolSrvSchedPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolSrvSchedPolicy.setStatus("mandatory")


class _SpoolSrvState_Type(Integer32):
    """Custom type spoolSrvState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2),
          ("shutdown", 3))
    )


_SpoolSrvState_Type.__name__ = "Integer32"
_SpoolSrvState_Object = MibTableColumn
spoolSrvState = _SpoolSrvState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 2, 2, 1, 6),
    _SpoolSrvState_Type()
)
spoolSrvState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolSrvState.setStatus("mandatory")


class _SpoolSrvSpoolin_Type(Integer32):
    """Custom type spoolSrvSpoolin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_SpoolSrvSpoolin_Type.__name__ = "Integer32"
_SpoolSrvSpoolin_Object = MibTableColumn
spoolSrvSpoolin = _SpoolSrvSpoolin_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 2, 2, 1, 7),
    _SpoolSrvSpoolin_Type()
)
spoolSrvSpoolin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolSrvSpoolin.setStatus("mandatory")


class _SpoolSrvSpoolout_Type(Integer32):
    """Custom type spoolSrvSpoolout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_SpoolSrvSpoolout_Type.__name__ = "Integer32"
_SpoolSrvSpoolout_Object = MibTableColumn
spoolSrvSpoolout = _SpoolSrvSpoolout_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 2, 2, 1, 8),
    _SpoolSrvSpoolout_Type()
)
spoolSrvSpoolout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolSrvSpoolout.setStatus("mandatory")


class _SpoolSrvLoadLevel_Type(Integer32):
    """Custom type spoolSrvLoadLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SpoolSrvLoadLevel_Type.__name__ = "Integer32"
_SpoolSrvLoadLevel_Object = MibTableColumn
spoolSrvLoadLevel = _SpoolSrvLoadLevel_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 2, 2, 1, 9),
    _SpoolSrvLoadLevel_Type()
)
spoolSrvLoadLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolSrvLoadLevel.setStatus("mandatory")


class _SpoolSrvMaxJobs_Type(Integer32):
    """Custom type spoolSrvMaxJobs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4294967296),
    )


_SpoolSrvMaxJobs_Type.__name__ = "Integer32"
_SpoolSrvMaxJobs_Object = MibTableColumn
spoolSrvMaxJobs = _SpoolSrvMaxJobs_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 2, 2, 1, 10),
    _SpoolSrvMaxJobs_Type()
)
spoolSrvMaxJobs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolSrvMaxJobs.setStatus("mandatory")


class _SpoolSrvWaitingJobs_Type(Integer32):
    """Custom type spoolSrvWaitingJobs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967296),
    )


_SpoolSrvWaitingJobs_Type.__name__ = "Integer32"
_SpoolSrvWaitingJobs_Object = MibTableColumn
spoolSrvWaitingJobs = _SpoolSrvWaitingJobs_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 2, 2, 1, 11),
    _SpoolSrvWaitingJobs_Type()
)
spoolSrvWaitingJobs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolSrvWaitingJobs.setStatus("mandatory")
_SniSpoolSpvTable_ObjectIdentity = ObjectIdentity
sniSpoolSpvTable = _SniSpoolSpvTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 3)
)
_SpoolSpvTabNum_Type = Integer32
_SpoolSpvTabNum_Object = MibScalar
spoolSpvTabNum = _SpoolSpvTabNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 3, 1),
    _SpoolSpvTabNum_Type()
)
spoolSpvTabNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolSpvTabNum.setStatus("mandatory")
_SpoolSpvTab_Object = MibTable
spoolSpvTab = _SpoolSpvTab_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 3, 2)
)
if mibBuilder.loadTexts:
    spoolSpvTab.setStatus("mandatory")
_SpoolSpvTabEntry_Object = MibTableRow
spoolSpvTabEntry = _SpoolSpvTabEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 3, 2, 1)
)
spoolSpvTabEntry.setIndexNames(
    (0, "Spool-MIB", "spoolSpvTabIndex"),
)
if mibBuilder.loadTexts:
    spoolSpvTabEntry.setStatus("mandatory")
_SpoolSpvTabIndex_Type = Integer32
_SpoolSpvTabIndex_Object = MibTableColumn
spoolSpvTabIndex = _SpoolSpvTabIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 3, 2, 1, 1),
    _SpoolSpvTabIndex_Type()
)
spoolSpvTabIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolSpvTabIndex.setStatus("mandatory")


class _SpoolSpvName_Type(DisplayString):
    """Custom type spoolSpvName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SpoolSpvName_Type.__name__ = "DisplayString"
_SpoolSpvName_Object = MibTableColumn
spoolSpvName = _SpoolSpvName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 3, 2, 1, 2),
    _SpoolSpvName_Type()
)
spoolSpvName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolSpvName.setStatus("mandatory")


class _SpoolSpvServName_Type(DisplayString):
    """Custom type spoolSpvServName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SpoolSpvServName_Type.__name__ = "DisplayString"
_SpoolSpvServName_Object = MibTableColumn
spoolSpvServName = _SpoolSpvServName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 3, 2, 1, 3),
    _SpoolSpvServName_Type()
)
spoolSpvServName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolSpvServName.setStatus("mandatory")


class _SpoolSpvAdmin_Type(DisplayString):
    """Custom type spoolSpvAdmin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SpoolSpvAdmin_Type.__name__ = "DisplayString"
_SpoolSpvAdmin_Object = MibTableColumn
spoolSpvAdmin = _SpoolSpvAdmin_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 3, 2, 1, 4),
    _SpoolSpvAdmin_Type()
)
spoolSpvAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolSpvAdmin.setStatus("mandatory")


class _SpoolSpvHost_Type(DisplayString):
    """Custom type spoolSpvHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SpoolSpvHost_Type.__name__ = "DisplayString"
_SpoolSpvHost_Object = MibTableColumn
spoolSpvHost = _SpoolSpvHost_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 3, 2, 1, 5),
    _SpoolSpvHost_Type()
)
spoolSpvHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolSpvHost.setStatus("mandatory")


class _SpoolSpvState_Type(Integer32):
    """Custom type spoolSpvState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2),
          ("shutdown", 3))
    )


_SpoolSpvState_Type.__name__ = "Integer32"
_SpoolSpvState_Object = MibTableColumn
spoolSpvState = _SpoolSpvState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 3, 2, 1, 6),
    _SpoolSpvState_Type()
)
spoolSpvState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolSpvState.setStatus("mandatory")
_SniSpoolDgrTable_ObjectIdentity = ObjectIdentity
sniSpoolDgrTable = _SniSpoolDgrTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 4)
)
_SpoolDgrTabNum_Type = Integer32
_SpoolDgrTabNum_Object = MibScalar
spoolDgrTabNum = _SpoolDgrTabNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 4, 1),
    _SpoolDgrTabNum_Type()
)
spoolDgrTabNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolDgrTabNum.setStatus("mandatory")
_SpoolDgrTab_Object = MibTable
spoolDgrTab = _SpoolDgrTab_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 4, 2)
)
if mibBuilder.loadTexts:
    spoolDgrTab.setStatus("mandatory")
_SpoolDgrTabEntry_Object = MibTableRow
spoolDgrTabEntry = _SpoolDgrTabEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 4, 2, 1)
)
spoolDgrTabEntry.setIndexNames(
    (0, "Spool-MIB", "spoolDgrTabIndex"),
)
if mibBuilder.loadTexts:
    spoolDgrTabEntry.setStatus("mandatory")
_SpoolDgrTabIndex_Type = Integer32
_SpoolDgrTabIndex_Object = MibTableColumn
spoolDgrTabIndex = _SpoolDgrTabIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 4, 2, 1, 1),
    _SpoolDgrTabIndex_Type()
)
spoolDgrTabIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolDgrTabIndex.setStatus("mandatory")


class _SpoolDgrName_Type(DisplayString):
    """Custom type spoolDgrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SpoolDgrName_Type.__name__ = "DisplayString"
_SpoolDgrName_Object = MibTableColumn
spoolDgrName = _SpoolDgrName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 4, 2, 1, 2),
    _SpoolDgrName_Type()
)
spoolDgrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolDgrName.setStatus("mandatory")


class _SpoolDgrAdmin_Type(DisplayString):
    """Custom type spoolDgrAdmin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SpoolDgrAdmin_Type.__name__ = "DisplayString"
_SpoolDgrAdmin_Object = MibTableColumn
spoolDgrAdmin = _SpoolDgrAdmin_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 4, 2, 1, 3),
    _SpoolDgrAdmin_Type()
)
spoolDgrAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolDgrAdmin.setStatus("mandatory")


class _SpoolDgrDeviceList_Type(DisplayString):
    """Custom type spoolDgrDeviceList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SpoolDgrDeviceList_Type.__name__ = "DisplayString"
_SpoolDgrDeviceList_Object = MibTableColumn
spoolDgrDeviceList = _SpoolDgrDeviceList_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 4, 2, 1, 4),
    _SpoolDgrDeviceList_Type()
)
spoolDgrDeviceList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolDgrDeviceList.setStatus("mandatory")


class _SpoolDgrSpoolin_Type(Integer32):
    """Custom type spoolDgrSpoolin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_SpoolDgrSpoolin_Type.__name__ = "Integer32"
_SpoolDgrSpoolin_Object = MibTableColumn
spoolDgrSpoolin = _SpoolDgrSpoolin_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 4, 2, 1, 5),
    _SpoolDgrSpoolin_Type()
)
spoolDgrSpoolin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolDgrSpoolin.setStatus("mandatory")


class _SpoolDgrDate_Type(DisplayString):
    """Custom type spoolDgrDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SpoolDgrDate_Type.__name__ = "DisplayString"
_SpoolDgrDate_Object = MibTableColumn
spoolDgrDate = _SpoolDgrDate_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 4, 2, 1, 6),
    _SpoolDgrDate_Type()
)
spoolDgrDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolDgrDate.setStatus("mandatory")


class _SpoolDgrComment_Type(DisplayString):
    """Custom type spoolDgrComment based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SpoolDgrComment_Type.__name__ = "DisplayString"
_SpoolDgrComment_Object = MibTableColumn
spoolDgrComment = _SpoolDgrComment_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 4, 2, 1, 7),
    _SpoolDgrComment_Type()
)
spoolDgrComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolDgrComment.setStatus("mandatory")
_SniSpoolHostTable_ObjectIdentity = ObjectIdentity
sniSpoolHostTable = _SniSpoolHostTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 5)
)
_SpoolHostTabNum_Type = Integer32
_SpoolHostTabNum_Object = MibScalar
spoolHostTabNum = _SpoolHostTabNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 5, 1),
    _SpoolHostTabNum_Type()
)
spoolHostTabNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolHostTabNum.setStatus("mandatory")
_SpoolHostTab_Object = MibTable
spoolHostTab = _SpoolHostTab_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 5, 2)
)
if mibBuilder.loadTexts:
    spoolHostTab.setStatus("mandatory")
_SpoolHostTabEntry_Object = MibTableRow
spoolHostTabEntry = _SpoolHostTabEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 5, 2, 1)
)
spoolHostTabEntry.setIndexNames(
    (0, "Spool-MIB", "spoolHostTabIndex"),
)
if mibBuilder.loadTexts:
    spoolHostTabEntry.setStatus("mandatory")
_SpoolHostTabIndex_Type = Integer32
_SpoolHostTabIndex_Object = MibTableColumn
spoolHostTabIndex = _SpoolHostTabIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 5, 2, 1, 1),
    _SpoolHostTabIndex_Type()
)
spoolHostTabIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolHostTabIndex.setStatus("mandatory")


class _SpoolHostName_Type(DisplayString):
    """Custom type spoolHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SpoolHostName_Type.__name__ = "DisplayString"
_SpoolHostName_Object = MibTableColumn
spoolHostName = _SpoolHostName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 5, 2, 1, 2),
    _SpoolHostName_Type()
)
spoolHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolHostName.setStatus("mandatory")


class _SpoolHostDestination_Type(DisplayString):
    """Custom type spoolHostDestination based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SpoolHostDestination_Type.__name__ = "DisplayString"
_SpoolHostDestination_Object = MibTableColumn
spoolHostDestination = _SpoolHostDestination_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 5, 2, 1, 5),
    _SpoolHostDestination_Type()
)
spoolHostDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolHostDestination.setStatus("mandatory")


class _SpoolHostSuppHost_Type(DisplayString):
    """Custom type spoolHostSuppHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SpoolHostSuppHost_Type.__name__ = "DisplayString"
_SpoolHostSuppHost_Object = MibTableColumn
spoolHostSuppHost = _SpoolHostSuppHost_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 5, 2, 1, 6),
    _SpoolHostSuppHost_Type()
)
spoolHostSuppHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolHostSuppHost.setStatus("mandatory")


class _SpoolHostResponsibility_Type(Integer32):
    """Custom type spoolHostResponsibility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("parasite", 3),
          ("potmaster", 1),
          ("slave", 2))
    )


_SpoolHostResponsibility_Type.__name__ = "Integer32"
_SpoolHostResponsibility_Object = MibTableColumn
spoolHostResponsibility = _SpoolHostResponsibility_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 5, 2, 1, 7),
    _SpoolHostResponsibility_Type()
)
spoolHostResponsibility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolHostResponsibility.setStatus("mandatory")


class _SpoolHostState_Type(Integer32):
    """Custom type spoolHostState based on Integer32"""
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
          ("activemaster", 2),
          ("inactive", 3),
          ("shutdown", 4))
    )


_SpoolHostState_Type.__name__ = "Integer32"
_SpoolHostState_Object = MibTableColumn
spoolHostState = _SpoolHostState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 5, 2, 1, 8),
    _SpoolHostState_Type()
)
spoolHostState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolHostState.setStatus("mandatory")
_SniSpoolJobTable_ObjectIdentity = ObjectIdentity
sniSpoolJobTable = _SniSpoolJobTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6)
)
_SpoolJobTabNum_Type = Integer32
_SpoolJobTabNum_Object = MibScalar
spoolJobTabNum = _SpoolJobTabNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6, 1),
    _SpoolJobTabNum_Type()
)
spoolJobTabNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolJobTabNum.setStatus("mandatory")
_SpoolJobTab_Object = MibTable
spoolJobTab = _SpoolJobTab_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6, 2)
)
if mibBuilder.loadTexts:
    spoolJobTab.setStatus("mandatory")
_SpoolJobTabEntry_Object = MibTableRow
spoolJobTabEntry = _SpoolJobTabEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6, 2, 1)
)
spoolJobTabEntry.setIndexNames(
    (0, "Spool-MIB", "spoolJobTabIndex"),
)
if mibBuilder.loadTexts:
    spoolJobTabEntry.setStatus("mandatory")
_SpoolJobTabIndex_Type = Integer32
_SpoolJobTabIndex_Object = MibTableColumn
spoolJobTabIndex = _SpoolJobTabIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6, 2, 1, 1),
    _SpoolJobTabIndex_Type()
)
spoolJobTabIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolJobTabIndex.setStatus("mandatory")


class _SpoolJobGlobalJid_Type(DisplayString):
    """Custom type spoolJobGlobalJid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SpoolJobGlobalJid_Type.__name__ = "DisplayString"
_SpoolJobGlobalJid_Object = MibTableColumn
spoolJobGlobalJid = _SpoolJobGlobalJid_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6, 2, 1, 2),
    _SpoolJobGlobalJid_Type()
)
spoolJobGlobalJid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolJobGlobalJid.setStatus("mandatory")


class _SpoolJobLocalJid_Type(Integer32):
    """Custom type spoolJobLocalJid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SpoolJobLocalJid_Type.__name__ = "Integer32"
_SpoolJobLocalJid_Object = MibTableColumn
spoolJobLocalJid = _SpoolJobLocalJid_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6, 2, 1, 3),
    _SpoolJobLocalJid_Type()
)
spoolJobLocalJid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolJobLocalJid.setStatus("mandatory")


class _SpoolJobTitle_Type(DisplayString):
    """Custom type spoolJobTitle based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SpoolJobTitle_Type.__name__ = "DisplayString"
_SpoolJobTitle_Object = MibTableColumn
spoolJobTitle = _SpoolJobTitle_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6, 2, 1, 4),
    _SpoolJobTitle_Type()
)
spoolJobTitle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolJobTitle.setStatus("mandatory")


class _SpoolJobComment_Type(DisplayString):
    """Custom type spoolJobComment based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SpoolJobComment_Type.__name__ = "DisplayString"
_SpoolJobComment_Object = MibTableColumn
spoolJobComment = _SpoolJobComment_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6, 2, 1, 5),
    _SpoolJobComment_Type()
)
spoolJobComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolJobComment.setStatus("mandatory")


class _SpoolJobOriginator_Type(DisplayString):
    """Custom type spoolJobOriginator based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SpoolJobOriginator_Type.__name__ = "DisplayString"
_SpoolJobOriginator_Object = MibTableColumn
spoolJobOriginator = _SpoolJobOriginator_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6, 2, 1, 6),
    _SpoolJobOriginator_Type()
)
spoolJobOriginator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolJobOriginator.setStatus("mandatory")


class _SpoolJobOrigHost_Type(DisplayString):
    """Custom type spoolJobOrigHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SpoolJobOrigHost_Type.__name__ = "DisplayString"
_SpoolJobOrigHost_Object = MibTableColumn
spoolJobOrigHost = _SpoolJobOrigHost_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6, 2, 1, 7),
    _SpoolJobOrigHost_Type()
)
spoolJobOrigHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolJobOrigHost.setStatus("mandatory")


class _SpoolJobOrigTime_Type(DisplayString):
    """Custom type spoolJobOrigTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SpoolJobOrigTime_Type.__name__ = "DisplayString"
_SpoolJobOrigTime_Object = MibTableColumn
spoolJobOrigTime = _SpoolJobOrigTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6, 2, 1, 8),
    _SpoolJobOrigTime_Type()
)
spoolJobOrigTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolJobOrigTime.setStatus("mandatory")


class _SpoolJobDestination_Type(DisplayString):
    """Custom type spoolJobDestination based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SpoolJobDestination_Type.__name__ = "DisplayString"
_SpoolJobDestination_Object = MibTableColumn
spoolJobDestination = _SpoolJobDestination_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6, 2, 1, 9),
    _SpoolJobDestination_Type()
)
spoolJobDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spoolJobDestination.setStatus("mandatory")


class _SpoolJobPriority_Type(Integer32):
    """Custom type spoolJobPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SpoolJobPriority_Type.__name__ = "Integer32"
_SpoolJobPriority_Object = MibTableColumn
spoolJobPriority = _SpoolJobPriority_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6, 2, 1, 10),
    _SpoolJobPriority_Type()
)
spoolJobPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spoolJobPriority.setStatus("mandatory")


class _SpoolJobSecurityLevel_Type(Integer32):
    """Custom type spoolJobSecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("confidential", 3),
          ("secret", 4),
          ("sensitive", 2),
          ("topsecret", 5),
          ("unclassified", 1))
    )


_SpoolJobSecurityLevel_Type.__name__ = "Integer32"
_SpoolJobSecurityLevel_Object = MibTableColumn
spoolJobSecurityLevel = _SpoolJobSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6, 2, 1, 11),
    _SpoolJobSecurityLevel_Type()
)
spoolJobSecurityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolJobSecurityLevel.setStatus("mandatory")


class _SpoolJobFileList_Type(DisplayString):
    """Custom type spoolJobFileList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SpoolJobFileList_Type.__name__ = "DisplayString"
_SpoolJobFileList_Object = MibTableColumn
spoolJobFileList = _SpoolJobFileList_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6, 2, 1, 12),
    _SpoolJobFileList_Type()
)
spoolJobFileList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolJobFileList.setStatus("mandatory")


class _SpoolJobTotalSize_Type(Integer32):
    """Custom type spoolJobTotalSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967296),
    )


_SpoolJobTotalSize_Type.__name__ = "Integer32"
_SpoolJobTotalSize_Object = MibTableColumn
spoolJobTotalSize = _SpoolJobTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6, 2, 1, 13),
    _SpoolJobTotalSize_Type()
)
spoolJobTotalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolJobTotalSize.setStatus("mandatory")


class _SpoolJobRawMode_Type(Integer32):
    """Custom type spoolJobRawMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_SpoolJobRawMode_Type.__name__ = "Integer32"
_SpoolJobRawMode_Object = MibTableColumn
spoolJobRawMode = _SpoolJobRawMode_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6, 2, 1, 14),
    _SpoolJobRawMode_Type()
)
spoolJobRawMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolJobRawMode.setStatus("mandatory")


class _SpoolJobStartTime_Type(DisplayString):
    """Custom type spoolJobStartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SpoolJobStartTime_Type.__name__ = "DisplayString"
_SpoolJobStartTime_Object = MibTableColumn
spoolJobStartTime = _SpoolJobStartTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6, 2, 1, 15),
    _SpoolJobStartTime_Type()
)
spoolJobStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolJobStartTime.setStatus("mandatory")


class _SpoolJobDelTime_Type(DisplayString):
    """Custom type spoolJobDelTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SpoolJobDelTime_Type.__name__ = "DisplayString"
_SpoolJobDelTime_Object = MibTableColumn
spoolJobDelTime = _SpoolJobDelTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6, 2, 1, 16),
    _SpoolJobDelTime_Type()
)
spoolJobDelTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolJobDelTime.setStatus("mandatory")


class _SpoolJobRetTime_Type(Integer32):
    """Custom type spoolJobRetTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4294967296),
    )


_SpoolJobRetTime_Type.__name__ = "Integer32"
_SpoolJobRetTime_Object = MibTableColumn
spoolJobRetTime = _SpoolJobRetTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6, 2, 1, 17),
    _SpoolJobRetTime_Type()
)
spoolJobRetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolJobRetTime.setStatus("mandatory")


class _SpoolJobDevName_Type(DisplayString):
    """Custom type spoolJobDevName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SpoolJobDevName_Type.__name__ = "DisplayString"
_SpoolJobDevName_Object = MibTableColumn
spoolJobDevName = _SpoolJobDevName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6, 2, 1, 18),
    _SpoolJobDevName_Type()
)
spoolJobDevName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolJobDevName.setStatus("mandatory")


class _SpoolJobState_Type(Integer32):
    """Custom type spoolJobState based on Integer32"""
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
        *(("active", 1),
          ("cancel", 10),
          ("data-filtering", 5),
          ("error", 7),
          ("file-transfer", 6),
          ("interrupted", 9),
          ("suspend", 3),
          ("terminated", 8),
          ("top", 4),
          ("wait", 2))
    )


_SpoolJobState_Type.__name__ = "Integer32"
_SpoolJobState_Object = MibTableColumn
spoolJobState = _SpoolJobState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6, 2, 1, 19),
    _SpoolJobState_Type()
)
spoolJobState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spoolJobState.setStatus("mandatory")


class _SpoolJobErrorMsg_Type(DisplayString):
    """Custom type spoolJobErrorMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SpoolJobErrorMsg_Type.__name__ = "DisplayString"
_SpoolJobErrorMsg_Object = MibTableColumn
spoolJobErrorMsg = _SpoolJobErrorMsg_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6, 2, 1, 20),
    _SpoolJobErrorMsg_Type()
)
spoolJobErrorMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolJobErrorMsg.setStatus("mandatory")


class _SpoolJobRank_Type(Integer32):
    """Custom type spoolJobRank based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SpoolJobRank_Type.__name__ = "Integer32"
_SpoolJobRank_Object = MibTableColumn
spoolJobRank = _SpoolJobRank_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6, 2, 1, 21),
    _SpoolJobRank_Type()
)
spoolJobRank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolJobRank.setStatus("mandatory")


class _SpoolJobRqCopies_Type(Integer32):
    """Custom type spoolJobRqCopies based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SpoolJobRqCopies_Type.__name__ = "Integer32"
_SpoolJobRqCopies_Object = MibTableColumn
spoolJobRqCopies = _SpoolJobRqCopies_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6, 2, 1, 22),
    _SpoolJobRqCopies_Type()
)
spoolJobRqCopies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolJobRqCopies.setStatus("mandatory")


class _SpoolJobPrCopies_Type(Integer32):
    """Custom type spoolJobPrCopies based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SpoolJobPrCopies_Type.__name__ = "Integer32"
_SpoolJobPrCopies_Object = MibTableColumn
spoolJobPrCopies = _SpoolJobPrCopies_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6, 2, 1, 23),
    _SpoolJobPrCopies_Type()
)
spoolJobPrCopies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolJobPrCopies.setStatus("mandatory")


class _SpoolJobPrPercent_Type(Integer32):
    """Custom type spoolJobPrPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SpoolJobPrPercent_Type.__name__ = "Integer32"
_SpoolJobPrPercent_Object = MibTableColumn
spoolJobPrPercent = _SpoolJobPrPercent_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 12, 1, 6, 2, 1, 24),
    _SpoolJobPrPercent_Type()
)
spoolJobPrPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spoolJobPrPercent.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Spool-MIB",
    **{"sni": sni,
       "sniProductMibs": sniProductMibs,
       "sniSpool": sniSpool,
       "sniSpoolObjects": sniSpoolObjects,
       "sniSpoolDevTable": sniSpoolDevTable,
       "spoolDevTabNum": spoolDevTabNum,
       "spoolDevTab": spoolDevTab,
       "spoolDevTabEntry": spoolDevTabEntry,
       "spoolDevTabIndex": spoolDevTabIndex,
       "spoolDevName": spoolDevName,
       "spoolDevState": spoolDevState,
       "spoolDevSpoolin": spoolDevSpoolin,
       "spoolDevSpoolout": spoolDevSpoolout,
       "spoolDevErrorMsg": spoolDevErrorMsg,
       "spoolDevStaDate": spoolDevStaDate,
       "spoolDevPriority": spoolDevPriority,
       "spoolDevWaitingJobs": spoolDevWaitingJobs,
       "spoolDevCurForm": spoolDevCurForm,
       "spoolDevActJid": spoolDevActJid,
       "spoolDevHost": spoolDevHost,
       "spoolDevAdmin": spoolDevAdmin,
       "spoolDevPcl": spoolDevPcl,
       "spoolDevDftForm": spoolDevDftForm,
       "spoolDevSupervisor": spoolDevSupervisor,
       "spoolDevAdmComment": spoolDevAdmComment,
       "spoolDevUsrComment": spoolDevUsrComment,
       "spoolDevEnablePoll": spoolDevEnablePoll,
       "sniSpoolSrvTable": sniSpoolSrvTable,
       "spoolSrvTabNum": spoolSrvTabNum,
       "spoolSrvTab": spoolSrvTab,
       "spoolSrvTabEntry": spoolSrvTabEntry,
       "spoolSrvTabIndex": spoolSrvTabIndex,
       "spoolSrvName": spoolSrvName,
       "spoolSrvAdmin": spoolSrvAdmin,
       "spoolSrvHost": spoolSrvHost,
       "spoolSrvSchedPolicy": spoolSrvSchedPolicy,
       "spoolSrvState": spoolSrvState,
       "spoolSrvSpoolin": spoolSrvSpoolin,
       "spoolSrvSpoolout": spoolSrvSpoolout,
       "spoolSrvLoadLevel": spoolSrvLoadLevel,
       "spoolSrvMaxJobs": spoolSrvMaxJobs,
       "spoolSrvWaitingJobs": spoolSrvWaitingJobs,
       "sniSpoolSpvTable": sniSpoolSpvTable,
       "spoolSpvTabNum": spoolSpvTabNum,
       "spoolSpvTab": spoolSpvTab,
       "spoolSpvTabEntry": spoolSpvTabEntry,
       "spoolSpvTabIndex": spoolSpvTabIndex,
       "spoolSpvName": spoolSpvName,
       "spoolSpvServName": spoolSpvServName,
       "spoolSpvAdmin": spoolSpvAdmin,
       "spoolSpvHost": spoolSpvHost,
       "spoolSpvState": spoolSpvState,
       "sniSpoolDgrTable": sniSpoolDgrTable,
       "spoolDgrTabNum": spoolDgrTabNum,
       "spoolDgrTab": spoolDgrTab,
       "spoolDgrTabEntry": spoolDgrTabEntry,
       "spoolDgrTabIndex": spoolDgrTabIndex,
       "spoolDgrName": spoolDgrName,
       "spoolDgrAdmin": spoolDgrAdmin,
       "spoolDgrDeviceList": spoolDgrDeviceList,
       "spoolDgrSpoolin": spoolDgrSpoolin,
       "spoolDgrDate": spoolDgrDate,
       "spoolDgrComment": spoolDgrComment,
       "sniSpoolHostTable": sniSpoolHostTable,
       "spoolHostTabNum": spoolHostTabNum,
       "spoolHostTab": spoolHostTab,
       "spoolHostTabEntry": spoolHostTabEntry,
       "spoolHostTabIndex": spoolHostTabIndex,
       "spoolHostName": spoolHostName,
       "spoolHostDestination": spoolHostDestination,
       "spoolHostSuppHost": spoolHostSuppHost,
       "spoolHostResponsibility": spoolHostResponsibility,
       "spoolHostState": spoolHostState,
       "sniSpoolJobTable": sniSpoolJobTable,
       "spoolJobTabNum": spoolJobTabNum,
       "spoolJobTab": spoolJobTab,
       "spoolJobTabEntry": spoolJobTabEntry,
       "spoolJobTabIndex": spoolJobTabIndex,
       "spoolJobGlobalJid": spoolJobGlobalJid,
       "spoolJobLocalJid": spoolJobLocalJid,
       "spoolJobTitle": spoolJobTitle,
       "spoolJobComment": spoolJobComment,
       "spoolJobOriginator": spoolJobOriginator,
       "spoolJobOrigHost": spoolJobOrigHost,
       "spoolJobOrigTime": spoolJobOrigTime,
       "spoolJobDestination": spoolJobDestination,
       "spoolJobPriority": spoolJobPriority,
       "spoolJobSecurityLevel": spoolJobSecurityLevel,
       "spoolJobFileList": spoolJobFileList,
       "spoolJobTotalSize": spoolJobTotalSize,
       "spoolJobRawMode": spoolJobRawMode,
       "spoolJobStartTime": spoolJobStartTime,
       "spoolJobDelTime": spoolJobDelTime,
       "spoolJobRetTime": spoolJobRetTime,
       "spoolJobDevName": spoolJobDevName,
       "spoolJobState": spoolJobState,
       "spoolJobErrorMsg": spoolJobErrorMsg,
       "spoolJobRank": spoolJobRank,
       "spoolJobRqCopies": spoolJobRqCopies,
       "spoolJobPrCopies": spoolJobPrCopies,
       "spoolJobPrPercent": spoolJobPrPercent}
)
