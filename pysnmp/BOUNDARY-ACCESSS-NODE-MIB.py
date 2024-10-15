# SNMP MIB module (BOUNDARY-ACCESSS-NODE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BOUNDARY-ACCESSS-NODE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:48:33 2024
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

_IbmBANMIB_ObjectIdentity = ObjectIdentity
ibmBANMIB = _IbmBANMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12)
)
_IbmBANTable_Object = MibTable
ibmBANTable = _IbmBANTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1)
)
if mibBuilder.loadTexts:
    ibmBANTable.setStatus("mandatory")
_IbmBANEntry_Object = MibTableRow
ibmBANEntry = _IbmBANEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1)
)
ibmBANEntry.setIndexNames(
    (0, "BOUNDARY-ACCESSS-NODE-MIB", "ibmBANbridgePort"),
)
if mibBuilder.loadTexts:
    ibmBANEntry.setStatus("mandatory")


class _IbmBANbridgePort_Type(Integer32):
    """Custom type ibmBANbridgePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IbmBANbridgePort_Type.__name__ = "Integer32"
_IbmBANbridgePort_Object = MibTableColumn
ibmBANbridgePort = _IbmBANbridgePort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 1),
    _IbmBANbridgePort_Type()
)
ibmBANbridgePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmBANbridgePort.setStatus("mandatory")
_IbmBANifIndex_Type = Integer32
_IbmBANifIndex_Object = MibTableColumn
ibmBANifIndex = _IbmBANifIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 2),
    _IbmBANifIndex_Type()
)
ibmBANifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBANifIndex.setStatus("mandatory")


class _IbmBANDLCImacAddress_Type(OctetString):
    """Custom type ibmBANDLCImacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmBANDLCImacAddress_Type.__name__ = "OctetString"
_IbmBANDLCImacAddress_Object = MibTableColumn
ibmBANDLCImacAddress = _IbmBANDLCImacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 3),
    _IbmBANDLCImacAddress_Type()
)
ibmBANDLCImacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBANDLCImacAddress.setStatus("mandatory")


class _IbmBANboundaryNodeID_Type(OctetString):
    """Custom type ibmBANboundaryNodeID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmBANboundaryNodeID_Type.__name__ = "OctetString"
_IbmBANboundaryNodeID_Object = MibTableColumn
ibmBANboundaryNodeID = _IbmBANboundaryNodeID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 4),
    _IbmBANboundaryNodeID_Type()
)
ibmBANboundaryNodeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBANboundaryNodeID.setStatus("mandatory")


class _IbmBANtype_Type(Integer32):
    """Custom type ibmBANtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bridged", 1),
          ("dlswTerminated", 2))
    )


_IbmBANtype_Type.__name__ = "Integer32"
_IbmBANtype_Object = MibTableColumn
ibmBANtype = _IbmBANtype_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 5),
    _IbmBANtype_Type()
)
ibmBANtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBANtype.setStatus("mandatory")


class _IbmBANstatus_Type(Integer32):
    """Custom type ibmBANstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("initFail", 3),
          ("up", 1))
    )


_IbmBANstatus_Type.__name__ = "Integer32"
_IbmBANstatus_Object = MibTableColumn
ibmBANstatus = _IbmBANstatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 6),
    _IbmBANstatus_Type()
)
ibmBANstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBANstatus.setStatus("mandatory")
_IbmBANinIFrames_Type = Counter32
_IbmBANinIFrames_Object = MibTableColumn
ibmBANinIFrames = _IbmBANinIFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 7),
    _IbmBANinIFrames_Type()
)
ibmBANinIFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBANinIFrames.setStatus("mandatory")
_IbmBANinRRs_Type = Counter32
_IbmBANinRRs_Object = MibTableColumn
ibmBANinRRs = _IbmBANinRRs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 8),
    _IbmBANinRRs_Type()
)
ibmBANinRRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBANinRRs.setStatus("mandatory")
_IbmBANinRNRs_Type = Counter32
_IbmBANinRNRs_Object = MibTableColumn
ibmBANinRNRs = _IbmBANinRNRs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 9),
    _IbmBANinRNRs_Type()
)
ibmBANinRNRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBANinRNRs.setStatus("mandatory")
_IbmBANinRejs_Type = Counter32
_IbmBANinRejs_Object = MibTableColumn
ibmBANinRejs = _IbmBANinRejs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 10),
    _IbmBANinRejs_Type()
)
ibmBANinRejs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBANinRejs.setStatus("mandatory")
_IbmBANinTests_Type = Counter32
_IbmBANinTests_Object = MibTableColumn
ibmBANinTests = _IbmBANinTests_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 11),
    _IbmBANinTests_Type()
)
ibmBANinTests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBANinTests.setStatus("mandatory")
_IbmBANinTestRsps_Type = Counter32
_IbmBANinTestRsps_Object = MibTableColumn
ibmBANinTestRsps = _IbmBANinTestRsps_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 12),
    _IbmBANinTestRsps_Type()
)
ibmBANinTestRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBANinTestRsps.setStatus("mandatory")
_IbmBANinXIDs_Type = Counter32
_IbmBANinXIDs_Object = MibTableColumn
ibmBANinXIDs = _IbmBANinXIDs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 13),
    _IbmBANinXIDs_Type()
)
ibmBANinXIDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBANinXIDs.setStatus("mandatory")
_IbmBANinXIDRsps_Type = Counter32
_IbmBANinXIDRsps_Object = MibTableColumn
ibmBANinXIDRsps = _IbmBANinXIDRsps_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 14),
    _IbmBANinXIDRsps_Type()
)
ibmBANinXIDRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBANinXIDRsps.setStatus("mandatory")
_IbmBANinSABMEs_Type = Counter32
_IbmBANinSABMEs_Object = MibTableColumn
ibmBANinSABMEs = _IbmBANinSABMEs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 15),
    _IbmBANinSABMEs_Type()
)
ibmBANinSABMEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBANinSABMEs.setStatus("mandatory")
_IbmBANinUAs_Type = Counter32
_IbmBANinUAs_Object = MibTableColumn
ibmBANinUAs = _IbmBANinUAs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 16),
    _IbmBANinUAs_Type()
)
ibmBANinUAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBANinUAs.setStatus("mandatory")
_IbmBANinDMs_Type = Counter32
_IbmBANinDMs_Object = MibTableColumn
ibmBANinDMs = _IbmBANinDMs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 17),
    _IbmBANinDMs_Type()
)
ibmBANinDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBANinDMs.setStatus("mandatory")
_IbmBANinDISCs_Type = Counter32
_IbmBANinDISCs_Object = MibTableColumn
ibmBANinDISCs = _IbmBANinDISCs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 18),
    _IbmBANinDISCs_Type()
)
ibmBANinDISCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBANinDISCs.setStatus("mandatory")
_IbmBANinFRMRs_Type = Counter32
_IbmBANinFRMRs_Object = MibTableColumn
ibmBANinFRMRs = _IbmBANinFRMRs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 19),
    _IbmBANinFRMRs_Type()
)
ibmBANinFRMRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBANinFRMRs.setStatus("mandatory")
_IbmBANinOthers_Type = Counter32
_IbmBANinOthers_Object = MibTableColumn
ibmBANinOthers = _IbmBANinOthers_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 20),
    _IbmBANinOthers_Type()
)
ibmBANinOthers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBANinOthers.setStatus("mandatory")
_IbmBANoutIFrames_Type = Counter32
_IbmBANoutIFrames_Object = MibTableColumn
ibmBANoutIFrames = _IbmBANoutIFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 21),
    _IbmBANoutIFrames_Type()
)
ibmBANoutIFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBANoutIFrames.setStatus("mandatory")
_IbmBANoutRRs_Type = Counter32
_IbmBANoutRRs_Object = MibTableColumn
ibmBANoutRRs = _IbmBANoutRRs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 22),
    _IbmBANoutRRs_Type()
)
ibmBANoutRRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBANoutRRs.setStatus("mandatory")
_IbmBANoutRNRs_Type = Counter32
_IbmBANoutRNRs_Object = MibTableColumn
ibmBANoutRNRs = _IbmBANoutRNRs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 23),
    _IbmBANoutRNRs_Type()
)
ibmBANoutRNRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBANoutRNRs.setStatus("mandatory")
_IbmBANoutRejs_Type = Counter32
_IbmBANoutRejs_Object = MibTableColumn
ibmBANoutRejs = _IbmBANoutRejs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 24),
    _IbmBANoutRejs_Type()
)
ibmBANoutRejs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBANoutRejs.setStatus("mandatory")
_IbmBANoutTests_Type = Counter32
_IbmBANoutTests_Object = MibTableColumn
ibmBANoutTests = _IbmBANoutTests_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 25),
    _IbmBANoutTests_Type()
)
ibmBANoutTests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBANoutTests.setStatus("mandatory")
_IbmBANoutTestRsps_Type = Counter32
_IbmBANoutTestRsps_Object = MibTableColumn
ibmBANoutTestRsps = _IbmBANoutTestRsps_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 26),
    _IbmBANoutTestRsps_Type()
)
ibmBANoutTestRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBANoutTestRsps.setStatus("mandatory")
_IbmBANoutXIDs_Type = Counter32
_IbmBANoutXIDs_Object = MibTableColumn
ibmBANoutXIDs = _IbmBANoutXIDs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 27),
    _IbmBANoutXIDs_Type()
)
ibmBANoutXIDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBANoutXIDs.setStatus("mandatory")
_IbmBANoutXIDRsps_Type = Counter32
_IbmBANoutXIDRsps_Object = MibTableColumn
ibmBANoutXIDRsps = _IbmBANoutXIDRsps_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 28),
    _IbmBANoutXIDRsps_Type()
)
ibmBANoutXIDRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBANoutXIDRsps.setStatus("mandatory")
_IbmBANoutSABMEs_Type = Counter32
_IbmBANoutSABMEs_Object = MibTableColumn
ibmBANoutSABMEs = _IbmBANoutSABMEs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 29),
    _IbmBANoutSABMEs_Type()
)
ibmBANoutSABMEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBANoutSABMEs.setStatus("mandatory")
_IbmBANoutUAs_Type = Counter32
_IbmBANoutUAs_Object = MibTableColumn
ibmBANoutUAs = _IbmBANoutUAs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 30),
    _IbmBANoutUAs_Type()
)
ibmBANoutUAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBANoutUAs.setStatus("mandatory")
_IbmBANoutDMs_Type = Counter32
_IbmBANoutDMs_Object = MibTableColumn
ibmBANoutDMs = _IbmBANoutDMs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 31),
    _IbmBANoutDMs_Type()
)
ibmBANoutDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBANoutDMs.setStatus("mandatory")
_IbmBANoutDISCs_Type = Counter32
_IbmBANoutDISCs_Object = MibTableColumn
ibmBANoutDISCs = _IbmBANoutDISCs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 32),
    _IbmBANoutDISCs_Type()
)
ibmBANoutDISCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBANoutDISCs.setStatus("mandatory")
_IbmBANoutFRMRs_Type = Counter32
_IbmBANoutFRMRs_Object = MibTableColumn
ibmBANoutFRMRs = _IbmBANoutFRMRs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 33),
    _IbmBANoutFRMRs_Type()
)
ibmBANoutFRMRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBANoutFRMRs.setStatus("mandatory")
_IbmBANoutOthers_Type = Counter32
_IbmBANoutOthers_Object = MibTableColumn
ibmBANoutOthers = _IbmBANoutOthers_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12, 1, 1, 34),
    _IbmBANoutOthers_Type()
)
ibmBANoutOthers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBANoutOthers.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BOUNDARY-ACCESSS-NODE-MIB",
    **{"ibmBANMIB": ibmBANMIB,
       "ibmBANTable": ibmBANTable,
       "ibmBANEntry": ibmBANEntry,
       "ibmBANbridgePort": ibmBANbridgePort,
       "ibmBANifIndex": ibmBANifIndex,
       "ibmBANDLCImacAddress": ibmBANDLCImacAddress,
       "ibmBANboundaryNodeID": ibmBANboundaryNodeID,
       "ibmBANtype": ibmBANtype,
       "ibmBANstatus": ibmBANstatus,
       "ibmBANinIFrames": ibmBANinIFrames,
       "ibmBANinRRs": ibmBANinRRs,
       "ibmBANinRNRs": ibmBANinRNRs,
       "ibmBANinRejs": ibmBANinRejs,
       "ibmBANinTests": ibmBANinTests,
       "ibmBANinTestRsps": ibmBANinTestRsps,
       "ibmBANinXIDs": ibmBANinXIDs,
       "ibmBANinXIDRsps": ibmBANinXIDRsps,
       "ibmBANinSABMEs": ibmBANinSABMEs,
       "ibmBANinUAs": ibmBANinUAs,
       "ibmBANinDMs": ibmBANinDMs,
       "ibmBANinDISCs": ibmBANinDISCs,
       "ibmBANinFRMRs": ibmBANinFRMRs,
       "ibmBANinOthers": ibmBANinOthers,
       "ibmBANoutIFrames": ibmBANoutIFrames,
       "ibmBANoutRRs": ibmBANoutRRs,
       "ibmBANoutRNRs": ibmBANoutRNRs,
       "ibmBANoutRejs": ibmBANoutRejs,
       "ibmBANoutTests": ibmBANoutTests,
       "ibmBANoutTestRsps": ibmBANoutTestRsps,
       "ibmBANoutXIDs": ibmBANoutXIDs,
       "ibmBANoutXIDRsps": ibmBANoutXIDRsps,
       "ibmBANoutSABMEs": ibmBANoutSABMEs,
       "ibmBANoutUAs": ibmBANoutUAs,
       "ibmBANoutDMs": ibmBANoutDMs,
       "ibmBANoutDISCs": ibmBANoutDISCs,
       "ibmBANoutFRMRs": ibmBANoutFRMRs,
       "ibmBANoutOthers": ibmBANoutOthers}
)
