# SNMP MIB module (CISCO-ATM-PVCTRAP-EXTN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ATM-PVCTRAP-EXTN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:56 2024
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

(atmInterfaceConfEntry,
 atmVclVci,
 atmVclVpi) = mibBuilder.importSymbols(
    "ATM-MIB",
    "atmInterfaceConfEntry",
    "atmVclVci",
    "atmVclVpi")

(atmIntfCurrentlyFailingPVcls,
 atmIntfPvcFailures) = mibBuilder.importSymbols(
    "CISCO-IETF-ATM2-PVCTRAP-MIB",
    "atmIntfCurrentlyFailingPVcls",
    "atmIntfPvcFailures")

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

ciscoAtmPvcTrapExtnMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 97)
)
ciscoAtmPvcTrapExtnMIB.setRevisions(
        ("2003-03-24 00:00",
         "2003-01-20 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CatmOAMRecoveryType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("catmAISRDIOAMRecover", 8),
          ("catmEndAISRDIOAMRecover", 32),
          ("catmEndCCOAMRecover", 4),
          ("catmLoopbackOAMRecover", 1),
          ("catmSegAISRDIOAMRecover", 16),
          ("catmSegmentCCOAMRecover", 2))
    )



class CatmOAMFailureType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("catmAISRDIOAMFailure", 8),
          ("catmEndAISRDIOAMFailure", 32),
          ("catmEndCCOAMFailure", 4),
          ("catmLoopbackOAMFailure", 1),
          ("catmSegAISRDIOAMFailure", 16),
          ("catmSegmentCCOAMFailure", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoAtmPvcTrapExtnMIBObjects_ObjectIdentity = ObjectIdentity
ciscoAtmPvcTrapExtnMIBObjects = _CiscoAtmPvcTrapExtnMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1)
)
_CatmInterfaceExt2Table_Object = MibTable
catmInterfaceExt2Table = _CatmInterfaceExt2Table_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 1)
)
if mibBuilder.loadTexts:
    catmInterfaceExt2Table.setStatus("current")
_CatmInterfaceExt2Entry_Object = MibTableRow
catmInterfaceExt2Entry = _CatmInterfaceExt2Entry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 1, 1)
)
if mibBuilder.loadTexts:
    catmInterfaceExt2Entry.setStatus("current")
_CatmIntfCurrentlyDownToUpPVcls_Type = Gauge32
_CatmIntfCurrentlyDownToUpPVcls_Object = MibTableColumn
catmIntfCurrentlyDownToUpPVcls = _CatmIntfCurrentlyDownToUpPVcls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 1, 1, 1),
    _CatmIntfCurrentlyDownToUpPVcls_Type()
)
catmIntfCurrentlyDownToUpPVcls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmIntfCurrentlyDownToUpPVcls.setStatus("current")
_CatmIntfOAMFailedPVcls_Type = Gauge32
_CatmIntfOAMFailedPVcls_Object = MibTableColumn
catmIntfOAMFailedPVcls = _CatmIntfOAMFailedPVcls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 1, 1, 2),
    _CatmIntfOAMFailedPVcls_Type()
)
catmIntfOAMFailedPVcls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmIntfOAMFailedPVcls.setStatus("current")
_CatmIntfCurrentOAMFailingPVcls_Type = Gauge32
_CatmIntfCurrentOAMFailingPVcls_Object = MibTableColumn
catmIntfCurrentOAMFailingPVcls = _CatmIntfCurrentOAMFailingPVcls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 1, 1, 3),
    _CatmIntfCurrentOAMFailingPVcls_Type()
)
catmIntfCurrentOAMFailingPVcls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmIntfCurrentOAMFailingPVcls.setStatus("current")
_CatmIntfSegCCOAMFailedPVcls_Type = Gauge32
_CatmIntfSegCCOAMFailedPVcls_Object = MibTableColumn
catmIntfSegCCOAMFailedPVcls = _CatmIntfSegCCOAMFailedPVcls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 1, 1, 4),
    _CatmIntfSegCCOAMFailedPVcls_Type()
)
catmIntfSegCCOAMFailedPVcls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmIntfSegCCOAMFailedPVcls.setStatus("current")
_CatmIntfCurSegCCOAMFailingPVcls_Type = Gauge32
_CatmIntfCurSegCCOAMFailingPVcls_Object = MibTableColumn
catmIntfCurSegCCOAMFailingPVcls = _CatmIntfCurSegCCOAMFailingPVcls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 1, 1, 5),
    _CatmIntfCurSegCCOAMFailingPVcls_Type()
)
catmIntfCurSegCCOAMFailingPVcls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmIntfCurSegCCOAMFailingPVcls.setStatus("current")
_CatmIntfEndCCOAMFailedPVcls_Type = Gauge32
_CatmIntfEndCCOAMFailedPVcls_Object = MibTableColumn
catmIntfEndCCOAMFailedPVcls = _CatmIntfEndCCOAMFailedPVcls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 1, 1, 6),
    _CatmIntfEndCCOAMFailedPVcls_Type()
)
catmIntfEndCCOAMFailedPVcls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmIntfEndCCOAMFailedPVcls.setStatus("current")
_CatmIntfCurEndCCOAMFailingPVcls_Type = Gauge32
_CatmIntfCurEndCCOAMFailingPVcls_Object = MibTableColumn
catmIntfCurEndCCOAMFailingPVcls = _CatmIntfCurEndCCOAMFailingPVcls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 1, 1, 7),
    _CatmIntfCurEndCCOAMFailingPVcls_Type()
)
catmIntfCurEndCCOAMFailingPVcls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmIntfCurEndCCOAMFailingPVcls.setStatus("current")
_CatmIntfAISRDIOAMFailedPVcls_Type = Gauge32
_CatmIntfAISRDIOAMFailedPVcls_Object = MibTableColumn
catmIntfAISRDIOAMFailedPVcls = _CatmIntfAISRDIOAMFailedPVcls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 1, 1, 8),
    _CatmIntfAISRDIOAMFailedPVcls_Type()
)
catmIntfAISRDIOAMFailedPVcls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmIntfAISRDIOAMFailedPVcls.setStatus("current")
_CatmIntfCurAISRDIOAMFailingPVcls_Type = Gauge32
_CatmIntfCurAISRDIOAMFailingPVcls_Object = MibTableColumn
catmIntfCurAISRDIOAMFailingPVcls = _CatmIntfCurAISRDIOAMFailingPVcls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 1, 1, 9),
    _CatmIntfCurAISRDIOAMFailingPVcls_Type()
)
catmIntfCurAISRDIOAMFailingPVcls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmIntfCurAISRDIOAMFailingPVcls.setStatus("current")
_CatmIntfAnyOAMFailedPVcls_Type = Gauge32
_CatmIntfAnyOAMFailedPVcls_Object = MibTableColumn
catmIntfAnyOAMFailedPVcls = _CatmIntfAnyOAMFailedPVcls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 1, 1, 10),
    _CatmIntfAnyOAMFailedPVcls_Type()
)
catmIntfAnyOAMFailedPVcls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmIntfAnyOAMFailedPVcls.setStatus("current")
_CatmIntfCurAnyOAMFailingPVcls_Type = Gauge32
_CatmIntfCurAnyOAMFailingPVcls_Object = MibTableColumn
catmIntfCurAnyOAMFailingPVcls = _CatmIntfCurAnyOAMFailingPVcls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 1, 1, 11),
    _CatmIntfCurAnyOAMFailingPVcls_Type()
)
catmIntfCurAnyOAMFailingPVcls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmIntfCurAnyOAMFailingPVcls.setStatus("current")
_CatmIntfTypeOfOAMFailure_Type = CatmOAMFailureType
_CatmIntfTypeOfOAMFailure_Object = MibTableColumn
catmIntfTypeOfOAMFailure = _CatmIntfTypeOfOAMFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 1, 1, 12),
    _CatmIntfTypeOfOAMFailure_Type()
)
catmIntfTypeOfOAMFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmIntfTypeOfOAMFailure.setStatus("current")
_CatmIntfOAMRcovedPVcls_Type = Gauge32
_CatmIntfOAMRcovedPVcls_Object = MibTableColumn
catmIntfOAMRcovedPVcls = _CatmIntfOAMRcovedPVcls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 1, 1, 13),
    _CatmIntfOAMRcovedPVcls_Type()
)
catmIntfOAMRcovedPVcls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmIntfOAMRcovedPVcls.setStatus("current")
_CatmIntfCurrentOAMRcovingPVcls_Type = Gauge32
_CatmIntfCurrentOAMRcovingPVcls_Object = MibTableColumn
catmIntfCurrentOAMRcovingPVcls = _CatmIntfCurrentOAMRcovingPVcls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 1, 1, 14),
    _CatmIntfCurrentOAMRcovingPVcls_Type()
)
catmIntfCurrentOAMRcovingPVcls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmIntfCurrentOAMRcovingPVcls.setStatus("current")
_CatmIntfSegCCOAMRcovedPVcls_Type = Gauge32
_CatmIntfSegCCOAMRcovedPVcls_Object = MibTableColumn
catmIntfSegCCOAMRcovedPVcls = _CatmIntfSegCCOAMRcovedPVcls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 1, 1, 15),
    _CatmIntfSegCCOAMRcovedPVcls_Type()
)
catmIntfSegCCOAMRcovedPVcls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmIntfSegCCOAMRcovedPVcls.setStatus("current")
_CatmIntfCurSegCCOAMRcovingPVcls_Type = Gauge32
_CatmIntfCurSegCCOAMRcovingPVcls_Object = MibTableColumn
catmIntfCurSegCCOAMRcovingPVcls = _CatmIntfCurSegCCOAMRcovingPVcls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 1, 1, 16),
    _CatmIntfCurSegCCOAMRcovingPVcls_Type()
)
catmIntfCurSegCCOAMRcovingPVcls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmIntfCurSegCCOAMRcovingPVcls.setStatus("current")
_CatmIntfEndCCOAMRcovedPVcls_Type = Gauge32
_CatmIntfEndCCOAMRcovedPVcls_Object = MibTableColumn
catmIntfEndCCOAMRcovedPVcls = _CatmIntfEndCCOAMRcovedPVcls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 1, 1, 17),
    _CatmIntfEndCCOAMRcovedPVcls_Type()
)
catmIntfEndCCOAMRcovedPVcls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmIntfEndCCOAMRcovedPVcls.setStatus("current")
_CatmIntfCurEndCCOAMRcovingPVcls_Type = Gauge32
_CatmIntfCurEndCCOAMRcovingPVcls_Object = MibTableColumn
catmIntfCurEndCCOAMRcovingPVcls = _CatmIntfCurEndCCOAMRcovingPVcls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 1, 1, 18),
    _CatmIntfCurEndCCOAMRcovingPVcls_Type()
)
catmIntfCurEndCCOAMRcovingPVcls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmIntfCurEndCCOAMRcovingPVcls.setStatus("current")
_CatmIntfAISRDIOAMRcovedPVcls_Type = Gauge32
_CatmIntfAISRDIOAMRcovedPVcls_Object = MibTableColumn
catmIntfAISRDIOAMRcovedPVcls = _CatmIntfAISRDIOAMRcovedPVcls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 1, 1, 19),
    _CatmIntfAISRDIOAMRcovedPVcls_Type()
)
catmIntfAISRDIOAMRcovedPVcls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmIntfAISRDIOAMRcovedPVcls.setStatus("current")
_CatmIntfCurAISRDIOAMRcovingPVcls_Type = Gauge32
_CatmIntfCurAISRDIOAMRcovingPVcls_Object = MibTableColumn
catmIntfCurAISRDIOAMRcovingPVcls = _CatmIntfCurAISRDIOAMRcovingPVcls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 1, 1, 20),
    _CatmIntfCurAISRDIOAMRcovingPVcls_Type()
)
catmIntfCurAISRDIOAMRcovingPVcls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmIntfCurAISRDIOAMRcovingPVcls.setStatus("current")
_CatmIntfAnyOAMRcovedPVcls_Type = Gauge32
_CatmIntfAnyOAMRcovedPVcls_Object = MibTableColumn
catmIntfAnyOAMRcovedPVcls = _CatmIntfAnyOAMRcovedPVcls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 1, 1, 21),
    _CatmIntfAnyOAMRcovedPVcls_Type()
)
catmIntfAnyOAMRcovedPVcls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmIntfAnyOAMRcovedPVcls.setStatus("current")
_CatmIntfCurAnyOAMRcovingPVcls_Type = Gauge32
_CatmIntfCurAnyOAMRcovingPVcls_Object = MibTableColumn
catmIntfCurAnyOAMRcovingPVcls = _CatmIntfCurAnyOAMRcovingPVcls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 1, 1, 22),
    _CatmIntfCurAnyOAMRcovingPVcls_Type()
)
catmIntfCurAnyOAMRcovingPVcls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmIntfCurAnyOAMRcovingPVcls.setStatus("current")
_CatmIntfTypeOfOAMRecover_Type = CatmOAMRecoveryType
_CatmIntfTypeOfOAMRecover_Object = MibTableColumn
catmIntfTypeOfOAMRecover = _CatmIntfTypeOfOAMRecover_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 1, 1, 23),
    _CatmIntfTypeOfOAMRecover_Type()
)
catmIntfTypeOfOAMRecover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmIntfTypeOfOAMRecover.setStatus("current")
_CatmIntfSegAISRDIFailedPVcls_Type = Gauge32
_CatmIntfSegAISRDIFailedPVcls_Object = MibTableColumn
catmIntfSegAISRDIFailedPVcls = _CatmIntfSegAISRDIFailedPVcls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 1, 1, 24),
    _CatmIntfSegAISRDIFailedPVcls_Type()
)
catmIntfSegAISRDIFailedPVcls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmIntfSegAISRDIFailedPVcls.setStatus("current")
_CatmIntfCurSegAISRDIFailingPVcls_Type = Gauge32
_CatmIntfCurSegAISRDIFailingPVcls_Object = MibTableColumn
catmIntfCurSegAISRDIFailingPVcls = _CatmIntfCurSegAISRDIFailingPVcls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 1, 1, 25),
    _CatmIntfCurSegAISRDIFailingPVcls_Type()
)
catmIntfCurSegAISRDIFailingPVcls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmIntfCurSegAISRDIFailingPVcls.setStatus("current")
_CatmIntfEndAISRDIFailedPVcls_Type = Gauge32
_CatmIntfEndAISRDIFailedPVcls_Object = MibTableColumn
catmIntfEndAISRDIFailedPVcls = _CatmIntfEndAISRDIFailedPVcls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 1, 1, 26),
    _CatmIntfEndAISRDIFailedPVcls_Type()
)
catmIntfEndAISRDIFailedPVcls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmIntfEndAISRDIFailedPVcls.setStatus("current")
_CatmIntfCurEndAISRDIFailingPVcls_Type = Gauge32
_CatmIntfCurEndAISRDIFailingPVcls_Object = MibTableColumn
catmIntfCurEndAISRDIFailingPVcls = _CatmIntfCurEndAISRDIFailingPVcls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 1, 1, 27),
    _CatmIntfCurEndAISRDIFailingPVcls_Type()
)
catmIntfCurEndAISRDIFailingPVcls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmIntfCurEndAISRDIFailingPVcls.setStatus("current")
_CatmIntfSegAISRDIRcovedPVcls_Type = Gauge32
_CatmIntfSegAISRDIRcovedPVcls_Object = MibTableColumn
catmIntfSegAISRDIRcovedPVcls = _CatmIntfSegAISRDIRcovedPVcls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 1, 1, 28),
    _CatmIntfSegAISRDIRcovedPVcls_Type()
)
catmIntfSegAISRDIRcovedPVcls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmIntfSegAISRDIRcovedPVcls.setStatus("current")
_CatmIntfCurSegAISRDIRcovingPVcls_Type = Gauge32
_CatmIntfCurSegAISRDIRcovingPVcls_Object = MibTableColumn
catmIntfCurSegAISRDIRcovingPVcls = _CatmIntfCurSegAISRDIRcovingPVcls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 1, 1, 29),
    _CatmIntfCurSegAISRDIRcovingPVcls_Type()
)
catmIntfCurSegAISRDIRcovingPVcls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmIntfCurSegAISRDIRcovingPVcls.setStatus("current")
_CatmIntfEndAISRDIRcovedPVcls_Type = Gauge32
_CatmIntfEndAISRDIRcovedPVcls_Object = MibTableColumn
catmIntfEndAISRDIRcovedPVcls = _CatmIntfEndAISRDIRcovedPVcls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 1, 1, 30),
    _CatmIntfEndAISRDIRcovedPVcls_Type()
)
catmIntfEndAISRDIRcovedPVcls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmIntfEndAISRDIRcovedPVcls.setStatus("current")
_CatmIntfCurEndAISRDIRcovingPVcls_Type = Gauge32
_CatmIntfCurEndAISRDIRcovingPVcls_Object = MibTableColumn
catmIntfCurEndAISRDIRcovingPVcls = _CatmIntfCurEndAISRDIRcovingPVcls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 1, 1, 31),
    _CatmIntfCurEndAISRDIRcovingPVcls_Type()
)
catmIntfCurEndAISRDIRcovingPVcls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmIntfCurEndAISRDIRcovingPVcls.setStatus("current")
_CatmCurStatChangePVclTable_Object = MibTable
catmCurStatChangePVclTable = _CatmCurStatChangePVclTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 2)
)
if mibBuilder.loadTexts:
    catmCurStatChangePVclTable.setStatus("current")
_CatmCurStatChangePVclEntry_Object = MibTableRow
catmCurStatChangePVclEntry = _CatmCurStatChangePVclEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 2, 1)
)
catmCurStatChangePVclEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
)
if mibBuilder.loadTexts:
    catmCurStatChangePVclEntry.setStatus("current")
_CatmPVclStatusTransition_Type = Counter32
_CatmPVclStatusTransition_Object = MibTableColumn
catmPVclStatusTransition = _CatmPVclStatusTransition_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 2, 1, 2),
    _CatmPVclStatusTransition_Type()
)
catmPVclStatusTransition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclStatusTransition.setStatus("current")
_CatmPVclStatusChangeStart_Type = TimeStamp
_CatmPVclStatusChangeStart_Object = MibTableColumn
catmPVclStatusChangeStart = _CatmPVclStatusChangeStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 2, 1, 3),
    _CatmPVclStatusChangeStart_Type()
)
catmPVclStatusChangeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclStatusChangeStart.setStatus("current")
_CatmPVclStatusChangeEnd_Type = TimeStamp
_CatmPVclStatusChangeEnd_Object = MibTableColumn
catmPVclStatusChangeEnd = _CatmPVclStatusChangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 2, 1, 4),
    _CatmPVclStatusChangeEnd_Type()
)
catmPVclStatusChangeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclStatusChangeEnd.setStatus("current")
_CatmPVclSegCCStatusTransition_Type = Counter32
_CatmPVclSegCCStatusTransition_Object = MibTableColumn
catmPVclSegCCStatusTransition = _CatmPVclSegCCStatusTransition_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 2, 1, 5),
    _CatmPVclSegCCStatusTransition_Type()
)
catmPVclSegCCStatusTransition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclSegCCStatusTransition.setStatus("current")
_CatmPVclSegCCStatusChangeStart_Type = TimeStamp
_CatmPVclSegCCStatusChangeStart_Object = MibTableColumn
catmPVclSegCCStatusChangeStart = _CatmPVclSegCCStatusChangeStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 2, 1, 6),
    _CatmPVclSegCCStatusChangeStart_Type()
)
catmPVclSegCCStatusChangeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclSegCCStatusChangeStart.setStatus("current")
_CatmPVclSegCCStatusChangeEnd_Type = TimeStamp
_CatmPVclSegCCStatusChangeEnd_Object = MibTableColumn
catmPVclSegCCStatusChangeEnd = _CatmPVclSegCCStatusChangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 2, 1, 7),
    _CatmPVclSegCCStatusChangeEnd_Type()
)
catmPVclSegCCStatusChangeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclSegCCStatusChangeEnd.setStatus("current")
_CatmPVclEndCCStatusTransition_Type = Counter32
_CatmPVclEndCCStatusTransition_Object = MibTableColumn
catmPVclEndCCStatusTransition = _CatmPVclEndCCStatusTransition_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 2, 1, 8),
    _CatmPVclEndCCStatusTransition_Type()
)
catmPVclEndCCStatusTransition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclEndCCStatusTransition.setStatus("current")
_CatmPVclEndCCStatusChangeStart_Type = TimeStamp
_CatmPVclEndCCStatusChangeStart_Object = MibTableColumn
catmPVclEndCCStatusChangeStart = _CatmPVclEndCCStatusChangeStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 2, 1, 9),
    _CatmPVclEndCCStatusChangeStart_Type()
)
catmPVclEndCCStatusChangeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclEndCCStatusChangeStart.setStatus("current")
_CatmPVclEndCCStatusChangeEnd_Type = TimeStamp
_CatmPVclEndCCStatusChangeEnd_Object = MibTableColumn
catmPVclEndCCStatusChangeEnd = _CatmPVclEndCCStatusChangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 2, 1, 10),
    _CatmPVclEndCCStatusChangeEnd_Type()
)
catmPVclEndCCStatusChangeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclEndCCStatusChangeEnd.setStatus("current")
_CatmPVclAISRDIStatusTransition_Type = Counter32
_CatmPVclAISRDIStatusTransition_Object = MibTableColumn
catmPVclAISRDIStatusTransition = _CatmPVclAISRDIStatusTransition_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 2, 1, 11),
    _CatmPVclAISRDIStatusTransition_Type()
)
catmPVclAISRDIStatusTransition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclAISRDIStatusTransition.setStatus("current")
_CatmPVclAISRDIStatusChangeStart_Type = TimeStamp
_CatmPVclAISRDIStatusChangeStart_Object = MibTableColumn
catmPVclAISRDIStatusChangeStart = _CatmPVclAISRDIStatusChangeStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 2, 1, 12),
    _CatmPVclAISRDIStatusChangeStart_Type()
)
catmPVclAISRDIStatusChangeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclAISRDIStatusChangeStart.setStatus("current")
_CatmPVclAISRDIStatusChangeEnd_Type = TimeStamp
_CatmPVclAISRDIStatusChangeEnd_Object = MibTableColumn
catmPVclAISRDIStatusChangeEnd = _CatmPVclAISRDIStatusChangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 2, 1, 13),
    _CatmPVclAISRDIStatusChangeEnd_Type()
)
catmPVclAISRDIStatusChangeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclAISRDIStatusChangeEnd.setStatus("current")
_CatmPVclCurFailTime_Type = TimeStamp
_CatmPVclCurFailTime_Object = MibTableColumn
catmPVclCurFailTime = _CatmPVclCurFailTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 2, 1, 14),
    _CatmPVclCurFailTime_Type()
)
catmPVclCurFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclCurFailTime.setStatus("current")
_CatmPVclPrevRecoverTime_Type = TimeStamp
_CatmPVclPrevRecoverTime_Object = MibTableColumn
catmPVclPrevRecoverTime = _CatmPVclPrevRecoverTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 2, 1, 15),
    _CatmPVclPrevRecoverTime_Type()
)
catmPVclPrevRecoverTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclPrevRecoverTime.setStatus("current")
_CatmPVclFailureReason_Type = CatmOAMFailureType
_CatmPVclFailureReason_Object = MibTableColumn
catmPVclFailureReason = _CatmPVclFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 2, 1, 16),
    _CatmPVclFailureReason_Type()
)
catmPVclFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclFailureReason.setStatus("current")
_CatmPVclSegAISRDIStatTransition_Type = Gauge32
_CatmPVclSegAISRDIStatTransition_Object = MibTableColumn
catmPVclSegAISRDIStatTransition = _CatmPVclSegAISRDIStatTransition_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 2, 1, 17),
    _CatmPVclSegAISRDIStatTransition_Type()
)
catmPVclSegAISRDIStatTransition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclSegAISRDIStatTransition.setStatus("current")
_CatmPVclSegAISRDIStatChangeStart_Type = TimeStamp
_CatmPVclSegAISRDIStatChangeStart_Object = MibTableColumn
catmPVclSegAISRDIStatChangeStart = _CatmPVclSegAISRDIStatChangeStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 2, 1, 18),
    _CatmPVclSegAISRDIStatChangeStart_Type()
)
catmPVclSegAISRDIStatChangeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclSegAISRDIStatChangeStart.setStatus("current")
_CatmPVclSegAISRDIStatChangeEnd_Type = TimeStamp
_CatmPVclSegAISRDIStatChangeEnd_Object = MibTableColumn
catmPVclSegAISRDIStatChangeEnd = _CatmPVclSegAISRDIStatChangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 2, 1, 19),
    _CatmPVclSegAISRDIStatChangeEnd_Type()
)
catmPVclSegAISRDIStatChangeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclSegAISRDIStatChangeEnd.setStatus("current")
_CatmPVclEndAISRDIStatTransition_Type = Gauge32
_CatmPVclEndAISRDIStatTransition_Object = MibTableColumn
catmPVclEndAISRDIStatTransition = _CatmPVclEndAISRDIStatTransition_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 2, 1, 20),
    _CatmPVclEndAISRDIStatTransition_Type()
)
catmPVclEndAISRDIStatTransition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclEndAISRDIStatTransition.setStatus("current")
_CatmPVclEndAISRDIStatChangeStart_Type = TimeStamp
_CatmPVclEndAISRDIStatChangeStart_Object = MibTableColumn
catmPVclEndAISRDIStatChangeStart = _CatmPVclEndAISRDIStatChangeStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 2, 1, 21),
    _CatmPVclEndAISRDIStatChangeStart_Type()
)
catmPVclEndAISRDIStatChangeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclEndAISRDIStatChangeStart.setStatus("current")
_CatmPVclEndAISRDIStatChangeEnd_Type = TimeStamp
_CatmPVclEndAISRDIStatChangeEnd_Object = MibTableColumn
catmPVclEndAISRDIStatChangeEnd = _CatmPVclEndAISRDIStatChangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 2, 1, 22),
    _CatmPVclEndAISRDIStatChangeEnd_Type()
)
catmPVclEndAISRDIStatChangeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclEndAISRDIStatChangeEnd.setStatus("current")
_CatmStatusChangePVclRangeTable_Object = MibTable
catmStatusChangePVclRangeTable = _CatmStatusChangePVclRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 3)
)
if mibBuilder.loadTexts:
    catmStatusChangePVclRangeTable.setStatus("current")
_CatmStatusChangePVclRangeEntry_Object = MibTableRow
catmStatusChangePVclRangeEntry = _CatmStatusChangePVclRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 3, 1)
)
catmStatusChangePVclRangeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "CISCO-ATM-PVCTRAP-EXTN-MIB", "catmStatusChangePVclRangeIndex"),
)
if mibBuilder.loadTexts:
    catmStatusChangePVclRangeEntry.setStatus("current")


class _CatmStatusChangePVclRangeIndex_Type(Integer32):
    """Custom type catmStatusChangePVclRangeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CatmStatusChangePVclRangeIndex_Type.__name__ = "Integer32"
_CatmStatusChangePVclRangeIndex_Object = MibTableColumn
catmStatusChangePVclRangeIndex = _CatmStatusChangePVclRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 3, 1, 1),
    _CatmStatusChangePVclRangeIndex_Type()
)
catmStatusChangePVclRangeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    catmStatusChangePVclRangeIndex.setStatus("current")


class _CatmPVclLowerRangeValue_Type(Integer32):
    """Custom type catmPVclLowerRangeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_CatmPVclLowerRangeValue_Type.__name__ = "Integer32"
_CatmPVclLowerRangeValue_Object = MibTableColumn
catmPVclLowerRangeValue = _CatmPVclLowerRangeValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 3, 1, 2),
    _CatmPVclLowerRangeValue_Type()
)
catmPVclLowerRangeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclLowerRangeValue.setStatus("current")


class _CatmPVclHigherRangeValue_Type(Integer32):
    """Custom type catmPVclHigherRangeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_CatmPVclHigherRangeValue_Type.__name__ = "Integer32"
_CatmPVclHigherRangeValue_Object = MibTableColumn
catmPVclHigherRangeValue = _CatmPVclHigherRangeValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 3, 1, 3),
    _CatmPVclHigherRangeValue_Type()
)
catmPVclHigherRangeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclHigherRangeValue.setStatus("current")
_CatmPVclRangeStatusChangeStart_Type = TimeStamp
_CatmPVclRangeStatusChangeStart_Object = MibTableColumn
catmPVclRangeStatusChangeStart = _CatmPVclRangeStatusChangeStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 3, 1, 4),
    _CatmPVclRangeStatusChangeStart_Type()
)
catmPVclRangeStatusChangeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclRangeStatusChangeStart.setStatus("current")
_CatmPVclRangeStatusChangeEnd_Type = TimeStamp
_CatmPVclRangeStatusChangeEnd_Object = MibTableColumn
catmPVclRangeStatusChangeEnd = _CatmPVclRangeStatusChangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 3, 1, 5),
    _CatmPVclRangeStatusChangeEnd_Type()
)
catmPVclRangeStatusChangeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclRangeStatusChangeEnd.setStatus("current")
_CatmSegCCStatusChPVclRangeTable_Object = MibTable
catmSegCCStatusChPVclRangeTable = _CatmSegCCStatusChPVclRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 5)
)
if mibBuilder.loadTexts:
    catmSegCCStatusChPVclRangeTable.setStatus("current")
_CatmSegCCStatusChPVclRangeEntry_Object = MibTableRow
catmSegCCStatusChPVclRangeEntry = _CatmSegCCStatusChPVclRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 5, 1)
)
catmSegCCStatusChPVclRangeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "CISCO-ATM-PVCTRAP-EXTN-MIB", "catmStatusChangePVclRangeIndex"),
)
if mibBuilder.loadTexts:
    catmSegCCStatusChPVclRangeEntry.setStatus("current")


class _CatmPVclSegCCLowerRangeValue_Type(Integer32):
    """Custom type catmPVclSegCCLowerRangeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_CatmPVclSegCCLowerRangeValue_Type.__name__ = "Integer32"
_CatmPVclSegCCLowerRangeValue_Object = MibTableColumn
catmPVclSegCCLowerRangeValue = _CatmPVclSegCCLowerRangeValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 5, 1, 1),
    _CatmPVclSegCCLowerRangeValue_Type()
)
catmPVclSegCCLowerRangeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclSegCCLowerRangeValue.setStatus("current")


class _CatmPVclSegCCHigherRangeValue_Type(Integer32):
    """Custom type catmPVclSegCCHigherRangeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_CatmPVclSegCCHigherRangeValue_Type.__name__ = "Integer32"
_CatmPVclSegCCHigherRangeValue_Object = MibTableColumn
catmPVclSegCCHigherRangeValue = _CatmPVclSegCCHigherRangeValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 5, 1, 2),
    _CatmPVclSegCCHigherRangeValue_Type()
)
catmPVclSegCCHigherRangeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclSegCCHigherRangeValue.setStatus("current")
_CatmPVclSegCCRangeStatusChStart_Type = TimeStamp
_CatmPVclSegCCRangeStatusChStart_Object = MibTableColumn
catmPVclSegCCRangeStatusChStart = _CatmPVclSegCCRangeStatusChStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 5, 1, 3),
    _CatmPVclSegCCRangeStatusChStart_Type()
)
catmPVclSegCCRangeStatusChStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclSegCCRangeStatusChStart.setStatus("current")
_CatmPVclSegCCRangeStatusChEnd_Type = TimeStamp
_CatmPVclSegCCRangeStatusChEnd_Object = MibTableColumn
catmPVclSegCCRangeStatusChEnd = _CatmPVclSegCCRangeStatusChEnd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 5, 1, 4),
    _CatmPVclSegCCRangeStatusChEnd_Type()
)
catmPVclSegCCRangeStatusChEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclSegCCRangeStatusChEnd.setStatus("current")
_CatmEndCCStatusChPVclRangeTable_Object = MibTable
catmEndCCStatusChPVclRangeTable = _CatmEndCCStatusChPVclRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 6)
)
if mibBuilder.loadTexts:
    catmEndCCStatusChPVclRangeTable.setStatus("current")
_CatmEndCCStatusChPVclRangeEntry_Object = MibTableRow
catmEndCCStatusChPVclRangeEntry = _CatmEndCCStatusChPVclRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 6, 1)
)
catmEndCCStatusChPVclRangeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "CISCO-ATM-PVCTRAP-EXTN-MIB", "catmStatusChangePVclRangeIndex"),
)
if mibBuilder.loadTexts:
    catmEndCCStatusChPVclRangeEntry.setStatus("current")


class _CatmPVclEndCCLowerRangeValue_Type(Integer32):
    """Custom type catmPVclEndCCLowerRangeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_CatmPVclEndCCLowerRangeValue_Type.__name__ = "Integer32"
_CatmPVclEndCCLowerRangeValue_Object = MibTableColumn
catmPVclEndCCLowerRangeValue = _CatmPVclEndCCLowerRangeValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 6, 1, 1),
    _CatmPVclEndCCLowerRangeValue_Type()
)
catmPVclEndCCLowerRangeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclEndCCLowerRangeValue.setStatus("current")


class _CatmPVclEndCCHigherRangeValue_Type(Integer32):
    """Custom type catmPVclEndCCHigherRangeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_CatmPVclEndCCHigherRangeValue_Type.__name__ = "Integer32"
_CatmPVclEndCCHigherRangeValue_Object = MibTableColumn
catmPVclEndCCHigherRangeValue = _CatmPVclEndCCHigherRangeValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 6, 1, 2),
    _CatmPVclEndCCHigherRangeValue_Type()
)
catmPVclEndCCHigherRangeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclEndCCHigherRangeValue.setStatus("current")
_CatmPVclEndCCRangeStatusChStart_Type = TimeStamp
_CatmPVclEndCCRangeStatusChStart_Object = MibTableColumn
catmPVclEndCCRangeStatusChStart = _CatmPVclEndCCRangeStatusChStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 6, 1, 3),
    _CatmPVclEndCCRangeStatusChStart_Type()
)
catmPVclEndCCRangeStatusChStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclEndCCRangeStatusChStart.setStatus("current")
_CatmPVclEndCCRangeStatusChEnd_Type = TimeStamp
_CatmPVclEndCCRangeStatusChEnd_Object = MibTableColumn
catmPVclEndCCRangeStatusChEnd = _CatmPVclEndCCRangeStatusChEnd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 6, 1, 4),
    _CatmPVclEndCCRangeStatusChEnd_Type()
)
catmPVclEndCCRangeStatusChEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclEndCCRangeStatusChEnd.setStatus("current")
_CatmAISRDIStatusChPVclRangeTable_Object = MibTable
catmAISRDIStatusChPVclRangeTable = _CatmAISRDIStatusChPVclRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 7)
)
if mibBuilder.loadTexts:
    catmAISRDIStatusChPVclRangeTable.setStatus("current")
_CatmAISRDIStatusChPVclRangeEntry_Object = MibTableRow
catmAISRDIStatusChPVclRangeEntry = _CatmAISRDIStatusChPVclRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 7, 1)
)
catmAISRDIStatusChPVclRangeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "CISCO-ATM-PVCTRAP-EXTN-MIB", "catmStatusChangePVclRangeIndex"),
)
if mibBuilder.loadTexts:
    catmAISRDIStatusChPVclRangeEntry.setStatus("current")


class _CatmPVclAISRDILowerRangeValue_Type(Integer32):
    """Custom type catmPVclAISRDILowerRangeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_CatmPVclAISRDILowerRangeValue_Type.__name__ = "Integer32"
_CatmPVclAISRDILowerRangeValue_Object = MibTableColumn
catmPVclAISRDILowerRangeValue = _CatmPVclAISRDILowerRangeValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 7, 1, 1),
    _CatmPVclAISRDILowerRangeValue_Type()
)
catmPVclAISRDILowerRangeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclAISRDILowerRangeValue.setStatus("current")


class _CatmPVclAISRDIHigherRangeValue_Type(Integer32):
    """Custom type catmPVclAISRDIHigherRangeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_CatmPVclAISRDIHigherRangeValue_Type.__name__ = "Integer32"
_CatmPVclAISRDIHigherRangeValue_Object = MibTableColumn
catmPVclAISRDIHigherRangeValue = _CatmPVclAISRDIHigherRangeValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 7, 1, 2),
    _CatmPVclAISRDIHigherRangeValue_Type()
)
catmPVclAISRDIHigherRangeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclAISRDIHigherRangeValue.setStatus("current")
_CatmPVclAISRDIRangeStatusChStart_Type = TimeStamp
_CatmPVclAISRDIRangeStatusChStart_Object = MibTableColumn
catmPVclAISRDIRangeStatusChStart = _CatmPVclAISRDIRangeStatusChStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 7, 1, 3),
    _CatmPVclAISRDIRangeStatusChStart_Type()
)
catmPVclAISRDIRangeStatusChStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclAISRDIRangeStatusChStart.setStatus("current")
_CatmPVclAISRDIRangeStatusChEnd_Type = TimeStamp
_CatmPVclAISRDIRangeStatusChEnd_Object = MibTableColumn
catmPVclAISRDIRangeStatusChEnd = _CatmPVclAISRDIRangeStatusChEnd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 7, 1, 4),
    _CatmPVclAISRDIRangeStatusChEnd_Type()
)
catmPVclAISRDIRangeStatusChEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclAISRDIRangeStatusChEnd.setStatus("current")
_CatmDownPVclRangeTable_Object = MibTable
catmDownPVclRangeTable = _CatmDownPVclRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 8)
)
if mibBuilder.loadTexts:
    catmDownPVclRangeTable.setStatus("current")
_CatmDownPVclRangeEntry_Object = MibTableRow
catmDownPVclRangeEntry = _CatmDownPVclRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 8, 1)
)
catmDownPVclRangeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "CISCO-ATM-PVCTRAP-EXTN-MIB", "catmStatusChangePVclRangeIndex"),
)
if mibBuilder.loadTexts:
    catmDownPVclRangeEntry.setStatus("current")


class _CatmDownPVclLowerRangeValue_Type(Integer32):
    """Custom type catmDownPVclLowerRangeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_CatmDownPVclLowerRangeValue_Type.__name__ = "Integer32"
_CatmDownPVclLowerRangeValue_Object = MibTableColumn
catmDownPVclLowerRangeValue = _CatmDownPVclLowerRangeValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 8, 1, 1),
    _CatmDownPVclLowerRangeValue_Type()
)
catmDownPVclLowerRangeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmDownPVclLowerRangeValue.setStatus("current")


class _CatmDownPVclHigherRangeValue_Type(Integer32):
    """Custom type catmDownPVclHigherRangeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_CatmDownPVclHigherRangeValue_Type.__name__ = "Integer32"
_CatmDownPVclHigherRangeValue_Object = MibTableColumn
catmDownPVclHigherRangeValue = _CatmDownPVclHigherRangeValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 8, 1, 2),
    _CatmDownPVclHigherRangeValue_Type()
)
catmDownPVclHigherRangeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmDownPVclHigherRangeValue.setStatus("current")
_CatmDownPVclRangeStart_Type = TimeStamp
_CatmDownPVclRangeStart_Object = MibTableColumn
catmDownPVclRangeStart = _CatmDownPVclRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 8, 1, 3),
    _CatmDownPVclRangeStart_Type()
)
catmDownPVclRangeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmDownPVclRangeStart.setStatus("current")
_CatmDownPVclRangeEnd_Type = TimeStamp
_CatmDownPVclRangeEnd_Object = MibTableColumn
catmDownPVclRangeEnd = _CatmDownPVclRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 8, 1, 4),
    _CatmDownPVclRangeEnd_Type()
)
catmDownPVclRangeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmDownPVclRangeEnd.setStatus("current")
_CatmPrevUpPVclRangeStart_Type = TimeStamp
_CatmPrevUpPVclRangeStart_Object = MibTableColumn
catmPrevUpPVclRangeStart = _CatmPrevUpPVclRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 8, 1, 5),
    _CatmPrevUpPVclRangeStart_Type()
)
catmPrevUpPVclRangeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPrevUpPVclRangeStart.setStatus("current")
_CatmPrevUpPVclRangeEnd_Type = TimeStamp
_CatmPrevUpPVclRangeEnd_Object = MibTableColumn
catmPrevUpPVclRangeEnd = _CatmPrevUpPVclRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 8, 1, 6),
    _CatmPrevUpPVclRangeEnd_Type()
)
catmPrevUpPVclRangeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPrevUpPVclRangeEnd.setStatus("current")
_CatmPVclRangeFailureReason_Type = CatmOAMFailureType
_CatmPVclRangeFailureReason_Object = MibTableColumn
catmPVclRangeFailureReason = _CatmPVclRangeFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 8, 1, 7),
    _CatmPVclRangeFailureReason_Type()
)
catmPVclRangeFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclRangeFailureReason.setStatus("current")
_CatmCurStatusUpPVclTable_Object = MibTable
catmCurStatusUpPVclTable = _CatmCurStatusUpPVclTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 9)
)
if mibBuilder.loadTexts:
    catmCurStatusUpPVclTable.setStatus("current")
_CatmCurStatusUpPVclEntry_Object = MibTableRow
catmCurStatusUpPVclEntry = _CatmCurStatusUpPVclEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 9, 1)
)
catmCurStatusUpPVclEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
)
if mibBuilder.loadTexts:
    catmCurStatusUpPVclEntry.setStatus("current")
_CatmPVclStatusUpTransition_Type = Gauge32
_CatmPVclStatusUpTransition_Object = MibTableColumn
catmPVclStatusUpTransition = _CatmPVclStatusUpTransition_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 9, 1, 1),
    _CatmPVclStatusUpTransition_Type()
)
catmPVclStatusUpTransition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclStatusUpTransition.setStatus("current")
_CatmPVclStatusUpStart_Type = TimeStamp
_CatmPVclStatusUpStart_Object = MibTableColumn
catmPVclStatusUpStart = _CatmPVclStatusUpStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 9, 1, 2),
    _CatmPVclStatusUpStart_Type()
)
catmPVclStatusUpStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclStatusUpStart.setStatus("current")
_CatmPVclStatusUpEnd_Type = TimeStamp
_CatmPVclStatusUpEnd_Object = MibTableColumn
catmPVclStatusUpEnd = _CatmPVclStatusUpEnd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 9, 1, 3),
    _CatmPVclStatusUpEnd_Type()
)
catmPVclStatusUpEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclStatusUpEnd.setStatus("current")
_CatmPVclSegCCStatusUpTransition_Type = Gauge32
_CatmPVclSegCCStatusUpTransition_Object = MibTableColumn
catmPVclSegCCStatusUpTransition = _CatmPVclSegCCStatusUpTransition_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 9, 1, 4),
    _CatmPVclSegCCStatusUpTransition_Type()
)
catmPVclSegCCStatusUpTransition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclSegCCStatusUpTransition.setStatus("current")
_CatmPVclSegCCStatusUpStart_Type = TimeStamp
_CatmPVclSegCCStatusUpStart_Object = MibTableColumn
catmPVclSegCCStatusUpStart = _CatmPVclSegCCStatusUpStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 9, 1, 5),
    _CatmPVclSegCCStatusUpStart_Type()
)
catmPVclSegCCStatusUpStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclSegCCStatusUpStart.setStatus("current")
_CatmPVclSegCCStatusUpEnd_Type = TimeStamp
_CatmPVclSegCCStatusUpEnd_Object = MibTableColumn
catmPVclSegCCStatusUpEnd = _CatmPVclSegCCStatusUpEnd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 9, 1, 6),
    _CatmPVclSegCCStatusUpEnd_Type()
)
catmPVclSegCCStatusUpEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclSegCCStatusUpEnd.setStatus("current")
_CatmPVclEndCCStatusUpTransition_Type = Gauge32
_CatmPVclEndCCStatusUpTransition_Object = MibTableColumn
catmPVclEndCCStatusUpTransition = _CatmPVclEndCCStatusUpTransition_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 9, 1, 7),
    _CatmPVclEndCCStatusUpTransition_Type()
)
catmPVclEndCCStatusUpTransition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclEndCCStatusUpTransition.setStatus("current")
_CatmPVclEndCCStatusUpStart_Type = TimeStamp
_CatmPVclEndCCStatusUpStart_Object = MibTableColumn
catmPVclEndCCStatusUpStart = _CatmPVclEndCCStatusUpStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 9, 1, 8),
    _CatmPVclEndCCStatusUpStart_Type()
)
catmPVclEndCCStatusUpStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclEndCCStatusUpStart.setStatus("current")
_CatmPVclEndCCStatusUpEnd_Type = TimeStamp
_CatmPVclEndCCStatusUpEnd_Object = MibTableColumn
catmPVclEndCCStatusUpEnd = _CatmPVclEndCCStatusUpEnd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 9, 1, 9),
    _CatmPVclEndCCStatusUpEnd_Type()
)
catmPVclEndCCStatusUpEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclEndCCStatusUpEnd.setStatus("current")
_CatmPVclAISRDIStatusUpTransition_Type = Gauge32
_CatmPVclAISRDIStatusUpTransition_Object = MibTableColumn
catmPVclAISRDIStatusUpTransition = _CatmPVclAISRDIStatusUpTransition_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 9, 1, 10),
    _CatmPVclAISRDIStatusUpTransition_Type()
)
catmPVclAISRDIStatusUpTransition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclAISRDIStatusUpTransition.setStatus("current")
_CatmPVclAISRDIStatusUpStart_Type = TimeStamp
_CatmPVclAISRDIStatusUpStart_Object = MibTableColumn
catmPVclAISRDIStatusUpStart = _CatmPVclAISRDIStatusUpStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 9, 1, 11),
    _CatmPVclAISRDIStatusUpStart_Type()
)
catmPVclAISRDIStatusUpStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclAISRDIStatusUpStart.setStatus("current")
_CatmPVclAISRDIStatusUpEnd_Type = TimeStamp
_CatmPVclAISRDIStatusUpEnd_Object = MibTableColumn
catmPVclAISRDIStatusUpEnd = _CatmPVclAISRDIStatusUpEnd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 9, 1, 12),
    _CatmPVclAISRDIStatusUpEnd_Type()
)
catmPVclAISRDIStatusUpEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclAISRDIStatusUpEnd.setStatus("current")
_CatmPVclCurRecoverTime_Type = TimeStamp
_CatmPVclCurRecoverTime_Object = MibTableColumn
catmPVclCurRecoverTime = _CatmPVclCurRecoverTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 9, 1, 13),
    _CatmPVclCurRecoverTime_Type()
)
catmPVclCurRecoverTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclCurRecoverTime.setStatus("current")
_CatmPVclPrevFailTime_Type = TimeStamp
_CatmPVclPrevFailTime_Object = MibTableColumn
catmPVclPrevFailTime = _CatmPVclPrevFailTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 9, 1, 14),
    _CatmPVclPrevFailTime_Type()
)
catmPVclPrevFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclPrevFailTime.setStatus("current")
_CatmPVclRecoveryReason_Type = CatmOAMRecoveryType
_CatmPVclRecoveryReason_Object = MibTableColumn
catmPVclRecoveryReason = _CatmPVclRecoveryReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 9, 1, 15),
    _CatmPVclRecoveryReason_Type()
)
catmPVclRecoveryReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclRecoveryReason.setStatus("current")
_CatmPVclSegAISRDIStatUpTransit_Type = Gauge32
_CatmPVclSegAISRDIStatUpTransit_Object = MibTableColumn
catmPVclSegAISRDIStatUpTransit = _CatmPVclSegAISRDIStatUpTransit_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 9, 1, 16),
    _CatmPVclSegAISRDIStatUpTransit_Type()
)
catmPVclSegAISRDIStatUpTransit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclSegAISRDIStatUpTransit.setStatus("current")
_CatmPVclSegAISRDIStatUpStart_Type = TimeStamp
_CatmPVclSegAISRDIStatUpStart_Object = MibTableColumn
catmPVclSegAISRDIStatUpStart = _CatmPVclSegAISRDIStatUpStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 9, 1, 17),
    _CatmPVclSegAISRDIStatUpStart_Type()
)
catmPVclSegAISRDIStatUpStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclSegAISRDIStatUpStart.setStatus("current")
_CatmPVclSegAISRDIStatUpEnd_Type = TimeStamp
_CatmPVclSegAISRDIStatUpEnd_Object = MibTableColumn
catmPVclSegAISRDIStatUpEnd = _CatmPVclSegAISRDIStatUpEnd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 9, 1, 18),
    _CatmPVclSegAISRDIStatUpEnd_Type()
)
catmPVclSegAISRDIStatUpEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclSegAISRDIStatUpEnd.setStatus("current")
_CatmPVclEndAISRDIStatUpTransit_Type = Gauge32
_CatmPVclEndAISRDIStatUpTransit_Object = MibTableColumn
catmPVclEndAISRDIStatUpTransit = _CatmPVclEndAISRDIStatUpTransit_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 9, 1, 19),
    _CatmPVclEndAISRDIStatUpTransit_Type()
)
catmPVclEndAISRDIStatUpTransit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclEndAISRDIStatUpTransit.setStatus("current")
_CatmPVclEndAISRDIStatUpStart_Type = TimeStamp
_CatmPVclEndAISRDIStatUpStart_Object = MibTableColumn
catmPVclEndAISRDIStatUpStart = _CatmPVclEndAISRDIStatUpStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 9, 1, 20),
    _CatmPVclEndAISRDIStatUpStart_Type()
)
catmPVclEndAISRDIStatUpStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclEndAISRDIStatUpStart.setStatus("current")
_CatmPVclEndAISRDIStatUpEnd_Type = TimeStamp
_CatmPVclEndAISRDIStatUpEnd_Object = MibTableColumn
catmPVclEndAISRDIStatUpEnd = _CatmPVclEndAISRDIStatUpEnd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 9, 1, 21),
    _CatmPVclEndAISRDIStatUpEnd_Type()
)
catmPVclEndAISRDIStatUpEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclEndAISRDIStatUpEnd.setStatus("current")
_CatmStatusUpPVclRangeTable_Object = MibTable
catmStatusUpPVclRangeTable = _CatmStatusUpPVclRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 10)
)
if mibBuilder.loadTexts:
    catmStatusUpPVclRangeTable.setStatus("current")
_CatmStatusUpPVclRangeEntry_Object = MibTableRow
catmStatusUpPVclRangeEntry = _CatmStatusUpPVclRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 10, 1)
)
catmStatusUpPVclRangeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "CISCO-ATM-PVCTRAP-EXTN-MIB", "catmStatusChangePVclRangeIndex"),
)
if mibBuilder.loadTexts:
    catmStatusUpPVclRangeEntry.setStatus("current")


class _CatmPVclUpLowerRangeValue_Type(Integer32):
    """Custom type catmPVclUpLowerRangeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_CatmPVclUpLowerRangeValue_Type.__name__ = "Integer32"
_CatmPVclUpLowerRangeValue_Object = MibTableColumn
catmPVclUpLowerRangeValue = _CatmPVclUpLowerRangeValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 10, 1, 1),
    _CatmPVclUpLowerRangeValue_Type()
)
catmPVclUpLowerRangeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclUpLowerRangeValue.setStatus("current")


class _CatmPVclUpHigherRangeValue_Type(Integer32):
    """Custom type catmPVclUpHigherRangeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_CatmPVclUpHigherRangeValue_Type.__name__ = "Integer32"
_CatmPVclUpHigherRangeValue_Object = MibTableColumn
catmPVclUpHigherRangeValue = _CatmPVclUpHigherRangeValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 10, 1, 2),
    _CatmPVclUpHigherRangeValue_Type()
)
catmPVclUpHigherRangeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclUpHigherRangeValue.setStatus("current")
_CatmPVclRangeStatusUpStart_Type = TimeStamp
_CatmPVclRangeStatusUpStart_Object = MibTableColumn
catmPVclRangeStatusUpStart = _CatmPVclRangeStatusUpStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 10, 1, 3),
    _CatmPVclRangeStatusUpStart_Type()
)
catmPVclRangeStatusUpStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclRangeStatusUpStart.setStatus("current")
_CatmPVclRangeStatusUpEnd_Type = TimeStamp
_CatmPVclRangeStatusUpEnd_Object = MibTableColumn
catmPVclRangeStatusUpEnd = _CatmPVclRangeStatusUpEnd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 10, 1, 4),
    _CatmPVclRangeStatusUpEnd_Type()
)
catmPVclRangeStatusUpEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclRangeStatusUpEnd.setStatus("current")
_CatmSegCCStatusUpPVclRangeTable_Object = MibTable
catmSegCCStatusUpPVclRangeTable = _CatmSegCCStatusUpPVclRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 11)
)
if mibBuilder.loadTexts:
    catmSegCCStatusUpPVclRangeTable.setStatus("current")
_CatmSegCCStatusUpPVclRangeEntry_Object = MibTableRow
catmSegCCStatusUpPVclRangeEntry = _CatmSegCCStatusUpPVclRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 11, 1)
)
catmSegCCStatusUpPVclRangeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "CISCO-ATM-PVCTRAP-EXTN-MIB", "catmStatusChangePVclRangeIndex"),
)
if mibBuilder.loadTexts:
    catmSegCCStatusUpPVclRangeEntry.setStatus("current")


class _CatmPVclSegCCUpLowerRangeValue_Type(Integer32):
    """Custom type catmPVclSegCCUpLowerRangeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_CatmPVclSegCCUpLowerRangeValue_Type.__name__ = "Integer32"
_CatmPVclSegCCUpLowerRangeValue_Object = MibTableColumn
catmPVclSegCCUpLowerRangeValue = _CatmPVclSegCCUpLowerRangeValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 11, 1, 1),
    _CatmPVclSegCCUpLowerRangeValue_Type()
)
catmPVclSegCCUpLowerRangeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclSegCCUpLowerRangeValue.setStatus("current")


class _CatmPVclSegCCUpHigherRangeValue_Type(Integer32):
    """Custom type catmPVclSegCCUpHigherRangeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_CatmPVclSegCCUpHigherRangeValue_Type.__name__ = "Integer32"
_CatmPVclSegCCUpHigherRangeValue_Object = MibTableColumn
catmPVclSegCCUpHigherRangeValue = _CatmPVclSegCCUpHigherRangeValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 11, 1, 2),
    _CatmPVclSegCCUpHigherRangeValue_Type()
)
catmPVclSegCCUpHigherRangeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclSegCCUpHigherRangeValue.setStatus("current")
_CatmPVclSegCCRangeStatusUpStart_Type = TimeStamp
_CatmPVclSegCCRangeStatusUpStart_Object = MibTableColumn
catmPVclSegCCRangeStatusUpStart = _CatmPVclSegCCRangeStatusUpStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 11, 1, 3),
    _CatmPVclSegCCRangeStatusUpStart_Type()
)
catmPVclSegCCRangeStatusUpStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclSegCCRangeStatusUpStart.setStatus("current")
_CatmPVclSegCCRangeStatusUpEnd_Type = TimeStamp
_CatmPVclSegCCRangeStatusUpEnd_Object = MibTableColumn
catmPVclSegCCRangeStatusUpEnd = _CatmPVclSegCCRangeStatusUpEnd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 11, 1, 4),
    _CatmPVclSegCCRangeStatusUpEnd_Type()
)
catmPVclSegCCRangeStatusUpEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclSegCCRangeStatusUpEnd.setStatus("current")
_CatmEndCCStatusUpPVclRangeTable_Object = MibTable
catmEndCCStatusUpPVclRangeTable = _CatmEndCCStatusUpPVclRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 12)
)
if mibBuilder.loadTexts:
    catmEndCCStatusUpPVclRangeTable.setStatus("current")
_CatmEndCCStatusUpPVclRangeEntry_Object = MibTableRow
catmEndCCStatusUpPVclRangeEntry = _CatmEndCCStatusUpPVclRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 12, 1)
)
catmEndCCStatusUpPVclRangeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "CISCO-ATM-PVCTRAP-EXTN-MIB", "catmStatusChangePVclRangeIndex"),
)
if mibBuilder.loadTexts:
    catmEndCCStatusUpPVclRangeEntry.setStatus("current")


class _CatmPVclEndCCUpLowerRangeValue_Type(Integer32):
    """Custom type catmPVclEndCCUpLowerRangeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_CatmPVclEndCCUpLowerRangeValue_Type.__name__ = "Integer32"
_CatmPVclEndCCUpLowerRangeValue_Object = MibTableColumn
catmPVclEndCCUpLowerRangeValue = _CatmPVclEndCCUpLowerRangeValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 12, 1, 1),
    _CatmPVclEndCCUpLowerRangeValue_Type()
)
catmPVclEndCCUpLowerRangeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclEndCCUpLowerRangeValue.setStatus("current")


class _CatmPVclEndCCUpHigherRangeValue_Type(Integer32):
    """Custom type catmPVclEndCCUpHigherRangeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_CatmPVclEndCCUpHigherRangeValue_Type.__name__ = "Integer32"
_CatmPVclEndCCUpHigherRangeValue_Object = MibTableColumn
catmPVclEndCCUpHigherRangeValue = _CatmPVclEndCCUpHigherRangeValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 12, 1, 2),
    _CatmPVclEndCCUpHigherRangeValue_Type()
)
catmPVclEndCCUpHigherRangeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclEndCCUpHigherRangeValue.setStatus("current")
_CatmPVclEndCCRangeStatusUpStart_Type = TimeStamp
_CatmPVclEndCCRangeStatusUpStart_Object = MibTableColumn
catmPVclEndCCRangeStatusUpStart = _CatmPVclEndCCRangeStatusUpStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 12, 1, 3),
    _CatmPVclEndCCRangeStatusUpStart_Type()
)
catmPVclEndCCRangeStatusUpStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclEndCCRangeStatusUpStart.setStatus("current")
_CatmPVclEndCCRangeStatusUpEnd_Type = TimeStamp
_CatmPVclEndCCRangeStatusUpEnd_Object = MibTableColumn
catmPVclEndCCRangeStatusUpEnd = _CatmPVclEndCCRangeStatusUpEnd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 12, 1, 4),
    _CatmPVclEndCCRangeStatusUpEnd_Type()
)
catmPVclEndCCRangeStatusUpEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclEndCCRangeStatusUpEnd.setStatus("current")
_CatmAISRDIStatusUpPVclRangeTable_Object = MibTable
catmAISRDIStatusUpPVclRangeTable = _CatmAISRDIStatusUpPVclRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 13)
)
if mibBuilder.loadTexts:
    catmAISRDIStatusUpPVclRangeTable.setStatus("current")
_CatmAISRDIStatusUpPVclRangeEntry_Object = MibTableRow
catmAISRDIStatusUpPVclRangeEntry = _CatmAISRDIStatusUpPVclRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 13, 1)
)
catmAISRDIStatusUpPVclRangeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "CISCO-ATM-PVCTRAP-EXTN-MIB", "catmStatusChangePVclRangeIndex"),
)
if mibBuilder.loadTexts:
    catmAISRDIStatusUpPVclRangeEntry.setStatus("current")


class _CatmPVclAISRDIUpLowerRangeValue_Type(Integer32):
    """Custom type catmPVclAISRDIUpLowerRangeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_CatmPVclAISRDIUpLowerRangeValue_Type.__name__ = "Integer32"
_CatmPVclAISRDIUpLowerRangeValue_Object = MibTableColumn
catmPVclAISRDIUpLowerRangeValue = _CatmPVclAISRDIUpLowerRangeValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 13, 1, 1),
    _CatmPVclAISRDIUpLowerRangeValue_Type()
)
catmPVclAISRDIUpLowerRangeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclAISRDIUpLowerRangeValue.setStatus("current")


class _CatmPVclAISRDIUpHigherRangeValue_Type(Integer32):
    """Custom type catmPVclAISRDIUpHigherRangeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_CatmPVclAISRDIUpHigherRangeValue_Type.__name__ = "Integer32"
_CatmPVclAISRDIUpHigherRangeValue_Object = MibTableColumn
catmPVclAISRDIUpHigherRangeValue = _CatmPVclAISRDIUpHigherRangeValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 13, 1, 2),
    _CatmPVclAISRDIUpHigherRangeValue_Type()
)
catmPVclAISRDIUpHigherRangeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclAISRDIUpHigherRangeValue.setStatus("current")
_CatmPVclAISRDIRangeStatusUpStart_Type = TimeStamp
_CatmPVclAISRDIRangeStatusUpStart_Object = MibTableColumn
catmPVclAISRDIRangeStatusUpStart = _CatmPVclAISRDIRangeStatusUpStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 13, 1, 3),
    _CatmPVclAISRDIRangeStatusUpStart_Type()
)
catmPVclAISRDIRangeStatusUpStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclAISRDIRangeStatusUpStart.setStatus("current")
_CatmPVclAISRDIRangeStatusUpEnd_Type = TimeStamp
_CatmPVclAISRDIRangeStatusUpEnd_Object = MibTableColumn
catmPVclAISRDIRangeStatusUpEnd = _CatmPVclAISRDIRangeStatusUpEnd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 13, 1, 4),
    _CatmPVclAISRDIRangeStatusUpEnd_Type()
)
catmPVclAISRDIRangeStatusUpEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclAISRDIRangeStatusUpEnd.setStatus("current")
_CatmUpPVclRangeTable_Object = MibTable
catmUpPVclRangeTable = _CatmUpPVclRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 14)
)
if mibBuilder.loadTexts:
    catmUpPVclRangeTable.setStatus("current")
_CatmUpPVclRangeEntry_Object = MibTableRow
catmUpPVclRangeEntry = _CatmUpPVclRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 14, 1)
)
catmUpPVclRangeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "CISCO-ATM-PVCTRAP-EXTN-MIB", "catmStatusChangePVclRangeIndex"),
)
if mibBuilder.loadTexts:
    catmUpPVclRangeEntry.setStatus("current")


class _CatmUpPVclLowerRangeValue_Type(Integer32):
    """Custom type catmUpPVclLowerRangeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_CatmUpPVclLowerRangeValue_Type.__name__ = "Integer32"
_CatmUpPVclLowerRangeValue_Object = MibTableColumn
catmUpPVclLowerRangeValue = _CatmUpPVclLowerRangeValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 14, 1, 1),
    _CatmUpPVclLowerRangeValue_Type()
)
catmUpPVclLowerRangeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmUpPVclLowerRangeValue.setStatus("current")


class _CatmUpPVclHigherRangeValue_Type(Integer32):
    """Custom type catmUpPVclHigherRangeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_CatmUpPVclHigherRangeValue_Type.__name__ = "Integer32"
_CatmUpPVclHigherRangeValue_Object = MibTableColumn
catmUpPVclHigherRangeValue = _CatmUpPVclHigherRangeValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 14, 1, 2),
    _CatmUpPVclHigherRangeValue_Type()
)
catmUpPVclHigherRangeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmUpPVclHigherRangeValue.setStatus("current")
_CatmUpPVclRangeStart_Type = TimeStamp
_CatmUpPVclRangeStart_Object = MibTableColumn
catmUpPVclRangeStart = _CatmUpPVclRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 14, 1, 3),
    _CatmUpPVclRangeStart_Type()
)
catmUpPVclRangeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmUpPVclRangeStart.setStatus("current")
_CatmUpPVclRangeEnd_Type = TimeStamp
_CatmUpPVclRangeEnd_Object = MibTableColumn
catmUpPVclRangeEnd = _CatmUpPVclRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 14, 1, 4),
    _CatmUpPVclRangeEnd_Type()
)
catmUpPVclRangeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmUpPVclRangeEnd.setStatus("current")
_CatmPrevDownPVclRangeStart_Type = TimeStamp
_CatmPrevDownPVclRangeStart_Object = MibTableColumn
catmPrevDownPVclRangeStart = _CatmPrevDownPVclRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 14, 1, 5),
    _CatmPrevDownPVclRangeStart_Type()
)
catmPrevDownPVclRangeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPrevDownPVclRangeStart.setStatus("current")
_CatmPrevDownPVclRangeEnd_Type = TimeStamp
_CatmPrevDownPVclRangeEnd_Object = MibTableColumn
catmPrevDownPVclRangeEnd = _CatmPrevDownPVclRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 14, 1, 6),
    _CatmPrevDownPVclRangeEnd_Type()
)
catmPrevDownPVclRangeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPrevDownPVclRangeEnd.setStatus("current")
_CatmPVclRangeRecoveryReason_Type = CatmOAMRecoveryType
_CatmPVclRangeRecoveryReason_Object = MibTableColumn
catmPVclRangeRecoveryReason = _CatmPVclRangeRecoveryReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 14, 1, 7),
    _CatmPVclRangeRecoveryReason_Type()
)
catmPVclRangeRecoveryReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclRangeRecoveryReason.setStatus("current")
_CatmSegAISRDIStatChPVclRngeTable_Object = MibTable
catmSegAISRDIStatChPVclRngeTable = _CatmSegAISRDIStatChPVclRngeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 15)
)
if mibBuilder.loadTexts:
    catmSegAISRDIStatChPVclRngeTable.setStatus("current")
_CatmSegAISRDIStatChPVclRngeEntry_Object = MibTableRow
catmSegAISRDIStatChPVclRngeEntry = _CatmSegAISRDIStatChPVclRngeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 15, 1)
)
catmSegAISRDIStatChPVclRngeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "CISCO-ATM-PVCTRAP-EXTN-MIB", "catmStatusChangePVclRangeIndex"),
)
if mibBuilder.loadTexts:
    catmSegAISRDIStatChPVclRngeEntry.setStatus("current")


class _CatmPVclSegAISRDILowerRangeValue_Type(Unsigned32):
    """Custom type catmPVclSegAISRDILowerRangeValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_CatmPVclSegAISRDILowerRangeValue_Type.__name__ = "Unsigned32"
_CatmPVclSegAISRDILowerRangeValue_Object = MibTableColumn
catmPVclSegAISRDILowerRangeValue = _CatmPVclSegAISRDILowerRangeValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 15, 1, 1),
    _CatmPVclSegAISRDILowerRangeValue_Type()
)
catmPVclSegAISRDILowerRangeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclSegAISRDILowerRangeValue.setStatus("current")


class _CatmPVclSegAISRDIHigherRangeValue_Type(Unsigned32):
    """Custom type catmPVclSegAISRDIHigherRangeValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_CatmPVclSegAISRDIHigherRangeValue_Type.__name__ = "Unsigned32"
_CatmPVclSegAISRDIHigherRangeValue_Object = MibTableColumn
catmPVclSegAISRDIHigherRangeValue = _CatmPVclSegAISRDIHigherRangeValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 15, 1, 2),
    _CatmPVclSegAISRDIHigherRangeValue_Type()
)
catmPVclSegAISRDIHigherRangeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclSegAISRDIHigherRangeValue.setStatus("current")
_CatmPVclSegAISRDIRangeStatChStart_Type = TimeStamp
_CatmPVclSegAISRDIRangeStatChStart_Object = MibTableColumn
catmPVclSegAISRDIRangeStatChStart = _CatmPVclSegAISRDIRangeStatChStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 15, 1, 3),
    _CatmPVclSegAISRDIRangeStatChStart_Type()
)
catmPVclSegAISRDIRangeStatChStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclSegAISRDIRangeStatChStart.setStatus("current")
_CatmPVclSegAISRDIRangeStatChEnd_Type = TimeStamp
_CatmPVclSegAISRDIRangeStatChEnd_Object = MibTableColumn
catmPVclSegAISRDIRangeStatChEnd = _CatmPVclSegAISRDIRangeStatChEnd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 15, 1, 4),
    _CatmPVclSegAISRDIRangeStatChEnd_Type()
)
catmPVclSegAISRDIRangeStatChEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclSegAISRDIRangeStatChEnd.setStatus("current")
_CatmEndAISRDIStatChPVclRngeTable_Object = MibTable
catmEndAISRDIStatChPVclRngeTable = _CatmEndAISRDIStatChPVclRngeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 16)
)
if mibBuilder.loadTexts:
    catmEndAISRDIStatChPVclRngeTable.setStatus("current")
_CatmEndAISRDIStatChPVclRngeEntry_Object = MibTableRow
catmEndAISRDIStatChPVclRngeEntry = _CatmEndAISRDIStatChPVclRngeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 16, 1)
)
catmEndAISRDIStatChPVclRngeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "CISCO-ATM-PVCTRAP-EXTN-MIB", "catmStatusChangePVclRangeIndex"),
)
if mibBuilder.loadTexts:
    catmEndAISRDIStatChPVclRngeEntry.setStatus("current")


class _CatmPVclEndAISRDILowerRangeValue_Type(Unsigned32):
    """Custom type catmPVclEndAISRDILowerRangeValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_CatmPVclEndAISRDILowerRangeValue_Type.__name__ = "Unsigned32"
_CatmPVclEndAISRDILowerRangeValue_Object = MibTableColumn
catmPVclEndAISRDILowerRangeValue = _CatmPVclEndAISRDILowerRangeValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 16, 1, 1),
    _CatmPVclEndAISRDILowerRangeValue_Type()
)
catmPVclEndAISRDILowerRangeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclEndAISRDILowerRangeValue.setStatus("current")


class _CatmPVclEndAISRDIHigherRngeValue_Type(Unsigned32):
    """Custom type catmPVclEndAISRDIHigherRngeValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_CatmPVclEndAISRDIHigherRngeValue_Type.__name__ = "Unsigned32"
_CatmPVclEndAISRDIHigherRngeValue_Object = MibTableColumn
catmPVclEndAISRDIHigherRngeValue = _CatmPVclEndAISRDIHigherRngeValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 16, 1, 2),
    _CatmPVclEndAISRDIHigherRngeValue_Type()
)
catmPVclEndAISRDIHigherRngeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclEndAISRDIHigherRngeValue.setStatus("current")
_CatmPVclEndAISRDIRngeStatChStart_Type = TimeStamp
_CatmPVclEndAISRDIRngeStatChStart_Object = MibTableColumn
catmPVclEndAISRDIRngeStatChStart = _CatmPVclEndAISRDIRngeStatChStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 16, 1, 3),
    _CatmPVclEndAISRDIRngeStatChStart_Type()
)
catmPVclEndAISRDIRngeStatChStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclEndAISRDIRngeStatChStart.setStatus("current")
_CatmPVclEndAISRDIRangeStatChEnd_Type = TimeStamp
_CatmPVclEndAISRDIRangeStatChEnd_Object = MibTableColumn
catmPVclEndAISRDIRangeStatChEnd = _CatmPVclEndAISRDIRangeStatChEnd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 16, 1, 4),
    _CatmPVclEndAISRDIRangeStatChEnd_Type()
)
catmPVclEndAISRDIRangeStatChEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclEndAISRDIRangeStatChEnd.setStatus("current")
_CatmSegAISRDIStatUpPVclRngeTable_Object = MibTable
catmSegAISRDIStatUpPVclRngeTable = _CatmSegAISRDIStatUpPVclRngeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 17)
)
if mibBuilder.loadTexts:
    catmSegAISRDIStatUpPVclRngeTable.setStatus("current")
_CatmSegAISRDIStatUpPVclRngeEntry_Object = MibTableRow
catmSegAISRDIStatUpPVclRngeEntry = _CatmSegAISRDIStatUpPVclRngeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 17, 1)
)
catmSegAISRDIStatUpPVclRngeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "CISCO-ATM-PVCTRAP-EXTN-MIB", "catmStatusChangePVclRangeIndex"),
)
if mibBuilder.loadTexts:
    catmSegAISRDIStatUpPVclRngeEntry.setStatus("current")


class _CatmPVclSegAISRDIUpLowerRangeVal_Type(Unsigned32):
    """Custom type catmPVclSegAISRDIUpLowerRangeVal based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_CatmPVclSegAISRDIUpLowerRangeVal_Type.__name__ = "Unsigned32"
_CatmPVclSegAISRDIUpLowerRangeVal_Object = MibTableColumn
catmPVclSegAISRDIUpLowerRangeVal = _CatmPVclSegAISRDIUpLowerRangeVal_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 17, 1, 1),
    _CatmPVclSegAISRDIUpLowerRangeVal_Type()
)
catmPVclSegAISRDIUpLowerRangeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclSegAISRDIUpLowerRangeVal.setStatus("current")


class _CatmPVclSegAISRDIUpHigherRngeVal_Type(Unsigned32):
    """Custom type catmPVclSegAISRDIUpHigherRngeVal based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_CatmPVclSegAISRDIUpHigherRngeVal_Type.__name__ = "Unsigned32"
_CatmPVclSegAISRDIUpHigherRngeVal_Object = MibTableColumn
catmPVclSegAISRDIUpHigherRngeVal = _CatmPVclSegAISRDIUpHigherRngeVal_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 17, 1, 2),
    _CatmPVclSegAISRDIUpHigherRngeVal_Type()
)
catmPVclSegAISRDIUpHigherRngeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclSegAISRDIUpHigherRngeVal.setStatus("current")
_CatmPVclSegAISRDIRngeStatUpStart_Type = TimeStamp
_CatmPVclSegAISRDIRngeStatUpStart_Object = MibTableColumn
catmPVclSegAISRDIRngeStatUpStart = _CatmPVclSegAISRDIRngeStatUpStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 17, 1, 3),
    _CatmPVclSegAISRDIRngeStatUpStart_Type()
)
catmPVclSegAISRDIRngeStatUpStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclSegAISRDIRngeStatUpStart.setStatus("current")
_CatmPVclSegAISRDIRangeStatUpEnd_Type = TimeStamp
_CatmPVclSegAISRDIRangeStatUpEnd_Object = MibTableColumn
catmPVclSegAISRDIRangeStatUpEnd = _CatmPVclSegAISRDIRangeStatUpEnd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 17, 1, 4),
    _CatmPVclSegAISRDIRangeStatUpEnd_Type()
)
catmPVclSegAISRDIRangeStatUpEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclSegAISRDIRangeStatUpEnd.setStatus("current")
_CatmEndAISRDIStatUpPVclRngeTable_Object = MibTable
catmEndAISRDIStatUpPVclRngeTable = _CatmEndAISRDIStatUpPVclRngeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 18)
)
if mibBuilder.loadTexts:
    catmEndAISRDIStatUpPVclRngeTable.setStatus("current")
_CatmEndAISRDIStatUpPVclRngeEntry_Object = MibTableRow
catmEndAISRDIStatUpPVclRngeEntry = _CatmEndAISRDIStatUpPVclRngeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 18, 1)
)
catmEndAISRDIStatUpPVclRngeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "CISCO-ATM-PVCTRAP-EXTN-MIB", "catmStatusChangePVclRangeIndex"),
)
if mibBuilder.loadTexts:
    catmEndAISRDIStatUpPVclRngeEntry.setStatus("current")


class _CatmPVclEndAISRDIUpLowerRangeVal_Type(Unsigned32):
    """Custom type catmPVclEndAISRDIUpLowerRangeVal based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_CatmPVclEndAISRDIUpLowerRangeVal_Type.__name__ = "Unsigned32"
_CatmPVclEndAISRDIUpLowerRangeVal_Object = MibTableColumn
catmPVclEndAISRDIUpLowerRangeVal = _CatmPVclEndAISRDIUpLowerRangeVal_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 18, 1, 1),
    _CatmPVclEndAISRDIUpLowerRangeVal_Type()
)
catmPVclEndAISRDIUpLowerRangeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclEndAISRDIUpLowerRangeVal.setStatus("current")


class _CatmPVclEndAISRDIUpHigherRngeVal_Type(Unsigned32):
    """Custom type catmPVclEndAISRDIUpHigherRngeVal based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_CatmPVclEndAISRDIUpHigherRngeVal_Type.__name__ = "Unsigned32"
_CatmPVclEndAISRDIUpHigherRngeVal_Object = MibTableColumn
catmPVclEndAISRDIUpHigherRngeVal = _CatmPVclEndAISRDIUpHigherRngeVal_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 18, 1, 2),
    _CatmPVclEndAISRDIUpHigherRngeVal_Type()
)
catmPVclEndAISRDIUpHigherRngeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclEndAISRDIUpHigherRngeVal.setStatus("current")
_CatmPVclEndAISRDIRngeStatUpStart_Type = TimeStamp
_CatmPVclEndAISRDIRngeStatUpStart_Object = MibTableColumn
catmPVclEndAISRDIRngeStatUpStart = _CatmPVclEndAISRDIRngeStatUpStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 18, 1, 3),
    _CatmPVclEndAISRDIRngeStatUpStart_Type()
)
catmPVclEndAISRDIRngeStatUpStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclEndAISRDIRngeStatUpStart.setStatus("current")
_CatmPVclEndAISRDIRangeStatUpEnd_Type = TimeStamp
_CatmPVclEndAISRDIRangeStatUpEnd_Object = MibTableColumn
catmPVclEndAISRDIRangeStatUpEnd = _CatmPVclEndAISRDIRangeStatUpEnd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 1, 18, 1, 4),
    _CatmPVclEndAISRDIRangeStatUpEnd_Type()
)
catmPVclEndAISRDIRangeStatUpEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmPVclEndAISRDIRangeStatUpEnd.setStatus("current")
_CAtmPvcTrapExtnMIBNotifPrefix_ObjectIdentity = ObjectIdentity
cAtmPvcTrapExtnMIBNotifPrefix = _CAtmPvcTrapExtnMIBNotifPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 2)
)
_CAtmPvcTrapExtnMIBNotif_ObjectIdentity = ObjectIdentity
cAtmPvcTrapExtnMIBNotif = _CAtmPvcTrapExtnMIBNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 2, 0)
)
_CiscoAtmPvcTrapExtnMIBConformance_ObjectIdentity = ObjectIdentity
ciscoAtmPvcTrapExtnMIBConformance = _CiscoAtmPvcTrapExtnMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 3)
)
_CiscoAtmPvcTrapExtnMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoAtmPvcTrapExtnMIBCompliances = _CiscoAtmPvcTrapExtnMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 3, 1)
)
_CiscoAtmPvcTrapExtnMIBGroups_ObjectIdentity = ObjectIdentity
ciscoAtmPvcTrapExtnMIBGroups = _CiscoAtmPvcTrapExtnMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 3, 2)
)
atmInterfaceConfEntry.registerAugmentions(
    ("CISCO-ATM-PVCTRAP-EXTN-MIB",
     "catmInterfaceExt2Entry")
)
catmInterfaceExt2Entry.setIndexNames(*atmInterfaceConfEntry.getIndexNames())

# Managed Objects groups

ciscoAtmPvcTrapExtnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 3, 2, 1)
)
ciscoAtmPvcTrapExtnGroup.setObjects(
      *(("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfOAMFailedPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfCurrentOAMFailingPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfSegCCOAMFailedPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfCurSegCCOAMFailingPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfEndCCOAMFailedPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfCurEndCCOAMFailingPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfAISRDIOAMFailedPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfCurAISRDIOAMFailingPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfAnyOAMFailedPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfCurAnyOAMFailingPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfTypeOfOAMFailure"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfCurrentlyDownToUpPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclLowerRangeValue"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclHigherRangeValue"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclRangeStatusChangeStart"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclRangeStatusChangeEnd"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclStatusTransition"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclStatusChangeStart"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclStatusChangeEnd"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclSegCCLowerRangeValue"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclSegCCHigherRangeValue"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclSegCCRangeStatusChStart"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclSegCCRangeStatusChEnd"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclSegCCStatusTransition"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclSegCCStatusChangeStart"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclSegCCStatusChangeEnd"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclEndCCLowerRangeValue"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclEndCCHigherRangeValue"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclEndCCRangeStatusChStart"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclEndCCRangeStatusChEnd"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclEndCCStatusTransition"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclEndCCStatusChangeStart"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclEndCCStatusChangeEnd"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclAISRDILowerRangeValue"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclAISRDIHigherRangeValue"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclAISRDIRangeStatusChStart"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclAISRDIRangeStatusChEnd"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclAISRDIStatusTransition"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclAISRDIStatusChangeStart"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclAISRDIStatusChangeEnd"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfOAMRcovedPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfCurrentOAMRcovingPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfSegCCOAMRcovedPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfCurSegCCOAMRcovingPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfEndCCOAMRcovedPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfCurEndCCOAMRcovingPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfAISRDIOAMRcovedPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfCurAISRDIOAMRcovingPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfAnyOAMRcovedPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfCurAnyOAMRcovingPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfTypeOfOAMRecover"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclCurFailTime"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclPrevRecoverTime"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclFailureReason"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmDownPVclLowerRangeValue"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmDownPVclHigherRangeValue"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmDownPVclRangeStart"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmDownPVclRangeEnd"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPrevUpPVclRangeStart"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPrevUpPVclRangeEnd"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclRangeFailureReason"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclStatusUpTransition"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclStatusUpStart"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclStatusUpEnd"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclSegCCStatusUpTransition"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclSegCCStatusUpStart"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclSegCCStatusUpEnd"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclEndCCStatusUpTransition"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclEndCCStatusUpStart"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclEndCCStatusUpEnd"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclAISRDIStatusUpTransition"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclAISRDIStatusUpStart"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclAISRDIStatusUpEnd"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclCurRecoverTime"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclPrevFailTime"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclRecoveryReason"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclUpLowerRangeValue"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclUpHigherRangeValue"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclRangeStatusUpStart"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclRangeStatusUpEnd"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclSegCCUpLowerRangeValue"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclSegCCUpHigherRangeValue"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclSegCCRangeStatusUpStart"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclSegCCRangeStatusUpEnd"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclEndCCUpLowerRangeValue"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclEndCCUpHigherRangeValue"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclEndCCRangeStatusUpStart"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclEndCCRangeStatusUpEnd"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclAISRDIUpLowerRangeValue"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclAISRDIUpHigherRangeValue"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclAISRDIRangeStatusUpStart"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclAISRDIRangeStatusUpEnd"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmUpPVclLowerRangeValue"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmUpPVclHigherRangeValue"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmUpPVclRangeStart"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmUpPVclRangeEnd"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPrevDownPVclRangeStart"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPrevDownPVclRangeEnd"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclRangeRecoveryReason"))
)
if mibBuilder.loadTexts:
    ciscoAtmPvcTrapExtnGroup.setStatus("deprecated")

ciscoAtmPvcTrapExtnGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 3, 2, 5)
)
ciscoAtmPvcTrapExtnGroup1.setObjects(
      *(("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfOAMFailedPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfCurrentOAMFailingPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfSegCCOAMFailedPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfCurSegCCOAMFailingPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfEndCCOAMFailedPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfCurEndCCOAMFailingPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfAISRDIOAMFailedPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfCurAISRDIOAMFailingPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfAnyOAMFailedPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfCurAnyOAMFailingPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfTypeOfOAMFailure"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfCurrentlyDownToUpPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclLowerRangeValue"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclHigherRangeValue"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclRangeStatusChangeStart"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclRangeStatusChangeEnd"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclStatusTransition"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclStatusChangeStart"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclStatusChangeEnd"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclSegCCLowerRangeValue"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclSegCCHigherRangeValue"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclSegCCRangeStatusChStart"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclSegCCRangeStatusChEnd"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclSegCCStatusTransition"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclSegCCStatusChangeStart"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclSegCCStatusChangeEnd"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclEndCCLowerRangeValue"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclEndCCHigherRangeValue"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclEndCCRangeStatusChStart"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclEndCCRangeStatusChEnd"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclEndCCStatusTransition"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclEndCCStatusChangeStart"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclEndCCStatusChangeEnd"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclAISRDILowerRangeValue"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclAISRDIHigherRangeValue"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclAISRDIRangeStatusChStart"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclAISRDIRangeStatusChEnd"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclAISRDIStatusTransition"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclAISRDIStatusChangeStart"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclAISRDIStatusChangeEnd"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfOAMRcovedPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfCurrentOAMRcovingPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfSegCCOAMRcovedPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfCurSegCCOAMRcovingPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfEndCCOAMRcovedPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfCurEndCCOAMRcovingPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfAISRDIOAMRcovedPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfCurAISRDIOAMRcovingPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfAnyOAMRcovedPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfCurAnyOAMRcovingPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfTypeOfOAMRecover"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclCurFailTime"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclPrevRecoverTime"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclFailureReason"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmDownPVclLowerRangeValue"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmDownPVclHigherRangeValue"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmDownPVclRangeStart"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmDownPVclRangeEnd"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPrevUpPVclRangeStart"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPrevUpPVclRangeEnd"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclRangeFailureReason"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclStatusUpTransition"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclStatusUpStart"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclStatusUpEnd"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclSegCCStatusUpTransition"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclSegCCStatusUpStart"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclSegCCStatusUpEnd"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclEndCCStatusUpTransition"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclEndCCStatusUpStart"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclEndCCStatusUpEnd"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclAISRDIStatusUpTransition"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclAISRDIStatusUpStart"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclAISRDIStatusUpEnd"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclCurRecoverTime"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclPrevFailTime"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclRecoveryReason"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclUpLowerRangeValue"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclUpHigherRangeValue"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclRangeStatusUpStart"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclRangeStatusUpEnd"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclSegCCUpLowerRangeValue"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclSegCCUpHigherRangeValue"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclSegCCRangeStatusUpStart"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclSegCCRangeStatusUpEnd"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclEndCCUpLowerRangeValue"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclEndCCUpHigherRangeValue"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclEndCCRangeStatusUpStart"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclEndCCRangeStatusUpEnd"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclAISRDIUpLowerRangeValue"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclAISRDIUpHigherRangeValue"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclAISRDIRangeStatusUpStart"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclAISRDIRangeStatusUpEnd"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmUpPVclLowerRangeValue"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmUpPVclHigherRangeValue"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmUpPVclRangeStart"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmUpPVclRangeEnd"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPrevDownPVclRangeStart"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPrevDownPVclRangeEnd"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclRangeRecoveryReason"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfSegAISRDIFailedPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfCurSegAISRDIFailingPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfEndAISRDIFailedPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfCurEndAISRDIFailingPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfSegAISRDIRcovedPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfCurSegAISRDIRcovingPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfEndAISRDIRcovedPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfCurEndAISRDIRcovingPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclSegAISRDIStatTransition"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclSegAISRDIStatChangeStart"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclSegAISRDIStatChangeEnd"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclEndAISRDIStatTransition"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclEndAISRDIStatChangeStart"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclEndAISRDIStatChangeEnd"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclSegAISRDILowerRangeValue"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclSegAISRDIHigherRangeValue"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclSegAISRDIRangeStatChStart"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclSegAISRDIRangeStatChEnd"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclEndAISRDILowerRangeValue"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclEndAISRDIHigherRngeValue"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclEndAISRDIRngeStatChStart"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclEndAISRDIRangeStatChEnd"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclSegAISRDIStatUpTransit"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclSegAISRDIStatUpStart"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclSegAISRDIStatUpEnd"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclEndAISRDIStatUpTransit"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclEndAISRDIStatUpStart"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclEndAISRDIStatUpEnd"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclSegAISRDIUpLowerRangeVal"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclSegAISRDIUpHigherRngeVal"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclSegAISRDIRngeStatUpStart"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclSegAISRDIRangeStatUpEnd"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclEndAISRDIUpLowerRangeVal"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclEndAISRDIUpHigherRngeVal"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclEndAISRDIRngeStatUpStart"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmPVclEndAISRDIRangeStatUpEnd"))
)
if mibBuilder.loadTexts:
    ciscoAtmPvcTrapExtnGroup1.setStatus("current")


# Notification objects

catmIntfPvcUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 2, 0, 1)
)
catmIntfPvcUpTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfCurrentlyDownToUpPVcls"))
)
if mibBuilder.loadTexts:
    catmIntfPvcUpTrap.setStatus(
        "deprecated"
    )

catmIntfPvcOAMFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 2, 0, 2)
)
catmIntfPvcOAMFailureTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfOAMFailedPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfCurrentOAMFailingPVcls"))
)
if mibBuilder.loadTexts:
    catmIntfPvcOAMFailureTrap.setStatus(
        "current"
    )

catmIntfPvcSegCCOAMFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 2, 0, 3)
)
catmIntfPvcSegCCOAMFailureTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfSegCCOAMFailedPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfCurSegCCOAMFailingPVcls"))
)
if mibBuilder.loadTexts:
    catmIntfPvcSegCCOAMFailureTrap.setStatus(
        "current"
    )

catmIntfPvcEndCCOAMFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 2, 0, 4)
)
catmIntfPvcEndCCOAMFailureTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfEndCCOAMFailedPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfCurEndCCOAMFailingPVcls"))
)
if mibBuilder.loadTexts:
    catmIntfPvcEndCCOAMFailureTrap.setStatus(
        "current"
    )

catmIntfPvcAISRDIOAMFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 2, 0, 5)
)
catmIntfPvcAISRDIOAMFailureTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfAISRDIOAMFailedPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfCurAISRDIOAMFailingPVcls"))
)
if mibBuilder.loadTexts:
    catmIntfPvcAISRDIOAMFailureTrap.setStatus(
        "deprecated"
    )

catmIntfPvcAnyOAMFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 2, 0, 6)
)
catmIntfPvcAnyOAMFailureTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfAnyOAMFailedPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfCurAnyOAMFailingPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfTypeOfOAMFailure"))
)
if mibBuilder.loadTexts:
    catmIntfPvcAnyOAMFailureTrap.setStatus(
        "current"
    )

catmIntfPvcOAMRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 2, 0, 7)
)
catmIntfPvcOAMRecoverTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfOAMRcovedPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfCurrentOAMRcovingPVcls"))
)
if mibBuilder.loadTexts:
    catmIntfPvcOAMRecoverTrap.setStatus(
        "current"
    )

catmIntfPvcSegCCOAMRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 2, 0, 8)
)
catmIntfPvcSegCCOAMRecoverTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfSegCCOAMRcovedPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfCurSegCCOAMRcovingPVcls"))
)
if mibBuilder.loadTexts:
    catmIntfPvcSegCCOAMRecoverTrap.setStatus(
        "current"
    )

catmIntfPvcEndCCOAMRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 2, 0, 9)
)
catmIntfPvcEndCCOAMRecoverTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfEndCCOAMRcovedPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfCurEndCCOAMRcovingPVcls"))
)
if mibBuilder.loadTexts:
    catmIntfPvcEndCCOAMRecoverTrap.setStatus(
        "current"
    )

catmIntfPvcAISRDIOAMRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 2, 0, 10)
)
catmIntfPvcAISRDIOAMRecoverTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfAISRDIOAMRcovedPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfCurAISRDIOAMRcovingPVcls"))
)
if mibBuilder.loadTexts:
    catmIntfPvcAISRDIOAMRecoverTrap.setStatus(
        "deprecated"
    )

catmIntfPvcAnyOAMRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 2, 0, 11)
)
catmIntfPvcAnyOAMRecoverTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfAnyOAMRcovedPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfCurAnyOAMRcovingPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfTypeOfOAMRecover"))
)
if mibBuilder.loadTexts:
    catmIntfPvcAnyOAMRecoverTrap.setStatus(
        "current"
    )

catmIntfPvcUp2Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 2, 0, 12)
)
catmIntfPvcUp2Trap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfCurrentlyDownToUpPVcls"))
)
if mibBuilder.loadTexts:
    catmIntfPvcUp2Trap.setStatus(
        "current"
    )

catmIntfPvcDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 2, 0, 13)
)
catmIntfPvcDownTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CISCO-IETF-ATM2-PVCTRAP-MIB", "atmIntfPvcFailures"),
        ("CISCO-IETF-ATM2-PVCTRAP-MIB", "atmIntfCurrentlyFailingPVcls"))
)
if mibBuilder.loadTexts:
    catmIntfPvcDownTrap.setStatus(
        "current"
    )

catmIntfPvcSegAISRDIFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 2, 0, 14)
)
catmIntfPvcSegAISRDIFailureTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfSegAISRDIFailedPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfCurSegAISRDIFailingPVcls"))
)
if mibBuilder.loadTexts:
    catmIntfPvcSegAISRDIFailureTrap.setStatus(
        "current"
    )

catmIntfPvcEndAISRDIFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 2, 0, 15)
)
catmIntfPvcEndAISRDIFailureTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfEndAISRDIFailedPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfCurEndAISRDIFailingPVcls"))
)
if mibBuilder.loadTexts:
    catmIntfPvcEndAISRDIFailureTrap.setStatus(
        "current"
    )

catmIntfPvcSegAISRDIRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 2, 0, 16)
)
catmIntfPvcSegAISRDIRecoverTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfSegAISRDIRcovedPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfCurSegAISRDIRcovingPVcls"))
)
if mibBuilder.loadTexts:
    catmIntfPvcSegAISRDIRecoverTrap.setStatus(
        "current"
    )

catmIntfPvcEndAISRDIRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 2, 0, 17)
)
catmIntfPvcEndAISRDIRecoverTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfEndAISRDIRcovedPVcls"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfCurEndAISRDIRcovingPVcls"))
)
if mibBuilder.loadTexts:
    catmIntfPvcEndAISRDIRecoverTrap.setStatus(
        "current"
    )


# Notifications groups

ciscoAtmPvcTrapExtnNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 3, 2, 2)
)
ciscoAtmPvcTrapExtnNotifGroup.setObjects(
      *(("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfPvcUpTrap"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfPvcOAMFailureTrap"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfPvcSegCCOAMFailureTrap"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfPvcEndCCOAMFailureTrap"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfPvcAISRDIOAMFailureTrap"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfPvcAnyOAMFailureTrap"))
)
if mibBuilder.loadTexts:
    ciscoAtmPvcTrapExtnNotifGroup.setStatus(
        "deprecated"
    )

ciscoAtmPvcTrapExtnNotifGroup1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 3, 2, 3)
)
ciscoAtmPvcTrapExtnNotifGroup1.setObjects(
      *(("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfPvcOAMFailureTrap"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfPvcSegCCOAMFailureTrap"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfPvcEndCCOAMFailureTrap"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfPvcAISRDIOAMFailureTrap"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfPvcAnyOAMFailureTrap"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfPvcOAMRecoverTrap"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfPvcSegCCOAMRecoverTrap"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfPvcEndCCOAMRecoverTrap"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfPvcAISRDIOAMRecoverTrap"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfPvcAnyOAMRecoverTrap"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfPvcUp2Trap"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfPvcDownTrap"))
)
if mibBuilder.loadTexts:
    ciscoAtmPvcTrapExtnNotifGroup1.setStatus(
        "deprecated"
    )

ciscoAtmPvcTrapExtnNotifGroup2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 3, 2, 4)
)
ciscoAtmPvcTrapExtnNotifGroup2.setObjects(
      *(("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfPvcOAMFailureTrap"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfPvcSegCCOAMFailureTrap"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfPvcEndCCOAMFailureTrap"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfPvcAnyOAMFailureTrap"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfPvcOAMRecoverTrap"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfPvcSegCCOAMRecoverTrap"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfPvcEndCCOAMRecoverTrap"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfPvcAnyOAMRecoverTrap"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfPvcUp2Trap"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfPvcDownTrap"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfPvcSegAISRDIFailureTrap"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfPvcEndAISRDIFailureTrap"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfPvcSegAISRDIRecoverTrap"),
        ("CISCO-ATM-PVCTRAP-EXTN-MIB", "catmIntfPvcEndAISRDIRecoverTrap"))
)
if mibBuilder.loadTexts:
    ciscoAtmPvcTrapExtnNotifGroup2.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoAtmPvcTrapExtnMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoAtmPvcTrapExtnMIBCompliance.setStatus(
        "deprecated"
    )

ciscoAtmPvcTrapExtnMIBCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoAtmPvcTrapExtnMIBCompliance1.setStatus(
        "deprecated"
    )

ciscoAtmPvcTrapExtnMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 97, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoAtmPvcTrapExtnMIBCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ATM-PVCTRAP-EXTN-MIB",
    **{"CatmOAMRecoveryType": CatmOAMRecoveryType,
       "CatmOAMFailureType": CatmOAMFailureType,
       "ciscoAtmPvcTrapExtnMIB": ciscoAtmPvcTrapExtnMIB,
       "ciscoAtmPvcTrapExtnMIBObjects": ciscoAtmPvcTrapExtnMIBObjects,
       "catmInterfaceExt2Table": catmInterfaceExt2Table,
       "catmInterfaceExt2Entry": catmInterfaceExt2Entry,
       "catmIntfCurrentlyDownToUpPVcls": catmIntfCurrentlyDownToUpPVcls,
       "catmIntfOAMFailedPVcls": catmIntfOAMFailedPVcls,
       "catmIntfCurrentOAMFailingPVcls": catmIntfCurrentOAMFailingPVcls,
       "catmIntfSegCCOAMFailedPVcls": catmIntfSegCCOAMFailedPVcls,
       "catmIntfCurSegCCOAMFailingPVcls": catmIntfCurSegCCOAMFailingPVcls,
       "catmIntfEndCCOAMFailedPVcls": catmIntfEndCCOAMFailedPVcls,
       "catmIntfCurEndCCOAMFailingPVcls": catmIntfCurEndCCOAMFailingPVcls,
       "catmIntfAISRDIOAMFailedPVcls": catmIntfAISRDIOAMFailedPVcls,
       "catmIntfCurAISRDIOAMFailingPVcls": catmIntfCurAISRDIOAMFailingPVcls,
       "catmIntfAnyOAMFailedPVcls": catmIntfAnyOAMFailedPVcls,
       "catmIntfCurAnyOAMFailingPVcls": catmIntfCurAnyOAMFailingPVcls,
       "catmIntfTypeOfOAMFailure": catmIntfTypeOfOAMFailure,
       "catmIntfOAMRcovedPVcls": catmIntfOAMRcovedPVcls,
       "catmIntfCurrentOAMRcovingPVcls": catmIntfCurrentOAMRcovingPVcls,
       "catmIntfSegCCOAMRcovedPVcls": catmIntfSegCCOAMRcovedPVcls,
       "catmIntfCurSegCCOAMRcovingPVcls": catmIntfCurSegCCOAMRcovingPVcls,
       "catmIntfEndCCOAMRcovedPVcls": catmIntfEndCCOAMRcovedPVcls,
       "catmIntfCurEndCCOAMRcovingPVcls": catmIntfCurEndCCOAMRcovingPVcls,
       "catmIntfAISRDIOAMRcovedPVcls": catmIntfAISRDIOAMRcovedPVcls,
       "catmIntfCurAISRDIOAMRcovingPVcls": catmIntfCurAISRDIOAMRcovingPVcls,
       "catmIntfAnyOAMRcovedPVcls": catmIntfAnyOAMRcovedPVcls,
       "catmIntfCurAnyOAMRcovingPVcls": catmIntfCurAnyOAMRcovingPVcls,
       "catmIntfTypeOfOAMRecover": catmIntfTypeOfOAMRecover,
       "catmIntfSegAISRDIFailedPVcls": catmIntfSegAISRDIFailedPVcls,
       "catmIntfCurSegAISRDIFailingPVcls": catmIntfCurSegAISRDIFailingPVcls,
       "catmIntfEndAISRDIFailedPVcls": catmIntfEndAISRDIFailedPVcls,
       "catmIntfCurEndAISRDIFailingPVcls": catmIntfCurEndAISRDIFailingPVcls,
       "catmIntfSegAISRDIRcovedPVcls": catmIntfSegAISRDIRcovedPVcls,
       "catmIntfCurSegAISRDIRcovingPVcls": catmIntfCurSegAISRDIRcovingPVcls,
       "catmIntfEndAISRDIRcovedPVcls": catmIntfEndAISRDIRcovedPVcls,
       "catmIntfCurEndAISRDIRcovingPVcls": catmIntfCurEndAISRDIRcovingPVcls,
       "catmCurStatChangePVclTable": catmCurStatChangePVclTable,
       "catmCurStatChangePVclEntry": catmCurStatChangePVclEntry,
       "catmPVclStatusTransition": catmPVclStatusTransition,
       "catmPVclStatusChangeStart": catmPVclStatusChangeStart,
       "catmPVclStatusChangeEnd": catmPVclStatusChangeEnd,
       "catmPVclSegCCStatusTransition": catmPVclSegCCStatusTransition,
       "catmPVclSegCCStatusChangeStart": catmPVclSegCCStatusChangeStart,
       "catmPVclSegCCStatusChangeEnd": catmPVclSegCCStatusChangeEnd,
       "catmPVclEndCCStatusTransition": catmPVclEndCCStatusTransition,
       "catmPVclEndCCStatusChangeStart": catmPVclEndCCStatusChangeStart,
       "catmPVclEndCCStatusChangeEnd": catmPVclEndCCStatusChangeEnd,
       "catmPVclAISRDIStatusTransition": catmPVclAISRDIStatusTransition,
       "catmPVclAISRDIStatusChangeStart": catmPVclAISRDIStatusChangeStart,
       "catmPVclAISRDIStatusChangeEnd": catmPVclAISRDIStatusChangeEnd,
       "catmPVclCurFailTime": catmPVclCurFailTime,
       "catmPVclPrevRecoverTime": catmPVclPrevRecoverTime,
       "catmPVclFailureReason": catmPVclFailureReason,
       "catmPVclSegAISRDIStatTransition": catmPVclSegAISRDIStatTransition,
       "catmPVclSegAISRDIStatChangeStart": catmPVclSegAISRDIStatChangeStart,
       "catmPVclSegAISRDIStatChangeEnd": catmPVclSegAISRDIStatChangeEnd,
       "catmPVclEndAISRDIStatTransition": catmPVclEndAISRDIStatTransition,
       "catmPVclEndAISRDIStatChangeStart": catmPVclEndAISRDIStatChangeStart,
       "catmPVclEndAISRDIStatChangeEnd": catmPVclEndAISRDIStatChangeEnd,
       "catmStatusChangePVclRangeTable": catmStatusChangePVclRangeTable,
       "catmStatusChangePVclRangeEntry": catmStatusChangePVclRangeEntry,
       "catmStatusChangePVclRangeIndex": catmStatusChangePVclRangeIndex,
       "catmPVclLowerRangeValue": catmPVclLowerRangeValue,
       "catmPVclHigherRangeValue": catmPVclHigherRangeValue,
       "catmPVclRangeStatusChangeStart": catmPVclRangeStatusChangeStart,
       "catmPVclRangeStatusChangeEnd": catmPVclRangeStatusChangeEnd,
       "catmSegCCStatusChPVclRangeTable": catmSegCCStatusChPVclRangeTable,
       "catmSegCCStatusChPVclRangeEntry": catmSegCCStatusChPVclRangeEntry,
       "catmPVclSegCCLowerRangeValue": catmPVclSegCCLowerRangeValue,
       "catmPVclSegCCHigherRangeValue": catmPVclSegCCHigherRangeValue,
       "catmPVclSegCCRangeStatusChStart": catmPVclSegCCRangeStatusChStart,
       "catmPVclSegCCRangeStatusChEnd": catmPVclSegCCRangeStatusChEnd,
       "catmEndCCStatusChPVclRangeTable": catmEndCCStatusChPVclRangeTable,
       "catmEndCCStatusChPVclRangeEntry": catmEndCCStatusChPVclRangeEntry,
       "catmPVclEndCCLowerRangeValue": catmPVclEndCCLowerRangeValue,
       "catmPVclEndCCHigherRangeValue": catmPVclEndCCHigherRangeValue,
       "catmPVclEndCCRangeStatusChStart": catmPVclEndCCRangeStatusChStart,
       "catmPVclEndCCRangeStatusChEnd": catmPVclEndCCRangeStatusChEnd,
       "catmAISRDIStatusChPVclRangeTable": catmAISRDIStatusChPVclRangeTable,
       "catmAISRDIStatusChPVclRangeEntry": catmAISRDIStatusChPVclRangeEntry,
       "catmPVclAISRDILowerRangeValue": catmPVclAISRDILowerRangeValue,
       "catmPVclAISRDIHigherRangeValue": catmPVclAISRDIHigherRangeValue,
       "catmPVclAISRDIRangeStatusChStart": catmPVclAISRDIRangeStatusChStart,
       "catmPVclAISRDIRangeStatusChEnd": catmPVclAISRDIRangeStatusChEnd,
       "catmDownPVclRangeTable": catmDownPVclRangeTable,
       "catmDownPVclRangeEntry": catmDownPVclRangeEntry,
       "catmDownPVclLowerRangeValue": catmDownPVclLowerRangeValue,
       "catmDownPVclHigherRangeValue": catmDownPVclHigherRangeValue,
       "catmDownPVclRangeStart": catmDownPVclRangeStart,
       "catmDownPVclRangeEnd": catmDownPVclRangeEnd,
       "catmPrevUpPVclRangeStart": catmPrevUpPVclRangeStart,
       "catmPrevUpPVclRangeEnd": catmPrevUpPVclRangeEnd,
       "catmPVclRangeFailureReason": catmPVclRangeFailureReason,
       "catmCurStatusUpPVclTable": catmCurStatusUpPVclTable,
       "catmCurStatusUpPVclEntry": catmCurStatusUpPVclEntry,
       "catmPVclStatusUpTransition": catmPVclStatusUpTransition,
       "catmPVclStatusUpStart": catmPVclStatusUpStart,
       "catmPVclStatusUpEnd": catmPVclStatusUpEnd,
       "catmPVclSegCCStatusUpTransition": catmPVclSegCCStatusUpTransition,
       "catmPVclSegCCStatusUpStart": catmPVclSegCCStatusUpStart,
       "catmPVclSegCCStatusUpEnd": catmPVclSegCCStatusUpEnd,
       "catmPVclEndCCStatusUpTransition": catmPVclEndCCStatusUpTransition,
       "catmPVclEndCCStatusUpStart": catmPVclEndCCStatusUpStart,
       "catmPVclEndCCStatusUpEnd": catmPVclEndCCStatusUpEnd,
       "catmPVclAISRDIStatusUpTransition": catmPVclAISRDIStatusUpTransition,
       "catmPVclAISRDIStatusUpStart": catmPVclAISRDIStatusUpStart,
       "catmPVclAISRDIStatusUpEnd": catmPVclAISRDIStatusUpEnd,
       "catmPVclCurRecoverTime": catmPVclCurRecoverTime,
       "catmPVclPrevFailTime": catmPVclPrevFailTime,
       "catmPVclRecoveryReason": catmPVclRecoveryReason,
       "catmPVclSegAISRDIStatUpTransit": catmPVclSegAISRDIStatUpTransit,
       "catmPVclSegAISRDIStatUpStart": catmPVclSegAISRDIStatUpStart,
       "catmPVclSegAISRDIStatUpEnd": catmPVclSegAISRDIStatUpEnd,
       "catmPVclEndAISRDIStatUpTransit": catmPVclEndAISRDIStatUpTransit,
       "catmPVclEndAISRDIStatUpStart": catmPVclEndAISRDIStatUpStart,
       "catmPVclEndAISRDIStatUpEnd": catmPVclEndAISRDIStatUpEnd,
       "catmStatusUpPVclRangeTable": catmStatusUpPVclRangeTable,
       "catmStatusUpPVclRangeEntry": catmStatusUpPVclRangeEntry,
       "catmPVclUpLowerRangeValue": catmPVclUpLowerRangeValue,
       "catmPVclUpHigherRangeValue": catmPVclUpHigherRangeValue,
       "catmPVclRangeStatusUpStart": catmPVclRangeStatusUpStart,
       "catmPVclRangeStatusUpEnd": catmPVclRangeStatusUpEnd,
       "catmSegCCStatusUpPVclRangeTable": catmSegCCStatusUpPVclRangeTable,
       "catmSegCCStatusUpPVclRangeEntry": catmSegCCStatusUpPVclRangeEntry,
       "catmPVclSegCCUpLowerRangeValue": catmPVclSegCCUpLowerRangeValue,
       "catmPVclSegCCUpHigherRangeValue": catmPVclSegCCUpHigherRangeValue,
       "catmPVclSegCCRangeStatusUpStart": catmPVclSegCCRangeStatusUpStart,
       "catmPVclSegCCRangeStatusUpEnd": catmPVclSegCCRangeStatusUpEnd,
       "catmEndCCStatusUpPVclRangeTable": catmEndCCStatusUpPVclRangeTable,
       "catmEndCCStatusUpPVclRangeEntry": catmEndCCStatusUpPVclRangeEntry,
       "catmPVclEndCCUpLowerRangeValue": catmPVclEndCCUpLowerRangeValue,
       "catmPVclEndCCUpHigherRangeValue": catmPVclEndCCUpHigherRangeValue,
       "catmPVclEndCCRangeStatusUpStart": catmPVclEndCCRangeStatusUpStart,
       "catmPVclEndCCRangeStatusUpEnd": catmPVclEndCCRangeStatusUpEnd,
       "catmAISRDIStatusUpPVclRangeTable": catmAISRDIStatusUpPVclRangeTable,
       "catmAISRDIStatusUpPVclRangeEntry": catmAISRDIStatusUpPVclRangeEntry,
       "catmPVclAISRDIUpLowerRangeValue": catmPVclAISRDIUpLowerRangeValue,
       "catmPVclAISRDIUpHigherRangeValue": catmPVclAISRDIUpHigherRangeValue,
       "catmPVclAISRDIRangeStatusUpStart": catmPVclAISRDIRangeStatusUpStart,
       "catmPVclAISRDIRangeStatusUpEnd": catmPVclAISRDIRangeStatusUpEnd,
       "catmUpPVclRangeTable": catmUpPVclRangeTable,
       "catmUpPVclRangeEntry": catmUpPVclRangeEntry,
       "catmUpPVclLowerRangeValue": catmUpPVclLowerRangeValue,
       "catmUpPVclHigherRangeValue": catmUpPVclHigherRangeValue,
       "catmUpPVclRangeStart": catmUpPVclRangeStart,
       "catmUpPVclRangeEnd": catmUpPVclRangeEnd,
       "catmPrevDownPVclRangeStart": catmPrevDownPVclRangeStart,
       "catmPrevDownPVclRangeEnd": catmPrevDownPVclRangeEnd,
       "catmPVclRangeRecoveryReason": catmPVclRangeRecoveryReason,
       "catmSegAISRDIStatChPVclRngeTable": catmSegAISRDIStatChPVclRngeTable,
       "catmSegAISRDIStatChPVclRngeEntry": catmSegAISRDIStatChPVclRngeEntry,
       "catmPVclSegAISRDILowerRangeValue": catmPVclSegAISRDILowerRangeValue,
       "catmPVclSegAISRDIHigherRangeValue": catmPVclSegAISRDIHigherRangeValue,
       "catmPVclSegAISRDIRangeStatChStart": catmPVclSegAISRDIRangeStatChStart,
       "catmPVclSegAISRDIRangeStatChEnd": catmPVclSegAISRDIRangeStatChEnd,
       "catmEndAISRDIStatChPVclRngeTable": catmEndAISRDIStatChPVclRngeTable,
       "catmEndAISRDIStatChPVclRngeEntry": catmEndAISRDIStatChPVclRngeEntry,
       "catmPVclEndAISRDILowerRangeValue": catmPVclEndAISRDILowerRangeValue,
       "catmPVclEndAISRDIHigherRngeValue": catmPVclEndAISRDIHigherRngeValue,
       "catmPVclEndAISRDIRngeStatChStart": catmPVclEndAISRDIRngeStatChStart,
       "catmPVclEndAISRDIRangeStatChEnd": catmPVclEndAISRDIRangeStatChEnd,
       "catmSegAISRDIStatUpPVclRngeTable": catmSegAISRDIStatUpPVclRngeTable,
       "catmSegAISRDIStatUpPVclRngeEntry": catmSegAISRDIStatUpPVclRngeEntry,
       "catmPVclSegAISRDIUpLowerRangeVal": catmPVclSegAISRDIUpLowerRangeVal,
       "catmPVclSegAISRDIUpHigherRngeVal": catmPVclSegAISRDIUpHigherRngeVal,
       "catmPVclSegAISRDIRngeStatUpStart": catmPVclSegAISRDIRngeStatUpStart,
       "catmPVclSegAISRDIRangeStatUpEnd": catmPVclSegAISRDIRangeStatUpEnd,
       "catmEndAISRDIStatUpPVclRngeTable": catmEndAISRDIStatUpPVclRngeTable,
       "catmEndAISRDIStatUpPVclRngeEntry": catmEndAISRDIStatUpPVclRngeEntry,
       "catmPVclEndAISRDIUpLowerRangeVal": catmPVclEndAISRDIUpLowerRangeVal,
       "catmPVclEndAISRDIUpHigherRngeVal": catmPVclEndAISRDIUpHigherRngeVal,
       "catmPVclEndAISRDIRngeStatUpStart": catmPVclEndAISRDIRngeStatUpStart,
       "catmPVclEndAISRDIRangeStatUpEnd": catmPVclEndAISRDIRangeStatUpEnd,
       "cAtmPvcTrapExtnMIBNotifPrefix": cAtmPvcTrapExtnMIBNotifPrefix,
       "cAtmPvcTrapExtnMIBNotif": cAtmPvcTrapExtnMIBNotif,
       "catmIntfPvcUpTrap": catmIntfPvcUpTrap,
       "catmIntfPvcOAMFailureTrap": catmIntfPvcOAMFailureTrap,
       "catmIntfPvcSegCCOAMFailureTrap": catmIntfPvcSegCCOAMFailureTrap,
       "catmIntfPvcEndCCOAMFailureTrap": catmIntfPvcEndCCOAMFailureTrap,
       "catmIntfPvcAISRDIOAMFailureTrap": catmIntfPvcAISRDIOAMFailureTrap,
       "catmIntfPvcAnyOAMFailureTrap": catmIntfPvcAnyOAMFailureTrap,
       "catmIntfPvcOAMRecoverTrap": catmIntfPvcOAMRecoverTrap,
       "catmIntfPvcSegCCOAMRecoverTrap": catmIntfPvcSegCCOAMRecoverTrap,
       "catmIntfPvcEndCCOAMRecoverTrap": catmIntfPvcEndCCOAMRecoverTrap,
       "catmIntfPvcAISRDIOAMRecoverTrap": catmIntfPvcAISRDIOAMRecoverTrap,
       "catmIntfPvcAnyOAMRecoverTrap": catmIntfPvcAnyOAMRecoverTrap,
       "catmIntfPvcUp2Trap": catmIntfPvcUp2Trap,
       "catmIntfPvcDownTrap": catmIntfPvcDownTrap,
       "catmIntfPvcSegAISRDIFailureTrap": catmIntfPvcSegAISRDIFailureTrap,
       "catmIntfPvcEndAISRDIFailureTrap": catmIntfPvcEndAISRDIFailureTrap,
       "catmIntfPvcSegAISRDIRecoverTrap": catmIntfPvcSegAISRDIRecoverTrap,
       "catmIntfPvcEndAISRDIRecoverTrap": catmIntfPvcEndAISRDIRecoverTrap,
       "ciscoAtmPvcTrapExtnMIBConformance": ciscoAtmPvcTrapExtnMIBConformance,
       "ciscoAtmPvcTrapExtnMIBCompliances": ciscoAtmPvcTrapExtnMIBCompliances,
       "ciscoAtmPvcTrapExtnMIBCompliance": ciscoAtmPvcTrapExtnMIBCompliance,
       "ciscoAtmPvcTrapExtnMIBCompliance1": ciscoAtmPvcTrapExtnMIBCompliance1,
       "ciscoAtmPvcTrapExtnMIBCompliance2": ciscoAtmPvcTrapExtnMIBCompliance2,
       "ciscoAtmPvcTrapExtnMIBGroups": ciscoAtmPvcTrapExtnMIBGroups,
       "ciscoAtmPvcTrapExtnGroup": ciscoAtmPvcTrapExtnGroup,
       "ciscoAtmPvcTrapExtnNotifGroup": ciscoAtmPvcTrapExtnNotifGroup,
       "ciscoAtmPvcTrapExtnNotifGroup1": ciscoAtmPvcTrapExtnNotifGroup1,
       "ciscoAtmPvcTrapExtnNotifGroup2": ciscoAtmPvcTrapExtnNotifGroup2,
       "ciscoAtmPvcTrapExtnGroup1": ciscoAtmPvcTrapExtnGroup1}
)
