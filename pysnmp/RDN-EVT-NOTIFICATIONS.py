# SNMP MIB module (RDN-EVT-NOTIFICATIONS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RDN-EVT-NOTIFICATIONS
# Produced by pysmi-1.5.4 at Mon Oct 14 22:46:08 2024
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

(docsDevEvId,
 docsDevEvLevel,
 docsDevEvText) = mibBuilder.importSymbols(
    "DOCS-CABLE-DEVICE-MIB",
    "docsDevEvId",
    "docsDevEvLevel",
    "docsDevEvText")

(docsIfDocsisBaseCapability,) = mibBuilder.importSymbols(
    "DOCS-IF-MIB",
    "docsIfDocsisBaseCapability")

(ifPhysAddress,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifPhysAddress")

(riverdelta,) = mibBuilder.importSymbols(
    "RDN-MIB",
    "riverdelta")

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

rdnEvtNotifications = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 0)
)
rdnEvtNotifications.setRevisions(
        ("2008-08-08 00:00",
         "2004-02-20 00:00",
         "2003-11-05 00:00",
         "2003-07-09 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects

rdnEvtMacrtrGetQIdFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473918722)
)
rdnEvtMacrtrGetQIdFailure.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtMacrtrGetQIdFailure.setStatus(
        "current"
    )

rdnEvtMacrtrUnknownCase = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473918723)
)
rdnEvtMacrtrUnknownCase.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtMacrtrUnknownCase.setStatus(
        "current"
    )

rdnEvtMacrtrMsgQReceiveFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473918724)
)
rdnEvtMacrtrMsgQReceiveFailure.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtMacrtrMsgQReceiveFailure.setStatus(
        "current"
    )

rdnEvtMacrtrRdbDefineTableFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473918726)
)
rdnEvtMacrtrRdbDefineTableFailure.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtMacrtrRdbDefineTableFailure.setStatus(
        "current"
    )

rdnEvtMacrtrRxUnexpectedMsgType = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473918730)
)
rdnEvtMacrtrRxUnexpectedMsgType.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtMacrtrRxUnexpectedMsgType.setStatus(
        "current"
    )

rdnEvtMacrtrRegTaskMonFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473918731)
)
rdnEvtMacrtrRegTaskMonFailure.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtMacrtrRegTaskMonFailure.setStatus(
        "current"
    )

rdnEvtMacrtrInvalidFuncParam = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473918732)
)
rdnEvtMacrtrInvalidFuncParam.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtMacrtrInvalidFuncParam.setStatus(
        "current"
    )

rdnEvtMacrtrUnknownCmId = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473918735)
)
rdnEvtMacrtrUnknownCmId.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtMacrtrUnknownCmId.setStatus(
        "current"
    )

rdnEvtBpiLoadAuthRunRecFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473919513)
)
rdnEvtBpiLoadAuthRunRecFailure.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtBpiLoadAuthRunRecFailure.setStatus(
        "current"
    )

rdnEvtBpiLoadTekRunRecFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473919514)
)
rdnEvtBpiLoadTekRunRecFailure.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtBpiLoadTekRunRecFailure.setStatus(
        "current"
    )

rdnEvtBpiLoadCmCertificateFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473919525)
)
rdnEvtBpiLoadCmCertificateFailure.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtBpiLoadCmCertificateFailure.setStatus(
        "current"
    )

rdnEvtDraTaskSpawnFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473919745)
)
rdnEvtDraTaskSpawnFailure.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtDraTaskSpawnFailure.setStatus(
        "current"
    )

rdnEvtDraMsgQCreateFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473919746)
)
rdnEvtDraMsgQCreateFailure.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtDraMsgQCreateFailure.setStatus(
        "current"
    )

rdnEvtDraMsgQReceiveFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473919747)
)
rdnEvtDraMsgQReceiveFailure.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtDraMsgQReceiveFailure.setStatus(
        "current"
    )

rdnEvtDraRegTaskMonFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473919748)
)
rdnEvtDraRegTaskMonFailure.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtDraRegTaskMonFailure.setStatus(
        "current"
    )

rdnEvtDraCreateRdbFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473919749)
)
rdnEvtDraCreateRdbFailure.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtDraCreateRdbFailure.setStatus(
        "current"
    )

rdnEvtDraRxUnexpectedMsgType = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473919754)
)
rdnEvtDraRxUnexpectedMsgType.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtDraRxUnexpectedMsgType.setStatus(
        "current"
    )

rdnEvtDraRxUnexpectedMsgSubType = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473919755)
)
rdnEvtDraRxUnexpectedMsgSubType.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtDraRxUnexpectedMsgSubType.setStatus(
        "current"
    )

rdnEvtDraTmrInitFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473919761)
)
rdnEvtDraTmrInitFailure.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtDraTmrInitFailure.setStatus(
        "current"
    )

rdnEvtDraInvalidFuncParam = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473919767)
)
rdnEvtDraInvalidFuncParam.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtDraInvalidFuncParam.setStatus(
        "current"
    )

rdnEvtDraInvalidMsgParam = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473919768)
)
rdnEvtDraInvalidMsgParam.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtDraInvalidMsgParam.setStatus(
        "current"
    )

rdnEvtRdbMsgQCheckFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473920006)
)
rdnEvtRdbMsgQCheckFailure.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtRdbMsgQCheckFailure.setStatus(
        "current"
    )

rdnEvtRdbCreateDatabaseFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473920025)
)
rdnEvtRdbCreateDatabaseFailure.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtRdbCreateDatabaseFailure.setStatus(
        "current"
    )

rdnEvtRdbInitDatabaseFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473920026)
)
rdnEvtRdbInitDatabaseFailure.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtRdbInitDatabaseFailure.setStatus(
        "current"
    )

rdnEvtRdbSemCreateFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473920048)
)
rdnEvtRdbSemCreateFailure.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtRdbSemCreateFailure.setStatus(
        "current"
    )

rdnEvtRdbUnknownTableFromPeer = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473920145)
)
rdnEvtRdbUnknownTableFromPeer.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtRdbUnknownTableFromPeer.setStatus(
        "current"
    )

rdnEvtRdbDefineTableNotEnoughMemory = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473920174)
)
rdnEvtRdbDefineTableNotEnoughMemory.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtRdbDefineTableNotEnoughMemory.setStatus(
        "current"
    )

rdnEvtRdbMsgBufAllocFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473920179)
)
rdnEvtRdbMsgBufAllocFailure.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtRdbMsgBufAllocFailure.setStatus(
        "current"
    )

rdnEvtRdbMemPoolAllocFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473920185)
)
rdnEvtRdbMemPoolAllocFailure.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtRdbMemPoolAllocFailure.setStatus(
        "current"
    )

rdnEvtRdbMallocFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473920186)
)
rdnEvtRdbMallocFailure.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtRdbMallocFailure.setStatus(
        "current"
    )

rdnEvtDrmSpareCmtsActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473920312)
)
rdnEvtDrmSpareCmtsActive.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtDrmSpareCmtsActive.setStatus(
        "current"
    )

rdnEvtDrmFailedAutoTakeover = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473920313)
)
rdnEvtDrmFailedAutoTakeover.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtDrmFailedAutoTakeover.setStatus(
        "current"
    )

rdnEvtDrmFailedAutoGiveback = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473920314)
)
rdnEvtDrmFailedAutoGiveback.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtDrmFailedAutoGiveback.setStatus(
        "current"
    )

rdnEvtDrmSpareXmittersRcvrsMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473920315)
)
rdnEvtDrmSpareXmittersRcvrsMismatch.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtDrmSpareXmittersRcvrsMismatch.setStatus(
        "current"
    )

rdnEvtDrmSpareDtxActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473920431)
)
rdnEvtDrmSpareDtxActive.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtDrmSpareDtxActive.setStatus(
        "current"
    )

rdnEvtDrmFailedDtxAutoTakeover = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473920432)
)
rdnEvtDrmFailedDtxAutoTakeover.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtDrmFailedDtxAutoTakeover.setStatus(
        "current"
    )

rdnEvtDrmFailedDtxAutoGiveback = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473920433)
)
rdnEvtDrmFailedDtxAutoGiveback.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtDrmFailedDtxAutoGiveback.setStatus(
        "current"
    )

rdnEvtDrmSpareDrxActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473920441)
)
rdnEvtDrmSpareDrxActive.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtDrmSpareDrxActive.setStatus(
        "current"
    )

rdnEvtDrmFailedDrxAutoTakeover = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473920442)
)
rdnEvtDrmFailedDrxAutoTakeover.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtDrmFailedDrxAutoTakeover.setStatus(
        "current"
    )

rdnEvtDrmFailedDrxAutoGiveback = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473920443)
)
rdnEvtDrmFailedDrxAutoGiveback.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtDrmFailedDrxAutoGiveback.setStatus(
        "current"
    )

rdnEvtAccrtrRdbDefineTableFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473920769)
)
rdnEvtAccrtrRdbDefineTableFailure.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtAccrtrRdbDefineTableFailure.setStatus(
        "current"
    )

rdnEvtAccrtrRdbNextFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473920775)
)
rdnEvtAccrtrRdbNextFailure.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtAccrtrRdbNextFailure.setStatus(
        "current"
    )

rdnEvtAccrtrNotFrozenLoad = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473920781)
)
rdnEvtAccrtrNotFrozenLoad.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtAccrtrNotFrozenLoad.setStatus(
        "current"
    )

rdnEvtArdrtrRdbDefineTableFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473921025)
)
rdnEvtArdrtrRdbDefineTableFailure.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtArdrtrRdbDefineTableFailure.setStatus(
        "current"
    )

rdnEvtArdrtrRdbNextFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473921031)
)
rdnEvtArdrtrRdbNextFailure.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtArdrtrRdbNextFailure.setStatus(
        "current"
    )

rdnEvtArdrtrNotFrozenLoad = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473921035)
)
rdnEvtArdrtrNotFrozenLoad.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtArdrtrNotFrozenLoad.setStatus(
        "current"
    )

rdnEvtArdrtrLoadFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473921039)
)
rdnEvtArdrtrLoadFailure.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtArdrtrLoadFailure.setStatus(
        "current"
    )

rdnEvtMacmgrValidateCmError = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473921541)
)
rdnEvtMacmgrValidateCmError.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtMacmgrValidateCmError.setStatus(
        "current"
    )

rdnEvtMacmgrInvalidateCmError = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473921568)
)
rdnEvtMacmgrInvalidateCmError.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtMacmgrInvalidateCmError.setStatus(
        "current"
    )

rdnEvtMacmgrNullPtr = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473921577)
)
rdnEvtMacmgrNullPtr.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtMacmgrNullPtr.setStatus(
        "current"
    )

rdnEvtDocsifCmtsCmIndexAddFreeListFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473924360)
)
rdnEvtDocsifCmtsCmIndexAddFreeListFailure.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtDocsifCmtsCmIndexAddFreeListFailure.setStatus(
        "current"
    )

rdnEvtDocsifCmtsCmIndexDelFreeListFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473924362)
)
rdnEvtDocsifCmtsCmIndexDelFreeListFailure.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtDocsifCmtsCmIndexDelFreeListFailure.setStatus(
        "current"
    )

rdnEvtDocsifCmtsCmIndexReloadFreeListFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473924371)
)
rdnEvtDocsifCmtsCmIndexReloadFreeListFailure.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtDocsifCmtsCmIndexReloadFreeListFailure.setStatus(
        "current"
    )

rdnEvtUpcTaskSpawnFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473925121)
)
rdnEvtUpcTaskSpawnFailure.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtUpcTaskSpawnFailure.setStatus(
        "current"
    )

rdnEvtUpcMsgQCreateFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473925122)
)
rdnEvtUpcMsgQCreateFailure.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtUpcMsgQCreateFailure.setStatus(
        "current"
    )

rdnEvtUpcMsgQReceiveFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473925123)
)
rdnEvtUpcMsgQReceiveFailure.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtUpcMsgQReceiveFailure.setStatus(
        "current"
    )

rdnEvtUpcRegTaskMonFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473925124)
)
rdnEvtUpcRegTaskMonFailure.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtUpcRegTaskMonFailure.setStatus(
        "current"
    )

rdnEvtUpcRxUnexpectedMsgType = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473925126)
)
rdnEvtUpcRxUnexpectedMsgType.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtUpcRxUnexpectedMsgType.setStatus(
        "current"
    )

rdnEvtUpcRxUnexpectedMsgSubType = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473925127)
)
rdnEvtUpcRxUnexpectedMsgSubType.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtUpcRxUnexpectedMsgSubType.setStatus(
        "current"
    )

rdnEvtUpcSemCreateFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473925142)
)
rdnEvtUpcSemCreateFailure.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtUpcSemCreateFailure.setStatus(
        "current"
    )

rdnEvtSvcfloNullPtr = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473925891)
)
rdnEvtSvcfloNullPtr.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtSvcfloNullPtr.setStatus(
        "current"
    )

rdnEvtSvcfloWriteNextFlowTlvError = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473925895)
)
rdnEvtSvcfloWriteNextFlowTlvError.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtSvcfloWriteNextFlowTlvError.setStatus(
        "current"
    )

rdnEvtSvcfloSidInsertFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473925899)
)
rdnEvtSvcfloSidInsertFailure.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtSvcfloSidInsertFailure.setStatus(
        "current"
    )

rdnEvtUbshaCollectionRspMallocError = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473927699)
)
rdnEvtUbshaCollectionRspMallocError.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtUbshaCollectionRspMallocError.setStatus(
        "current"
    )

rdnEvtUbshaTaskSuspended = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 0, 2473927709)
)
rdnEvtUbshaTaskSuspended.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-IF-MIB", "docsIfDocsisBaseCapability"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    rdnEvtUbshaTaskSuspended.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RDN-EVT-NOTIFICATIONS",
    **{"rdnEvtNotifications": rdnEvtNotifications,
       "rdnEvtMacrtrGetQIdFailure": rdnEvtMacrtrGetQIdFailure,
       "rdnEvtMacrtrUnknownCase": rdnEvtMacrtrUnknownCase,
       "rdnEvtMacrtrMsgQReceiveFailure": rdnEvtMacrtrMsgQReceiveFailure,
       "rdnEvtMacrtrRdbDefineTableFailure": rdnEvtMacrtrRdbDefineTableFailure,
       "rdnEvtMacrtrRxUnexpectedMsgType": rdnEvtMacrtrRxUnexpectedMsgType,
       "rdnEvtMacrtrRegTaskMonFailure": rdnEvtMacrtrRegTaskMonFailure,
       "rdnEvtMacrtrInvalidFuncParam": rdnEvtMacrtrInvalidFuncParam,
       "rdnEvtMacrtrUnknownCmId": rdnEvtMacrtrUnknownCmId,
       "rdnEvtBpiLoadAuthRunRecFailure": rdnEvtBpiLoadAuthRunRecFailure,
       "rdnEvtBpiLoadTekRunRecFailure": rdnEvtBpiLoadTekRunRecFailure,
       "rdnEvtBpiLoadCmCertificateFailure": rdnEvtBpiLoadCmCertificateFailure,
       "rdnEvtDraTaskSpawnFailure": rdnEvtDraTaskSpawnFailure,
       "rdnEvtDraMsgQCreateFailure": rdnEvtDraMsgQCreateFailure,
       "rdnEvtDraMsgQReceiveFailure": rdnEvtDraMsgQReceiveFailure,
       "rdnEvtDraRegTaskMonFailure": rdnEvtDraRegTaskMonFailure,
       "rdnEvtDraCreateRdbFailure": rdnEvtDraCreateRdbFailure,
       "rdnEvtDraRxUnexpectedMsgType": rdnEvtDraRxUnexpectedMsgType,
       "rdnEvtDraRxUnexpectedMsgSubType": rdnEvtDraRxUnexpectedMsgSubType,
       "rdnEvtDraTmrInitFailure": rdnEvtDraTmrInitFailure,
       "rdnEvtDraInvalidFuncParam": rdnEvtDraInvalidFuncParam,
       "rdnEvtDraInvalidMsgParam": rdnEvtDraInvalidMsgParam,
       "rdnEvtRdbMsgQCheckFailure": rdnEvtRdbMsgQCheckFailure,
       "rdnEvtRdbCreateDatabaseFailure": rdnEvtRdbCreateDatabaseFailure,
       "rdnEvtRdbInitDatabaseFailure": rdnEvtRdbInitDatabaseFailure,
       "rdnEvtRdbSemCreateFailure": rdnEvtRdbSemCreateFailure,
       "rdnEvtRdbUnknownTableFromPeer": rdnEvtRdbUnknownTableFromPeer,
       "rdnEvtRdbDefineTableNotEnoughMemory": rdnEvtRdbDefineTableNotEnoughMemory,
       "rdnEvtRdbMsgBufAllocFailure": rdnEvtRdbMsgBufAllocFailure,
       "rdnEvtRdbMemPoolAllocFailure": rdnEvtRdbMemPoolAllocFailure,
       "rdnEvtRdbMallocFailure": rdnEvtRdbMallocFailure,
       "rdnEvtDrmSpareCmtsActive": rdnEvtDrmSpareCmtsActive,
       "rdnEvtDrmFailedAutoTakeover": rdnEvtDrmFailedAutoTakeover,
       "rdnEvtDrmFailedAutoGiveback": rdnEvtDrmFailedAutoGiveback,
       "rdnEvtDrmSpareXmittersRcvrsMismatch": rdnEvtDrmSpareXmittersRcvrsMismatch,
       "rdnEvtDrmSpareDtxActive": rdnEvtDrmSpareDtxActive,
       "rdnEvtDrmFailedDtxAutoTakeover": rdnEvtDrmFailedDtxAutoTakeover,
       "rdnEvtDrmFailedDtxAutoGiveback": rdnEvtDrmFailedDtxAutoGiveback,
       "rdnEvtDrmSpareDrxActive": rdnEvtDrmSpareDrxActive,
       "rdnEvtDrmFailedDrxAutoTakeover": rdnEvtDrmFailedDrxAutoTakeover,
       "rdnEvtDrmFailedDrxAutoGiveback": rdnEvtDrmFailedDrxAutoGiveback,
       "rdnEvtAccrtrRdbDefineTableFailure": rdnEvtAccrtrRdbDefineTableFailure,
       "rdnEvtAccrtrRdbNextFailure": rdnEvtAccrtrRdbNextFailure,
       "rdnEvtAccrtrNotFrozenLoad": rdnEvtAccrtrNotFrozenLoad,
       "rdnEvtArdrtrRdbDefineTableFailure": rdnEvtArdrtrRdbDefineTableFailure,
       "rdnEvtArdrtrRdbNextFailure": rdnEvtArdrtrRdbNextFailure,
       "rdnEvtArdrtrNotFrozenLoad": rdnEvtArdrtrNotFrozenLoad,
       "rdnEvtArdrtrLoadFailure": rdnEvtArdrtrLoadFailure,
       "rdnEvtMacmgrValidateCmError": rdnEvtMacmgrValidateCmError,
       "rdnEvtMacmgrInvalidateCmError": rdnEvtMacmgrInvalidateCmError,
       "rdnEvtMacmgrNullPtr": rdnEvtMacmgrNullPtr,
       "rdnEvtDocsifCmtsCmIndexAddFreeListFailure": rdnEvtDocsifCmtsCmIndexAddFreeListFailure,
       "rdnEvtDocsifCmtsCmIndexDelFreeListFailure": rdnEvtDocsifCmtsCmIndexDelFreeListFailure,
       "rdnEvtDocsifCmtsCmIndexReloadFreeListFailure": rdnEvtDocsifCmtsCmIndexReloadFreeListFailure,
       "rdnEvtUpcTaskSpawnFailure": rdnEvtUpcTaskSpawnFailure,
       "rdnEvtUpcMsgQCreateFailure": rdnEvtUpcMsgQCreateFailure,
       "rdnEvtUpcMsgQReceiveFailure": rdnEvtUpcMsgQReceiveFailure,
       "rdnEvtUpcRegTaskMonFailure": rdnEvtUpcRegTaskMonFailure,
       "rdnEvtUpcRxUnexpectedMsgType": rdnEvtUpcRxUnexpectedMsgType,
       "rdnEvtUpcRxUnexpectedMsgSubType": rdnEvtUpcRxUnexpectedMsgSubType,
       "rdnEvtUpcSemCreateFailure": rdnEvtUpcSemCreateFailure,
       "rdnEvtSvcfloNullPtr": rdnEvtSvcfloNullPtr,
       "rdnEvtSvcfloWriteNextFlowTlvError": rdnEvtSvcfloWriteNextFlowTlvError,
       "rdnEvtSvcfloSidInsertFailure": rdnEvtSvcfloSidInsertFailure,
       "rdnEvtUbshaCollectionRspMallocError": rdnEvtUbshaCollectionRspMallocError,
       "rdnEvtUbshaTaskSuspended": rdnEvtUbshaTaskSuspended}
)
