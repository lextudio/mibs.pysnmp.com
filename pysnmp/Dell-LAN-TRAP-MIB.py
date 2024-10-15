# SNMP MIB module (Dell-LAN-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Dell-LAN-TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:34:36 2024
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

(dellLan,
 dellLanCommon) = mibBuilder.importSymbols(
    "Dell-Vendor-MIB",
    "dellLan",
    "dellLanCommon")

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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

dellAlarmGroup = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DellTrapInfo_Type = DisplayString
_DellTrapInfo_Object = MibScalar
dellTrapInfo = _DellTrapInfo_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 1, 1),
    _DellTrapInfo_Type()
)
dellTrapInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellTrapInfo.setStatus("current")


class _DellTrapSeverity_Type(Integer32):
    """Custom type dellTrapSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("clear", 0),
          ("critical", 4),
          ("info", 1),
          ("major", 3),
          ("minor", 2))
    )


_DellTrapSeverity_Type.__name__ = "Integer32"
_DellTrapSeverity_Object = MibScalar
dellTrapSeverity = _DellTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 1, 2),
    _DellTrapSeverity_Type()
)
dellTrapSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellTrapSeverity.setStatus("current")
_DellTrapSource_Type = DisplayString
_DellTrapSource_Object = MibScalar
dellTrapSource = _DellTrapSource_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 1, 3),
    _DellTrapSource_Type()
)
dellTrapSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellTrapSource.setStatus("current")
_DellTrapSeqNum_Type = Unsigned32
_DellTrapSeqNum_Object = MibScalar
dellTrapSeqNum = _DellTrapSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 1, 4),
    _DellTrapSeqNum_Type()
)
dellTrapSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellTrapSeqNum.setStatus("current")
_DellTrapTimeStamp_Type = DateAndTime
_DellTrapTimeStamp_Object = MibScalar
dellTrapTimeStamp = _DellTrapTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 1, 5),
    _DellTrapTimeStamp_Type()
)
dellTrapTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellTrapTimeStamp.setStatus("current")

# Managed Objects groups


# Notification objects

hwResourceOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 500)
)
hwResourceOverflow.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    hwResourceOverflow.setStatus(
        "current"
    )

swResourceOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 510)
)
swResourceOverflow.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    swResourceOverflow.setStatus(
        "current"
    )

configChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 520)
)
configChanged.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    configChanged.setStatus(
        "current"
    )

resetRequired = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 530)
)
resetRequired.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    resetRequired.setStatus(
        "current"
    )

endTftp = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 540)
)
endTftp.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    endTftp.setStatus(
        "current"
    )

abortTftp = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 550)
)
abortTftp.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    abortTftp.setStatus(
        "current"
    )

startTftp = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 560)
)
startTftp.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    startTftp.setStatus(
        "current"
    )

linkFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 570)
)
linkFailure.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    linkFailure.setStatus(
        "current"
    )

linkFailureSwitchBackUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 580)
)
linkFailureSwitchBackUp.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    linkFailureSwitchBackUp.setStatus(
        "current"
    )

mainLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 590)
)
mainLinkUp.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    mainLinkUp.setStatus(
        "current"
    )

errorsDuringInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 600)
)
errorsDuringInit.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    errorsDuringInit.setStatus(
        "current"
    )

vlanDynPortAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 610)
)
vlanDynPortAdded.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    vlanDynPortAdded.setStatus(
        "current"
    )

vlanDynPortRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 620)
)
vlanDynPortRemoved.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    vlanDynPortRemoved.setStatus(
        "current"
    )

ipZhrReqStaticConnNotAccepted = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 630)
)
ipZhrReqStaticConnNotAccepted.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    ipZhrReqStaticConnNotAccepted.setStatus(
        "current"
    )

ipZhrVirtualIpAsSource = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 640)
)
ipZhrVirtualIpAsSource.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    ipZhrVirtualIpAsSource.setStatus(
        "current"
    )

ipZhrNotAllocVirtualIp = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 650)
)
ipZhrNotAllocVirtualIp.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    ipZhrNotAllocVirtualIp.setStatus(
        "current"
    )

stackMasterFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 660)
)
stackMasterFailed.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    stackMasterFailed.setStatus(
        "current"
    )

stackNewMasterElected = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 670)
)
stackNewMasterElected.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    stackNewMasterElected.setStatus(
        "current"
    )

stackMemberUnitFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 680)
)
stackMemberUnitFailed.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    stackMemberUnitFailed.setStatus(
        "current"
    )

stackNewMemberUnitAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 690)
)
stackNewMemberUnitAdded.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    stackNewMemberUnitAdded.setStatus(
        "current"
    )

stackMemberUnitRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 700)
)
stackMemberUnitRemoved.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    stackMemberUnitRemoved.setStatus(
        "current"
    )

stackSplitMasterReport = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 710)
)
stackSplitMasterReport.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    stackSplitMasterReport.setStatus(
        "current"
    )

stackSplitNewMasterReport = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 720)
)
stackSplitNewMasterReport.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    stackSplitNewMasterReport.setStatus(
        "current"
    )

stackRejoined = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 730)
)
stackRejoined.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    stackRejoined.setStatus(
        "current"
    )

stackLinkFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 740)
)
stackLinkFailed.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    stackLinkFailed.setStatus(
        "current"
    )

dhcpAllocationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 750)
)
dhcpAllocationFailure.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    dhcpAllocationFailure.setStatus(
        "current"
    )

dot1dStpPortStateForwarding = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 760)
)
dot1dStpPortStateForwarding.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    dot1dStpPortStateForwarding.setStatus(
        "current"
    )

dot1dStpPortStateNotForwarding = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 770)
)
dot1dStpPortStateNotForwarding.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    dot1dStpPortStateNotForwarding.setStatus(
        "current"
    )

policyDropPacketTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 780)
)
policyDropPacketTrap.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    policyDropPacketTrap.setStatus(
        "current"
    )

policyForwardPacketTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 790)
)
policyForwardPacketTrap.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    policyForwardPacketTrap.setStatus(
        "current"
    )

igmpV1MsgReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 800)
)
igmpV1MsgReceived.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    igmpV1MsgReceived.setStatus(
        "current"
    )

vrrpEntriesDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 810)
)
vrrpEntriesDeleted.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    vrrpEntriesDeleted.setStatus(
        "current"
    )

trunkPortAddedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 820)
)
trunkPortAddedTrap.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    trunkPortAddedTrap.setStatus(
        "current"
    )

trunkPortRemovedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 830)
)
trunkPortRemovedTrap.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    trunkPortRemovedTrap.setStatus(
        "current"
    )

lockPortTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 840)
)
lockPortTrap.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    lockPortTrap.setStatus(
        "current"
    )

vlanDynVlanAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 850)
)
vlanDynVlanAdded.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    vlanDynVlanAdded.setStatus(
        "current"
    )

vlanDynVlanRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 860)
)
vlanDynVlanRemoved.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    vlanDynVlanRemoved.setStatus(
        "current"
    )

vlanDynamicToStatic = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 870)
)
vlanDynamicToStatic.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    vlanDynamicToStatic.setStatus(
        "current"
    )

vlanStaticToDynamic = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 880)
)
vlanStaticToDynamic.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    vlanStaticToDynamic.setStatus(
        "current"
    )

envMonFanStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 890)
)
envMonFanStateChange.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    envMonFanStateChange.setStatus(
        "current"
    )

envMonPowerSupplyStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 900)
)
envMonPowerSupplyStateChange.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    envMonPowerSupplyStateChange.setStatus(
        "current"
    )

envMonTemperatureRisingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 910)
)
envMonTemperatureRisingAlarm.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    envMonTemperatureRisingAlarm.setStatus(
        "current"
    )

copyFinished = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 920)
)
copyFinished.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    copyFinished.setStatus(
        "current"
    )

copyFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 930)
)
copyFailed.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    copyFailed.setStatus(
        "current"
    )

dot1xPortStatusAuthorizedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 940)
)
dot1xPortStatusAuthorizedTrap.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    dot1xPortStatusAuthorizedTrap.setStatus(
        "current"
    )

dot1xPortStatusUnauthorizedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 950)
)
dot1xPortStatusUnauthorizedTrap.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    dot1xPortStatusUnauthorizedTrap.setStatus(
        "current"
    )

broadcastStormDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 960)
)
broadcastStormDetected.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    broadcastStormDetected.setStatus(
        "current"
    )

stpElectedAsRoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 970)
)
stpElectedAsRoot.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    stpElectedAsRoot.setStatus(
        "current"
    )

stpNewRootElected = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 980)
)
stpNewRootElected.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    stpNewRootElected.setStatus(
        "current"
    )

igmpElectedAsQuerier = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 990)
)
igmpElectedAsQuerier.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    igmpElectedAsQuerier.setStatus(
        "current"
    )

invalidUserLoginAttempted = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 1000)
)
invalidUserLoginAttempted.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    invalidUserLoginAttempted.setStatus(
        "current"
    )

managementACLViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 1010)
)
managementACLViolation.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    managementACLViolation.setStatus(
        "current"
    )

sfpInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 1020)
)
sfpInserted.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    sfpInserted.setStatus(
        "current"
    )

sfpRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 1030)
)
sfpRemoved.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    sfpRemoved.setStatus(
        "current"
    )

xfpInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 1040)
)
xfpInserted.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    xfpInserted.setStatus(
        "current"
    )

xfpRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 1050)
)
xfpRemoved.setObjects(
      *(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSource"),
        ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"),
        ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
)
if mibBuilder.loadTexts:
    xfpRemoved.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Dell-LAN-TRAP-MIB",
    **{"hwResourceOverflow": hwResourceOverflow,
       "swResourceOverflow": swResourceOverflow,
       "configChanged": configChanged,
       "resetRequired": resetRequired,
       "endTftp": endTftp,
       "abortTftp": abortTftp,
       "startTftp": startTftp,
       "linkFailure": linkFailure,
       "linkFailureSwitchBackUp": linkFailureSwitchBackUp,
       "mainLinkUp": mainLinkUp,
       "errorsDuringInit": errorsDuringInit,
       "vlanDynPortAdded": vlanDynPortAdded,
       "vlanDynPortRemoved": vlanDynPortRemoved,
       "ipZhrReqStaticConnNotAccepted": ipZhrReqStaticConnNotAccepted,
       "ipZhrVirtualIpAsSource": ipZhrVirtualIpAsSource,
       "ipZhrNotAllocVirtualIp": ipZhrNotAllocVirtualIp,
       "stackMasterFailed": stackMasterFailed,
       "stackNewMasterElected": stackNewMasterElected,
       "stackMemberUnitFailed": stackMemberUnitFailed,
       "stackNewMemberUnitAdded": stackNewMemberUnitAdded,
       "stackMemberUnitRemoved": stackMemberUnitRemoved,
       "stackSplitMasterReport": stackSplitMasterReport,
       "stackSplitNewMasterReport": stackSplitNewMasterReport,
       "stackRejoined": stackRejoined,
       "stackLinkFailed": stackLinkFailed,
       "dhcpAllocationFailure": dhcpAllocationFailure,
       "dot1dStpPortStateForwarding": dot1dStpPortStateForwarding,
       "dot1dStpPortStateNotForwarding": dot1dStpPortStateNotForwarding,
       "policyDropPacketTrap": policyDropPacketTrap,
       "policyForwardPacketTrap": policyForwardPacketTrap,
       "igmpV1MsgReceived": igmpV1MsgReceived,
       "vrrpEntriesDeleted": vrrpEntriesDeleted,
       "trunkPortAddedTrap": trunkPortAddedTrap,
       "trunkPortRemovedTrap": trunkPortRemovedTrap,
       "lockPortTrap": lockPortTrap,
       "vlanDynVlanAdded": vlanDynVlanAdded,
       "vlanDynVlanRemoved": vlanDynVlanRemoved,
       "vlanDynamicToStatic": vlanDynamicToStatic,
       "vlanStaticToDynamic": vlanStaticToDynamic,
       "envMonFanStateChange": envMonFanStateChange,
       "envMonPowerSupplyStateChange": envMonPowerSupplyStateChange,
       "envMonTemperatureRisingAlarm": envMonTemperatureRisingAlarm,
       "copyFinished": copyFinished,
       "copyFailed": copyFailed,
       "dot1xPortStatusAuthorizedTrap": dot1xPortStatusAuthorizedTrap,
       "dot1xPortStatusUnauthorizedTrap": dot1xPortStatusUnauthorizedTrap,
       "broadcastStormDetected": broadcastStormDetected,
       "stpElectedAsRoot": stpElectedAsRoot,
       "stpNewRootElected": stpNewRootElected,
       "igmpElectedAsQuerier": igmpElectedAsQuerier,
       "invalidUserLoginAttempted": invalidUserLoginAttempted,
       "managementACLViolation": managementACLViolation,
       "sfpInserted": sfpInserted,
       "sfpRemoved": sfpRemoved,
       "xfpInserted": xfpInserted,
       "xfpRemoved": xfpRemoved,
       "dellAlarmGroup": dellAlarmGroup,
       "dellTrapInfo": dellTrapInfo,
       "dellTrapSeverity": dellTrapSeverity,
       "dellTrapSource": dellTrapSource,
       "dellTrapSeqNum": dellTrapSeqNum,
       "dellTrapTimeStamp": dellTrapTimeStamp}
)
