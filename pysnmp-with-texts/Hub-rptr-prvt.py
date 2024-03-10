"""SNMP MIB module (Hub-rptr-prvt) expressed in pysnmp data model.

This Python module is designed to be imported and executed by the
pysnmp library.

See https://www.pysnmp.com/pysnmp for further information.

Notes
-----
ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Hub-rptr-prvt
Produced by pysmi-1.3.3 at Sun Mar 10 11:15:12 2024
On host MacBook-Pro.local platform Darwin version 23.4.0 by user lextm
Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]
"""
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

(rptrPortAdminStatus,
 rptrPortGroupIndex,
 rptrPortIndex) = mibBuilder.importSymbols(
    "SNMP-REPEATER-MIB",
    "rptrPortAdminStatus",
    "rptrPortGroupIndex",
    "rptrPortIndex")

(NotificationGroup,
 ModuleCompliance) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "NotificationGroup",
    "ModuleCompliance")

(TimeTicks,
 IpAddress,
 internet,
 iso,
 Counter32,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 Bits,
 ObjectIdentity,
 Integer32,
 NotificationType,
 Gauge32,
 Counter64,
 NotificationType,
 MibIdentifier,
 ModuleIdentity,
 Unsigned32) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "TimeTicks",
    "IpAddress",
    "internet",
    "iso",
    "Counter32",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "Bits",
    "ObjectIdentity",
    "Integer32",
    "NotificationType",
    "Gauge32",
    "Counter64",
    "NotificationType",
    "MibIdentifier",
    "ModuleIdentity",
    "Unsigned32")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Fibronics_ObjectIdentity = ObjectIdentity
fibronics = _Fibronics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22)
)
_Trap_ObjectIdentity = ObjectIdentity
trap = _Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 3)
)
_Traprun_ObjectIdentity = ObjectIdentity
traprun = _Traprun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 3, 1)
)
_Traperm_ObjectIdentity = ObjectIdentity
traperm = _Traperm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 3, 2)
)
_Trapvar_ObjectIdentity = ObjectIdentity
trapvar = _Trapvar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 3, 3)
)
_Fm800_ObjectIdentity = ObjectIdentity
fm800 = _Fm800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 51)
)
_Fmsystem_ObjectIdentity = ObjectIdentity
fmsystem = _Fmsystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 51, 1)
)
_Fmsystemrun_ObjectIdentity = ObjectIdentity
fmsystemrun = _Fmsystemrun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 51, 1, 1)
)
_Fmsystemperm_ObjectIdentity = ObjectIdentity
fmsystemperm = _Fmsystemperm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 51, 1, 2)
)
_Fmslot_ObjectIdentity = ObjectIdentity
fmslot = _Fmslot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 51, 2)
)
_Fmlu_ObjectIdentity = ObjectIdentity
fmlu = _Fmlu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 51, 3)
)
_Fmdiag_ObjectIdentity = ObjectIdentity
fmdiag = _Fmdiag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 51, 5)
)
_Fmdebug_ObjectIdentity = ObjectIdentity
fmdebug = _Fmdebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 51, 6)
)
_Fmethrptr_ObjectIdentity = ObjectIdentity
fmethrptr = _Fmethrptr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 51, 11)
)
_Rptrinfo_ObjectIdentity = ObjectIdentity
rptrinfo = _Rptrinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 51, 11, 1)
)
_RptrRxDscrptrOverFlow_Type = Counter32
_RptrRxDscrptrOverFlow_Object = MibScalar
rptrRxDscrptrOverFlow = _RptrRxDscrptrOverFlow_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 11, 1, 1),
    _RptrRxDscrptrOverFlow_Type()
)
rptrRxDscrptrOverFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrRxDscrptrOverFlow.setStatus("mandatory")
if mibBuilder.loadTexts:
    rptrRxDscrptrOverFlow.setDescription("""\
This counter reflects the number of the missed received packets due to lack of
resourcees such as descriptors or memory buffers
""")
_RptrTxDscrptrOverFlow_Type = Counter32
_RptrTxDscrptrOverFlow_Object = MibScalar
rptrTxDscrptrOverFlow = _RptrTxDscrptrOverFlow_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 11, 1, 2),
    _RptrTxDscrptrOverFlow_Type()
)
rptrTxDscrptrOverFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrTxDscrptrOverFlow.setStatus("mandatory")
if mibBuilder.loadTexts:
    rptrTxDscrptrOverFlow.setDescription("""\
This counter is incremented evry time there is a transmit over flow
""")
_RptrMemoryErrors_Type = Counter32
_RptrMemoryErrors_Object = MibScalar
rptrMemoryErrors = _RptrMemoryErrors_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 11, 1, 3),
    _RptrMemoryErrors_Type()
)
rptrMemoryErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMemoryErrors.setStatus("mandatory")
if mibBuilder.loadTexts:
    rptrMemoryErrors.setDescription("""\
This counter is incremented evry time there is a memory error
""")
_RptrJabberCounter_Type = Counter32
_RptrJabberCounter_Object = MibScalar
rptrJabberCounter = _RptrJabberCounter_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 11, 1, 4),
    _RptrJabberCounter_Type()
)
rptrJabberCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrJabberCounter.setStatus("mandatory")
if mibBuilder.loadTexts:
    rptrJabberCounter.setDescription("""\
This counter is incremented evry time there is a jubber in one of the ports.
""")
_RptrNMSConnectionPort_Type = Integer32
_RptrNMSConnectionPort_Object = MibScalar
rptrNMSConnectionPort = _RptrNMSConnectionPort_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 11, 1, 5),
    _RptrNMSConnectionPort_Type()
)
rptrNMSConnectionPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrNMSConnectionPort.setStatus("mandatory")
if mibBuilder.loadTexts:
    rptrNMSConnectionPort.setDescription("""\
Returns the port number which the NMS is connected.
""")
_RptrEDBPort_Type = Integer32
_RptrEDBPort_Object = MibScalar
rptrEDBPort = _RptrEDBPort_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 11, 1, 6),
    _RptrEDBPort_Type()
)
rptrEDBPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrEDBPort.setStatus("mandatory")
if mibBuilder.loadTexts:
    rptrEDBPort.setDescription("""\
Returns the port number which the MultiHub (EDB) is connected to. if the
MultiHub is not connected to the card the value returned will be 99, if the
card is installed in a stand alone chassis then reading this object will return
99
""")
_Rptrgroup_ObjectIdentity = ObjectIdentity
rptrgroup = _Rptrgroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 51, 11, 2)
)
_RptrfmGroupTable_Object = MibTable
rptrfmGroupTable = _RptrfmGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 11, 2, 1)
)
if mibBuilder.loadTexts:
    rptrfmGroupTable.setStatus("mandatory")
_RptrfmGroupEntry_Object = MibTableRow
rptrfmGroupEntry = _RptrfmGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 11, 2, 1, 1)
)
rptrfmGroupEntry.setIndexNames(
    (0, "Hub-rptr-prvt", "rptrGroupIndex"),
)
if mibBuilder.loadTexts:
    rptrfmGroupEntry.setStatus("mandatory")
_RptrGroupIndex_Type = Integer32
_RptrGroupIndex_Object = MibTableColumn
rptrGroupIndex = _RptrGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 11, 2, 1, 1, 1),
    _RptrGroupIndex_Type()
)
rptrGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrGroupIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    rptrGroupIndex.setDescription("""\
Group Number
""")
_RptrGroupGlobalStatus_Type = OctetString
_RptrGroupGlobalStatus_Object = MibTableColumn
rptrGroupGlobalStatus = _RptrGroupGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 11, 2, 1, 1, 2),
    _RptrGroupGlobalStatus_Type()
)
rptrGroupGlobalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrGroupGlobalStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    rptrGroupGlobalStatus.setDescription("""\
8 bytes. 60 status bits of the card. For more information about the meaning of
the status, read the specific user manual of each card. The channel leds are
encoded into 2 bytes.
""")
_RptrGroupPrevStatus_Type = OctetString
_RptrGroupPrevStatus_Object = MibTableColumn
rptrGroupPrevStatus = _RptrGroupPrevStatus_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 11, 2, 1, 1, 3),
    _RptrGroupPrevStatus_Type()
)
rptrGroupPrevStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrGroupPrevStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    rptrGroupPrevStatus.setDescription("""\
8 bytes. Previous 60 status bits of the card. This object id is used mainly for
traps (see Card Trap)
""")


class _RptrGroupGlobalError_Type(Integer32):
    """Custom type rptrGroupGlobalError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fault-exist", 1),
          ("no-fault-exist", 2))
    )


_RptrGroupGlobalError_Type.__name__ = "Integer32"
_RptrGroupGlobalError_Object = MibTableColumn
rptrGroupGlobalError = _RptrGroupGlobalError_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 11, 2, 1, 1, 4),
    _RptrGroupGlobalError_Type()
)
rptrGroupGlobalError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrGroupGlobalError.setStatus("mandatory")
if mibBuilder.loadTexts:
    rptrGroupGlobalError.setDescription("""\
Group Global Fault status. If the value is one - there is a fault in the card.
""")


class _RptrGroupJabberError_Type(Integer32):
    """Custom type rptrGroupJabberError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fault-exist", 1),
          ("no-fault-exist", 2))
    )


_RptrGroupJabberError_Type.__name__ = "Integer32"
_RptrGroupJabberError_Object = MibTableColumn
rptrGroupJabberError = _RptrGroupJabberError_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 11, 2, 1, 1, 5),
    _RptrGroupJabberError_Type()
)
rptrGroupJabberError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrGroupJabberError.setStatus("mandatory")
if mibBuilder.loadTexts:
    rptrGroupJabberError.setDescription("""\
Jabber Fault status. If the value is one - there is a jabber event.
""")


class _RptrGroupCpuError_Type(Integer32):
    """Custom type rptrGroupCpuError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fault-exist", 1),
          ("no-fault-exist", 2))
    )


_RptrGroupCpuError_Type.__name__ = "Integer32"
_RptrGroupCpuError_Object = MibTableColumn
rptrGroupCpuError = _RptrGroupCpuError_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 11, 2, 1, 1, 6),
    _RptrGroupCpuError_Type()
)
rptrGroupCpuError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrGroupCpuError.setStatus("mandatory")
if mibBuilder.loadTexts:
    rptrGroupCpuError.setDescription("""\
CPU Fault status. If the value is one - there is a CPU fault in the card.
""")


class _RptrGroupSQE_Type(Integer32):
    """Custom type rptrGroupSQE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fault-exist", 1),
          ("no-fault-exist", 2))
    )


_RptrGroupSQE_Type.__name__ = "Integer32"
_RptrGroupSQE_Object = MibTableColumn
rptrGroupSQE = _RptrGroupSQE_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 11, 2, 1, 1, 7),
    _RptrGroupSQE_Type()
)
rptrGroupSQE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrGroupSQE.setStatus("mandatory")
if mibBuilder.loadTexts:
    rptrGroupSQE.setDescription("""\
Group SQE Fault status (for AUI module (339)). If the value is one - there is
an SQE indication to the card.
""")


class _RptrGroupRepeaterBlockError_Type(Integer32):
    """Custom type rptrGroupRepeaterBlockError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fault-exist", 1),
          ("no-fault-exist", 2))
    )


_RptrGroupRepeaterBlockError_Type.__name__ = "Integer32"
_RptrGroupRepeaterBlockError_Object = MibTableColumn
rptrGroupRepeaterBlockError = _RptrGroupRepeaterBlockError_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 11, 2, 1, 1, 8),
    _RptrGroupRepeaterBlockError_Type()
)
rptrGroupRepeaterBlockError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrGroupRepeaterBlockError.setStatus("mandatory")
if mibBuilder.loadTexts:
    rptrGroupRepeaterBlockError.setDescription("""\
Repeater Block Fault status. If the value is one - there is a fault in the
repeater block.
""")


class _RptrGroupAutoPartition_Type(Integer32):
    """Custom type rptrGroupAutoPartition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fault-exist", 1),
          ("no-fault-exist", 2))
    )


_RptrGroupAutoPartition_Type.__name__ = "Integer32"
_RptrGroupAutoPartition_Object = MibTableColumn
rptrGroupAutoPartition = _RptrGroupAutoPartition_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 11, 2, 1, 1, 9),
    _RptrGroupAutoPartition_Type()
)
rptrGroupAutoPartition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrGroupAutoPartition.setStatus("mandatory")
if mibBuilder.loadTexts:
    rptrGroupAutoPartition.setDescription("""\
Group Auto partition Fault status. If the value is one - at least one of the
ports is in auto-partition.
""")


class _RptrGroupDetachStatus_Type(Integer32):
    """Custom type rptrGroupDetachStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("detach-exist", 1),
          ("no-detach-exist", 2))
    )


_RptrGroupDetachStatus_Type.__name__ = "Integer32"
_RptrGroupDetachStatus_Object = MibTableColumn
rptrGroupDetachStatus = _RptrGroupDetachStatus_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 11, 2, 1, 1, 10),
    _RptrGroupDetachStatus_Type()
)
rptrGroupDetachStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrGroupDetachStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    rptrGroupDetachStatus.setDescription("""\
Global Detach status. If the value is one - at least one of the ports is
detached.
""")


class _RptrGroupGlobalCommandCode_Type(Integer32):
    """Custom type rptrGroupGlobalCommandCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("attach-all-ports", 1),
          ("detach-all-ports", 2))
    )


_RptrGroupGlobalCommandCode_Type.__name__ = "Integer32"
_RptrGroupGlobalCommandCode_Object = MibTableColumn
rptrGroupGlobalCommandCode = _RptrGroupGlobalCommandCode_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 11, 2, 1, 1, 11),
    _RptrGroupGlobalCommandCode_Type()
)
rptrGroupGlobalCommandCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrGroupGlobalCommandCode.setStatus("mandatory")
if mibBuilder.loadTexts:
    rptrGroupGlobalCommandCode.setDescription("""\
Enable the user to attach/detach all repeater ports. Note: in case off detach
command - all port will detach except the port on which the last NMS message
was received. when reading this object the value returned is always attach-all-
ports(1)
""")


class _RptrGroupTrapMask_Type(Integer32):
    """Custom type rptrGroupTrapMask based on Integer32"""
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
        *(("mask-all", 1),
          ("mask-fatal", 2),
          ("mask-info", 4),
          ("mask-warn", 3))
    )


_RptrGroupTrapMask_Type.__name__ = "Integer32"
_RptrGroupTrapMask_Object = MibTableColumn
rptrGroupTrapMask = _RptrGroupTrapMask_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 11, 2, 1, 1, 12),
    _RptrGroupTrapMask_Type()
)
rptrGroupTrapMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrGroupTrapMask.setStatus("mandatory")
if mibBuilder.loadTexts:
    rptrGroupTrapMask.setDescription("""\
When setting this variable to mask-info(4) then only all traps will be sent.
When setting this variable to mask-warn(3) then only traps with severity of
warn or fatal will be sent.When setting this variable to mask-fatal(2) then
only traps with severity of fatal will be sent. When setting this variable to
mask-all(1) then no traps will be sent.
""")


class _RptrGroupLinkSelectHead1_Type(Integer32):
    """Custom type rptrGroupLinkSelectHead1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("toggle-link-select", 1)
    )


_RptrGroupLinkSelectHead1_Type.__name__ = "Integer32"
_RptrGroupLinkSelectHead1_Object = MibTableColumn
rptrGroupLinkSelectHead1 = _RptrGroupLinkSelectHead1_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 11, 2, 1, 1, 13),
    _RptrGroupLinkSelectHead1_Type()
)
rptrGroupLinkSelectHead1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrGroupLinkSelectHead1.setStatus("mandatory")
if mibBuilder.loadTexts:
    rptrGroupLinkSelectHead1.setDescription("""\
Enable the user to switch between MAIN and SECOND link only in Head module in
the 303 type cards.
""")


class _RptrGroupBackupHead1State_Type(Integer32):
    """Custom type rptrGroupBackupHead1State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("normal", 3))
    )


_RptrGroupBackupHead1State_Type.__name__ = "Integer32"
_RptrGroupBackupHead1State_Object = MibTableColumn
rptrGroupBackupHead1State = _RptrGroupBackupHead1State_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 11, 2, 1, 1, 14),
    _RptrGroupBackupHead1State_Type()
)
rptrGroupBackupHead1State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrGroupBackupHead1State.setStatus("mandatory")
if mibBuilder.loadTexts:
    rptrGroupBackupHead1State.setDescription("""\
Enable the user to enable or disable the backup port for Head module only in
303 cards. when set to enabled(1) the active port will be the primary port,
when set to disabled(2) the active port will be the secondary port and when set
to normal(3) the active port will be set by the backup algorithm
""")


class _RptrGroupTailState_Type(Integer32):
    """Custom type rptrGroupTailState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RptrGroupTailState_Type.__name__ = "Integer32"
_RptrGroupTailState_Object = MibTableColumn
rptrGroupTailState = _RptrGroupTailState_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 11, 2, 1, 1, 15),
    _RptrGroupTailState_Type()
)
rptrGroupTailState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrGroupTailState.setStatus("deprecated")
if mibBuilder.loadTexts:
    rptrGroupTailState.setDescription("""\
Enable the user to enable or disable Tail in 303 card
""")
_RptrGroupMaxModuleNumber_Type = Integer32
_RptrGroupMaxModuleNumber_Object = MibTableColumn
rptrGroupMaxModuleNumber = _RptrGroupMaxModuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 11, 2, 1, 1, 16),
    _RptrGroupMaxModuleNumber_Type()
)
rptrGroupMaxModuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrGroupMaxModuleNumber.setStatus("mandatory")
if mibBuilder.loadTexts:
    rptrGroupMaxModuleNumber.setDescription("""\
Maximum Number of modules in a group.
""")
_Rptrgroupport_ObjectIdentity = ObjectIdentity
rptrgroupport = _Rptrgroupport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 51, 11, 3)
)
_RptrGroupPortTable_Object = MibTable
rptrGroupPortTable = _RptrGroupPortTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 11, 3, 1)
)
if mibBuilder.loadTexts:
    rptrGroupPortTable.setStatus("mandatory")
_RptrGroupPortEntry_Object = MibTableRow
rptrGroupPortEntry = _RptrGroupPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 11, 3, 1, 1)
)
rptrGroupPortEntry.setIndexNames(
    (0, "Hub-rptr-prvt", "rptrGroupPIndex"),
    (0, "Hub-rptr-prvt", "rptrGroupPortIndex"),
)
if mibBuilder.loadTexts:
    rptrGroupPortEntry.setStatus("mandatory")
_RptrGroupPIndex_Type = Integer32
_RptrGroupPIndex_Object = MibTableColumn
rptrGroupPIndex = _RptrGroupPIndex_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 11, 3, 1, 1, 1),
    _RptrGroupPIndex_Type()
)
rptrGroupPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrGroupPIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    rptrGroupPIndex.setDescription("""\
Group Number
""")
_RptrGroupPortIndex_Type = Integer32
_RptrGroupPortIndex_Object = MibTableColumn
rptrGroupPortIndex = _RptrGroupPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 11, 3, 1, 1, 2),
    _RptrGroupPortIndex_Type()
)
rptrGroupPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrGroupPortIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    rptrGroupPortIndex.setDescription("""\
Port Number
""")


class _RptrGroupPortLinkStatus_Type(Integer32):
    """Custom type rptrGroupPortLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("link-not-applicable", 3),
          ("link-not-ok", 2),
          ("link-ok", 1))
    )


_RptrGroupPortLinkStatus_Type.__name__ = "Integer32"
_RptrGroupPortLinkStatus_Object = MibTableColumn
rptrGroupPortLinkStatus = _RptrGroupPortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 11, 3, 1, 1, 3),
    _RptrGroupPortLinkStatus_Type()
)
rptrGroupPortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrGroupPortLinkStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    rptrGroupPortLinkStatus.setDescription("""\
When the value is 1, link status is O.K.
""")


class _RptrGroupPortRcvStatus_Type(Integer32):
    """Custom type rptrGroupPortRcvStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-receive", 2),
          ("receive", 1))
    )


_RptrGroupPortRcvStatus_Type.__name__ = "Integer32"
_RptrGroupPortRcvStatus_Object = MibTableColumn
rptrGroupPortRcvStatus = _RptrGroupPortRcvStatus_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 11, 3, 1, 1, 4),
    _RptrGroupPortRcvStatus_Type()
)
rptrGroupPortRcvStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrGroupPortRcvStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    rptrGroupPortRcvStatus.setDescription("""\
This object describes the receive status of the port, When a port is receiveing
data the object gets the value receive(1), when the port does not receive any
data the object gets the value no-receive(2)
""")
_RptrGroupPortLinkFaultCounter_Type = Counter32
_RptrGroupPortLinkFaultCounter_Object = MibTableColumn
rptrGroupPortLinkFaultCounter = _RptrGroupPortLinkFaultCounter_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 11, 3, 1, 1, 5),
    _RptrGroupPortLinkFaultCounter_Type()
)
rptrGroupPortLinkFaultCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrGroupPortLinkFaultCounter.setStatus("mandatory")
if mibBuilder.loadTexts:
    rptrGroupPortLinkFaultCounter.setDescription("""\
This counter is incremented evry time a link change is detected in the port. A
link change is encountered on the port whenever the link is disappearing or
apearing on the port
""")
_RptrGroupPortAutoPartitionCount_Type = Counter32
_RptrGroupPortAutoPartitionCount_Object = MibTableColumn
rptrGroupPortAutoPartitionCount = _RptrGroupPortAutoPartitionCount_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 11, 3, 1, 1, 6),
    _RptrGroupPortAutoPartitionCount_Type()
)
rptrGroupPortAutoPartitionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrGroupPortAutoPartitionCount.setStatus("mandatory")
if mibBuilder.loadTexts:
    rptrGroupPortAutoPartitionCount.setDescription("""\
This counter is incremented evry time there is a Auto Partition state in the
port.
""")


class _RptrGroupPortAutoPartitionType_Type(Integer32):
    """Custom type rptrGroupPortAutoPartitionType based on Integer32"""
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
        *(("collision-length-limit", 2),
          ("collision-limit", 1),
          ("cpu-forced-reconnection", 4),
          ("loopback-failure", 3),
          ("none", 5))
    )


_RptrGroupPortAutoPartitionType_Type.__name__ = "Integer32"
_RptrGroupPortAutoPartitionType_Object = MibTableColumn
rptrGroupPortAutoPartitionType = _RptrGroupPortAutoPartitionType_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 11, 3, 1, 1, 7),
    _RptrGroupPortAutoPartitionType_Type()
)
rptrGroupPortAutoPartitionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrGroupPortAutoPartitionType.setStatus("mandatory")
if mibBuilder.loadTexts:
    rptrGroupPortAutoPartitionType.setDescription("""\
Auto Partition type.
""")
_Rptrgroupmodule_ObjectIdentity = ObjectIdentity
rptrgroupmodule = _Rptrgroupmodule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 51, 11, 4)
)
_RptrGroupModuleTable_Object = MibTable
rptrGroupModuleTable = _RptrGroupModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 11, 4, 1)
)
if mibBuilder.loadTexts:
    rptrGroupModuleTable.setStatus("mandatory")
_RptrGroupModuleEntry_Object = MibTableRow
rptrGroupModuleEntry = _RptrGroupModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 11, 4, 1, 1)
)
rptrGroupModuleEntry.setIndexNames(
    (0, "Hub-rptr-prvt", "rptrGroupMIndex"),
    (0, "Hub-rptr-prvt", "rptrGroupModuleIndex"),
)
if mibBuilder.loadTexts:
    rptrGroupModuleEntry.setStatus("mandatory")
_RptrGroupMIndex_Type = Integer32
_RptrGroupMIndex_Object = MibTableColumn
rptrGroupMIndex = _RptrGroupMIndex_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 11, 4, 1, 1, 1),
    _RptrGroupMIndex_Type()
)
rptrGroupMIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrGroupMIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    rptrGroupMIndex.setDescription("""\
Group Number
""")
_RptrGroupModuleIndex_Type = Integer32
_RptrGroupModuleIndex_Object = MibTableColumn
rptrGroupModuleIndex = _RptrGroupModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 11, 4, 1, 1, 2),
    _RptrGroupModuleIndex_Type()
)
rptrGroupModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrGroupModuleIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    rptrGroupModuleIndex.setDescription("""\
Module Number
""")


class _RptrGroupModuleStructInfo_Type(Integer32):
    """Custom type rptrGroupModuleStructInfo based on Integer32"""
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
        *(("em892-330-blank", 1),
          ("em892-331-fo1", 2),
          ("em892-332-fo2", 3),
          ("em892-332b-fo2b", 6),
          ("em892-333-cx1", 4),
          ("em892-334-cx2", 5),
          ("em892-335-tp1", 7),
          ("em892-336-tp2", 9),
          ("em892-337-dte", 8),
          ("em892-339-aui", 10))
    )


_RptrGroupModuleStructInfo_Type.__name__ = "Integer32"
_RptrGroupModuleStructInfo_Object = MibTableColumn
rptrGroupModuleStructInfo = _RptrGroupModuleStructInfo_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 11, 4, 1, 1, 3),
    _RptrGroupModuleStructInfo_Type()
)
rptrGroupModuleStructInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrGroupModuleStructInfo.setStatus("mandatory")
if mibBuilder.loadTexts:
    rptrGroupModuleStructInfo.setDescription("""\
 List of modules numnbers: eM892.330 /* BLANK */ EM892.331 /* FO single port */
EM892.332 /* FO dual port */ EM892.333 /* COAX single port */ EM892.334 /* COAX
dual port */ EM892.332B /* FO dual port for Dual Homing */ EM892.335 /* 10BASET
single port */ EM892.337 /* DTE */ EM892.336 /* 10BASET dual port */ EM892.339
/* AUI */
""")


class _RptrGroupModuleBackupState_Type(Integer32):
    """Custom type rptrGroupModuleBackupState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("hardware", 3))
    )


_RptrGroupModuleBackupState_Type.__name__ = "Integer32"
_RptrGroupModuleBackupState_Object = MibTableColumn
rptrGroupModuleBackupState = _RptrGroupModuleBackupState_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 11, 4, 1, 1, 4),
    _RptrGroupModuleBackupState_Type()
)
rptrGroupModuleBackupState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrGroupModuleBackupState.setStatus("mandatory")
if mibBuilder.loadTexts:
    rptrGroupModuleBackupState.setDescription("""\
Enable the user to overide the backup switch (enable/disable). or let the state
be as the switch is (hardware) This object applies only to the 308 card.
setting this object will take effect only after the next reset or power up of
the card.
""")

# Managed Objects groups


# Notification objects

rptrGroupHead1BackupMainActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 22, 51, 0, 10)
)
rptrGroupHead1BackupMainActive.setObjects(
    ("Hub-rptr-prvt", "rptrGroupIndex")
)
if mibBuilder.loadTexts:
    rptrGroupHead1BackupMainActive.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    rptrGroupHead1BackupMainActive.setDescription("""\
Indicates that the MAIN link is active
""")

rptrGroupHead1BackupSecondActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 22, 51, 0, 11)
)
rptrGroupHead1BackupSecondActive.setObjects(
    ("Hub-rptr-prvt", "rptrGroupIndex")
)
if mibBuilder.loadTexts:
    rptrGroupHead1BackupSecondActive.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    rptrGroupHead1BackupSecondActive.setDescription("""\
Indicates that the SECOND link is active
""")

rptrGroupPortStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 22, 51, 11, 0, 1)
)
rptrGroupPortStatus.setObjects(
      *(("SNMP-REPEATER-MIB", "rptrPortGroupIndex"),
        ("SNMP-REPEATER-MIB", "rptrPortIndex"),
        ("SNMP-REPEATER-MIB", "rptrPortAdminStatus"))
)
if mibBuilder.loadTexts:
    rptrGroupPortStatus.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    rptrGroupPortStatus.setDescription("""\
Issued when the port changed its status
""")

rptrGroupJabberFaultStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 22, 51, 11, 0, 2)
)
rptrGroupJabberFaultStatus.setObjects(
      *(("Hub-rptr-prvt", "rptrGroupIndex"),
        ("Hub-rptr-prvt", "rptrGroupPortIndex"),
        ("Hub-rptr-prvt", "rptrGroupJabberError"))
)
if mibBuilder.loadTexts:
    rptrGroupJabberFaultStatus.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    rptrGroupJabberFaultStatus.setDescription("""\
Issued when the port enters the jabber lock state
""")

rptrGroupCPUFaultStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 22, 51, 11, 0, 3)
)
rptrGroupCPUFaultStatus.setObjects(
      *(("Hub-rptr-prvt", "rptrGroupIndex"),
        ("Hub-rptr-prvt", "rptrGroupCpuError"))
)
if mibBuilder.loadTexts:
    rptrGroupCPUFaultStatus.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    rptrGroupCPUFaultStatus.setDescription("""\
Issued when a CPU fault is detected
""")

rptrGroupSQEStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 22, 51, 11, 0, 4)
)
rptrGroupSQEStatus.setObjects(
      *(("Hub-rptr-prvt", "rptrGroupIndex"),
        ("Hub-rptr-prvt", "rptrGroupPortIndex"),
        ("Hub-rptr-prvt", "rptrGroupSQE"))
)
if mibBuilder.loadTexts:
    rptrGroupSQEStatus.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    rptrGroupSQEStatus.setDescription("""\
Issued when a SQE error is detected
""")

rptrGroupRepeaterBlockFaultStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 22, 51, 11, 0, 5)
)
rptrGroupRepeaterBlockFaultStatus.setObjects(
      *(("Hub-rptr-prvt", "rptrGroupIndex"),
        ("Hub-rptr-prvt", "rptrGroupRepeaterBlockError"))
)
if mibBuilder.loadTexts:
    rptrGroupRepeaterBlockFaultStatus.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    rptrGroupRepeaterBlockFaultStatus.setDescription("""\
Issued when a repeater block error is detected
""")

rptrGroupPortAutoPartitionStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 22, 51, 11, 0, 6)
)
rptrGroupPortAutoPartitionStatus.setObjects(
      *(("Hub-rptr-prvt", "rptrGroupPIndex"),
        ("Hub-rptr-prvt", "rptrGroupPortIndex"),
        ("Hub-rptr-prvt", "rptrGroupPortAutoPartitionType"))
)
if mibBuilder.loadTexts:
    rptrGroupPortAutoPartitionStatus.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    rptrGroupPortAutoPartitionStatus.setDescription("""\
Issued when the port is auto partitioned
""")

rptrGroupTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 22, 51, 11, 0, 7)
)
rptrGroupTrap.setObjects(
      *(("Hub-rptr-prvt", "rptrGroupIndex"),
        ("Hub-rptr-prvt", "rptrGroupGlobalStatus"),
        ("Hub-rptr-prvt", "rptrGroupPrevStatus"))
)
if mibBuilder.loadTexts:
    rptrGroupTrap.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    rptrGroupTrap.setDescription("""\
Generated when a significant status has changed in a group. By xoring the 2
statuses, the NMS can identify the cause of the trap.
""")

rptrGroupPortLinkStatus2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 22, 51, 11, 0, 8)
)
rptrGroupPortLinkStatus2.setObjects(
      *(("SNMP-REPEATER-MIB", "rptrPortGroupIndex"),
        ("SNMP-REPEATER-MIB", "rptrPortIndex"),
        ("Hub-rptr-prvt", "rptrGroupPortLinkStatus"))
)
if mibBuilder.loadTexts:
    rptrGroupPortLinkStatus2.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    rptrGroupPortLinkStatus2.setDescription("""\
Issued when the link status of the port changed its status
""")

rptrGroupDetachNmsPort = NotificationType(
    (1, 3, 6, 1, 4, 1, 22, 51, 11, 0, 9)
)
rptrGroupDetachNmsPort.setObjects(
    ("Hub-rptr-prvt", "rptrNMSConnectionPort")
)
if mibBuilder.loadTexts:
    rptrGroupDetachNmsPort.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    rptrGroupDetachNmsPort.setDescription("""\
Issued when the port connected to the NMS Is not dettached by a detach command
received from the NMS
""")

rptrGroupDetachEdbPort = NotificationType(
    (1, 3, 6, 1, 4, 1, 22, 51, 11, 0, 12)
)
rptrGroupDetachEdbPort.setObjects(
    ("Hub-rptr-prvt", "rptrEDBPort")
)
if mibBuilder.loadTexts:
    rptrGroupDetachEdbPort.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    rptrGroupDetachEdbPort.setDescription("""\
Issued when the port connected to the EDB Is not dettached by a detach command
received from the NMS
""")


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Hub-rptr-prvt",
    **{"private": private,
       "enterprises": enterprises,
       "fibronics": fibronics,
       "trap": trap,
       "traprun": traprun,
       "traperm": traperm,
       "trapvar": trapvar,
       "fm800": fm800,
       "rptrGroupHead1BackupMainActive": rptrGroupHead1BackupMainActive,
       "rptrGroupHead1BackupSecondActive": rptrGroupHead1BackupSecondActive,
       "fmsystem": fmsystem,
       "fmsystemrun": fmsystemrun,
       "fmsystemperm": fmsystemperm,
       "fmslot": fmslot,
       "fmlu": fmlu,
       "fmdiag": fmdiag,
       "fmdebug": fmdebug,
       "fmethrptr": fmethrptr,
       "rptrGroupPortStatus": rptrGroupPortStatus,
       "rptrGroupJabberFaultStatus": rptrGroupJabberFaultStatus,
       "rptrGroupCPUFaultStatus": rptrGroupCPUFaultStatus,
       "rptrGroupSQEStatus": rptrGroupSQEStatus,
       "rptrGroupRepeaterBlockFaultStatus": rptrGroupRepeaterBlockFaultStatus,
       "rptrGroupPortAutoPartitionStatus": rptrGroupPortAutoPartitionStatus,
       "rptrGroupTrap": rptrGroupTrap,
       "rptrGroupPortLinkStatus2": rptrGroupPortLinkStatus2,
       "rptrGroupDetachNmsPort": rptrGroupDetachNmsPort,
       "rptrGroupDetachEdbPort": rptrGroupDetachEdbPort,
       "rptrinfo": rptrinfo,
       "rptrRxDscrptrOverFlow": rptrRxDscrptrOverFlow,
       "rptrTxDscrptrOverFlow": rptrTxDscrptrOverFlow,
       "rptrMemoryErrors": rptrMemoryErrors,
       "rptrJabberCounter": rptrJabberCounter,
       "rptrNMSConnectionPort": rptrNMSConnectionPort,
       "rptrEDBPort": rptrEDBPort,
       "rptrgroup": rptrgroup,
       "rptrfmGroupTable": rptrfmGroupTable,
       "rptrfmGroupEntry": rptrfmGroupEntry,
       "rptrGroupIndex": rptrGroupIndex,
       "rptrGroupGlobalStatus": rptrGroupGlobalStatus,
       "rptrGroupPrevStatus": rptrGroupPrevStatus,
       "rptrGroupGlobalError": rptrGroupGlobalError,
       "rptrGroupJabberError": rptrGroupJabberError,
       "rptrGroupCpuError": rptrGroupCpuError,
       "rptrGroupSQE": rptrGroupSQE,
       "rptrGroupRepeaterBlockError": rptrGroupRepeaterBlockError,
       "rptrGroupAutoPartition": rptrGroupAutoPartition,
       "rptrGroupDetachStatus": rptrGroupDetachStatus,
       "rptrGroupGlobalCommandCode": rptrGroupGlobalCommandCode,
       "rptrGroupTrapMask": rptrGroupTrapMask,
       "rptrGroupLinkSelectHead1": rptrGroupLinkSelectHead1,
       "rptrGroupBackupHead1State": rptrGroupBackupHead1State,
       "rptrGroupTailState": rptrGroupTailState,
       "rptrGroupMaxModuleNumber": rptrGroupMaxModuleNumber,
       "rptrgroupport": rptrgroupport,
       "rptrGroupPortTable": rptrGroupPortTable,
       "rptrGroupPortEntry": rptrGroupPortEntry,
       "rptrGroupPIndex": rptrGroupPIndex,
       "rptrGroupPortIndex": rptrGroupPortIndex,
       "rptrGroupPortLinkStatus": rptrGroupPortLinkStatus,
       "rptrGroupPortRcvStatus": rptrGroupPortRcvStatus,
       "rptrGroupPortLinkFaultCounter": rptrGroupPortLinkFaultCounter,
       "rptrGroupPortAutoPartitionCount": rptrGroupPortAutoPartitionCount,
       "rptrGroupPortAutoPartitionType": rptrGroupPortAutoPartitionType,
       "rptrgroupmodule": rptrgroupmodule,
       "rptrGroupModuleTable": rptrGroupModuleTable,
       "rptrGroupModuleEntry": rptrGroupModuleEntry,
       "rptrGroupMIndex": rptrGroupMIndex,
       "rptrGroupModuleIndex": rptrGroupModuleIndex,
       "rptrGroupModuleStructInfo": rptrGroupModuleStructInfo,
       "rptrGroupModuleBackupState": rptrGroupModuleBackupState}
)
