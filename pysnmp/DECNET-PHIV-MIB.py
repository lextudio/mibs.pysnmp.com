# SNMP MIB module (DECNET-PHIV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DECNET-PHIV-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:23:43 2024
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


# MODULE-IDENTITY


# Types definitions



class PhivAddr(OctetString):
    """Custom type PhivAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )





class PhivCounter(Integer32):
    """Custom type PhivCounter based on Integer32"""




class InterfaceIndex(Integer32):
    """Custom type InterfaceIndex based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Phiv_ObjectIdentity = ObjectIdentity
phiv = _Phiv_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 18)
)
_PhivSystem_ObjectIdentity = ObjectIdentity
phivSystem = _PhivSystem_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 18, 1)
)


class _PhivSystemState_Type(Integer32):
    """Custom type phivSystemState based on Integer32"""
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
        *(("off", 2),
          ("on", 1),
          ("restricted", 4),
          ("shut", 3))
    )


_PhivSystemState_Type.__name__ = "Integer32"
_PhivSystemState_Object = MibScalar
phivSystemState = _PhivSystemState_Object(
    (1, 3, 6, 1, 2, 1, 18, 1, 1),
    _PhivSystemState_Type()
)
phivSystemState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivSystemState.setStatus("mandatory")


class _PhivExecIdent_Type(DisplayString):
    """Custom type phivExecIdent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PhivExecIdent_Type.__name__ = "DisplayString"
_PhivExecIdent_Object = MibScalar
phivExecIdent = _PhivExecIdent_Object(
    (1, 3, 6, 1, 2, 1, 18, 1, 2),
    _PhivExecIdent_Type()
)
phivExecIdent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivExecIdent.setStatus("mandatory")
_PhivManagement_ObjectIdentity = ObjectIdentity
phivManagement = _PhivManagement_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 18, 2)
)


class _PhivMgmtMgmtVers_Type(DisplayString):
    """Custom type phivMgmtMgmtVers based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PhivMgmtMgmtVers_Type.__name__ = "DisplayString"
_PhivMgmtMgmtVers_Object = MibScalar
phivMgmtMgmtVers = _PhivMgmtMgmtVers_Object(
    (1, 3, 6, 1, 2, 1, 18, 2, 1),
    _PhivMgmtMgmtVers_Type()
)
phivMgmtMgmtVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivMgmtMgmtVers.setStatus("mandatory")
_Session_ObjectIdentity = ObjectIdentity
session = _Session_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 18, 3)
)


class _PhivSessionSystemName_Type(DisplayString):
    """Custom type phivSessionSystemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_PhivSessionSystemName_Type.__name__ = "DisplayString"
_PhivSessionSystemName_Object = MibScalar
phivSessionSystemName = _PhivSessionSystemName_Object(
    (1, 3, 6, 1, 2, 1, 18, 3, 1),
    _PhivSessionSystemName_Type()
)
phivSessionSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivSessionSystemName.setStatus("mandatory")


class _PhivSessionInTimer_Type(Integer32):
    """Custom type phivSessionInTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PhivSessionInTimer_Type.__name__ = "Integer32"
_PhivSessionInTimer_Object = MibScalar
phivSessionInTimer = _PhivSessionInTimer_Object(
    (1, 3, 6, 1, 2, 1, 18, 3, 2),
    _PhivSessionInTimer_Type()
)
phivSessionInTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivSessionInTimer.setStatus("mandatory")


class _PhivSessionOutTimer_Type(Integer32):
    """Custom type phivSessionOutTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PhivSessionOutTimer_Type.__name__ = "Integer32"
_PhivSessionOutTimer_Object = MibScalar
phivSessionOutTimer = _PhivSessionOutTimer_Object(
    (1, 3, 6, 1, 2, 1, 18, 3, 3),
    _PhivSessionOutTimer_Type()
)
phivSessionOutTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivSessionOutTimer.setStatus("mandatory")
_End_ObjectIdentity = ObjectIdentity
end = _End_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 18, 4)
)
_PhivEndRemoteTable_Object = MibTable
phivEndRemoteTable = _PhivEndRemoteTable_Object(
    (1, 3, 6, 1, 2, 1, 18, 4, 1)
)
if mibBuilder.loadTexts:
    phivEndRemoteTable.setStatus("mandatory")
_PhivEndRemoteEntry_Object = MibTableRow
phivEndRemoteEntry = _PhivEndRemoteEntry_Object(
    (1, 3, 6, 1, 2, 1, 18, 4, 1, 1)
)
phivEndRemoteEntry.setIndexNames(
    (0, "DECNET-PHIV-MIB", "phivEndRemoteHostNodeID"),
)
if mibBuilder.loadTexts:
    phivEndRemoteEntry.setStatus("mandatory")
_PhivEndRemoteHostNodeID_Type = PhivAddr
_PhivEndRemoteHostNodeID_Object = MibTableColumn
phivEndRemoteHostNodeID = _PhivEndRemoteHostNodeID_Object(
    (1, 3, 6, 1, 2, 1, 18, 4, 1, 1, 1),
    _PhivEndRemoteHostNodeID_Type()
)
phivEndRemoteHostNodeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivEndRemoteHostNodeID.setStatus("mandatory")


class _PhivEndRemoteState_Type(Integer32):
    """Custom type phivEndRemoteState based on Integer32"""
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
        *(("off", 2),
          ("on", 1),
          ("restricted", 4),
          ("shut", 3))
    )


_PhivEndRemoteState_Type.__name__ = "Integer32"
_PhivEndRemoteState_Object = MibTableColumn
phivEndRemoteState = _PhivEndRemoteState_Object(
    (1, 3, 6, 1, 2, 1, 18, 4, 1, 1, 2),
    _PhivEndRemoteState_Type()
)
phivEndRemoteState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivEndRemoteState.setStatus("mandatory")


class _PhivEndCircuitIndex_Type(Integer32):
    """Custom type phivEndCircuitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PhivEndCircuitIndex_Type.__name__ = "Integer32"
_PhivEndCircuitIndex_Object = MibTableColumn
phivEndCircuitIndex = _PhivEndCircuitIndex_Object(
    (1, 3, 6, 1, 2, 1, 18, 4, 1, 1, 3),
    _PhivEndCircuitIndex_Type()
)
phivEndCircuitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivEndCircuitIndex.setStatus("mandatory")


class _PhivEndActiveLinks_Type(Integer32):
    """Custom type phivEndActiveLinks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PhivEndActiveLinks_Type.__name__ = "Integer32"
_PhivEndActiveLinks_Object = MibTableColumn
phivEndActiveLinks = _PhivEndActiveLinks_Object(
    (1, 3, 6, 1, 2, 1, 18, 4, 1, 1, 4),
    _PhivEndActiveLinks_Type()
)
phivEndActiveLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivEndActiveLinks.setStatus("mandatory")


class _PhivEndDelay_Type(Integer32):
    """Custom type phivEndDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PhivEndDelay_Type.__name__ = "Integer32"
_PhivEndDelay_Object = MibTableColumn
phivEndDelay = _PhivEndDelay_Object(
    (1, 3, 6, 1, 2, 1, 18, 4, 1, 1, 5),
    _PhivEndDelay_Type()
)
phivEndDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivEndDelay.setStatus("mandatory")
_PhivEndCountTable_Object = MibTable
phivEndCountTable = _PhivEndCountTable_Object(
    (1, 3, 6, 1, 2, 1, 18, 4, 2)
)
if mibBuilder.loadTexts:
    phivEndCountTable.setStatus("mandatory")
_PhivEndCountEntry_Object = MibTableRow
phivEndCountEntry = _PhivEndCountEntry_Object(
    (1, 3, 6, 1, 2, 1, 18, 4, 2, 1)
)
phivEndCountEntry.setIndexNames(
    (0, "DECNET-PHIV-MIB", "phivEndCountHostNodeID"),
)
if mibBuilder.loadTexts:
    phivEndCountEntry.setStatus("mandatory")
_PhivEndCountHostNodeID_Type = PhivAddr
_PhivEndCountHostNodeID_Object = MibTableColumn
phivEndCountHostNodeID = _PhivEndCountHostNodeID_Object(
    (1, 3, 6, 1, 2, 1, 18, 4, 2, 1, 1),
    _PhivEndCountHostNodeID_Type()
)
phivEndCountHostNodeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivEndCountHostNodeID.setStatus("mandatory")


class _PhivEndCountSecsLastZeroed_Type(PhivCounter):
    """Custom type phivEndCountSecsLastZeroed based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PhivEndCountSecsLastZeroed_Type.__name__ = "PhivCounter"
_PhivEndCountSecsLastZeroed_Object = MibTableColumn
phivEndCountSecsLastZeroed = _PhivEndCountSecsLastZeroed_Object(
    (1, 3, 6, 1, 2, 1, 18, 4, 2, 1, 2),
    _PhivEndCountSecsLastZeroed_Type()
)
phivEndCountSecsLastZeroed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivEndCountSecsLastZeroed.setStatus("mandatory")


class _PhivEndCountUsrBytesRec_Type(PhivCounter):
    """Custom type phivEndCountUsrBytesRec based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PhivEndCountUsrBytesRec_Type.__name__ = "PhivCounter"
_PhivEndCountUsrBytesRec_Object = MibTableColumn
phivEndCountUsrBytesRec = _PhivEndCountUsrBytesRec_Object(
    (1, 3, 6, 1, 2, 1, 18, 4, 2, 1, 3),
    _PhivEndCountUsrBytesRec_Type()
)
phivEndCountUsrBytesRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivEndCountUsrBytesRec.setStatus("mandatory")


class _PhivEndCountUsrBytesSent_Type(PhivCounter):
    """Custom type phivEndCountUsrBytesSent based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PhivEndCountUsrBytesSent_Type.__name__ = "PhivCounter"
_PhivEndCountUsrBytesSent_Object = MibTableColumn
phivEndCountUsrBytesSent = _PhivEndCountUsrBytesSent_Object(
    (1, 3, 6, 1, 2, 1, 18, 4, 2, 1, 4),
    _PhivEndCountUsrBytesSent_Type()
)
phivEndCountUsrBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivEndCountUsrBytesSent.setStatus("mandatory")


class _PhivEndUCountUsrMessRec_Type(PhivCounter):
    """Custom type phivEndUCountUsrMessRec based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PhivEndUCountUsrMessRec_Type.__name__ = "PhivCounter"
_PhivEndUCountUsrMessRec_Object = MibTableColumn
phivEndUCountUsrMessRec = _PhivEndUCountUsrMessRec_Object(
    (1, 3, 6, 1, 2, 1, 18, 4, 2, 1, 5),
    _PhivEndUCountUsrMessRec_Type()
)
phivEndUCountUsrMessRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivEndUCountUsrMessRec.setStatus("mandatory")


class _PhivEndCountUsrMessSent_Type(PhivCounter):
    """Custom type phivEndCountUsrMessSent based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PhivEndCountUsrMessSent_Type.__name__ = "PhivCounter"
_PhivEndCountUsrMessSent_Object = MibTableColumn
phivEndCountUsrMessSent = _PhivEndCountUsrMessSent_Object(
    (1, 3, 6, 1, 2, 1, 18, 4, 2, 1, 6),
    _PhivEndCountUsrMessSent_Type()
)
phivEndCountUsrMessSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivEndCountUsrMessSent.setStatus("mandatory")


class _PhivEndCountTotalBytesRec_Type(PhivCounter):
    """Custom type phivEndCountTotalBytesRec based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PhivEndCountTotalBytesRec_Type.__name__ = "PhivCounter"
_PhivEndCountTotalBytesRec_Object = MibTableColumn
phivEndCountTotalBytesRec = _PhivEndCountTotalBytesRec_Object(
    (1, 3, 6, 1, 2, 1, 18, 4, 2, 1, 7),
    _PhivEndCountTotalBytesRec_Type()
)
phivEndCountTotalBytesRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivEndCountTotalBytesRec.setStatus("mandatory")


class _PhivEndCountTotalBytesSent_Type(PhivCounter):
    """Custom type phivEndCountTotalBytesSent based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PhivEndCountTotalBytesSent_Type.__name__ = "PhivCounter"
_PhivEndCountTotalBytesSent_Object = MibTableColumn
phivEndCountTotalBytesSent = _PhivEndCountTotalBytesSent_Object(
    (1, 3, 6, 1, 2, 1, 18, 4, 2, 1, 8),
    _PhivEndCountTotalBytesSent_Type()
)
phivEndCountTotalBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivEndCountTotalBytesSent.setStatus("mandatory")


class _PhivEndCountTotalMessRec_Type(PhivCounter):
    """Custom type phivEndCountTotalMessRec based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PhivEndCountTotalMessRec_Type.__name__ = "PhivCounter"
_PhivEndCountTotalMessRec_Object = MibTableColumn
phivEndCountTotalMessRec = _PhivEndCountTotalMessRec_Object(
    (1, 3, 6, 1, 2, 1, 18, 4, 2, 1, 9),
    _PhivEndCountTotalMessRec_Type()
)
phivEndCountTotalMessRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivEndCountTotalMessRec.setStatus("mandatory")


class _PhivEndCountTotalMessSent_Type(PhivCounter):
    """Custom type phivEndCountTotalMessSent based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PhivEndCountTotalMessSent_Type.__name__ = "PhivCounter"
_PhivEndCountTotalMessSent_Object = MibTableColumn
phivEndCountTotalMessSent = _PhivEndCountTotalMessSent_Object(
    (1, 3, 6, 1, 2, 1, 18, 4, 2, 1, 10),
    _PhivEndCountTotalMessSent_Type()
)
phivEndCountTotalMessSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivEndCountTotalMessSent.setStatus("mandatory")


class _PhivEndCountConnectsRecd_Type(PhivCounter):
    """Custom type phivEndCountConnectsRecd based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PhivEndCountConnectsRecd_Type.__name__ = "PhivCounter"
_PhivEndCountConnectsRecd_Object = MibTableColumn
phivEndCountConnectsRecd = _PhivEndCountConnectsRecd_Object(
    (1, 3, 6, 1, 2, 1, 18, 4, 2, 1, 11),
    _PhivEndCountConnectsRecd_Type()
)
phivEndCountConnectsRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivEndCountConnectsRecd.setStatus("mandatory")


class _PhivEndCountConnectsSent_Type(PhivCounter):
    """Custom type phivEndCountConnectsSent based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PhivEndCountConnectsSent_Type.__name__ = "PhivCounter"
_PhivEndCountConnectsSent_Object = MibTableColumn
phivEndCountConnectsSent = _PhivEndCountConnectsSent_Object(
    (1, 3, 6, 1, 2, 1, 18, 4, 2, 1, 12),
    _PhivEndCountConnectsSent_Type()
)
phivEndCountConnectsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivEndCountConnectsSent.setStatus("mandatory")


class _PhivEndCountReponseTimeouts_Type(PhivCounter):
    """Custom type phivEndCountReponseTimeouts based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PhivEndCountReponseTimeouts_Type.__name__ = "PhivCounter"
_PhivEndCountReponseTimeouts_Object = MibTableColumn
phivEndCountReponseTimeouts = _PhivEndCountReponseTimeouts_Object(
    (1, 3, 6, 1, 2, 1, 18, 4, 2, 1, 13),
    _PhivEndCountReponseTimeouts_Type()
)
phivEndCountReponseTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivEndCountReponseTimeouts.setStatus("mandatory")


class _PhivEndCountRecdConnectResErrs_Type(PhivCounter):
    """Custom type phivEndCountRecdConnectResErrs based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PhivEndCountRecdConnectResErrs_Type.__name__ = "PhivCounter"
_PhivEndCountRecdConnectResErrs_Object = MibTableColumn
phivEndCountRecdConnectResErrs = _PhivEndCountRecdConnectResErrs_Object(
    (1, 3, 6, 1, 2, 1, 18, 4, 2, 1, 14),
    _PhivEndCountRecdConnectResErrs_Type()
)
phivEndCountRecdConnectResErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivEndCountRecdConnectResErrs.setStatus("mandatory")


class _PhivEndMaxLinks_Type(Integer32):
    """Custom type phivEndMaxLinks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PhivEndMaxLinks_Type.__name__ = "Integer32"
_PhivEndMaxLinks_Object = MibScalar
phivEndMaxLinks = _PhivEndMaxLinks_Object(
    (1, 3, 6, 1, 2, 1, 18, 4, 3),
    _PhivEndMaxLinks_Type()
)
phivEndMaxLinks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivEndMaxLinks.setStatus("mandatory")


class _PhivEndNSPVers_Type(DisplayString):
    """Custom type phivEndNSPVers based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PhivEndNSPVers_Type.__name__ = "DisplayString"
_PhivEndNSPVers_Object = MibScalar
phivEndNSPVers = _PhivEndNSPVers_Object(
    (1, 3, 6, 1, 2, 1, 18, 4, 4),
    _PhivEndNSPVers_Type()
)
phivEndNSPVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivEndNSPVers.setStatus("mandatory")


class _PhivEndRetransmitFactor_Type(Integer32):
    """Custom type phivEndRetransmitFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PhivEndRetransmitFactor_Type.__name__ = "Integer32"
_PhivEndRetransmitFactor_Object = MibScalar
phivEndRetransmitFactor = _PhivEndRetransmitFactor_Object(
    (1, 3, 6, 1, 2, 1, 18, 4, 5),
    _PhivEndRetransmitFactor_Type()
)
phivEndRetransmitFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivEndRetransmitFactor.setStatus("mandatory")


class _PhivEndDelayFact_Type(Integer32):
    """Custom type phivEndDelayFact based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PhivEndDelayFact_Type.__name__ = "Integer32"
_PhivEndDelayFact_Object = MibScalar
phivEndDelayFact = _PhivEndDelayFact_Object(
    (1, 3, 6, 1, 2, 1, 18, 4, 6),
    _PhivEndDelayFact_Type()
)
phivEndDelayFact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivEndDelayFact.setStatus("mandatory")


class _PhivEndDelayWeight_Type(Integer32):
    """Custom type phivEndDelayWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PhivEndDelayWeight_Type.__name__ = "Integer32"
_PhivEndDelayWeight_Object = MibScalar
phivEndDelayWeight = _PhivEndDelayWeight_Object(
    (1, 3, 6, 1, 2, 1, 18, 4, 7),
    _PhivEndDelayWeight_Type()
)
phivEndDelayWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivEndDelayWeight.setStatus("mandatory")


class _PhivEndInactivityTimer_Type(Integer32):
    """Custom type phivEndInactivityTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PhivEndInactivityTimer_Type.__name__ = "Integer32"
_PhivEndInactivityTimer_Object = MibScalar
phivEndInactivityTimer = _PhivEndInactivityTimer_Object(
    (1, 3, 6, 1, 2, 1, 18, 4, 8),
    _PhivEndInactivityTimer_Type()
)
phivEndInactivityTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivEndInactivityTimer.setStatus("mandatory")


class _PhivEndCountZeroCount_Type(Integer32):
    """Custom type phivEndCountZeroCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reset", 2))
    )


_PhivEndCountZeroCount_Type.__name__ = "Integer32"
_PhivEndCountZeroCount_Object = MibScalar
phivEndCountZeroCount = _PhivEndCountZeroCount_Object(
    (1, 3, 6, 1, 2, 1, 18, 4, 9),
    _PhivEndCountZeroCount_Type()
)
phivEndCountZeroCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivEndCountZeroCount.setStatus("mandatory")


class _PhivEndMaxLinksActive_Type(PhivCounter):
    """Custom type phivEndMaxLinksActive based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PhivEndMaxLinksActive_Type.__name__ = "PhivCounter"
_PhivEndMaxLinksActive_Object = MibScalar
phivEndMaxLinksActive = _PhivEndMaxLinksActive_Object(
    (1, 3, 6, 1, 2, 1, 18, 4, 10),
    _PhivEndMaxLinksActive_Type()
)
phivEndMaxLinksActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivEndMaxLinksActive.setStatus("mandatory")
_Routing_ObjectIdentity = ObjectIdentity
routing = _Routing_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 18, 5)
)


class _PhivRouteBroadcastRouteTimer_Type(Integer32):
    """Custom type phivRouteBroadcastRouteTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PhivRouteBroadcastRouteTimer_Type.__name__ = "Integer32"
_PhivRouteBroadcastRouteTimer_Object = MibScalar
phivRouteBroadcastRouteTimer = _PhivRouteBroadcastRouteTimer_Object(
    (1, 3, 6, 1, 2, 1, 18, 5, 1),
    _PhivRouteBroadcastRouteTimer_Type()
)
phivRouteBroadcastRouteTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivRouteBroadcastRouteTimer.setStatus("mandatory")


class _PhivRouteBuffSize_Type(Integer32):
    """Custom type phivRouteBuffSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PhivRouteBuffSize_Type.__name__ = "Integer32"
_PhivRouteBuffSize_Object = MibScalar
phivRouteBuffSize = _PhivRouteBuffSize_Object(
    (1, 3, 6, 1, 2, 1, 18, 5, 2),
    _PhivRouteBuffSize_Type()
)
phivRouteBuffSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivRouteBuffSize.setStatus("mandatory")


class _PhivRouteRoutingVers_Type(DisplayString):
    """Custom type phivRouteRoutingVers based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PhivRouteRoutingVers_Type.__name__ = "DisplayString"
_PhivRouteRoutingVers_Object = MibScalar
phivRouteRoutingVers = _PhivRouteRoutingVers_Object(
    (1, 3, 6, 1, 2, 1, 18, 5, 3),
    _PhivRouteRoutingVers_Type()
)
phivRouteRoutingVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivRouteRoutingVers.setStatus("mandatory")


class _PhivRouteMaxAddr_Type(Integer32):
    """Custom type phivRouteMaxAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_PhivRouteMaxAddr_Type.__name__ = "Integer32"
_PhivRouteMaxAddr_Object = MibScalar
phivRouteMaxAddr = _PhivRouteMaxAddr_Object(
    (1, 3, 6, 1, 2, 1, 18, 5, 4),
    _PhivRouteMaxAddr_Type()
)
phivRouteMaxAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivRouteMaxAddr.setStatus("mandatory")


class _PhivRouteMaxBdcastNonRouters_Type(Integer32):
    """Custom type phivRouteMaxBdcastNonRouters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PhivRouteMaxBdcastNonRouters_Type.__name__ = "Integer32"
_PhivRouteMaxBdcastNonRouters_Object = MibScalar
phivRouteMaxBdcastNonRouters = _PhivRouteMaxBdcastNonRouters_Object(
    (1, 3, 6, 1, 2, 1, 18, 5, 5),
    _PhivRouteMaxBdcastNonRouters_Type()
)
phivRouteMaxBdcastNonRouters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivRouteMaxBdcastNonRouters.setStatus("mandatory")


class _PhivRouteMaxBdcastRouters_Type(Integer32):
    """Custom type phivRouteMaxBdcastRouters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PhivRouteMaxBdcastRouters_Type.__name__ = "Integer32"
_PhivRouteMaxBdcastRouters_Object = MibScalar
phivRouteMaxBdcastRouters = _PhivRouteMaxBdcastRouters_Object(
    (1, 3, 6, 1, 2, 1, 18, 5, 6),
    _PhivRouteMaxBdcastRouters_Type()
)
phivRouteMaxBdcastRouters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivRouteMaxBdcastRouters.setStatus("mandatory")


class _PhivRouteMaxBuffs_Type(Integer32):
    """Custom type phivRouteMaxBuffs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PhivRouteMaxBuffs_Type.__name__ = "Integer32"
_PhivRouteMaxBuffs_Object = MibScalar
phivRouteMaxBuffs = _PhivRouteMaxBuffs_Object(
    (1, 3, 6, 1, 2, 1, 18, 5, 7),
    _PhivRouteMaxBuffs_Type()
)
phivRouteMaxBuffs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivRouteMaxBuffs.setStatus("mandatory")


class _PhivRouteMaxCircuits_Type(Integer32):
    """Custom type phivRouteMaxCircuits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PhivRouteMaxCircuits_Type.__name__ = "Integer32"
_PhivRouteMaxCircuits_Object = MibScalar
phivRouteMaxCircuits = _PhivRouteMaxCircuits_Object(
    (1, 3, 6, 1, 2, 1, 18, 5, 8),
    _PhivRouteMaxCircuits_Type()
)
phivRouteMaxCircuits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivRouteMaxCircuits.setStatus("mandatory")


class _PhivRouteMaxCost_Type(Integer32):
    """Custom type phivRouteMaxCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1022),
    )


_PhivRouteMaxCost_Type.__name__ = "Integer32"
_PhivRouteMaxCost_Object = MibScalar
phivRouteMaxCost = _PhivRouteMaxCost_Object(
    (1, 3, 6, 1, 2, 1, 18, 5, 9),
    _PhivRouteMaxCost_Type()
)
phivRouteMaxCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivRouteMaxCost.setStatus("mandatory")


class _PhivRouteMaxHops_Type(Integer32):
    """Custom type phivRouteMaxHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_PhivRouteMaxHops_Type.__name__ = "Integer32"
_PhivRouteMaxHops_Object = MibScalar
phivRouteMaxHops = _PhivRouteMaxHops_Object(
    (1, 3, 6, 1, 2, 1, 18, 5, 10),
    _PhivRouteMaxHops_Type()
)
phivRouteMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivRouteMaxHops.setStatus("mandatory")


class _PhivRouteMaxVisits_Type(Integer32):
    """Custom type phivRouteMaxVisits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_PhivRouteMaxVisits_Type.__name__ = "Integer32"
_PhivRouteMaxVisits_Object = MibScalar
phivRouteMaxVisits = _PhivRouteMaxVisits_Object(
    (1, 3, 6, 1, 2, 1, 18, 5, 11),
    _PhivRouteMaxVisits_Type()
)
phivRouteMaxVisits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivRouteMaxVisits.setStatus("mandatory")


class _PhivRouteRoutingTimer_Type(Integer32):
    """Custom type phivRouteRoutingTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PhivRouteRoutingTimer_Type.__name__ = "Integer32"
_PhivRouteRoutingTimer_Object = MibScalar
phivRouteRoutingTimer = _PhivRouteRoutingTimer_Object(
    (1, 3, 6, 1, 2, 1, 18, 5, 12),
    _PhivRouteRoutingTimer_Type()
)
phivRouteRoutingTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivRouteRoutingTimer.setStatus("mandatory")


class _PhivRouteSegBuffSize_Type(Integer32):
    """Custom type phivRouteSegBuffSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PhivRouteSegBuffSize_Type.__name__ = "Integer32"
_PhivRouteSegBuffSize_Object = MibScalar
phivRouteSegBuffSize = _PhivRouteSegBuffSize_Object(
    (1, 3, 6, 1, 2, 1, 18, 5, 13),
    _PhivRouteSegBuffSize_Type()
)
phivRouteSegBuffSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivRouteSegBuffSize.setStatus("mandatory")


class _PhivRouteType_Type(Integer32):
    """Custom type phivRouteType based on Integer32"""
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
        *(("area", 3),
          ("nonrouting-III", 2),
          ("nonrouting-IV", 5),
          ("routing-III", 1),
          ("routing-IV", 4))
    )


_PhivRouteType_Type.__name__ = "Integer32"
_PhivRouteType_Object = MibScalar
phivRouteType = _PhivRouteType_Object(
    (1, 3, 6, 1, 2, 1, 18, 5, 14),
    _PhivRouteType_Type()
)
phivRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivRouteType.setStatus("obsolete")


class _PhivRouteCountAgedPktLoss_Type(PhivCounter):
    """Custom type phivRouteCountAgedPktLoss based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_PhivRouteCountAgedPktLoss_Type.__name__ = "PhivCounter"
_PhivRouteCountAgedPktLoss_Object = MibScalar
phivRouteCountAgedPktLoss = _PhivRouteCountAgedPktLoss_Object(
    (1, 3, 6, 1, 2, 1, 18, 5, 15),
    _PhivRouteCountAgedPktLoss_Type()
)
phivRouteCountAgedPktLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivRouteCountAgedPktLoss.setStatus("mandatory")


class _PhivRouteCountNodeUnrPktLoss_Type(PhivCounter):
    """Custom type phivRouteCountNodeUnrPktLoss based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PhivRouteCountNodeUnrPktLoss_Type.__name__ = "PhivCounter"
_PhivRouteCountNodeUnrPktLoss_Object = MibScalar
phivRouteCountNodeUnrPktLoss = _PhivRouteCountNodeUnrPktLoss_Object(
    (1, 3, 6, 1, 2, 1, 18, 5, 16),
    _PhivRouteCountNodeUnrPktLoss_Type()
)
phivRouteCountNodeUnrPktLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivRouteCountNodeUnrPktLoss.setStatus("mandatory")


class _PhivRouteCountOutRngePktLoss_Type(PhivCounter):
    """Custom type phivRouteCountOutRngePktLoss based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_PhivRouteCountOutRngePktLoss_Type.__name__ = "PhivCounter"
_PhivRouteCountOutRngePktLoss_Object = MibScalar
phivRouteCountOutRngePktLoss = _PhivRouteCountOutRngePktLoss_Object(
    (1, 3, 6, 1, 2, 1, 18, 5, 17),
    _PhivRouteCountOutRngePktLoss_Type()
)
phivRouteCountOutRngePktLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivRouteCountOutRngePktLoss.setStatus("mandatory")


class _PhivRouteCountOverSzePktLoss_Type(PhivCounter):
    """Custom type phivRouteCountOverSzePktLoss based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_PhivRouteCountOverSzePktLoss_Type.__name__ = "PhivCounter"
_PhivRouteCountOverSzePktLoss_Object = MibScalar
phivRouteCountOverSzePktLoss = _PhivRouteCountOverSzePktLoss_Object(
    (1, 3, 6, 1, 2, 1, 18, 5, 18),
    _PhivRouteCountOverSzePktLoss_Type()
)
phivRouteCountOverSzePktLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivRouteCountOverSzePktLoss.setStatus("mandatory")


class _PhivRouteCountPacketFmtErr_Type(PhivCounter):
    """Custom type phivRouteCountPacketFmtErr based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_PhivRouteCountPacketFmtErr_Type.__name__ = "PhivCounter"
_PhivRouteCountPacketFmtErr_Object = MibScalar
phivRouteCountPacketFmtErr = _PhivRouteCountPacketFmtErr_Object(
    (1, 3, 6, 1, 2, 1, 18, 5, 19),
    _PhivRouteCountPacketFmtErr_Type()
)
phivRouteCountPacketFmtErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivRouteCountPacketFmtErr.setStatus("mandatory")


class _PhivRouteCountPtlRteUpdtLoss_Type(PhivCounter):
    """Custom type phivRouteCountPtlRteUpdtLoss based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_PhivRouteCountPtlRteUpdtLoss_Type.__name__ = "PhivCounter"
_PhivRouteCountPtlRteUpdtLoss_Object = MibScalar
phivRouteCountPtlRteUpdtLoss = _PhivRouteCountPtlRteUpdtLoss_Object(
    (1, 3, 6, 1, 2, 1, 18, 5, 20),
    _PhivRouteCountPtlRteUpdtLoss_Type()
)
phivRouteCountPtlRteUpdtLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivRouteCountPtlRteUpdtLoss.setStatus("mandatory")


class _PhivRouteCountVerifReject_Type(PhivCounter):
    """Custom type phivRouteCountVerifReject based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_PhivRouteCountVerifReject_Type.__name__ = "PhivCounter"
_PhivRouteCountVerifReject_Object = MibScalar
phivRouteCountVerifReject = _PhivRouteCountVerifReject_Object(
    (1, 3, 6, 1, 2, 1, 18, 5, 21),
    _PhivRouteCountVerifReject_Type()
)
phivRouteCountVerifReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivRouteCountVerifReject.setStatus("mandatory")
_PhivLevel1RouteTable_Object = MibTable
phivLevel1RouteTable = _PhivLevel1RouteTable_Object(
    (1, 3, 6, 1, 2, 1, 18, 5, 22)
)
if mibBuilder.loadTexts:
    phivLevel1RouteTable.setStatus("mandatory")
_PhivLevel1RouteEntry_Object = MibTableRow
phivLevel1RouteEntry = _PhivLevel1RouteEntry_Object(
    (1, 3, 6, 1, 2, 1, 18, 5, 22, 1)
)
phivLevel1RouteEntry.setIndexNames(
    (0, "DECNET-PHIV-MIB", "phivLevel1RouteNodeAddr"),
)
if mibBuilder.loadTexts:
    phivLevel1RouteEntry.setStatus("mandatory")
_PhivLevel1RouteNodeAddr_Type = PhivAddr
_PhivLevel1RouteNodeAddr_Object = MibTableColumn
phivLevel1RouteNodeAddr = _PhivLevel1RouteNodeAddr_Object(
    (1, 3, 6, 1, 2, 1, 18, 5, 22, 1, 1),
    _PhivLevel1RouteNodeAddr_Type()
)
phivLevel1RouteNodeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivLevel1RouteNodeAddr.setStatus("mandatory")


class _PhivLevel1RouteCircuitIndex_Type(Integer32):
    """Custom type phivLevel1RouteCircuitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PhivLevel1RouteCircuitIndex_Type.__name__ = "Integer32"
_PhivLevel1RouteCircuitIndex_Object = MibTableColumn
phivLevel1RouteCircuitIndex = _PhivLevel1RouteCircuitIndex_Object(
    (1, 3, 6, 1, 2, 1, 18, 5, 22, 1, 2),
    _PhivLevel1RouteCircuitIndex_Type()
)
phivLevel1RouteCircuitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivLevel1RouteCircuitIndex.setStatus("mandatory")


class _PhivLevel1RouteCost_Type(Integer32):
    """Custom type phivLevel1RouteCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PhivLevel1RouteCost_Type.__name__ = "Integer32"
_PhivLevel1RouteCost_Object = MibTableColumn
phivLevel1RouteCost = _PhivLevel1RouteCost_Object(
    (1, 3, 6, 1, 2, 1, 18, 5, 22, 1, 3),
    _PhivLevel1RouteCost_Type()
)
phivLevel1RouteCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivLevel1RouteCost.setStatus("mandatory")


class _PhivLevel1RouteHops_Type(Integer32):
    """Custom type phivLevel1RouteHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_PhivLevel1RouteHops_Type.__name__ = "Integer32"
_PhivLevel1RouteHops_Object = MibTableColumn
phivLevel1RouteHops = _PhivLevel1RouteHops_Object(
    (1, 3, 6, 1, 2, 1, 18, 5, 22, 1, 4),
    _PhivLevel1RouteHops_Type()
)
phivLevel1RouteHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivLevel1RouteHops.setStatus("mandatory")
_PhivLevel1RouteNextNode_Type = PhivAddr
_PhivLevel1RouteNextNode_Object = MibTableColumn
phivLevel1RouteNextNode = _PhivLevel1RouteNextNode_Object(
    (1, 3, 6, 1, 2, 1, 18, 5, 22, 1, 5),
    _PhivLevel1RouteNextNode_Type()
)
phivLevel1RouteNextNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivLevel1RouteNextNode.setStatus("mandatory")


class _PhivRouteCountZeroCount_Type(Integer32):
    """Custom type phivRouteCountZeroCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reset", 2))
    )


_PhivRouteCountZeroCount_Type.__name__ = "Integer32"
_PhivRouteCountZeroCount_Object = MibScalar
phivRouteCountZeroCount = _PhivRouteCountZeroCount_Object(
    (1, 3, 6, 1, 2, 1, 18, 5, 23),
    _PhivRouteCountZeroCount_Type()
)
phivRouteCountZeroCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivRouteCountZeroCount.setStatus("mandatory")
_PhivRouteSystemAddr_Type = PhivAddr
_PhivRouteSystemAddr_Object = MibScalar
phivRouteSystemAddr = _PhivRouteSystemAddr_Object(
    (1, 3, 6, 1, 2, 1, 18, 5, 24),
    _PhivRouteSystemAddr_Type()
)
phivRouteSystemAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivRouteSystemAddr.setStatus("obsolete")


class _PhivRouteRoutingType_Type(Integer32):
    """Custom type phivRouteRoutingType based on Integer32"""
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
        *(("area", 3),
          ("nonrouting-III", 2),
          ("nonrouting-IV", 5),
          ("routing-III", 1),
          ("routing-IV", 4))
    )


_PhivRouteRoutingType_Type.__name__ = "Integer32"
_PhivRouteRoutingType_Object = MibScalar
phivRouteRoutingType = _PhivRouteRoutingType_Object(
    (1, 3, 6, 1, 2, 1, 18, 5, 25),
    _PhivRouteRoutingType_Type()
)
phivRouteRoutingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivRouteRoutingType.setStatus("mandatory")
_PhivRouteSystemAddress_Type = PhivAddr
_PhivRouteSystemAddress_Object = MibScalar
phivRouteSystemAddress = _PhivRouteSystemAddress_Object(
    (1, 3, 6, 1, 2, 1, 18, 5, 26),
    _PhivRouteSystemAddress_Type()
)
phivRouteSystemAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivRouteSystemAddress.setStatus("mandatory")
_Circuit_ObjectIdentity = ObjectIdentity
circuit = _Circuit_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 18, 6)
)
_PhivCircuitParametersTable_Object = MibTable
phivCircuitParametersTable = _PhivCircuitParametersTable_Object(
    (1, 3, 6, 1, 2, 1, 18, 6, 1)
)
if mibBuilder.loadTexts:
    phivCircuitParametersTable.setStatus("mandatory")
_PhivCircuitParametersEntry_Object = MibTableRow
phivCircuitParametersEntry = _PhivCircuitParametersEntry_Object(
    (1, 3, 6, 1, 2, 1, 18, 6, 1, 1)
)
phivCircuitParametersEntry.setIndexNames(
    (0, "DECNET-PHIV-MIB", "phivCircuitIndex"),
)
if mibBuilder.loadTexts:
    phivCircuitParametersEntry.setStatus("mandatory")


class _PhivCircuitIndex_Type(Integer32):
    """Custom type phivCircuitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PhivCircuitIndex_Type.__name__ = "Integer32"
_PhivCircuitIndex_Object = MibTableColumn
phivCircuitIndex = _PhivCircuitIndex_Object(
    (1, 3, 6, 1, 2, 1, 18, 6, 1, 1, 1),
    _PhivCircuitIndex_Type()
)
phivCircuitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCircuitIndex.setStatus("mandatory")
_PhivCircuitLineIndex_Type = InterfaceIndex
_PhivCircuitLineIndex_Object = MibTableColumn
phivCircuitLineIndex = _PhivCircuitLineIndex_Object(
    (1, 3, 6, 1, 2, 1, 18, 6, 1, 1, 2),
    _PhivCircuitLineIndex_Type()
)
phivCircuitLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCircuitLineIndex.setStatus("mandatory")


class _PhivCircuitCommonState_Type(Integer32):
    """Custom type phivCircuitCommonState based on Integer32"""
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
        *(("cleared", 4),
          ("off", 2),
          ("on", 1),
          ("service", 3))
    )


_PhivCircuitCommonState_Type.__name__ = "Integer32"
_PhivCircuitCommonState_Object = MibTableColumn
phivCircuitCommonState = _PhivCircuitCommonState_Object(
    (1, 3, 6, 1, 2, 1, 18, 6, 1, 1, 3),
    _PhivCircuitCommonState_Type()
)
phivCircuitCommonState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivCircuitCommonState.setStatus("mandatory")


class _PhivCircuitCommonSubState_Type(Integer32):
    """Custom type phivCircuitCommonSubState based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("autodumping", 9),
          ("autoloading", 8),
          ("autoservice", 7),
          ("autotriggering", 10),
          ("dumping", 5),
          ("failed", 12),
          ("loading", 4),
          ("looping", 3),
          ("reflecting", 2),
          ("running", 13),
          ("starting", 1),
          ("synchronizing", 11),
          ("triggering", 6))
    )


_PhivCircuitCommonSubState_Type.__name__ = "Integer32"
_PhivCircuitCommonSubState_Object = MibTableColumn
phivCircuitCommonSubState = _PhivCircuitCommonSubState_Object(
    (1, 3, 6, 1, 2, 1, 18, 6, 1, 1, 4),
    _PhivCircuitCommonSubState_Type()
)
phivCircuitCommonSubState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCircuitCommonSubState.setStatus("mandatory")


class _PhivCircuitCommonName_Type(DisplayString):
    """Custom type phivCircuitCommonName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PhivCircuitCommonName_Type.__name__ = "DisplayString"
_PhivCircuitCommonName_Object = MibTableColumn
phivCircuitCommonName = _PhivCircuitCommonName_Object(
    (1, 3, 6, 1, 2, 1, 18, 6, 1, 1, 5),
    _PhivCircuitCommonName_Type()
)
phivCircuitCommonName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCircuitCommonName.setStatus("mandatory")


class _PhivCircuitExecRecallTimer_Type(Integer32):
    """Custom type phivCircuitExecRecallTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PhivCircuitExecRecallTimer_Type.__name__ = "Integer32"
_PhivCircuitExecRecallTimer_Object = MibTableColumn
phivCircuitExecRecallTimer = _PhivCircuitExecRecallTimer_Object(
    (1, 3, 6, 1, 2, 1, 18, 6, 1, 1, 6),
    _PhivCircuitExecRecallTimer_Type()
)
phivCircuitExecRecallTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivCircuitExecRecallTimer.setStatus("mandatory")


class _PhivCircuitCommonType_Type(Integer32):
    """Custom type phivCircuitCommonType based on Integer32"""
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
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("bisync", 9),
          ("ci", 7),
          ("ddcmp-control", 2),
          ("ddcmp-dmc", 5),
          ("ddcmp-point", 1),
          ("ddcmp-tributary", 3),
          ("ethernet", 6),
          ("fddi", 15),
          ("other", 14),
          ("qp2-dte20", 8),
          ("x25", 4))
    )


_PhivCircuitCommonType_Type.__name__ = "Integer32"
_PhivCircuitCommonType_Object = MibTableColumn
phivCircuitCommonType = _PhivCircuitCommonType_Object(
    (1, 3, 6, 1, 2, 1, 18, 6, 1, 1, 7),
    _PhivCircuitCommonType_Type()
)
phivCircuitCommonType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCircuitCommonType.setStatus("mandatory")


class _PhivCircuitService_Type(Integer32):
    """Custom type phivCircuitService based on Integer32"""
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


_PhivCircuitService_Type.__name__ = "Integer32"
_PhivCircuitService_Object = MibTableColumn
phivCircuitService = _PhivCircuitService_Object(
    (1, 3, 6, 1, 2, 1, 18, 6, 1, 1, 8),
    _PhivCircuitService_Type()
)
phivCircuitService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivCircuitService.setStatus("mandatory")


class _PhivCircuitExecCost_Type(Integer32):
    """Custom type phivCircuitExecCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_PhivCircuitExecCost_Type.__name__ = "Integer32"
_PhivCircuitExecCost_Object = MibTableColumn
phivCircuitExecCost = _PhivCircuitExecCost_Object(
    (1, 3, 6, 1, 2, 1, 18, 6, 1, 1, 9),
    _PhivCircuitExecCost_Type()
)
phivCircuitExecCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivCircuitExecCost.setStatus("mandatory")


class _PhivCircuitExecHelloTimer_Type(Integer32):
    """Custom type phivCircuitExecHelloTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_PhivCircuitExecHelloTimer_Type.__name__ = "Integer32"
_PhivCircuitExecHelloTimer_Object = MibTableColumn
phivCircuitExecHelloTimer = _PhivCircuitExecHelloTimer_Object(
    (1, 3, 6, 1, 2, 1, 18, 6, 1, 1, 10),
    _PhivCircuitExecHelloTimer_Type()
)
phivCircuitExecHelloTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivCircuitExecHelloTimer.setStatus("mandatory")
_PhivCircuitCountTable_Object = MibTable
phivCircuitCountTable = _PhivCircuitCountTable_Object(
    (1, 3, 6, 1, 2, 1, 18, 6, 2)
)
if mibBuilder.loadTexts:
    phivCircuitCountTable.setStatus("mandatory")
_PhivCircuitCountEntry_Object = MibTableRow
phivCircuitCountEntry = _PhivCircuitCountEntry_Object(
    (1, 3, 6, 1, 2, 1, 18, 6, 2, 1)
)
phivCircuitCountEntry.setIndexNames(
    (0, "DECNET-PHIV-MIB", "phivCircuitIndex"),
)
if mibBuilder.loadTexts:
    phivCircuitCountEntry.setStatus("mandatory")


class _PhivCircuitCountSecLastZeroed_Type(PhivCounter):
    """Custom type phivCircuitCountSecLastZeroed based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PhivCircuitCountSecLastZeroed_Type.__name__ = "PhivCounter"
_PhivCircuitCountSecLastZeroed_Object = MibTableColumn
phivCircuitCountSecLastZeroed = _PhivCircuitCountSecLastZeroed_Object(
    (1, 3, 6, 1, 2, 1, 18, 6, 2, 1, 1),
    _PhivCircuitCountSecLastZeroed_Type()
)
phivCircuitCountSecLastZeroed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCircuitCountSecLastZeroed.setStatus("mandatory")


class _PhivCircuitCountTermPacketsRecd_Type(PhivCounter):
    """Custom type phivCircuitCountTermPacketsRecd based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PhivCircuitCountTermPacketsRecd_Type.__name__ = "PhivCounter"
_PhivCircuitCountTermPacketsRecd_Object = MibTableColumn
phivCircuitCountTermPacketsRecd = _PhivCircuitCountTermPacketsRecd_Object(
    (1, 3, 6, 1, 2, 1, 18, 6, 2, 1, 2),
    _PhivCircuitCountTermPacketsRecd_Type()
)
phivCircuitCountTermPacketsRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCircuitCountTermPacketsRecd.setStatus("mandatory")


class _PhivCircuitCountOriginPackSent_Type(PhivCounter):
    """Custom type phivCircuitCountOriginPackSent based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PhivCircuitCountOriginPackSent_Type.__name__ = "PhivCounter"
_PhivCircuitCountOriginPackSent_Object = MibTableColumn
phivCircuitCountOriginPackSent = _PhivCircuitCountOriginPackSent_Object(
    (1, 3, 6, 1, 2, 1, 18, 6, 2, 1, 3),
    _PhivCircuitCountOriginPackSent_Type()
)
phivCircuitCountOriginPackSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCircuitCountOriginPackSent.setStatus("mandatory")


class _PhivCircuitCountTermCongLoss_Type(PhivCounter):
    """Custom type phivCircuitCountTermCongLoss based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PhivCircuitCountTermCongLoss_Type.__name__ = "PhivCounter"
_PhivCircuitCountTermCongLoss_Object = MibTableColumn
phivCircuitCountTermCongLoss = _PhivCircuitCountTermCongLoss_Object(
    (1, 3, 6, 1, 2, 1, 18, 6, 2, 1, 4),
    _PhivCircuitCountTermCongLoss_Type()
)
phivCircuitCountTermCongLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCircuitCountTermCongLoss.setStatus("mandatory")


class _PhivCircuitCountCorruptLoss_Type(PhivCounter):
    """Custom type phivCircuitCountCorruptLoss based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhivCircuitCountCorruptLoss_Type.__name__ = "PhivCounter"
_PhivCircuitCountCorruptLoss_Object = MibTableColumn
phivCircuitCountCorruptLoss = _PhivCircuitCountCorruptLoss_Object(
    (1, 3, 6, 1, 2, 1, 18, 6, 2, 1, 5),
    _PhivCircuitCountCorruptLoss_Type()
)
phivCircuitCountCorruptLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCircuitCountCorruptLoss.setStatus("mandatory")


class _PhivCircuitCountTransitPksRecd_Type(PhivCounter):
    """Custom type phivCircuitCountTransitPksRecd based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PhivCircuitCountTransitPksRecd_Type.__name__ = "PhivCounter"
_PhivCircuitCountTransitPksRecd_Object = MibTableColumn
phivCircuitCountTransitPksRecd = _PhivCircuitCountTransitPksRecd_Object(
    (1, 3, 6, 1, 2, 1, 18, 6, 2, 1, 6),
    _PhivCircuitCountTransitPksRecd_Type()
)
phivCircuitCountTransitPksRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCircuitCountTransitPksRecd.setStatus("mandatory")


class _PhivCircuitCountTransitPkSent_Type(PhivCounter):
    """Custom type phivCircuitCountTransitPkSent based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PhivCircuitCountTransitPkSent_Type.__name__ = "PhivCounter"
_PhivCircuitCountTransitPkSent_Object = MibTableColumn
phivCircuitCountTransitPkSent = _PhivCircuitCountTransitPkSent_Object(
    (1, 3, 6, 1, 2, 1, 18, 6, 2, 1, 7),
    _PhivCircuitCountTransitPkSent_Type()
)
phivCircuitCountTransitPkSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCircuitCountTransitPkSent.setStatus("mandatory")


class _PhivCircuitCountTransitCongestLoss_Type(PhivCounter):
    """Custom type phivCircuitCountTransitCongestLoss based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PhivCircuitCountTransitCongestLoss_Type.__name__ = "PhivCounter"
_PhivCircuitCountTransitCongestLoss_Object = MibTableColumn
phivCircuitCountTransitCongestLoss = _PhivCircuitCountTransitCongestLoss_Object(
    (1, 3, 6, 1, 2, 1, 18, 6, 2, 1, 8),
    _PhivCircuitCountTransitCongestLoss_Type()
)
phivCircuitCountTransitCongestLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCircuitCountTransitCongestLoss.setStatus("mandatory")


class _PhivCircuitCountCircuitDown_Type(PhivCounter):
    """Custom type phivCircuitCountCircuitDown based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhivCircuitCountCircuitDown_Type.__name__ = "PhivCounter"
_PhivCircuitCountCircuitDown_Object = MibTableColumn
phivCircuitCountCircuitDown = _PhivCircuitCountCircuitDown_Object(
    (1, 3, 6, 1, 2, 1, 18, 6, 2, 1, 9),
    _PhivCircuitCountCircuitDown_Type()
)
phivCircuitCountCircuitDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCircuitCountCircuitDown.setStatus("mandatory")


class _PhivCircuitCountInitFailure_Type(PhivCounter):
    """Custom type phivCircuitCountInitFailure based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhivCircuitCountInitFailure_Type.__name__ = "PhivCounter"
_PhivCircuitCountInitFailure_Object = MibTableColumn
phivCircuitCountInitFailure = _PhivCircuitCountInitFailure_Object(
    (1, 3, 6, 1, 2, 1, 18, 6, 2, 1, 10),
    _PhivCircuitCountInitFailure_Type()
)
phivCircuitCountInitFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCircuitCountInitFailure.setStatus("mandatory")


class _PhivCircuitCountAdjDown_Type(PhivCounter):
    """Custom type phivCircuitCountAdjDown based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PhivCircuitCountAdjDown_Type.__name__ = "PhivCounter"
_PhivCircuitCountAdjDown_Object = MibTableColumn
phivCircuitCountAdjDown = _PhivCircuitCountAdjDown_Object(
    (1, 3, 6, 1, 2, 1, 18, 6, 2, 1, 11),
    _PhivCircuitCountAdjDown_Type()
)
phivCircuitCountAdjDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCircuitCountAdjDown.setStatus("mandatory")


class _PhivCircuitCountPeakAdj_Type(PhivCounter):
    """Custom type phivCircuitCountPeakAdj based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PhivCircuitCountPeakAdj_Type.__name__ = "PhivCounter"
_PhivCircuitCountPeakAdj_Object = MibTableColumn
phivCircuitCountPeakAdj = _PhivCircuitCountPeakAdj_Object(
    (1, 3, 6, 1, 2, 1, 18, 6, 2, 1, 12),
    _PhivCircuitCountPeakAdj_Type()
)
phivCircuitCountPeakAdj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCircuitCountPeakAdj.setStatus("mandatory")


class _PhivCircuitCountBytesRecd_Type(PhivCounter):
    """Custom type phivCircuitCountBytesRecd based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PhivCircuitCountBytesRecd_Type.__name__ = "PhivCounter"
_PhivCircuitCountBytesRecd_Object = MibTableColumn
phivCircuitCountBytesRecd = _PhivCircuitCountBytesRecd_Object(
    (1, 3, 6, 1, 2, 1, 18, 6, 2, 1, 13),
    _PhivCircuitCountBytesRecd_Type()
)
phivCircuitCountBytesRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCircuitCountBytesRecd.setStatus("mandatory")


class _PhivCircuitCountBytesSent_Type(PhivCounter):
    """Custom type phivCircuitCountBytesSent based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PhivCircuitCountBytesSent_Type.__name__ = "PhivCounter"
_PhivCircuitCountBytesSent_Object = MibTableColumn
phivCircuitCountBytesSent = _PhivCircuitCountBytesSent_Object(
    (1, 3, 6, 1, 2, 1, 18, 6, 2, 1, 14),
    _PhivCircuitCountBytesSent_Type()
)
phivCircuitCountBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCircuitCountBytesSent.setStatus("mandatory")


class _PhivCircuitCountDataBlocksRecd_Type(PhivCounter):
    """Custom type phivCircuitCountDataBlocksRecd based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PhivCircuitCountDataBlocksRecd_Type.__name__ = "PhivCounter"
_PhivCircuitCountDataBlocksRecd_Object = MibTableColumn
phivCircuitCountDataBlocksRecd = _PhivCircuitCountDataBlocksRecd_Object(
    (1, 3, 6, 1, 2, 1, 18, 6, 2, 1, 15),
    _PhivCircuitCountDataBlocksRecd_Type()
)
phivCircuitCountDataBlocksRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCircuitCountDataBlocksRecd.setStatus("mandatory")


class _PhivCircuitCountDataBlocksSent_Type(PhivCounter):
    """Custom type phivCircuitCountDataBlocksSent based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PhivCircuitCountDataBlocksSent_Type.__name__ = "PhivCounter"
_PhivCircuitCountDataBlocksSent_Object = MibTableColumn
phivCircuitCountDataBlocksSent = _PhivCircuitCountDataBlocksSent_Object(
    (1, 3, 6, 1, 2, 1, 18, 6, 2, 1, 16),
    _PhivCircuitCountDataBlocksSent_Type()
)
phivCircuitCountDataBlocksSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCircuitCountDataBlocksSent.setStatus("mandatory")


class _PhivCircuitCountUsrBuffUnav_Type(PhivCounter):
    """Custom type phivCircuitCountUsrBuffUnav based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PhivCircuitCountUsrBuffUnav_Type.__name__ = "PhivCounter"
_PhivCircuitCountUsrBuffUnav_Object = MibTableColumn
phivCircuitCountUsrBuffUnav = _PhivCircuitCountUsrBuffUnav_Object(
    (1, 3, 6, 1, 2, 1, 18, 6, 2, 1, 17),
    _PhivCircuitCountUsrBuffUnav_Type()
)
phivCircuitCountUsrBuffUnav.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCircuitCountUsrBuffUnav.setStatus("mandatory")
_PhivCircuitOrigQueueLimit_Type = Integer32
_PhivCircuitOrigQueueLimit_Object = MibScalar
phivCircuitOrigQueueLimit = _PhivCircuitOrigQueueLimit_Object(
    (1, 3, 6, 1, 2, 1, 18, 6, 3),
    _PhivCircuitOrigQueueLimit_Type()
)
phivCircuitOrigQueueLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivCircuitOrigQueueLimit.setStatus("mandatory")


class _PhivCircuitCountZeroCount_Type(Integer32):
    """Custom type phivCircuitCountZeroCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reset", 2))
    )


_PhivCircuitCountZeroCount_Type.__name__ = "Integer32"
_PhivCircuitCountZeroCount_Object = MibScalar
phivCircuitCountZeroCount = _PhivCircuitCountZeroCount_Object(
    (1, 3, 6, 1, 2, 1, 18, 6, 4),
    _PhivCircuitCountZeroCount_Type()
)
phivCircuitCountZeroCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivCircuitCountZeroCount.setStatus("mandatory")
_Ddcmp_ObjectIdentity = ObjectIdentity
ddcmp = _Ddcmp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 18, 7)
)
_PhivDDCMPCircuitParametersTable_Object = MibTable
phivDDCMPCircuitParametersTable = _PhivDDCMPCircuitParametersTable_Object(
    (1, 3, 6, 1, 2, 1, 18, 7, 1)
)
if mibBuilder.loadTexts:
    phivDDCMPCircuitParametersTable.setStatus("mandatory")
_PhivDDCMPCircuitParametersEntry_Object = MibTableRow
phivDDCMPCircuitParametersEntry = _PhivDDCMPCircuitParametersEntry_Object(
    (1, 3, 6, 1, 2, 1, 18, 7, 1, 1)
)
phivDDCMPCircuitParametersEntry.setIndexNames(
    (0, "DECNET-PHIV-MIB", "phivDDCMPCircuitIndex"),
)
if mibBuilder.loadTexts:
    phivDDCMPCircuitParametersEntry.setStatus("mandatory")


class _PhivDDCMPCircuitIndex_Type(Integer32):
    """Custom type phivDDCMPCircuitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PhivDDCMPCircuitIndex_Type.__name__ = "Integer32"
_PhivDDCMPCircuitIndex_Object = MibTableColumn
phivDDCMPCircuitIndex = _PhivDDCMPCircuitIndex_Object(
    (1, 3, 6, 1, 2, 1, 18, 7, 1, 1, 1),
    _PhivDDCMPCircuitIndex_Type()
)
phivDDCMPCircuitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivDDCMPCircuitIndex.setStatus("mandatory")
_PhivDDCMPCircuitAdjNodeAddr_Type = PhivAddr
_PhivDDCMPCircuitAdjNodeAddr_Object = MibTableColumn
phivDDCMPCircuitAdjNodeAddr = _PhivDDCMPCircuitAdjNodeAddr_Object(
    (1, 3, 6, 1, 2, 1, 18, 7, 1, 1, 2),
    _PhivDDCMPCircuitAdjNodeAddr_Type()
)
phivDDCMPCircuitAdjNodeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivDDCMPCircuitAdjNodeAddr.setStatus("mandatory")


class _PhivDDCMPCircuitTributary_Type(Integer32):
    """Custom type phivDDCMPCircuitTributary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhivDDCMPCircuitTributary_Type.__name__ = "Integer32"
_PhivDDCMPCircuitTributary_Object = MibTableColumn
phivDDCMPCircuitTributary = _PhivDDCMPCircuitTributary_Object(
    (1, 3, 6, 1, 2, 1, 18, 7, 1, 1, 3),
    _PhivDDCMPCircuitTributary_Type()
)
phivDDCMPCircuitTributary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivDDCMPCircuitTributary.setStatus("mandatory")
_PhivDDCMPCircuitCountTable_Object = MibTable
phivDDCMPCircuitCountTable = _PhivDDCMPCircuitCountTable_Object(
    (1, 3, 6, 1, 2, 1, 18, 7, 2)
)
if mibBuilder.loadTexts:
    phivDDCMPCircuitCountTable.setStatus("mandatory")
_PhivDDCMPCircuitCountEntry_Object = MibTableRow
phivDDCMPCircuitCountEntry = _PhivDDCMPCircuitCountEntry_Object(
    (1, 3, 6, 1, 2, 1, 18, 7, 2, 1)
)
phivDDCMPCircuitCountEntry.setIndexNames(
    (0, "DECNET-PHIV-MIB", "phivCircuitIndex"),
)
if mibBuilder.loadTexts:
    phivDDCMPCircuitCountEntry.setStatus("mandatory")


class _PhivDDCMPCircuitErrorsInbd_Type(PhivCounter):
    """Custom type phivDDCMPCircuitErrorsInbd based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhivDDCMPCircuitErrorsInbd_Type.__name__ = "PhivCounter"
_PhivDDCMPCircuitErrorsInbd_Object = MibTableColumn
phivDDCMPCircuitErrorsInbd = _PhivDDCMPCircuitErrorsInbd_Object(
    (1, 3, 6, 1, 2, 1, 18, 7, 2, 1, 1),
    _PhivDDCMPCircuitErrorsInbd_Type()
)
phivDDCMPCircuitErrorsInbd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivDDCMPCircuitErrorsInbd.setStatus("mandatory")


class _PhivDDCMPCircuitErrorsOutbd_Type(PhivCounter):
    """Custom type phivDDCMPCircuitErrorsOutbd based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhivDDCMPCircuitErrorsOutbd_Type.__name__ = "PhivCounter"
_PhivDDCMPCircuitErrorsOutbd_Object = MibTableColumn
phivDDCMPCircuitErrorsOutbd = _PhivDDCMPCircuitErrorsOutbd_Object(
    (1, 3, 6, 1, 2, 1, 18, 7, 2, 1, 2),
    _PhivDDCMPCircuitErrorsOutbd_Type()
)
phivDDCMPCircuitErrorsOutbd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivDDCMPCircuitErrorsOutbd.setStatus("mandatory")


class _PhivDDCMPCircuitRmteReplyTimeouts_Type(PhivCounter):
    """Custom type phivDDCMPCircuitRmteReplyTimeouts based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhivDDCMPCircuitRmteReplyTimeouts_Type.__name__ = "PhivCounter"
_PhivDDCMPCircuitRmteReplyTimeouts_Object = MibTableColumn
phivDDCMPCircuitRmteReplyTimeouts = _PhivDDCMPCircuitRmteReplyTimeouts_Object(
    (1, 3, 6, 1, 2, 1, 18, 7, 2, 1, 3),
    _PhivDDCMPCircuitRmteReplyTimeouts_Type()
)
phivDDCMPCircuitRmteReplyTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivDDCMPCircuitRmteReplyTimeouts.setStatus("mandatory")


class _PhivDDCMPCircuitLocalReplyTimeouts_Type(PhivCounter):
    """Custom type phivDDCMPCircuitLocalReplyTimeouts based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhivDDCMPCircuitLocalReplyTimeouts_Type.__name__ = "PhivCounter"
_PhivDDCMPCircuitLocalReplyTimeouts_Object = MibTableColumn
phivDDCMPCircuitLocalReplyTimeouts = _PhivDDCMPCircuitLocalReplyTimeouts_Object(
    (1, 3, 6, 1, 2, 1, 18, 7, 2, 1, 4),
    _PhivDDCMPCircuitLocalReplyTimeouts_Type()
)
phivDDCMPCircuitLocalReplyTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivDDCMPCircuitLocalReplyTimeouts.setStatus("mandatory")


class _PhivDDCMPCircuitRmteBuffErrors_Type(PhivCounter):
    """Custom type phivDDCMPCircuitRmteBuffErrors based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhivDDCMPCircuitRmteBuffErrors_Type.__name__ = "PhivCounter"
_PhivDDCMPCircuitRmteBuffErrors_Object = MibTableColumn
phivDDCMPCircuitRmteBuffErrors = _PhivDDCMPCircuitRmteBuffErrors_Object(
    (1, 3, 6, 1, 2, 1, 18, 7, 2, 1, 5),
    _PhivDDCMPCircuitRmteBuffErrors_Type()
)
phivDDCMPCircuitRmteBuffErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivDDCMPCircuitRmteBuffErrors.setStatus("mandatory")


class _PhivDDCMPCircuitLocalBuffErrors_Type(PhivCounter):
    """Custom type phivDDCMPCircuitLocalBuffErrors based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhivDDCMPCircuitLocalBuffErrors_Type.__name__ = "PhivCounter"
_PhivDDCMPCircuitLocalBuffErrors_Object = MibTableColumn
phivDDCMPCircuitLocalBuffErrors = _PhivDDCMPCircuitLocalBuffErrors_Object(
    (1, 3, 6, 1, 2, 1, 18, 7, 2, 1, 6),
    _PhivDDCMPCircuitLocalBuffErrors_Type()
)
phivDDCMPCircuitLocalBuffErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivDDCMPCircuitLocalBuffErrors.setStatus("mandatory")


class _PhivDDCMPCircuitSelectIntervalsElap_Type(PhivCounter):
    """Custom type phivDDCMPCircuitSelectIntervalsElap based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PhivDDCMPCircuitSelectIntervalsElap_Type.__name__ = "PhivCounter"
_PhivDDCMPCircuitSelectIntervalsElap_Object = MibTableColumn
phivDDCMPCircuitSelectIntervalsElap = _PhivDDCMPCircuitSelectIntervalsElap_Object(
    (1, 3, 6, 1, 2, 1, 18, 7, 2, 1, 7),
    _PhivDDCMPCircuitSelectIntervalsElap_Type()
)
phivDDCMPCircuitSelectIntervalsElap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivDDCMPCircuitSelectIntervalsElap.setStatus("mandatory")


class _PhivDDCMPCircuitSelectTimeouts_Type(Integer32):
    """Custom type phivDDCMPCircuitSelectTimeouts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhivDDCMPCircuitSelectTimeouts_Type.__name__ = "Integer32"
_PhivDDCMPCircuitSelectTimeouts_Object = MibTableColumn
phivDDCMPCircuitSelectTimeouts = _PhivDDCMPCircuitSelectTimeouts_Object(
    (1, 3, 6, 1, 2, 1, 18, 7, 2, 1, 8),
    _PhivDDCMPCircuitSelectTimeouts_Type()
)
phivDDCMPCircuitSelectTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivDDCMPCircuitSelectTimeouts.setStatus("mandatory")
_PhivDDCMPLineCountTable_Object = MibTable
phivDDCMPLineCountTable = _PhivDDCMPLineCountTable_Object(
    (1, 3, 6, 1, 2, 1, 18, 7, 3)
)
if mibBuilder.loadTexts:
    phivDDCMPLineCountTable.setStatus("mandatory")
_PhivDDCMPLineCountEntry_Object = MibTableRow
phivDDCMPLineCountEntry = _PhivDDCMPLineCountEntry_Object(
    (1, 3, 6, 1, 2, 1, 18, 7, 3, 1)
)
phivDDCMPLineCountEntry.setIndexNames(
    (0, "DECNET-PHIV-MIB", "phivDDCMPLineCountIndex"),
)
if mibBuilder.loadTexts:
    phivDDCMPLineCountEntry.setStatus("mandatory")
_PhivDDCMPLineCountIndex_Type = InterfaceIndex
_PhivDDCMPLineCountIndex_Object = MibTableColumn
phivDDCMPLineCountIndex = _PhivDDCMPLineCountIndex_Object(
    (1, 3, 6, 1, 2, 1, 18, 7, 3, 1, 1),
    _PhivDDCMPLineCountIndex_Type()
)
phivDDCMPLineCountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivDDCMPLineCountIndex.setStatus("mandatory")


class _PhivDDCMPLineCountDataErrsIn_Type(PhivCounter):
    """Custom type phivDDCMPLineCountDataErrsIn based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhivDDCMPLineCountDataErrsIn_Type.__name__ = "PhivCounter"
_PhivDDCMPLineCountDataErrsIn_Object = MibTableColumn
phivDDCMPLineCountDataErrsIn = _PhivDDCMPLineCountDataErrsIn_Object(
    (1, 3, 6, 1, 2, 1, 18, 7, 3, 1, 2),
    _PhivDDCMPLineCountDataErrsIn_Type()
)
phivDDCMPLineCountDataErrsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivDDCMPLineCountDataErrsIn.setStatus("mandatory")


class _PhivDDCMPLineCountRmteStationErrs_Type(PhivCounter):
    """Custom type phivDDCMPLineCountRmteStationErrs based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhivDDCMPLineCountRmteStationErrs_Type.__name__ = "PhivCounter"
_PhivDDCMPLineCountRmteStationErrs_Object = MibTableColumn
phivDDCMPLineCountRmteStationErrs = _PhivDDCMPLineCountRmteStationErrs_Object(
    (1, 3, 6, 1, 2, 1, 18, 7, 3, 1, 3),
    _PhivDDCMPLineCountRmteStationErrs_Type()
)
phivDDCMPLineCountRmteStationErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivDDCMPLineCountRmteStationErrs.setStatus("mandatory")


class _PhivDDCMPLineCountLocalStationErrs_Type(PhivCounter):
    """Custom type phivDDCMPLineCountLocalStationErrs based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhivDDCMPLineCountLocalStationErrs_Type.__name__ = "PhivCounter"
_PhivDDCMPLineCountLocalStationErrs_Object = MibTableColumn
phivDDCMPLineCountLocalStationErrs = _PhivDDCMPLineCountLocalStationErrs_Object(
    (1, 3, 6, 1, 2, 1, 18, 7, 3, 1, 4),
    _PhivDDCMPLineCountLocalStationErrs_Type()
)
phivDDCMPLineCountLocalStationErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivDDCMPLineCountLocalStationErrs.setStatus("mandatory")
_Control_ObjectIdentity = ObjectIdentity
control = _Control_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 18, 8)
)


class _PhivControlSchedTimer_Type(Integer32):
    """Custom type phivControlSchedTimer based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 65535),
    )


_PhivControlSchedTimer_Type.__name__ = "Integer32"
_PhivControlSchedTimer_Object = MibScalar
phivControlSchedTimer = _PhivControlSchedTimer_Object(
    (1, 3, 6, 1, 2, 1, 18, 8, 1),
    _PhivControlSchedTimer_Type()
)
phivControlSchedTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivControlSchedTimer.setStatus("mandatory")


class _PhivControlDeadTimer_Type(Integer32):
    """Custom type phivControlDeadTimer based on Integer32"""
    defaultValue = 10000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PhivControlDeadTimer_Type.__name__ = "Integer32"
_PhivControlDeadTimer_Object = MibScalar
phivControlDeadTimer = _PhivControlDeadTimer_Object(
    (1, 3, 6, 1, 2, 1, 18, 8, 2),
    _PhivControlDeadTimer_Type()
)
phivControlDeadTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivControlDeadTimer.setStatus("mandatory")


class _PhivControlDelayTimer_Type(Integer32):
    """Custom type phivControlDelayTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PhivControlDelayTimer_Type.__name__ = "Integer32"
_PhivControlDelayTimer_Object = MibScalar
phivControlDelayTimer = _PhivControlDelayTimer_Object(
    (1, 3, 6, 1, 2, 1, 18, 8, 3),
    _PhivControlDelayTimer_Type()
)
phivControlDelayTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivControlDelayTimer.setStatus("mandatory")


class _PhivControlStreamTimer_Type(Integer32):
    """Custom type phivControlStreamTimer based on Integer32"""
    defaultValue = 6000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PhivControlStreamTimer_Type.__name__ = "Integer32"
_PhivControlStreamTimer_Object = MibScalar
phivControlStreamTimer = _PhivControlStreamTimer_Object(
    (1, 3, 6, 1, 2, 1, 18, 8, 4),
    _PhivControlStreamTimer_Type()
)
phivControlStreamTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivControlStreamTimer.setStatus("mandatory")
_PhivControlParametersTable_Object = MibTable
phivControlParametersTable = _PhivControlParametersTable_Object(
    (1, 3, 6, 1, 2, 1, 18, 8, 5)
)
if mibBuilder.loadTexts:
    phivControlParametersTable.setStatus("mandatory")
_PhivControlParametersEntry_Object = MibTableRow
phivControlParametersEntry = _PhivControlParametersEntry_Object(
    (1, 3, 6, 1, 2, 1, 18, 8, 5, 1)
)
phivControlParametersEntry.setIndexNames(
    (0, "DECNET-PHIV-MIB", "phivControlCircuitIndex"),
)
if mibBuilder.loadTexts:
    phivControlParametersEntry.setStatus("mandatory")


class _PhivControlCircuitIndex_Type(Integer32):
    """Custom type phivControlCircuitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PhivControlCircuitIndex_Type.__name__ = "Integer32"
_PhivControlCircuitIndex_Object = MibTableColumn
phivControlCircuitIndex = _PhivControlCircuitIndex_Object(
    (1, 3, 6, 1, 2, 1, 18, 8, 5, 1, 1),
    _PhivControlCircuitIndex_Type()
)
phivControlCircuitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivControlCircuitIndex.setStatus("mandatory")


class _PhivControlBabbleTimer_Type(Integer32):
    """Custom type phivControlBabbleTimer based on Integer32"""
    defaultValue = 6000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PhivControlBabbleTimer_Type.__name__ = "Integer32"
_PhivControlBabbleTimer_Object = MibTableColumn
phivControlBabbleTimer = _PhivControlBabbleTimer_Object(
    (1, 3, 6, 1, 2, 1, 18, 8, 5, 1, 2),
    _PhivControlBabbleTimer_Type()
)
phivControlBabbleTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivControlBabbleTimer.setStatus("mandatory")


class _PhivControlMaxBuffs_Type(Integer32):
    """Custom type phivControlMaxBuffs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_PhivControlMaxBuffs_Type.__name__ = "Integer32"
_PhivControlMaxBuffs_Object = MibTableColumn
phivControlMaxBuffs = _PhivControlMaxBuffs_Object(
    (1, 3, 6, 1, 2, 1, 18, 8, 5, 1, 3),
    _PhivControlMaxBuffs_Type()
)
phivControlMaxBuffs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivControlMaxBuffs.setStatus("mandatory")


class _PhivControlMaxTransmits_Type(Integer32):
    """Custom type phivControlMaxTransmits based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PhivControlMaxTransmits_Type.__name__ = "Integer32"
_PhivControlMaxTransmits_Object = MibTableColumn
phivControlMaxTransmits = _PhivControlMaxTransmits_Object(
    (1, 3, 6, 1, 2, 1, 18, 8, 5, 1, 4),
    _PhivControlMaxTransmits_Type()
)
phivControlMaxTransmits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivControlMaxTransmits.setStatus("mandatory")


class _PhivControlDyingBase_Type(Integer32):
    """Custom type phivControlDyingBase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhivControlDyingBase_Type.__name__ = "Integer32"
_PhivControlDyingBase_Object = MibTableColumn
phivControlDyingBase = _PhivControlDyingBase_Object(
    (1, 3, 6, 1, 2, 1, 18, 8, 5, 1, 5),
    _PhivControlDyingBase_Type()
)
phivControlDyingBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivControlDyingBase.setStatus("mandatory")


class _PhivControlDyingIncrement_Type(Integer32):
    """Custom type phivControlDyingIncrement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhivControlDyingIncrement_Type.__name__ = "Integer32"
_PhivControlDyingIncrement_Object = MibTableColumn
phivControlDyingIncrement = _PhivControlDyingIncrement_Object(
    (1, 3, 6, 1, 2, 1, 18, 8, 5, 1, 6),
    _PhivControlDyingIncrement_Type()
)
phivControlDyingIncrement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivControlDyingIncrement.setStatus("mandatory")


class _PhivControlDeadThreshold_Type(Integer32):
    """Custom type phivControlDeadThreshold based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhivControlDeadThreshold_Type.__name__ = "Integer32"
_PhivControlDeadThreshold_Object = MibTableColumn
phivControlDeadThreshold = _PhivControlDeadThreshold_Object(
    (1, 3, 6, 1, 2, 1, 18, 8, 5, 1, 7),
    _PhivControlDeadThreshold_Type()
)
phivControlDeadThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivControlDeadThreshold.setStatus("mandatory")


class _PhivControlDyingThreshold_Type(Integer32):
    """Custom type phivControlDyingThreshold based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhivControlDyingThreshold_Type.__name__ = "Integer32"
_PhivControlDyingThreshold_Object = MibTableColumn
phivControlDyingThreshold = _PhivControlDyingThreshold_Object(
    (1, 3, 6, 1, 2, 1, 18, 8, 5, 1, 8),
    _PhivControlDyingThreshold_Type()
)
phivControlDyingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivControlDyingThreshold.setStatus("mandatory")


class _PhivControlInactTreshold_Type(Integer32):
    """Custom type phivControlInactTreshold based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhivControlInactTreshold_Type.__name__ = "Integer32"
_PhivControlInactTreshold_Object = MibTableColumn
phivControlInactTreshold = _PhivControlInactTreshold_Object(
    (1, 3, 6, 1, 2, 1, 18, 8, 5, 1, 9),
    _PhivControlInactTreshold_Type()
)
phivControlInactTreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivControlInactTreshold.setStatus("mandatory")


class _PhivControlPollingState_Type(Integer32):
    """Custom type phivControlPollingState based on Integer32"""
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
        *(("active", 2),
          ("automatic", 1),
          ("dead", 5),
          ("dying", 4),
          ("inactive", 3))
    )


_PhivControlPollingState_Type.__name__ = "Integer32"
_PhivControlPollingState_Object = MibTableColumn
phivControlPollingState = _PhivControlPollingState_Object(
    (1, 3, 6, 1, 2, 1, 18, 8, 5, 1, 10),
    _PhivControlPollingState_Type()
)
phivControlPollingState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivControlPollingState.setStatus("mandatory")


class _PhivControlPollingSubState_Type(Integer32):
    """Custom type phivControlPollingSubState based on Integer32"""
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
          ("dead", 4),
          ("dying", 3),
          ("inactive", 2))
    )


_PhivControlPollingSubState_Type.__name__ = "Integer32"
_PhivControlPollingSubState_Object = MibTableColumn
phivControlPollingSubState = _PhivControlPollingSubState_Object(
    (1, 3, 6, 1, 2, 1, 18, 8, 5, 1, 11),
    _PhivControlPollingSubState_Type()
)
phivControlPollingSubState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivControlPollingSubState.setStatus("mandatory")


class _PhivControlTransTimer_Type(Integer32):
    """Custom type phivControlTransTimer based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PhivControlTransTimer_Type.__name__ = "Integer32"
_PhivControlTransTimer_Object = MibTableColumn
phivControlTransTimer = _PhivControlTransTimer_Object(
    (1, 3, 6, 1, 2, 1, 18, 8, 5, 1, 12),
    _PhivControlTransTimer_Type()
)
phivControlTransTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivControlTransTimer.setStatus("mandatory")
_Ethernet_ObjectIdentity = ObjectIdentity
ethernet = _Ethernet_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 18, 9)
)
_PhivEthLinkParametersTable_Object = MibTable
phivEthLinkParametersTable = _PhivEthLinkParametersTable_Object(
    (1, 3, 6, 1, 2, 1, 18, 9, 1)
)
if mibBuilder.loadTexts:
    phivEthLinkParametersTable.setStatus("mandatory")
_PhivEthLinkParametersEntry_Object = MibTableRow
phivEthLinkParametersEntry = _PhivEthLinkParametersEntry_Object(
    (1, 3, 6, 1, 2, 1, 18, 9, 1, 1)
)
phivEthLinkParametersEntry.setIndexNames(
    (0, "DECNET-PHIV-MIB", "phivEthLinkIndex"),
)
if mibBuilder.loadTexts:
    phivEthLinkParametersEntry.setStatus("mandatory")


class _PhivEthLinkIndex_Type(Integer32):
    """Custom type phivEthLinkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PhivEthLinkIndex_Type.__name__ = "Integer32"
_PhivEthLinkIndex_Object = MibTableColumn
phivEthLinkIndex = _PhivEthLinkIndex_Object(
    (1, 3, 6, 1, 2, 1, 18, 9, 1, 1, 1),
    _PhivEthLinkIndex_Type()
)
phivEthLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivEthLinkIndex.setStatus("mandatory")
_PhivEthDesigRouterNodeAddr_Type = PhivAddr
_PhivEthDesigRouterNodeAddr_Object = MibTableColumn
phivEthDesigRouterNodeAddr = _PhivEthDesigRouterNodeAddr_Object(
    (1, 3, 6, 1, 2, 1, 18, 9, 1, 1, 2),
    _PhivEthDesigRouterNodeAddr_Type()
)
phivEthDesigRouterNodeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivEthDesigRouterNodeAddr.setStatus("mandatory")


class _PhivEthMaxRouters_Type(Integer32):
    """Custom type phivEthMaxRouters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhivEthMaxRouters_Type.__name__ = "Integer32"
_PhivEthMaxRouters_Object = MibTableColumn
phivEthMaxRouters = _PhivEthMaxRouters_Object(
    (1, 3, 6, 1, 2, 1, 18, 9, 1, 1, 3),
    _PhivEthMaxRouters_Type()
)
phivEthMaxRouters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivEthMaxRouters.setStatus("mandatory")


class _PhivEthRouterPri_Type(Integer32):
    """Custom type phivEthRouterPri based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_PhivEthRouterPri_Type.__name__ = "Integer32"
_PhivEthRouterPri_Object = MibTableColumn
phivEthRouterPri = _PhivEthRouterPri_Object(
    (1, 3, 6, 1, 2, 1, 18, 9, 1, 1, 4),
    _PhivEthRouterPri_Type()
)
phivEthRouterPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivEthRouterPri.setStatus("mandatory")


class _PhivEthHardwareAddr_Type(OctetString):
    """Custom type phivEthHardwareAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_PhivEthHardwareAddr_Type.__name__ = "OctetString"
_PhivEthHardwareAddr_Object = MibTableColumn
phivEthHardwareAddr = _PhivEthHardwareAddr_Object(
    (1, 3, 6, 1, 2, 1, 18, 9, 1, 1, 5),
    _PhivEthHardwareAddr_Type()
)
phivEthHardwareAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivEthHardwareAddr.setStatus("mandatory")
_Counters_ObjectIdentity = ObjectIdentity
counters = _Counters_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 18, 10)
)
_PhivCountersCountTable_Object = MibTable
phivCountersCountTable = _PhivCountersCountTable_Object(
    (1, 3, 6, 1, 2, 1, 18, 10, 1)
)
if mibBuilder.loadTexts:
    phivCountersCountTable.setStatus("mandatory")
_PhivCountersCountEntry_Object = MibTableRow
phivCountersCountEntry = _PhivCountersCountEntry_Object(
    (1, 3, 6, 1, 2, 1, 18, 10, 1, 1)
)
phivCountersCountEntry.setIndexNames(
    (0, "DECNET-PHIV-MIB", "phivCountersIndex"),
)
if mibBuilder.loadTexts:
    phivCountersCountEntry.setStatus("mandatory")
_PhivCountersIndex_Type = InterfaceIndex
_PhivCountersIndex_Object = MibTableColumn
phivCountersIndex = _PhivCountersIndex_Object(
    (1, 3, 6, 1, 2, 1, 18, 10, 1, 1, 1),
    _PhivCountersIndex_Type()
)
phivCountersIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCountersIndex.setStatus("mandatory")


class _PhivCountersCountBytesRecd_Type(PhivCounter):
    """Custom type phivCountersCountBytesRecd based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PhivCountersCountBytesRecd_Type.__name__ = "PhivCounter"
_PhivCountersCountBytesRecd_Object = MibTableColumn
phivCountersCountBytesRecd = _PhivCountersCountBytesRecd_Object(
    (1, 3, 6, 1, 2, 1, 18, 10, 1, 1, 2),
    _PhivCountersCountBytesRecd_Type()
)
phivCountersCountBytesRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCountersCountBytesRecd.setStatus("mandatory")


class _PhivCountersCountBytesSent_Type(PhivCounter):
    """Custom type phivCountersCountBytesSent based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PhivCountersCountBytesSent_Type.__name__ = "PhivCounter"
_PhivCountersCountBytesSent_Object = MibTableColumn
phivCountersCountBytesSent = _PhivCountersCountBytesSent_Object(
    (1, 3, 6, 1, 2, 1, 18, 10, 1, 1, 3),
    _PhivCountersCountBytesSent_Type()
)
phivCountersCountBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCountersCountBytesSent.setStatus("mandatory")


class _PhivCountersCountDataBlocksRecd_Type(PhivCounter):
    """Custom type phivCountersCountDataBlocksRecd based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PhivCountersCountDataBlocksRecd_Type.__name__ = "PhivCounter"
_PhivCountersCountDataBlocksRecd_Object = MibTableColumn
phivCountersCountDataBlocksRecd = _PhivCountersCountDataBlocksRecd_Object(
    (1, 3, 6, 1, 2, 1, 18, 10, 1, 1, 4),
    _PhivCountersCountDataBlocksRecd_Type()
)
phivCountersCountDataBlocksRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCountersCountDataBlocksRecd.setStatus("obsolete")


class _PhivCountersCountDataBlocksSent_Type(PhivCounter):
    """Custom type phivCountersCountDataBlocksSent based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PhivCountersCountDataBlocksSent_Type.__name__ = "PhivCounter"
_PhivCountersCountDataBlocksSent_Object = MibTableColumn
phivCountersCountDataBlocksSent = _PhivCountersCountDataBlocksSent_Object(
    (1, 3, 6, 1, 2, 1, 18, 10, 1, 1, 5),
    _PhivCountersCountDataBlocksSent_Type()
)
phivCountersCountDataBlocksSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCountersCountDataBlocksSent.setStatus("obsolete")


class _PhivCountersCountEthUsrBuffUnav_Type(PhivCounter):
    """Custom type phivCountersCountEthUsrBuffUnav based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PhivCountersCountEthUsrBuffUnav_Type.__name__ = "PhivCounter"
_PhivCountersCountEthUsrBuffUnav_Object = MibTableColumn
phivCountersCountEthUsrBuffUnav = _PhivCountersCountEthUsrBuffUnav_Object(
    (1, 3, 6, 1, 2, 1, 18, 10, 1, 1, 6),
    _PhivCountersCountEthUsrBuffUnav_Type()
)
phivCountersCountEthUsrBuffUnav.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCountersCountEthUsrBuffUnav.setStatus("mandatory")


class _PhivCountersCountMcastBytesRecd_Type(PhivCounter):
    """Custom type phivCountersCountMcastBytesRecd based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PhivCountersCountMcastBytesRecd_Type.__name__ = "PhivCounter"
_PhivCountersCountMcastBytesRecd_Object = MibTableColumn
phivCountersCountMcastBytesRecd = _PhivCountersCountMcastBytesRecd_Object(
    (1, 3, 6, 1, 2, 1, 18, 10, 1, 1, 7),
    _PhivCountersCountMcastBytesRecd_Type()
)
phivCountersCountMcastBytesRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCountersCountMcastBytesRecd.setStatus("mandatory")


class _PhivCountersCountDataBlksRecd_Type(PhivCounter):
    """Custom type phivCountersCountDataBlksRecd based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PhivCountersCountDataBlksRecd_Type.__name__ = "PhivCounter"
_PhivCountersCountDataBlksRecd_Object = MibTableColumn
phivCountersCountDataBlksRecd = _PhivCountersCountDataBlksRecd_Object(
    (1, 3, 6, 1, 2, 1, 18, 10, 1, 1, 8),
    _PhivCountersCountDataBlksRecd_Type()
)
phivCountersCountDataBlksRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCountersCountDataBlksRecd.setStatus("mandatory")


class _PhivCountersCountDataBlksSent_Type(PhivCounter):
    """Custom type phivCountersCountDataBlksSent based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PhivCountersCountDataBlksSent_Type.__name__ = "PhivCounter"
_PhivCountersCountDataBlksSent_Object = MibTableColumn
phivCountersCountDataBlksSent = _PhivCountersCountDataBlksSent_Object(
    (1, 3, 6, 1, 2, 1, 18, 10, 1, 1, 9),
    _PhivCountersCountDataBlksSent_Type()
)
phivCountersCountDataBlksSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCountersCountDataBlksSent.setStatus("mandatory")


class _PhivCountersCountMcastBlksRecd_Type(PhivCounter):
    """Custom type phivCountersCountMcastBlksRecd based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PhivCountersCountMcastBlksRecd_Type.__name__ = "PhivCounter"
_PhivCountersCountMcastBlksRecd_Object = MibTableColumn
phivCountersCountMcastBlksRecd = _PhivCountersCountMcastBlksRecd_Object(
    (1, 3, 6, 1, 2, 1, 18, 10, 1, 1, 10),
    _PhivCountersCountMcastBlksRecd_Type()
)
phivCountersCountMcastBlksRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCountersCountMcastBlksRecd.setStatus("mandatory")


class _PhivCountersCountBlksSentDef_Type(PhivCounter):
    """Custom type phivCountersCountBlksSentDef based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PhivCountersCountBlksSentDef_Type.__name__ = "PhivCounter"
_PhivCountersCountBlksSentDef_Object = MibTableColumn
phivCountersCountBlksSentDef = _PhivCountersCountBlksSentDef_Object(
    (1, 3, 6, 1, 2, 1, 18, 10, 1, 1, 11),
    _PhivCountersCountBlksSentDef_Type()
)
phivCountersCountBlksSentDef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCountersCountBlksSentDef.setStatus("mandatory")


class _PhivCountersCountBlksSentSingleCol_Type(PhivCounter):
    """Custom type phivCountersCountBlksSentSingleCol based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PhivCountersCountBlksSentSingleCol_Type.__name__ = "PhivCounter"
_PhivCountersCountBlksSentSingleCol_Object = MibTableColumn
phivCountersCountBlksSentSingleCol = _PhivCountersCountBlksSentSingleCol_Object(
    (1, 3, 6, 1, 2, 1, 18, 10, 1, 1, 12),
    _PhivCountersCountBlksSentSingleCol_Type()
)
phivCountersCountBlksSentSingleCol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCountersCountBlksSentSingleCol.setStatus("mandatory")


class _PhivCountersCountBlksSentMultCol_Type(PhivCounter):
    """Custom type phivCountersCountBlksSentMultCol based on PhivCounter"""
    subtypeSpec = PhivCounter.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PhivCountersCountBlksSentMultCol_Type.__name__ = "PhivCounter"
_PhivCountersCountBlksSentMultCol_Object = MibTableColumn
phivCountersCountBlksSentMultCol = _PhivCountersCountBlksSentMultCol_Object(
    (1, 3, 6, 1, 2, 1, 18, 10, 1, 1, 13),
    _PhivCountersCountBlksSentMultCol_Type()
)
phivCountersCountBlksSentMultCol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCountersCountBlksSentMultCol.setStatus("mandatory")


class _PhivCountersCountSendFailure_Type(Integer32):
    """Custom type phivCountersCountSendFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PhivCountersCountSendFailure_Type.__name__ = "Integer32"
_PhivCountersCountSendFailure_Object = MibTableColumn
phivCountersCountSendFailure = _PhivCountersCountSendFailure_Object(
    (1, 3, 6, 1, 2, 1, 18, 10, 1, 1, 14),
    _PhivCountersCountSendFailure_Type()
)
phivCountersCountSendFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCountersCountSendFailure.setStatus("mandatory")


class _PhivCountersCountCollDetectFailure_Type(Integer32):
    """Custom type phivCountersCountCollDetectFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PhivCountersCountCollDetectFailure_Type.__name__ = "Integer32"
_PhivCountersCountCollDetectFailure_Object = MibTableColumn
phivCountersCountCollDetectFailure = _PhivCountersCountCollDetectFailure_Object(
    (1, 3, 6, 1, 2, 1, 18, 10, 1, 1, 15),
    _PhivCountersCountCollDetectFailure_Type()
)
phivCountersCountCollDetectFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCountersCountCollDetectFailure.setStatus("mandatory")


class _PhivCountersCountReceiveFailure_Type(Integer32):
    """Custom type phivCountersCountReceiveFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PhivCountersCountReceiveFailure_Type.__name__ = "Integer32"
_PhivCountersCountReceiveFailure_Object = MibTableColumn
phivCountersCountReceiveFailure = _PhivCountersCountReceiveFailure_Object(
    (1, 3, 6, 1, 2, 1, 18, 10, 1, 1, 16),
    _PhivCountersCountReceiveFailure_Type()
)
phivCountersCountReceiveFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCountersCountReceiveFailure.setStatus("mandatory")


class _PhivCountersCountUnrecFrameDest_Type(Integer32):
    """Custom type phivCountersCountUnrecFrameDest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PhivCountersCountUnrecFrameDest_Type.__name__ = "Integer32"
_PhivCountersCountUnrecFrameDest_Object = MibTableColumn
phivCountersCountUnrecFrameDest = _PhivCountersCountUnrecFrameDest_Object(
    (1, 3, 6, 1, 2, 1, 18, 10, 1, 1, 17),
    _PhivCountersCountUnrecFrameDest_Type()
)
phivCountersCountUnrecFrameDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCountersCountUnrecFrameDest.setStatus("mandatory")


class _PhivCountersCountDataOver_Type(Integer32):
    """Custom type phivCountersCountDataOver based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PhivCountersCountDataOver_Type.__name__ = "Integer32"
_PhivCountersCountDataOver_Object = MibTableColumn
phivCountersCountDataOver = _PhivCountersCountDataOver_Object(
    (1, 3, 6, 1, 2, 1, 18, 10, 1, 1, 18),
    _PhivCountersCountDataOver_Type()
)
phivCountersCountDataOver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCountersCountDataOver.setStatus("mandatory")


class _PhivCountersCountSysBuffUnav_Type(Integer32):
    """Custom type phivCountersCountSysBuffUnav based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PhivCountersCountSysBuffUnav_Type.__name__ = "Integer32"
_PhivCountersCountSysBuffUnav_Object = MibTableColumn
phivCountersCountSysBuffUnav = _PhivCountersCountSysBuffUnav_Object(
    (1, 3, 6, 1, 2, 1, 18, 10, 1, 1, 19),
    _PhivCountersCountSysBuffUnav_Type()
)
phivCountersCountSysBuffUnav.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCountersCountSysBuffUnav.setStatus("mandatory")


class _PhivCountersCountUsrBuffUnav_Type(Integer32):
    """Custom type phivCountersCountUsrBuffUnav based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PhivCountersCountUsrBuffUnav_Type.__name__ = "Integer32"
_PhivCountersCountUsrBuffUnav_Object = MibTableColumn
phivCountersCountUsrBuffUnav = _PhivCountersCountUsrBuffUnav_Object(
    (1, 3, 6, 1, 2, 1, 18, 10, 1, 1, 20),
    _PhivCountersCountUsrBuffUnav_Type()
)
phivCountersCountUsrBuffUnav.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivCountersCountUsrBuffUnav.setStatus("mandatory")
_Adjacency_ObjectIdentity = ObjectIdentity
adjacency = _Adjacency_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 18, 11)
)
_PhivAdjTable_Object = MibTable
phivAdjTable = _PhivAdjTable_Object(
    (1, 3, 6, 1, 2, 1, 18, 11, 1)
)
if mibBuilder.loadTexts:
    phivAdjTable.setStatus("obsolete")
_PhivAdjEntry_Object = MibTableRow
phivAdjEntry = _PhivAdjEntry_Object(
    (1, 3, 6, 1, 2, 1, 18, 11, 1, 1)
)
phivAdjEntry.setIndexNames(
    (0, "DECNET-PHIV-MIB", "phivAdjCircuitIndex"),
)
if mibBuilder.loadTexts:
    phivAdjEntry.setStatus("obsolete")
_PhivAdjCircuitIndex_Type = Integer32
_PhivAdjCircuitIndex_Object = MibTableColumn
phivAdjCircuitIndex = _PhivAdjCircuitIndex_Object(
    (1, 3, 6, 1, 2, 1, 18, 11, 1, 1, 1),
    _PhivAdjCircuitIndex_Type()
)
phivAdjCircuitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivAdjCircuitIndex.setStatus("obsolete")
_PhivAdjNodeAddr_Type = PhivAddr
_PhivAdjNodeAddr_Object = MibTableColumn
phivAdjNodeAddr = _PhivAdjNodeAddr_Object(
    (1, 3, 6, 1, 2, 1, 18, 11, 1, 1, 2),
    _PhivAdjNodeAddr_Type()
)
phivAdjNodeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivAdjNodeAddr.setStatus("obsolete")
_PhivAdjBlockSize_Type = Integer32
_PhivAdjBlockSize_Object = MibTableColumn
phivAdjBlockSize = _PhivAdjBlockSize_Object(
    (1, 3, 6, 1, 2, 1, 18, 11, 1, 1, 3),
    _PhivAdjBlockSize_Type()
)
phivAdjBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivAdjBlockSize.setStatus("obsolete")


class _PhivAdjListenTimer_Type(Integer32):
    """Custom type phivAdjListenTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PhivAdjListenTimer_Type.__name__ = "Integer32"
_PhivAdjListenTimer_Object = MibTableColumn
phivAdjListenTimer = _PhivAdjListenTimer_Object(
    (1, 3, 6, 1, 2, 1, 18, 11, 1, 1, 4),
    _PhivAdjListenTimer_Type()
)
phivAdjListenTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivAdjListenTimer.setStatus("obsolete")


class _PhivAdjCircuitEtherServPhysAddr_Type(OctetString):
    """Custom type phivAdjCircuitEtherServPhysAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_PhivAdjCircuitEtherServPhysAddr_Type.__name__ = "OctetString"
_PhivAdjCircuitEtherServPhysAddr_Object = MibTableColumn
phivAdjCircuitEtherServPhysAddr = _PhivAdjCircuitEtherServPhysAddr_Object(
    (1, 3, 6, 1, 2, 1, 18, 11, 1, 1, 5),
    _PhivAdjCircuitEtherServPhysAddr_Type()
)
phivAdjCircuitEtherServPhysAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivAdjCircuitEtherServPhysAddr.setStatus("obsolete")


class _PhivAdjType_Type(Integer32):
    """Custom type phivAdjType based on Integer32"""
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
        *(("area", 3),
          ("nonrouting-III", 2),
          ("nonrouting-IV", 5),
          ("routing-III", 1),
          ("routing-IV", 4))
    )


_PhivAdjType_Type.__name__ = "Integer32"
_PhivAdjType_Object = MibTableColumn
phivAdjType = _PhivAdjType_Object(
    (1, 3, 6, 1, 2, 1, 18, 11, 1, 1, 6),
    _PhivAdjType_Type()
)
phivAdjType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivAdjType.setStatus("obsolete")


class _PhivAdjState_Type(Integer32):
    """Custom type phivAdjState based on Integer32"""
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
        *(("circuit-rejected", 4),
          ("data-link-start", 5),
          ("halt", 10),
          ("initializing", 1),
          ("off", 9),
          ("routing-layer-complete", 8),
          ("routing-layer-initialize", 6),
          ("routing-layer-verify", 7),
          ("run", 3),
          ("up", 2))
    )


_PhivAdjState_Type.__name__ = "Integer32"
_PhivAdjState_Object = MibTableColumn
phivAdjState = _PhivAdjState_Object(
    (1, 3, 6, 1, 2, 1, 18, 11, 1, 1, 7),
    _PhivAdjState_Type()
)
phivAdjState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivAdjState.setStatus("obsolete")


class _PhivAdjPriority_Type(Integer32):
    """Custom type phivAdjPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhivAdjPriority_Type.__name__ = "Integer32"
_PhivAdjPriority_Object = MibTableColumn
phivAdjPriority = _PhivAdjPriority_Object(
    (1, 3, 6, 1, 2, 1, 18, 11, 1, 1, 8),
    _PhivAdjPriority_Type()
)
phivAdjPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivAdjPriority.setStatus("obsolete")


class _PhivAdjExecListenTimer_Type(Integer32):
    """Custom type phivAdjExecListenTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PhivAdjExecListenTimer_Type.__name__ = "Integer32"
_PhivAdjExecListenTimer_Object = MibTableColumn
phivAdjExecListenTimer = _PhivAdjExecListenTimer_Object(
    (1, 3, 6, 1, 2, 1, 18, 11, 1, 1, 9),
    _PhivAdjExecListenTimer_Type()
)
phivAdjExecListenTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivAdjExecListenTimer.setStatus("obsolete")
_PhivAdjNodeTable_Object = MibTable
phivAdjNodeTable = _PhivAdjNodeTable_Object(
    (1, 3, 6, 1, 2, 1, 18, 11, 2)
)
if mibBuilder.loadTexts:
    phivAdjNodeTable.setStatus("mandatory")
_PhivAdjNodeEntry_Object = MibTableRow
phivAdjNodeEntry = _PhivAdjNodeEntry_Object(
    (1, 3, 6, 1, 2, 1, 18, 11, 2, 1)
)
phivAdjNodeEntry.setIndexNames(
    (0, "DECNET-PHIV-MIB", "phivAdjNodeCircuitIndex"),
    (0, "DECNET-PHIV-MIB", "phivAdjAddr"),
)
if mibBuilder.loadTexts:
    phivAdjNodeEntry.setStatus("mandatory")


class _PhivAdjNodeCircuitIndex_Type(Integer32):
    """Custom type phivAdjNodeCircuitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PhivAdjNodeCircuitIndex_Type.__name__ = "Integer32"
_PhivAdjNodeCircuitIndex_Object = MibTableColumn
phivAdjNodeCircuitIndex = _PhivAdjNodeCircuitIndex_Object(
    (1, 3, 6, 1, 2, 1, 18, 11, 2, 1, 1),
    _PhivAdjNodeCircuitIndex_Type()
)
phivAdjNodeCircuitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivAdjNodeCircuitIndex.setStatus("mandatory")
_PhivAdjAddr_Type = PhivAddr
_PhivAdjAddr_Object = MibTableColumn
phivAdjAddr = _PhivAdjAddr_Object(
    (1, 3, 6, 1, 2, 1, 18, 11, 2, 1, 2),
    _PhivAdjAddr_Type()
)
phivAdjAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivAdjAddr.setStatus("mandatory")
_PhivAdjNodeBlockSize_Type = Integer32
_PhivAdjNodeBlockSize_Object = MibTableColumn
phivAdjNodeBlockSize = _PhivAdjNodeBlockSize_Object(
    (1, 3, 6, 1, 2, 1, 18, 11, 2, 1, 3),
    _PhivAdjNodeBlockSize_Type()
)
phivAdjNodeBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivAdjNodeBlockSize.setStatus("mandatory")


class _PhivAdjNodeListenTimer_Type(Integer32):
    """Custom type phivAdjNodeListenTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PhivAdjNodeListenTimer_Type.__name__ = "Integer32"
_PhivAdjNodeListenTimer_Object = MibTableColumn
phivAdjNodeListenTimer = _PhivAdjNodeListenTimer_Object(
    (1, 3, 6, 1, 2, 1, 18, 11, 2, 1, 4),
    _PhivAdjNodeListenTimer_Type()
)
phivAdjNodeListenTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivAdjNodeListenTimer.setStatus("mandatory")


class _PhivAdjNodeCircuitEtherServPhysAddr_Type(OctetString):
    """Custom type phivAdjNodeCircuitEtherServPhysAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_PhivAdjNodeCircuitEtherServPhysAddr_Type.__name__ = "OctetString"
_PhivAdjNodeCircuitEtherServPhysAddr_Object = MibTableColumn
phivAdjNodeCircuitEtherServPhysAddr = _PhivAdjNodeCircuitEtherServPhysAddr_Object(
    (1, 3, 6, 1, 2, 1, 18, 11, 2, 1, 5),
    _PhivAdjNodeCircuitEtherServPhysAddr_Type()
)
phivAdjNodeCircuitEtherServPhysAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivAdjNodeCircuitEtherServPhysAddr.setStatus("mandatory")


class _PhivAdjNodeType_Type(Integer32):
    """Custom type phivAdjNodeType based on Integer32"""
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
        *(("area", 3),
          ("nonrouting-III", 2),
          ("nonrouting-IV", 5),
          ("routing-III", 1),
          ("routing-IV", 4))
    )


_PhivAdjNodeType_Type.__name__ = "Integer32"
_PhivAdjNodeType_Object = MibTableColumn
phivAdjNodeType = _PhivAdjNodeType_Object(
    (1, 3, 6, 1, 2, 1, 18, 11, 2, 1, 6),
    _PhivAdjNodeType_Type()
)
phivAdjNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivAdjNodeType.setStatus("mandatory")


class _PhivAdjNodeState_Type(Integer32):
    """Custom type phivAdjNodeState based on Integer32"""
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
        *(("circuit-rejected", 4),
          ("data-link-start", 5),
          ("halt", 10),
          ("initializing", 1),
          ("off", 9),
          ("routing-layer-complete", 8),
          ("routing-layer-initialize", 6),
          ("routing-layer-verify", 7),
          ("run", 3),
          ("up", 2))
    )


_PhivAdjNodeState_Type.__name__ = "Integer32"
_PhivAdjNodeState_Object = MibTableColumn
phivAdjNodeState = _PhivAdjNodeState_Object(
    (1, 3, 6, 1, 2, 1, 18, 11, 2, 1, 7),
    _PhivAdjNodeState_Type()
)
phivAdjNodeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivAdjNodeState.setStatus("mandatory")


class _PhivAdjNodePriority_Type(Integer32):
    """Custom type phivAdjNodePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhivAdjNodePriority_Type.__name__ = "Integer32"
_PhivAdjNodePriority_Object = MibTableColumn
phivAdjNodePriority = _PhivAdjNodePriority_Object(
    (1, 3, 6, 1, 2, 1, 18, 11, 2, 1, 8),
    _PhivAdjNodePriority_Type()
)
phivAdjNodePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivAdjNodePriority.setStatus("mandatory")
_Line_ObjectIdentity = ObjectIdentity
line = _Line_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 18, 12)
)
_PhivLineTable_Object = MibTable
phivLineTable = _PhivLineTable_Object(
    (1, 3, 6, 1, 2, 1, 18, 12, 1)
)
if mibBuilder.loadTexts:
    phivLineTable.setStatus("mandatory")
_PhivLineEntry_Object = MibTableRow
phivLineEntry = _PhivLineEntry_Object(
    (1, 3, 6, 1, 2, 1, 18, 12, 1, 1)
)
phivLineEntry.setIndexNames(
    (0, "DECNET-PHIV-MIB", "phivLineIndex"),
)
if mibBuilder.loadTexts:
    phivLineEntry.setStatus("mandatory")
_PhivLineIndex_Type = InterfaceIndex
_PhivLineIndex_Object = MibTableColumn
phivLineIndex = _PhivLineIndex_Object(
    (1, 3, 6, 1, 2, 1, 18, 12, 1, 1, 1),
    _PhivLineIndex_Type()
)
phivLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivLineIndex.setStatus("mandatory")


class _PhivLineName_Type(DisplayString):
    """Custom type phivLineName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PhivLineName_Type.__name__ = "DisplayString"
_PhivLineName_Object = MibTableColumn
phivLineName = _PhivLineName_Object(
    (1, 3, 6, 1, 2, 1, 18, 12, 1, 1, 2),
    _PhivLineName_Type()
)
phivLineName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivLineName.setStatus("mandatory")


class _PhivLineState_Type(Integer32):
    """Custom type phivLineState based on Integer32"""
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
        *(("cleared", 4),
          ("off", 2),
          ("on", 1),
          ("service", 3))
    )


_PhivLineState_Type.__name__ = "Integer32"
_PhivLineState_Object = MibTableColumn
phivLineState = _PhivLineState_Object(
    (1, 3, 6, 1, 2, 1, 18, 12, 1, 1, 3),
    _PhivLineState_Type()
)
phivLineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivLineState.setStatus("mandatory")


class _PhivLineSubstate_Type(Integer32):
    """Custom type phivLineSubstate based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("auto-dumping", 9),
          ("auto-loading", 8),
          ("auto-service", 7),
          ("auto-triggering", 10),
          ("dumping", 5),
          ("failed", 12),
          ("loading", 4),
          ("looping", 3),
          ("reflecting", 2),
          ("running", 13),
          ("starting", 1),
          ("synchronizing", 11),
          ("triggering", 6))
    )


_PhivLineSubstate_Type.__name__ = "Integer32"
_PhivLineSubstate_Object = MibTableColumn
phivLineSubstate = _PhivLineSubstate_Object(
    (1, 3, 6, 1, 2, 1, 18, 12, 1, 1, 4),
    _PhivLineSubstate_Type()
)
phivLineSubstate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivLineSubstate.setStatus("mandatory")


class _PhivLineService_Type(Integer32):
    """Custom type phivLineService based on Integer32"""
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
        *(("looping", 3),
          ("other", 4),
          ("reflecting", 2),
          ("starting", 1))
    )


_PhivLineService_Type.__name__ = "Integer32"
_PhivLineService_Object = MibTableColumn
phivLineService = _PhivLineService_Object(
    (1, 3, 6, 1, 2, 1, 18, 12, 1, 1, 5),
    _PhivLineService_Type()
)
phivLineService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivLineService.setStatus("mandatory")


class _PhivLineDevice_Type(DisplayString):
    """Custom type phivLineDevice based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PhivLineDevice_Type.__name__ = "DisplayString"
_PhivLineDevice_Object = MibTableColumn
phivLineDevice = _PhivLineDevice_Object(
    (1, 3, 6, 1, 2, 1, 18, 12, 1, 1, 6),
    _PhivLineDevice_Type()
)
phivLineDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivLineDevice.setStatus("mandatory")


class _PhivLineReceiveBuffs_Type(Integer32):
    """Custom type phivLineReceiveBuffs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PhivLineReceiveBuffs_Type.__name__ = "Integer32"
_PhivLineReceiveBuffs_Object = MibTableColumn
phivLineReceiveBuffs = _PhivLineReceiveBuffs_Object(
    (1, 3, 6, 1, 2, 1, 18, 12, 1, 1, 7),
    _PhivLineReceiveBuffs_Type()
)
phivLineReceiveBuffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivLineReceiveBuffs.setStatus("mandatory")


class _PhivLineProtocol_Type(Integer32):
    """Custom type phivLineProtocol based on Integer32"""
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
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("ci", 8),
          ("ddcmp-control", 2),
          ("ddcmp-dmc", 5),
          ("ddcmp-point", 1),
          ("ddcmp-tributary", 3),
          ("ethernet", 7),
          ("fddi", 15),
          ("olapb", 6),
          ("other", 14),
          ("qp2", 9),
          ("reserved", 4))
    )


_PhivLineProtocol_Type.__name__ = "Integer32"
_PhivLineProtocol_Object = MibTableColumn
phivLineProtocol = _PhivLineProtocol_Object(
    (1, 3, 6, 1, 2, 1, 18, 12, 1, 1, 8),
    _PhivLineProtocol_Type()
)
phivLineProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivLineProtocol.setStatus("mandatory")


class _PhivLineServiceTimer_Type(Integer32):
    """Custom type phivLineServiceTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PhivLineServiceTimer_Type.__name__ = "Integer32"
_PhivLineServiceTimer_Object = MibTableColumn
phivLineServiceTimer = _PhivLineServiceTimer_Object(
    (1, 3, 6, 1, 2, 1, 18, 12, 1, 1, 9),
    _PhivLineServiceTimer_Type()
)
phivLineServiceTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivLineServiceTimer.setStatus("mandatory")


class _PhivLineMaxBlock_Type(Integer32):
    """Custom type phivLineMaxBlock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PhivLineMaxBlock_Type.__name__ = "Integer32"
_PhivLineMaxBlock_Object = MibTableColumn
phivLineMaxBlock = _PhivLineMaxBlock_Object(
    (1, 3, 6, 1, 2, 1, 18, 12, 1, 1, 10),
    _PhivLineMaxBlock_Type()
)
phivLineMaxBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivLineMaxBlock.setStatus("mandatory")
_NonBroadcastLine_ObjectIdentity = ObjectIdentity
nonBroadcastLine = _NonBroadcastLine_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 18, 14)
)
_PhivNonBroadcastTable_Object = MibTable
phivNonBroadcastTable = _PhivNonBroadcastTable_Object(
    (1, 3, 6, 1, 2, 1, 18, 14, 1)
)
if mibBuilder.loadTexts:
    phivNonBroadcastTable.setStatus("mandatory")
_PhivNonBroadcastEntry_Object = MibTableRow
phivNonBroadcastEntry = _PhivNonBroadcastEntry_Object(
    (1, 3, 6, 1, 2, 1, 18, 14, 1, 1)
)
phivNonBroadcastEntry.setIndexNames(
    (0, "DECNET-PHIV-MIB", "phivNonBroadcastIndex"),
)
if mibBuilder.loadTexts:
    phivNonBroadcastEntry.setStatus("mandatory")
_PhivNonBroadcastIndex_Type = InterfaceIndex
_PhivNonBroadcastIndex_Object = MibTableColumn
phivNonBroadcastIndex = _PhivNonBroadcastIndex_Object(
    (1, 3, 6, 1, 2, 1, 18, 14, 1, 1, 1),
    _PhivNonBroadcastIndex_Type()
)
phivNonBroadcastIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivNonBroadcastIndex.setStatus("mandatory")


class _PhivNonBroadcastController_Type(Integer32):
    """Custom type phivNonBroadcastController based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("loopback", 2),
          ("normal", 1),
          ("other", 3))
    )


_PhivNonBroadcastController_Type.__name__ = "Integer32"
_PhivNonBroadcastController_Object = MibTableColumn
phivNonBroadcastController = _PhivNonBroadcastController_Object(
    (1, 3, 6, 1, 2, 1, 18, 14, 1, 1, 2),
    _PhivNonBroadcastController_Type()
)
phivNonBroadcastController.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivNonBroadcastController.setStatus("mandatory")


class _PhivNonBroadcastDuplex_Type(Integer32):
    """Custom type phivNonBroadcastDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 2))
    )


_PhivNonBroadcastDuplex_Type.__name__ = "Integer32"
_PhivNonBroadcastDuplex_Object = MibTableColumn
phivNonBroadcastDuplex = _PhivNonBroadcastDuplex_Object(
    (1, 3, 6, 1, 2, 1, 18, 14, 1, 1, 3),
    _PhivNonBroadcastDuplex_Type()
)
phivNonBroadcastDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivNonBroadcastDuplex.setStatus("mandatory")


class _PhivNonBroadcastClock_Type(Integer32):
    """Custom type phivNonBroadcastClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("external", 1),
          ("internal", 2),
          ("other", 3))
    )


_PhivNonBroadcastClock_Type.__name__ = "Integer32"
_PhivNonBroadcastClock_Object = MibTableColumn
phivNonBroadcastClock = _PhivNonBroadcastClock_Object(
    (1, 3, 6, 1, 2, 1, 18, 14, 1, 1, 4),
    _PhivNonBroadcastClock_Type()
)
phivNonBroadcastClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivNonBroadcastClock.setStatus("mandatory")


class _PhivNonBroadcastRetransmitTimer_Type(Integer32):
    """Custom type phivNonBroadcastRetransmitTimer based on Integer32"""
    defaultValue = 3000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PhivNonBroadcastRetransmitTimer_Type.__name__ = "Integer32"
_PhivNonBroadcastRetransmitTimer_Object = MibTableColumn
phivNonBroadcastRetransmitTimer = _PhivNonBroadcastRetransmitTimer_Object(
    (1, 3, 6, 1, 2, 1, 18, 14, 1, 1, 5),
    _PhivNonBroadcastRetransmitTimer_Type()
)
phivNonBroadcastRetransmitTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivNonBroadcastRetransmitTimer.setStatus("mandatory")
_Area_ObjectIdentity = ObjectIdentity
area = _Area_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 18, 15)
)
_PhivAreaTable_Object = MibTable
phivAreaTable = _PhivAreaTable_Object(
    (1, 3, 6, 1, 2, 1, 18, 15, 1)
)
if mibBuilder.loadTexts:
    phivAreaTable.setStatus("mandatory")
_PhivAreaEntry_Object = MibTableRow
phivAreaEntry = _PhivAreaEntry_Object(
    (1, 3, 6, 1, 2, 1, 18, 15, 1, 1)
)
phivAreaEntry.setIndexNames(
    (0, "DECNET-PHIV-MIB", "phivAreaNum"),
)
if mibBuilder.loadTexts:
    phivAreaEntry.setStatus("mandatory")


class _PhivAreaNum_Type(Integer32):
    """Custom type phivAreaNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_PhivAreaNum_Type.__name__ = "Integer32"
_PhivAreaNum_Object = MibTableColumn
phivAreaNum = _PhivAreaNum_Object(
    (1, 3, 6, 1, 2, 1, 18, 15, 1, 1, 1),
    _PhivAreaNum_Type()
)
phivAreaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivAreaNum.setStatus("mandatory")


class _PhivAreaState_Type(Integer32):
    """Custom type phivAreaState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("reachable", 4),
          ("unreachable", 5))
    )


_PhivAreaState_Type.__name__ = "Integer32"
_PhivAreaState_Object = MibTableColumn
phivAreaState = _PhivAreaState_Object(
    (1, 3, 6, 1, 2, 1, 18, 15, 1, 1, 2),
    _PhivAreaState_Type()
)
phivAreaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivAreaState.setStatus("mandatory")
_PhivAreaCost_Type = Gauge32
_PhivAreaCost_Object = MibTableColumn
phivAreaCost = _PhivAreaCost_Object(
    (1, 3, 6, 1, 2, 1, 18, 15, 1, 1, 3),
    _PhivAreaCost_Type()
)
phivAreaCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivAreaCost.setStatus("mandatory")


class _PhivAreaHops_Type(Integer32):
    """Custom type phivAreaHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhivAreaHops_Type.__name__ = "Integer32"
_PhivAreaHops_Object = MibTableColumn
phivAreaHops = _PhivAreaHops_Object(
    (1, 3, 6, 1, 2, 1, 18, 15, 1, 1, 4),
    _PhivAreaHops_Type()
)
phivAreaHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivAreaHops.setStatus("mandatory")
_PhivAreaNextNode_Type = PhivAddr
_PhivAreaNextNode_Object = MibTableColumn
phivAreaNextNode = _PhivAreaNextNode_Object(
    (1, 3, 6, 1, 2, 1, 18, 15, 1, 1, 5),
    _PhivAreaNextNode_Type()
)
phivAreaNextNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivAreaNextNode.setStatus("mandatory")


class _PhivAreaCircuitIndex_Type(Integer32):
    """Custom type phivAreaCircuitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PhivAreaCircuitIndex_Type.__name__ = "Integer32"
_PhivAreaCircuitIndex_Object = MibTableColumn
phivAreaCircuitIndex = _PhivAreaCircuitIndex_Object(
    (1, 3, 6, 1, 2, 1, 18, 15, 1, 1, 6),
    _PhivAreaCircuitIndex_Type()
)
phivAreaCircuitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phivAreaCircuitIndex.setStatus("mandatory")


class _PhivAreaMaxCost_Type(Integer32):
    """Custom type phivAreaMaxCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1022),
    )


_PhivAreaMaxCost_Type.__name__ = "Integer32"
_PhivAreaMaxCost_Object = MibScalar
phivAreaMaxCost = _PhivAreaMaxCost_Object(
    (1, 3, 6, 1, 2, 1, 18, 15, 2),
    _PhivAreaMaxCost_Type()
)
phivAreaMaxCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivAreaMaxCost.setStatus("mandatory")


class _PhivAreaMaxHops_Type(Integer32):
    """Custom type phivAreaMaxHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_PhivAreaMaxHops_Type.__name__ = "Integer32"
_PhivAreaMaxHops_Object = MibScalar
phivAreaMaxHops = _PhivAreaMaxHops_Object(
    (1, 3, 6, 1, 2, 1, 18, 15, 3),
    _PhivAreaMaxHops_Type()
)
phivAreaMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivAreaMaxHops.setStatus("mandatory")


class _PhivRouteMaxArea_Type(Integer32):
    """Custom type phivRouteMaxArea based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_PhivRouteMaxArea_Type.__name__ = "Integer32"
_PhivRouteMaxArea_Object = MibScalar
phivRouteMaxArea = _PhivRouteMaxArea_Object(
    (1, 3, 6, 1, 2, 1, 18, 15, 4),
    _PhivRouteMaxArea_Type()
)
phivRouteMaxArea.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phivRouteMaxArea.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DECNET-PHIV-MIB",
    **{"PhivAddr": PhivAddr,
       "PhivCounter": PhivCounter,
       "InterfaceIndex": InterfaceIndex,
       "phiv": phiv,
       "phivSystem": phivSystem,
       "phivSystemState": phivSystemState,
       "phivExecIdent": phivExecIdent,
       "phivManagement": phivManagement,
       "phivMgmtMgmtVers": phivMgmtMgmtVers,
       "session": session,
       "phivSessionSystemName": phivSessionSystemName,
       "phivSessionInTimer": phivSessionInTimer,
       "phivSessionOutTimer": phivSessionOutTimer,
       "end": end,
       "phivEndRemoteTable": phivEndRemoteTable,
       "phivEndRemoteEntry": phivEndRemoteEntry,
       "phivEndRemoteHostNodeID": phivEndRemoteHostNodeID,
       "phivEndRemoteState": phivEndRemoteState,
       "phivEndCircuitIndex": phivEndCircuitIndex,
       "phivEndActiveLinks": phivEndActiveLinks,
       "phivEndDelay": phivEndDelay,
       "phivEndCountTable": phivEndCountTable,
       "phivEndCountEntry": phivEndCountEntry,
       "phivEndCountHostNodeID": phivEndCountHostNodeID,
       "phivEndCountSecsLastZeroed": phivEndCountSecsLastZeroed,
       "phivEndCountUsrBytesRec": phivEndCountUsrBytesRec,
       "phivEndCountUsrBytesSent": phivEndCountUsrBytesSent,
       "phivEndUCountUsrMessRec": phivEndUCountUsrMessRec,
       "phivEndCountUsrMessSent": phivEndCountUsrMessSent,
       "phivEndCountTotalBytesRec": phivEndCountTotalBytesRec,
       "phivEndCountTotalBytesSent": phivEndCountTotalBytesSent,
       "phivEndCountTotalMessRec": phivEndCountTotalMessRec,
       "phivEndCountTotalMessSent": phivEndCountTotalMessSent,
       "phivEndCountConnectsRecd": phivEndCountConnectsRecd,
       "phivEndCountConnectsSent": phivEndCountConnectsSent,
       "phivEndCountReponseTimeouts": phivEndCountReponseTimeouts,
       "phivEndCountRecdConnectResErrs": phivEndCountRecdConnectResErrs,
       "phivEndMaxLinks": phivEndMaxLinks,
       "phivEndNSPVers": phivEndNSPVers,
       "phivEndRetransmitFactor": phivEndRetransmitFactor,
       "phivEndDelayFact": phivEndDelayFact,
       "phivEndDelayWeight": phivEndDelayWeight,
       "phivEndInactivityTimer": phivEndInactivityTimer,
       "phivEndCountZeroCount": phivEndCountZeroCount,
       "phivEndMaxLinksActive": phivEndMaxLinksActive,
       "routing": routing,
       "phivRouteBroadcastRouteTimer": phivRouteBroadcastRouteTimer,
       "phivRouteBuffSize": phivRouteBuffSize,
       "phivRouteRoutingVers": phivRouteRoutingVers,
       "phivRouteMaxAddr": phivRouteMaxAddr,
       "phivRouteMaxBdcastNonRouters": phivRouteMaxBdcastNonRouters,
       "phivRouteMaxBdcastRouters": phivRouteMaxBdcastRouters,
       "phivRouteMaxBuffs": phivRouteMaxBuffs,
       "phivRouteMaxCircuits": phivRouteMaxCircuits,
       "phivRouteMaxCost": phivRouteMaxCost,
       "phivRouteMaxHops": phivRouteMaxHops,
       "phivRouteMaxVisits": phivRouteMaxVisits,
       "phivRouteRoutingTimer": phivRouteRoutingTimer,
       "phivRouteSegBuffSize": phivRouteSegBuffSize,
       "phivRouteType": phivRouteType,
       "phivRouteCountAgedPktLoss": phivRouteCountAgedPktLoss,
       "phivRouteCountNodeUnrPktLoss": phivRouteCountNodeUnrPktLoss,
       "phivRouteCountOutRngePktLoss": phivRouteCountOutRngePktLoss,
       "phivRouteCountOverSzePktLoss": phivRouteCountOverSzePktLoss,
       "phivRouteCountPacketFmtErr": phivRouteCountPacketFmtErr,
       "phivRouteCountPtlRteUpdtLoss": phivRouteCountPtlRteUpdtLoss,
       "phivRouteCountVerifReject": phivRouteCountVerifReject,
       "phivLevel1RouteTable": phivLevel1RouteTable,
       "phivLevel1RouteEntry": phivLevel1RouteEntry,
       "phivLevel1RouteNodeAddr": phivLevel1RouteNodeAddr,
       "phivLevel1RouteCircuitIndex": phivLevel1RouteCircuitIndex,
       "phivLevel1RouteCost": phivLevel1RouteCost,
       "phivLevel1RouteHops": phivLevel1RouteHops,
       "phivLevel1RouteNextNode": phivLevel1RouteNextNode,
       "phivRouteCountZeroCount": phivRouteCountZeroCount,
       "phivRouteSystemAddr": phivRouteSystemAddr,
       "phivRouteRoutingType": phivRouteRoutingType,
       "phivRouteSystemAddress": phivRouteSystemAddress,
       "circuit": circuit,
       "phivCircuitParametersTable": phivCircuitParametersTable,
       "phivCircuitParametersEntry": phivCircuitParametersEntry,
       "phivCircuitIndex": phivCircuitIndex,
       "phivCircuitLineIndex": phivCircuitLineIndex,
       "phivCircuitCommonState": phivCircuitCommonState,
       "phivCircuitCommonSubState": phivCircuitCommonSubState,
       "phivCircuitCommonName": phivCircuitCommonName,
       "phivCircuitExecRecallTimer": phivCircuitExecRecallTimer,
       "phivCircuitCommonType": phivCircuitCommonType,
       "phivCircuitService": phivCircuitService,
       "phivCircuitExecCost": phivCircuitExecCost,
       "phivCircuitExecHelloTimer": phivCircuitExecHelloTimer,
       "phivCircuitCountTable": phivCircuitCountTable,
       "phivCircuitCountEntry": phivCircuitCountEntry,
       "phivCircuitCountSecLastZeroed": phivCircuitCountSecLastZeroed,
       "phivCircuitCountTermPacketsRecd": phivCircuitCountTermPacketsRecd,
       "phivCircuitCountOriginPackSent": phivCircuitCountOriginPackSent,
       "phivCircuitCountTermCongLoss": phivCircuitCountTermCongLoss,
       "phivCircuitCountCorruptLoss": phivCircuitCountCorruptLoss,
       "phivCircuitCountTransitPksRecd": phivCircuitCountTransitPksRecd,
       "phivCircuitCountTransitPkSent": phivCircuitCountTransitPkSent,
       "phivCircuitCountTransitCongestLoss": phivCircuitCountTransitCongestLoss,
       "phivCircuitCountCircuitDown": phivCircuitCountCircuitDown,
       "phivCircuitCountInitFailure": phivCircuitCountInitFailure,
       "phivCircuitCountAdjDown": phivCircuitCountAdjDown,
       "phivCircuitCountPeakAdj": phivCircuitCountPeakAdj,
       "phivCircuitCountBytesRecd": phivCircuitCountBytesRecd,
       "phivCircuitCountBytesSent": phivCircuitCountBytesSent,
       "phivCircuitCountDataBlocksRecd": phivCircuitCountDataBlocksRecd,
       "phivCircuitCountDataBlocksSent": phivCircuitCountDataBlocksSent,
       "phivCircuitCountUsrBuffUnav": phivCircuitCountUsrBuffUnav,
       "phivCircuitOrigQueueLimit": phivCircuitOrigQueueLimit,
       "phivCircuitCountZeroCount": phivCircuitCountZeroCount,
       "ddcmp": ddcmp,
       "phivDDCMPCircuitParametersTable": phivDDCMPCircuitParametersTable,
       "phivDDCMPCircuitParametersEntry": phivDDCMPCircuitParametersEntry,
       "phivDDCMPCircuitIndex": phivDDCMPCircuitIndex,
       "phivDDCMPCircuitAdjNodeAddr": phivDDCMPCircuitAdjNodeAddr,
       "phivDDCMPCircuitTributary": phivDDCMPCircuitTributary,
       "phivDDCMPCircuitCountTable": phivDDCMPCircuitCountTable,
       "phivDDCMPCircuitCountEntry": phivDDCMPCircuitCountEntry,
       "phivDDCMPCircuitErrorsInbd": phivDDCMPCircuitErrorsInbd,
       "phivDDCMPCircuitErrorsOutbd": phivDDCMPCircuitErrorsOutbd,
       "phivDDCMPCircuitRmteReplyTimeouts": phivDDCMPCircuitRmteReplyTimeouts,
       "phivDDCMPCircuitLocalReplyTimeouts": phivDDCMPCircuitLocalReplyTimeouts,
       "phivDDCMPCircuitRmteBuffErrors": phivDDCMPCircuitRmteBuffErrors,
       "phivDDCMPCircuitLocalBuffErrors": phivDDCMPCircuitLocalBuffErrors,
       "phivDDCMPCircuitSelectIntervalsElap": phivDDCMPCircuitSelectIntervalsElap,
       "phivDDCMPCircuitSelectTimeouts": phivDDCMPCircuitSelectTimeouts,
       "phivDDCMPLineCountTable": phivDDCMPLineCountTable,
       "phivDDCMPLineCountEntry": phivDDCMPLineCountEntry,
       "phivDDCMPLineCountIndex": phivDDCMPLineCountIndex,
       "phivDDCMPLineCountDataErrsIn": phivDDCMPLineCountDataErrsIn,
       "phivDDCMPLineCountRmteStationErrs": phivDDCMPLineCountRmteStationErrs,
       "phivDDCMPLineCountLocalStationErrs": phivDDCMPLineCountLocalStationErrs,
       "control": control,
       "phivControlSchedTimer": phivControlSchedTimer,
       "phivControlDeadTimer": phivControlDeadTimer,
       "phivControlDelayTimer": phivControlDelayTimer,
       "phivControlStreamTimer": phivControlStreamTimer,
       "phivControlParametersTable": phivControlParametersTable,
       "phivControlParametersEntry": phivControlParametersEntry,
       "phivControlCircuitIndex": phivControlCircuitIndex,
       "phivControlBabbleTimer": phivControlBabbleTimer,
       "phivControlMaxBuffs": phivControlMaxBuffs,
       "phivControlMaxTransmits": phivControlMaxTransmits,
       "phivControlDyingBase": phivControlDyingBase,
       "phivControlDyingIncrement": phivControlDyingIncrement,
       "phivControlDeadThreshold": phivControlDeadThreshold,
       "phivControlDyingThreshold": phivControlDyingThreshold,
       "phivControlInactTreshold": phivControlInactTreshold,
       "phivControlPollingState": phivControlPollingState,
       "phivControlPollingSubState": phivControlPollingSubState,
       "phivControlTransTimer": phivControlTransTimer,
       "ethernet": ethernet,
       "phivEthLinkParametersTable": phivEthLinkParametersTable,
       "phivEthLinkParametersEntry": phivEthLinkParametersEntry,
       "phivEthLinkIndex": phivEthLinkIndex,
       "phivEthDesigRouterNodeAddr": phivEthDesigRouterNodeAddr,
       "phivEthMaxRouters": phivEthMaxRouters,
       "phivEthRouterPri": phivEthRouterPri,
       "phivEthHardwareAddr": phivEthHardwareAddr,
       "counters": counters,
       "phivCountersCountTable": phivCountersCountTable,
       "phivCountersCountEntry": phivCountersCountEntry,
       "phivCountersIndex": phivCountersIndex,
       "phivCountersCountBytesRecd": phivCountersCountBytesRecd,
       "phivCountersCountBytesSent": phivCountersCountBytesSent,
       "phivCountersCountDataBlocksRecd": phivCountersCountDataBlocksRecd,
       "phivCountersCountDataBlocksSent": phivCountersCountDataBlocksSent,
       "phivCountersCountEthUsrBuffUnav": phivCountersCountEthUsrBuffUnav,
       "phivCountersCountMcastBytesRecd": phivCountersCountMcastBytesRecd,
       "phivCountersCountDataBlksRecd": phivCountersCountDataBlksRecd,
       "phivCountersCountDataBlksSent": phivCountersCountDataBlksSent,
       "phivCountersCountMcastBlksRecd": phivCountersCountMcastBlksRecd,
       "phivCountersCountBlksSentDef": phivCountersCountBlksSentDef,
       "phivCountersCountBlksSentSingleCol": phivCountersCountBlksSentSingleCol,
       "phivCountersCountBlksSentMultCol": phivCountersCountBlksSentMultCol,
       "phivCountersCountSendFailure": phivCountersCountSendFailure,
       "phivCountersCountCollDetectFailure": phivCountersCountCollDetectFailure,
       "phivCountersCountReceiveFailure": phivCountersCountReceiveFailure,
       "phivCountersCountUnrecFrameDest": phivCountersCountUnrecFrameDest,
       "phivCountersCountDataOver": phivCountersCountDataOver,
       "phivCountersCountSysBuffUnav": phivCountersCountSysBuffUnav,
       "phivCountersCountUsrBuffUnav": phivCountersCountUsrBuffUnav,
       "adjacency": adjacency,
       "phivAdjTable": phivAdjTable,
       "phivAdjEntry": phivAdjEntry,
       "phivAdjCircuitIndex": phivAdjCircuitIndex,
       "phivAdjNodeAddr": phivAdjNodeAddr,
       "phivAdjBlockSize": phivAdjBlockSize,
       "phivAdjListenTimer": phivAdjListenTimer,
       "phivAdjCircuitEtherServPhysAddr": phivAdjCircuitEtherServPhysAddr,
       "phivAdjType": phivAdjType,
       "phivAdjState": phivAdjState,
       "phivAdjPriority": phivAdjPriority,
       "phivAdjExecListenTimer": phivAdjExecListenTimer,
       "phivAdjNodeTable": phivAdjNodeTable,
       "phivAdjNodeEntry": phivAdjNodeEntry,
       "phivAdjNodeCircuitIndex": phivAdjNodeCircuitIndex,
       "phivAdjAddr": phivAdjAddr,
       "phivAdjNodeBlockSize": phivAdjNodeBlockSize,
       "phivAdjNodeListenTimer": phivAdjNodeListenTimer,
       "phivAdjNodeCircuitEtherServPhysAddr": phivAdjNodeCircuitEtherServPhysAddr,
       "phivAdjNodeType": phivAdjNodeType,
       "phivAdjNodeState": phivAdjNodeState,
       "phivAdjNodePriority": phivAdjNodePriority,
       "line": line,
       "phivLineTable": phivLineTable,
       "phivLineEntry": phivLineEntry,
       "phivLineIndex": phivLineIndex,
       "phivLineName": phivLineName,
       "phivLineState": phivLineState,
       "phivLineSubstate": phivLineSubstate,
       "phivLineService": phivLineService,
       "phivLineDevice": phivLineDevice,
       "phivLineReceiveBuffs": phivLineReceiveBuffs,
       "phivLineProtocol": phivLineProtocol,
       "phivLineServiceTimer": phivLineServiceTimer,
       "phivLineMaxBlock": phivLineMaxBlock,
       "nonBroadcastLine": nonBroadcastLine,
       "phivNonBroadcastTable": phivNonBroadcastTable,
       "phivNonBroadcastEntry": phivNonBroadcastEntry,
       "phivNonBroadcastIndex": phivNonBroadcastIndex,
       "phivNonBroadcastController": phivNonBroadcastController,
       "phivNonBroadcastDuplex": phivNonBroadcastDuplex,
       "phivNonBroadcastClock": phivNonBroadcastClock,
       "phivNonBroadcastRetransmitTimer": phivNonBroadcastRetransmitTimer,
       "area": area,
       "phivAreaTable": phivAreaTable,
       "phivAreaEntry": phivAreaEntry,
       "phivAreaNum": phivAreaNum,
       "phivAreaState": phivAreaState,
       "phivAreaCost": phivAreaCost,
       "phivAreaHops": phivAreaHops,
       "phivAreaNextNode": phivAreaNextNode,
       "phivAreaCircuitIndex": phivAreaCircuitIndex,
       "phivAreaMaxCost": phivAreaMaxCost,
       "phivAreaMaxHops": phivAreaMaxHops,
       "phivRouteMaxArea": phivRouteMaxArea}
)
